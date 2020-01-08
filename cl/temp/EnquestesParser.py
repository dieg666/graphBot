# Generated from Enquestes.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\30\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\6\3\20\n\3\r\3\16\3\21\3\3\3\3\3\4\3\4\3\4\2\2\5\2")
        buf.write("\4\6\2\2\2\25\2\b\3\2\2\2\4\f\3\2\2\2\6\25\3\2\2\2\b\t")
        buf.write("\5\4\3\2\t\n\5\6\4\2\n\13\7\2\2\3\13\3\3\2\2\2\f\r\7\5")
        buf.write("\2\2\r\17\7\4\2\2\16\20\7\6\2\2\17\16\3\2\2\2\20\21\3")
        buf.write("\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\23\3\2\2\2\23\24")
        buf.write("\7\b\2\2\24\5\3\2\2\2\25\26\7\3\2\2\26\7\3\2\2\2\3\21")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'END'", "'PREGUNTA'", "<INVALID>", "<INVALID>", 
                     "' '", "'?'" ]

    symbolicNames = [ "<INVALID>", "END", "QUEST", "ID", "WORD", "WHITESPACE", 
                      "QMARK", "WS" ]

    RULE_root = 0
    RULE_op = 1
    RULE_stop = 2

    ruleNames =  [ "root", "op", "stop" ]

    EOF = Token.EOF
    END=1
    QUEST=2
    ID=3
    WORD=4
    WHITESPACE=5
    QMARK=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self):
            return self.getTypedRuleContext(EnquestesParser.OpContext,0)


        def stop(self):
            return self.getTypedRuleContext(EnquestesParser.StopContext,0)


        def EOF(self):
            return self.getToken(EnquestesParser.EOF, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = EnquestesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.op()
            self.state = 7
            self.stop()
            self.state = 8
            self.match(EnquestesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def QUEST(self):
            return self.getToken(EnquestesParser.QUEST, 0)

        def QMARK(self):
            return self.getToken(EnquestesParser.QMARK, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.WORD)
            else:
                return self.getToken(EnquestesParser.WORD, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = EnquestesParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(EnquestesParser.ID)
            self.state = 11
            self.match(EnquestesParser.QUEST)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.match(EnquestesParser.WORD)
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.WORD):
                    break

            self.state = 17
            self.match(EnquestesParser.QMARK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(EnquestesParser.END, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_stop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStop" ):
                return visitor.visitStop(self)
            else:
                return visitor.visitChildren(self)




    def stop(self):

        localctx = EnquestesParser.StopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(EnquestesParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





