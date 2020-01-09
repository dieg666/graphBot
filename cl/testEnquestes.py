import sys
import pickle as pk
import networkx as nx
from antlr4 import *
from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from antlr4.InputStream import InputStream
from EnquestesVisitor import EnquestesVisitor
from testDrawGraph import drawGraph
from os import path
if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1])
else:
    input_stream = InputStream(input('? '))

lexer = EnquestesLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = EnquestesParser(token_stream)
tree = parser.botGraph()
visitor = EnquestesVisitor()
G = visitor.visit(tree)
idEnquesta = visitor.getStartNode()
nx.write_gpickle(G, "../GeneratedEnquestes/"+idEnquesta+".pickle")
pathQuizzesIDs = "../GeneratedEnquestes/0QuizzesIDs.pickle"
if not path.exists(pathQuizzesIDs):
    pickleOut = open(pathQuizzesIDs, "wb")
    quizzesIDs = {idEnquesta}
    pk.dump(quizzesIDs, pickleOut)
    pickleOut.close()
else:
    pickleQuizzesIDs = open(pathQuizzesIDs, "rb")
    quizzesIDs = pk.load(pickleQuizzesIDs)
    pickleQuizzesIDs.close()
    pickleOut = open(pathQuizzesIDs, "wb")
    quizzesIDs.add(idEnquesta)
    pk.dump(quizzesIDs, pickleOut)
    pickleOut.close()
drawGraph(G, idEnquesta)
