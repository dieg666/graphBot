# Generated from Enquestes.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\6\3!\n\3\r\3\16\3\"\3\4\3\4\3\4")
        buf.write("\3\4\5\4)\n\4\3\5\3\5\3\5\3\5\6\5/\n\5\r\5\16\5\60\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\6\69\n\6\r\6\16\6:\3\7\3\7\3\7\6")
        buf.write("\7@\n\7\r\7\16\7A\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\7\n\\\n\n\f\n\16\n_\13\n\3\n\2\2\13\2\4\6\b\n\f")
        buf.write("\16\20\22\2\2\2`\2\25\3\2\2\2\4\34\3\2\2\2\6(\3\2\2\2")
        buf.write("\b*\3\2\2\2\n\64\3\2\2\2\f<\3\2\2\2\16E\3\2\2\2\20L\3")
        buf.write("\2\2\2\22T\3\2\2\2\24\26\5\6\4\2\25\24\3\2\2\2\26\27\3")
        buf.write("\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31\32")
        buf.write("\5\4\3\2\32\33\7\21\2\2\33\3\3\2\2\2\34\35\7\27\2\2\35")
        buf.write("\36\7\4\2\2\36 \7\17\2\2\37!\7\23\2\2 \37\3\2\2\2!\"\3")
        buf.write("\2\2\2\" \3\2\2\2\"#\3\2\2\2#\5\3\2\2\2$)\5\b\5\2%)\5")
        buf.write("\n\6\2&)\5\16\b\2\')\5\20\t\2($\3\2\2\2(%\3\2\2\2(&\3")
        buf.write("\2\2\2(\'\3\2\2\2)\7\3\2\2\2*+\7\24\2\2+,\7\4\2\2,.\7")
        buf.write("\f\2\2-/\7\27\2\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\62\3\2\2\2\62\63\7\6\2\2\63\t\3\2\2\2\64")
        buf.write("\65\7\25\2\2\65\66\7\4\2\2\668\7\r\2\2\679\5\f\7\28\67")
        buf.write("\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\13\3\2\2\2<=\7")
        buf.write("\22\2\2=?\7\4\2\2>@\7\27\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2")
        buf.write("\2\2AB\3\2\2\2BC\3\2\2\2CD\7\5\2\2D\r\3\2\2\2EF\7\23\2")
        buf.write("\2FG\7\4\2\2GH\7\20\2\2HI\7\24\2\2IJ\7\7\2\2JK\7\25\2")
        buf.write("\2K\17\3\2\2\2LM\7\26\2\2MN\7\4\2\2NO\7\16\2\2OP\7\23")
        buf.write("\2\2PQ\7\n\2\2QR\5\22\n\2RS\7\13\2\2S\21\3\2\2\2TU\7\b")
        buf.write("\2\2UV\7\22\2\2VW\7\3\2\2WX\7\23\2\2X]\7\t\2\2YZ\7\3\2")
        buf.write("\2Z\\\5\22\n\2[Y\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2")
        buf.write("\2^\23\3\2\2\2_]\3\2\2\2\t\27\"(\60:A]")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "':'", "';'", "'?'", "'->'", "'('", 
                     "')'", "'['", "']'", "'PREGUNTA'", "'RESPOSTA'", "'ALTERNATIVA'", 
                     "'ENQUESTA'", "'ITEM'", "'END'" ]

    symbolicNames = [ "<INVALID>", "COMA", "EQ", "SEMIQ", "QMARK", "ASSIG", 
                      "RPAR", "LPAR", "RBRAC", "LBRAC", "PREGUNTA", "RESPOSTA", 
                      "ALTERNATIVA", "ENQUESTA", "ITEM", "END", "NUM", "IDTEM", 
                      "IDPREG", "IDRES", "IDALT", "WORD", "WS" ]

    RULE_botGraph = 0
    RULE_enquesta = 1
    RULE_op = 2
    RULE_preg = 3
    RULE_resp = 4
    RULE_opcio = 5
    RULE_item = 6
    RULE_alter = 7
    RULE_alterItems = 8

    ruleNames =  [ "botGraph", "enquesta", "op", "preg", "resp", "opcio", 
                   "item", "alter", "alterItems" ]

    EOF = Token.EOF
    COMA=1
    EQ=2
    SEMIQ=3
    QMARK=4
    ASSIG=5
    RPAR=6
    LPAR=7
    RBRAC=8
    LBRAC=9
    PREGUNTA=10
    RESPOSTA=11
    ALTERNATIVA=12
    ENQUESTA=13
    ITEM=14
    END=15
    NUM=16
    IDTEM=17
    IDPREG=18
    IDRES=19
    IDALT=20
    WORD=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class BotGraphContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enquesta(self):
            return self.getTypedRuleContext(EnquestesParser.EnquestaContext,0)


        def END(self):
            return self.getToken(EnquestesParser.END, 0)

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.OpContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.OpContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_botGraph

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBotGraph" ):
                return visitor.visitBotGraph(self)
            else:
                return visitor.visitChildren(self)




    def botGraph(self):

        localctx = EnquestesParser.BotGraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_botGraph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.op()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EnquestesParser.IDTEM) | (1 << EnquestesParser.IDPREG) | (1 << EnquestesParser.IDRES) | (1 << EnquestesParser.IDALT))) != 0)):
                    break

            self.state = 23
            self.enquesta()
            self.state = 24
            self.match(EnquestesParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnquestaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(EnquestesParser.WORD, 0)

        def EQ(self):
            return self.getToken(EnquestesParser.EQ, 0)

        def ENQUESTA(self):
            return self.getToken(EnquestesParser.ENQUESTA, 0)

        def IDTEM(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.IDTEM)
            else:
                return self.getToken(EnquestesParser.IDTEM, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_enquesta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnquesta" ):
                return visitor.visitEnquesta(self)
            else:
                return visitor.visitChildren(self)




    def enquesta(self):

        localctx = EnquestesParser.EnquestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enquesta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(EnquestesParser.WORD)
            self.state = 27
            self.match(EnquestesParser.EQ)
            self.state = 28
            self.match(EnquestesParser.ENQUESTA)
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 29
                self.match(EnquestesParser.IDTEM)
                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.IDTEM):
                    break

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

        def preg(self):
            return self.getTypedRuleContext(EnquestesParser.PregContext,0)


        def resp(self):
            return self.getTypedRuleContext(EnquestesParser.RespContext,0)


        def item(self):
            return self.getTypedRuleContext(EnquestesParser.ItemContext,0)


        def alter(self):
            return self.getTypedRuleContext(EnquestesParser.AlterContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = EnquestesParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_op)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EnquestesParser.IDPREG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.preg()
                pass
            elif token in [EnquestesParser.IDRES]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.resp()
                pass
            elif token in [EnquestesParser.IDTEM]:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.item()
                pass
            elif token in [EnquestesParser.IDALT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.alter()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PregContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDPREG(self):
            return self.getToken(EnquestesParser.IDPREG, 0)

        def EQ(self):
            return self.getToken(EnquestesParser.EQ, 0)

        def PREGUNTA(self):
            return self.getToken(EnquestesParser.PREGUNTA, 0)

        def QMARK(self):
            return self.getToken(EnquestesParser.QMARK, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.WORD)
            else:
                return self.getToken(EnquestesParser.WORD, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_preg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreg" ):
                return visitor.visitPreg(self)
            else:
                return visitor.visitChildren(self)




    def preg(self):

        localctx = EnquestesParser.PregContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_preg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(EnquestesParser.IDPREG)
            self.state = 41
            self.match(EnquestesParser.EQ)
            self.state = 42
            self.match(EnquestesParser.PREGUNTA)
            self.state = 44 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 43
                self.match(EnquestesParser.WORD)
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.WORD):
                    break

            self.state = 48
            self.match(EnquestesParser.QMARK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RespContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDRES(self):
            return self.getToken(EnquestesParser.IDRES, 0)

        def EQ(self):
            return self.getToken(EnquestesParser.EQ, 0)

        def RESPOSTA(self):
            return self.getToken(EnquestesParser.RESPOSTA, 0)

        def opcio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.OpcioContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.OpcioContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_resp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResp" ):
                return visitor.visitResp(self)
            else:
                return visitor.visitChildren(self)




    def resp(self):

        localctx = EnquestesParser.RespContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_resp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(EnquestesParser.IDRES)
            self.state = 51
            self.match(EnquestesParser.EQ)
            self.state = 52
            self.match(EnquestesParser.RESPOSTA)
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.opcio()
                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.NUM):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpcioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(EnquestesParser.NUM, 0)

        def EQ(self):
            return self.getToken(EnquestesParser.EQ, 0)

        def SEMIQ(self):
            return self.getToken(EnquestesParser.SEMIQ, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.WORD)
            else:
                return self.getToken(EnquestesParser.WORD, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_opcio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcio" ):
                return visitor.visitOpcio(self)
            else:
                return visitor.visitChildren(self)




    def opcio(self):

        localctx = EnquestesParser.OpcioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_opcio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(EnquestesParser.NUM)
            self.state = 59
            self.match(EnquestesParser.EQ)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.match(EnquestesParser.WORD)
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.WORD):
                    break

            self.state = 65
            self.match(EnquestesParser.SEMIQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDTEM(self):
            return self.getToken(EnquestesParser.IDTEM, 0)

        def EQ(self):
            return self.getToken(EnquestesParser.EQ, 0)

        def ITEM(self):
            return self.getToken(EnquestesParser.ITEM, 0)

        def IDPREG(self):
            return self.getToken(EnquestesParser.IDPREG, 0)

        def ASSIG(self):
            return self.getToken(EnquestesParser.ASSIG, 0)

        def IDRES(self):
            return self.getToken(EnquestesParser.IDRES, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(EnquestesParser.IDTEM)
            self.state = 68
            self.match(EnquestesParser.EQ)
            self.state = 69
            self.match(EnquestesParser.ITEM)
            self.state = 70
            self.match(EnquestesParser.IDPREG)
            self.state = 71
            self.match(EnquestesParser.ASSIG)
            self.state = 72
            self.match(EnquestesParser.IDRES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDALT(self):
            return self.getToken(EnquestesParser.IDALT, 0)

        def EQ(self):
            return self.getToken(EnquestesParser.EQ, 0)

        def ALTERNATIVA(self):
            return self.getToken(EnquestesParser.ALTERNATIVA, 0)

        def IDTEM(self):
            return self.getToken(EnquestesParser.IDTEM, 0)

        def RBRAC(self):
            return self.getToken(EnquestesParser.RBRAC, 0)

        def alterItems(self):
            return self.getTypedRuleContext(EnquestesParser.AlterItemsContext,0)


        def LBRAC(self):
            return self.getToken(EnquestesParser.LBRAC, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_alter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlter" ):
                return visitor.visitAlter(self)
            else:
                return visitor.visitChildren(self)




    def alter(self):

        localctx = EnquestesParser.AlterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_alter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(EnquestesParser.IDALT)
            self.state = 75
            self.match(EnquestesParser.EQ)
            self.state = 76
            self.match(EnquestesParser.ALTERNATIVA)
            self.state = 77
            self.match(EnquestesParser.IDTEM)
            self.state = 78
            self.match(EnquestesParser.RBRAC)
            self.state = 79
            self.alterItems()
            self.state = 80
            self.match(EnquestesParser.LBRAC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlterItemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPAR(self):
            return self.getToken(EnquestesParser.RPAR, 0)

        def NUM(self):
            return self.getToken(EnquestesParser.NUM, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.COMA)
            else:
                return self.getToken(EnquestesParser.COMA, i)

        def IDTEM(self):
            return self.getToken(EnquestesParser.IDTEM, 0)

        def LPAR(self):
            return self.getToken(EnquestesParser.LPAR, 0)

        def alterItems(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.AlterItemsContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.AlterItemsContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_alterItems

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlterItems" ):
                return visitor.visitAlterItems(self)
            else:
                return visitor.visitChildren(self)




    def alterItems(self):

        localctx = EnquestesParser.AlterItemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_alterItems)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(EnquestesParser.RPAR)
            self.state = 83
            self.match(EnquestesParser.NUM)
            self.state = 84
            self.match(EnquestesParser.COMA)
            self.state = 85
            self.match(EnquestesParser.IDTEM)
            self.state = 86
            self.match(EnquestesParser.LPAR)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 87
                    self.match(EnquestesParser.COMA)
                    self.state = 88
                    self.alterItems() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





