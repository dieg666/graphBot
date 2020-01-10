# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
import matplotlib.pyplot as plt
import networkx as nx
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.


class EnquestesVisitor(ParseTreeVisitor):
    def __init__(self):
        self.AST = nx.DiGraph()
        self.items = {}
        self.startNode = None
    # Visit a parse tree produced by EnquestesParser#botGraph.

    def visitBotGraph(self, ctx: EnquestesParser.BotGraphContext):
        self.visitChildren(ctx)
        return self.AST

    def getStartNode(self):
        return self.startNode

    # Visit a parse tree produced by EnquestesParser#enquesta.
    def visitEnquesta(self, ctx: EnquestesParser.EnquestaContext):
        g = ctx.getChildren()
        n = ctx.getChildCount()
        ll = [next(g) for i in range(n)]
        # nombre de la enquesta en first
        first = ll[0].getText()
        self.startNode = first
        for i in range(3, n):
            self.AST.add_edge(
                first,
                self.items[ll[i].getText()],
                color="black",
                labelAlternativa="",
                labelItem="")
            first = self.items[ll[i].getText()]
        self.AST.add_edge(
            first,
            "END",
            color="black",
            labelAlternativa="",
            labelItem="")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#op.
    def visitOp(self, ctx: EnquestesParser.OpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#preg.
    def visitPreg(self, ctx: EnquestesParser.PregContext):
        n = ctx.getChildCount()
        g = ctx.getChildren()
        ll = [next(g) for i in range(n)]
        textQuestion = []
        for i in range(3, n):
            textQuestion.append(ll[i].getText())
        self.AST.add_node(
            ll[0].getText(),
            question=textQuestion)

    # Visit a parse tree produced by EnquestesParser#resp.
    def visitResp(self, ctx: EnquestesParser.RespContext):
        n = ctx.getChildCount()
        g = ctx.getChildren()
        ll = [next(g) for i in range(n)]
        textAnswer = []
        for i in range(3, n):
            answerID, resposta = self.visit(ll[i])
            textAnswer.append((answerID, resposta))
        self.AST.add_node(
            ll[0].getText(),
            answer=textAnswer)

    # Visit a parse tree produced by EnquestesParser#opcio.
    def visitOpcio(self, ctx: EnquestesParser.OpcioContext):
        n = ctx.getChildCount()
        g = ctx.getChildren()
        ll = [next(g) for i in range(0, n)]
        answer = []
        answerID = ll[0].getText()
        for i in range(2, n-1):
            answer.append(ll[i].getText())
        return (answerID, answer)
    # Visit a parse tree produced by EnquestesParser#item.

    def visitItem(self, ctx: EnquestesParser.ItemContext):
        g = ctx.getChildren()
        n = ctx.getChildCount()
        ll = [next(g) for i in range(n)]
        self.AST.add_edge(
            ll[3].getText(),
            ll[5].getText(),
            color="blue",
            labelItem=ll[0].getText(),
            labelAlternativa="")
        self.items[ll[0].getText()] = ll[3].getText()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#alter.
    def visitAlter(self, ctx: EnquestesParser.AlterContext):
        n = ctx.getChildCount()
        g = ctx.getChildren()
        ll = [next(g) for i in range(n)]
        listalternatives = self.visit(ll[5])
        pregunta = self.items[ll[3].getText()]
        if isinstance(listalternatives, tuple):
            listalternatives = [listalternatives]
        for (a, i) in listalternatives:
            self.AST.add_edge(
                pregunta,
                self.items[i],
                labelItem="",
                labelAlternativa=a,
                color="green")

    # Visit a parse tree produced by EnquestesParser#alterItems.
    def visitAlterItems(self, ctx: EnquestesParser.AlterItemsContext):
        n = ctx.getChildCount()
        g = ctx.getChildren()
        ll = [next(g) for i in range(n)]
        if n == 7:
            return [(ll[1].getText(), ll[3].getText()), self.visit(ll[6])]
        else:
            return (ll[1].getText(), ll[3].getText())
