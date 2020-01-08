from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import networkx as nx
import pickle as pk
from os import path
import logging
import matplotlib.pyplot as plt
# loading the access token from token.txt
# defining callback function for the /start command
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class botGraph:
    def __init__(self):
        self.actualQuiz = None
        self.Graph = None
        self.actualQuestion = None
        self.IDQuizzes = self.getLocalIDQuizzes()
        self.questions = None
        self.answers = None
        self.updateAux = None
        self.dictQA = {}
        self.queueQuestions = []
        self.statsQuiz = {}

    def restartValues(self, actualQuiz):
        self.actualQuiz = actualQuiz
        self.getLocalStats()
        self.queueQuestions = []
        self.dictQA = {}
        self.actualQuestion = actualQuiz
        self.Graph = self.getLocalQuiz()
        self.actualQuestion = next(self.Graph.successors(self.actualQuestion))
        self.queueQuestions.append(self.actualQuestion)

    # HANDLERS
    def getLocalIDQuizzes(self):
        pickleQuizzesIDs = open("../EnquestesGenerated/QuizzesIDs.pickle", "rb")
        idQuizzes = pk.load(pickleQuizzesIDs)
        pickleQuizzesIDs.close()
        return idQuizzes

    def getLocalQuiz(self):
        pathQuizGraph = "../EnquestesGenerated/"+self.actualQuiz+".pickle"
        graph = nx.read_gpickle(pathQuizGraph)
        self.questions = nx.get_node_attributes(graph, 'question')
        self.answers = nx.get_node_attributes(graph, 'answer')
        return graph

    def saveStats(self):
        for question in self.dictQA.keys():
            if question in list(self.statsQuiz.keys()):
                if self.dictQA[question] in list(self.statsQuiz[question].keys()):
                    self.statsQuiz[question][self.dictQA[question]] += 1
                else:
                    self.statsQuiz[question][self.dictQA[question]] = 1

            else:
                self.statsQuiz[question] = {self.dictQA[question]: 1}
        pathStats = "../EnquestesGenerated/Stats/"+self.actualQuiz+".pickle"
        pickleOut = open(pathStats, "wb")
        # print(self.statsQuiz)
        # hace falta tratar
        pk.dump(self.statsQuiz, pickleOut)
        pickleOut.close()

    def getLocalStats(self):
        pathStats = "../EnquestesGenerated/Stats/"+self.actualQuiz+".pickle"
        if not path.exists(pathStats):
            pickleOut = open(pathStats, "wb")
            self.statsQuiz = {}
            pk.dump(self.dictQA, pickleOut)
            pickleOut.close()
        else:
            pickleStats = open(pathStats, "rb")
            self.statsQuiz = pk.load(pickleStats)
            pickleStats.close()

    def getKeyboardInline(self, answers):
        it = 0
        keyboard = []
        for idAnswer, answer in answers:
            keyboard = keyboard + [[InlineKeyboardButton(
                str(idAnswer)+": "+self.getAnswerStr(answer),
                callback_data=str(idAnswer))]]
            it = it + 1
        return keyboard

    def getQuestionStr(self, questionList):
        return " ".join(questionList[:-1])+questionList[-1]

    def getAnswerStr(self, answerList):
        return " ".join(answerList)

    # Messages
    def start(self, update, context):
        first_Name = update.message.from_user['first_name']
        sizeQuizzes = len(self.IDQuizzes)
        quizzPlural = "quiz" if sizeQuizzes == 1 else "quizzes"
        update.message.reply_text(
            text="Welcome *"+first_Name+"😊\n" +
            "*Here you can answer "+str(sizeQuizzes) +
            " "+quizzPlural+" and check some stats.\n" +
            "Check /help for more info!", parse_mode='Markdown')

    def help(self, update, context):
        update.message.reply_text(
            text="Welcome to the *help* message!\n" +
            "Here you can find a complete list of the available bot commands:\n" +
            "🔷 /start - welcome message\n" +
            "🔷 /help - show this message\n" +
            "🔷 /author - info about author\n" +
            "🔷 /getIDQuizzes - get the ID of all the quizzes\n" +
            "🔷 /quiz _idQuiz_ - start the Quiz with ID _idQuiz_\n" +
            " When you finish answering the quiz you can:\n" +
            "🔷 /getIDQuestions - get the ID of all the questions\n" +
            "🔷 /bar _idQuestion_ - display a bar graphic with stats about _idQuestion_\n" +
            "🔷 /pie _idQuestion_ - display a pie graphic with stats about _idQuestion_\n" +
            "🔷 /report - get a text based report with stats about all questions\n" +
            "🔷 /exitQuiz - exit Quiz ", parse_mode='Markdown')

    def author(self, update, context):
        update.message.reply_text(
            text="🧔🏻 Name = Diego Delgado Díaz"
            "\n📧 Mail= diego.delgado.diaz@est.fib.upc.edu",
            parse_mode='Markdown')

    def sendIDQuizzes(self, update, context):
        sizeQuizzes = len(self.IDQuizzes)
        quizzPlural = "quiz" if sizeQuizzes == 1 else "quizzes"
        message = "You have "+str(sizeQuizzes)+" "+quizzPlural+":"
        for IDQuizz in self.IDQuizzes:
            message = message + "\n🔷 "+IDQuizz
        update.message.reply_text(text=message)

    def getAnswers(self):
        # nSuccessors = len(self.Graph[self.actualQuestion])
        answers = None
        for i in self.Graph[self.actualQuestion]:
            if self.Graph[self.actualQuestion][i]['color'] == 'blue':
                answers = self.answers[i]
                break
        return answers

    def quizAuxiliar(self, update, context):
        # se checkea el END y rompe la recursividad
        self.actualQuestion = self.queueQuestions[0]
        if self.actualQuestion == 'END':
            self.saveStats()
            return
        self.dictQA[self.queueQuestions.pop(0)] = None
        # questionParsed el es mensaje que se envía
        questionRaw = self.questions[self.actualQuestion]
        questionParsed = self.getQuestionStr(questionRaw)

        # conseguimos las respuestas
        answers = self.getAnswers()

        # con las respuestas se consigue un teclado tipo inline
        keyboard = self.getKeyboardInline(answers)
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            reply_markup=reply_markup,
            text=questionParsed,
            parse_mode='Markdown')
        # guardo el estado del update para volver a enviar
        self.updateAux = update
        # se  la siguiente pregunta
        for i in self.Graph[self.actualQuestion]:
            if self.Graph[self.actualQuestion][i]['color'] == 'black':
                self.queueQuestions.append(i)
                break

    def quiz(self, update, context):
        response = update.message.text[6:]
        # repone las variables
        self.restartValues(response)
        update.message.reply_text(text="Quiz " + self.actualQuiz)
        # ataca a las futuras preguntas
        self.quizAuxiliar(update, context)

    def getAlternatives(self, answer):
        alternativas = []
        for i in self.Graph[self.actualQuestion]:
            if self.Graph[self.actualQuestion][i]['color'] == 'green':
                alternativas.append(i)
        for alternativa in alternativas:
            if self.Graph[self.actualQuestion][alternativa]['labelAlternativa'] == answer:
                self.queueQuestions.insert(0, alternativa)
                return True
        return False

    def button(self, update, context):
        query = update.callback_query
        query.edit_message_text(text="Selected option: {}".format(query.data))
        self.dictQA[self.actualQuestion] = query.data
        self.getAlternatives(query.data)
        self.quizAuxiliar(self.updateAux, context)

    def graphGenerated(self, update, bot):
        bot.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open("../GraphsGenerated/"+self.actualQuiz+".png", 'rb'))

    def barr(self, update, bot):
        response = update.message.text[5:]
        statQuestion = self.statsQuiz[response]
        # print(statQuestion)
        plt.bar(*zip(*statQuestion.items()))
        # plt.xticks(len(statQuestion), statQuestion.keys())
        plt.savefig('generatedPlots/'+self.actualQuiz+response+'bar.png')
        bot.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open("generatedPlots/"+self.actualQuiz+response+"bar.png", 'rb'))
        plt.clf()

    def pie(self, update, bot):
        response = update.message.text[5:]
        statQuestion = self.statsQuiz[response]
        fig1, ax1 = plt.subplots()
        ax1.pie(
            list(statQuestion.values()), labels=list(statQuestion.keys()), autopct='%1.1f%%')
        # print(statQuestion)
        ax1.axis('equal')
        # plt.xticks(len(statQuestion), statQuestion.keys())
        plt.savefig('generatedPlots/'+self.actualQuiz+response+'pie.png')
        bot.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open("generatedPlots/"+self.actualQuiz+response+"pie.png", 'rb'))
        plt.clf()

    def report(self, update, bot):
        message = "question idAnswer numberAsnswers"
        # for question in self.statsQuiz.keys():
        #   for answer in question[question].keys():
        #      pass
        bot.bot.send_message(chat_id=update.message.chat_id, text=message)
    # hace falta añadirlo a help

    def sendIDQuestions(self, update, bot):
        sizeQuestion = len(self.Graph.nodes())
        questionPlural = "question" if sizeQuestion == 1 else "questions"
        message = "You have "+str(sizeQuestion)+" "+questionPlural+":"
        for question in list(self.Graph.nodes(data='question')):
            if question[1]:
                message = message + "\n🔷 "+str(question[0])
        bot.bot.send_message(chat_id=update.message.chat_id, text=message)


if __name__ == "__main__":
    # call main Telegram objects
    TOKEN = open('token.txt').read().strip()
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    bott = botGraph()
    dispatcher.add_handler(CommandHandler('start', bott.start))
    dispatcher.add_handler(CommandHandler('help', bott.help))
    dispatcher.add_handler(CommandHandler('author', bott.author))
    dispatcher.add_handler(CallbackQueryHandler(bott.button))
    dispatcher.add_handler(CommandHandler('quiz', bott.quiz))
    dispatcher.add_handler(CommandHandler('bar', bott.barr))
    dispatcher.add_handler(CommandHandler('pie', bott.pie))
    dispatcher.add_handler(CommandHandler('report', bott.report))
    dispatcher.add_handler(CommandHandler('getIDQuizzes', bott.sendIDQuizzes))
    dispatcher.add_handler(CommandHandler('graphGenerated', bott.graphGenerated))
    dispatcher.add_handler(CommandHandler('getIDQuestions', bott.sendIDQuestions))
    # starting the bot
    updater.start_polling()
