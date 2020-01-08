# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\7\4!\n\4\f\4\16\4$\13\4\3\4\3\4\3\5\6\5")
        buf.write(")\n\5\r\5\16\5*\3\6\3\6\3\6\3\6\3\7\3\7\3\b\6\b\64\n\b")
        buf.write("\r\b\16\b\65\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\3\2\6\4\2C\\c|\5\2\62;C\\c|\3\2\62;\4\2\f\f\"\"\2;")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\25\3")
        buf.write("\2\2\2\7\36\3\2\2\2\t(\3\2\2\2\13,\3\2\2\2\r\60\3\2\2")
        buf.write("\2\17\63\3\2\2\2\21\22\7G\2\2\22\23\7P\2\2\23\24\7F\2")
        buf.write("\2\24\4\3\2\2\2\25\26\7R\2\2\26\27\7T\2\2\27\30\7G\2\2")
        buf.write("\30\31\7I\2\2\31\32\7W\2\2\32\33\7P\2\2\33\34\7V\2\2\34")
        buf.write("\35\7C\2\2\35\6\3\2\2\2\36\"\t\2\2\2\37!\t\3\2\2 \37\3")
        buf.write("\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\"\3")
        buf.write("\2\2\2%&\t\4\2\2&\b\3\2\2\2\')\t\2\2\2(\'\3\2\2\2)*\3")
        buf.write("\2\2\2*(\3\2\2\2*+\3\2\2\2+\n\3\2\2\2,-\7\"\2\2-.\3\2")
        buf.write("\2\2./\b\6\2\2/\f\3\2\2\2\60\61\7A\2\2\61\16\3\2\2\2\62")
        buf.write("\64\t\5\2\2\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2")
        buf.write("\65\66\3\2\2\2\66\67\3\2\2\2\678\b\b\2\28\20\3\2\2\2\6")
        buf.write("\2\"*\65\3\b\2\2")
        return buf.getvalue()


class EnquestesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    END = 1
    QUEST = 2
    ID = 3
    WORD = 4
    WHITESPACE = 5
    QMARK = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'END'", "'PREGUNTA'", "' '", "'?'" ]

    symbolicNames = [ "<INVALID>",
            "END", "QUEST", "ID", "WORD", "WHITESPACE", "QMARK", "WS" ]

    ruleNames = [ "END", "QUEST", "ID", "WORD", "WHITESPACE", "QMARK", "WS" ]

    grammarFileName = "Enquestes.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


