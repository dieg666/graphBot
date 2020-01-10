# graphBot
## Llenguatges de Programació's final project.
This work can be splitted in two sub-projects:
  * **Compilator**:
    * A new language for creating quizzes is generated.
    * When creating a new quiz, a digraph is locally saved (also the image representation of it). This graph contains all the quiz information.
  * **Telegram Bot**:
    * A Telegram bot that retrieves the data generated in the Compilator part and handles the generated quizzes, asking to user questions with given answers. Also stores locally all the given answers, and gives textual and images based statistics
### Perequisites
**Python 3.8.0** with [this packages](requirements.txt)
### Compilator
###### This section will show how the Compilator part works.
First of all the grammar is defined in [Enquestes.g](cl/Enquestes.g), using antlr4 (check + info [here](https://gebakx.github.io/Python3/compiladors.html#2)) some python files are created in cl folder. The important files in this projects were:

File [EnquestesVisitor.py](cl/EnquestesVisitor.py) is a *tree walker* (iterate through the AST), but only a template was genereated, so a little bit of code was mandatory.

File [testEnquestes.py](cl/testEnquestes.py) is our man here. When executed with a file as argument (that file has to be in our quiz language) locally saves the generated tree of the quiz (as a pickle) and also the graph image representation of it.
Execution example:
```
python testEnquestes.py input2
```
> An example of the input can be found at [here](http://gebakx.github.io/QuizBot/#compilador)

The digraph is saved in folder [GeneratedData/GeneratedEnquestes](GeneratedData/GeneratedEnquestes) and the representation of it can be found [GeneratedData/GeneratedGraphs](GeneratedData/GeneratedGraphs) as a png. 
> Note that the saved data has the id of the Quiz as filename.
### Telegram Bot
###### This section will show how to execute the Telegram Bot.
A file was created for the bot in folder bot: [bot.py](bot/bot.py)
It handles everything, from inlineKeyboards to getting our local pickles... 
The execution is quite simple:
```
python bot.py
```
And open [this link](https://t.me/DiegoDelgado_graphBot) to automatically start talking to the bot.
You can play with the bot in **any way**, commands are reachable from the start.
> Some commands that were not mandatory were created by mere interest in the project, like /getIDQuizzes, /getIDQuestions or /graphGenerated.

For storing statistics, a dictionary of dictionaries was needed. The key of this dictionary is the questionID of the quizz, and the data is a dictionary (with idAnswer as key and data as Int that count the number of answers). It can be found as a pickle in [GeneratedData/GeneratedEnquestes/0QuizzesIDs.pickle](GeneratedData/GeneratedEnquestes/0QuizzesIDs.pickle)

## Built With
* [NeoVim](https://neovim.io/) - Vim-based text editor
* [Python 3.8](https://www.python.org/downloads/release/python-380) - Programming language
* [ANTLR4](https://github.com/antlr/antlr4/blob/master/doc/python-target.md) - (ANother Tool for Language Recognition)

### Some improvements that can be done
- [ ] Lock the file with the statistics when the user needs it, so in case another user also has to use it, there are no data racing problems.
- [ ] Find a better way than storing the plots when user asks /pie IDQuestion. Delete the file when no one needs it can be a solution, but I hope for a better answer.

## Author
* **Diego Delgado** - [@diegexe](https://github.com/diegexe)



