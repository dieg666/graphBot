// Generated from Enquestes.g by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class EnquestesParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASSIG=1, LINK=2, EOA=3, COMMA=4, LPAR=5, RPAR=6, LBRA=7, RBRA=8, QMARK=9, 
		QUEST=10, ANSW=11, ALT=12, ITEM=13, ENQUE=14, END=15, NUM=16, ID=17, WORD=18, 
		SPACE=19, NEWLINE=20;
	public static final int
		RULE_root = 0, RULE_op = 1, RULE_assigs = 2, RULE_question = 3, RULE_link = 4;
	public static final String[] ruleNames = {
		"root", "op", "assigs", "question", "link"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "':'", "'->'", "';'", "','", "'('", "')'", "'['", "']'", "'?'", 
		"'PREGUNTA'", "'RESPOSTA'", "'ALTERNATIVA'", "'ITEM'", "'ENQUESTA'", "'END'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "ASSIG", "LINK", "EOA", "COMMA", "LPAR", "RPAR", "LBRA", "RBRA", 
		"QMARK", "QUEST", "ANSW", "ALT", "ITEM", "ENQUE", "END", "NUM", "ID", 
		"WORD", "SPACE", "NEWLINE"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Enquestes.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public EnquestesParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class RootContext extends ParserRuleContext {
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public TerminalNode END() { return getToken(EnquestesParser.END, 0); }
		public TerminalNode EOF() { return getToken(EnquestesParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterRoot(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitRoot(this);
		}
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			op();
			setState(11);
			match(END);
			setState(12);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OpContext extends ParserRuleContext {
		public AssigsContext assigs() {
			return getRuleContext(AssigsContext.class,0);
		}
		public LinkContext link() {
			return getRuleContext(LinkContext.class,0);
		}
		public OpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitOp(this);
		}
	}

	public final OpContext op() throws RecognitionException {
		OpContext _localctx = new OpContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_op);
		try {
			setState(16);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(14);
				assigs();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(15);
				link();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssigsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(EnquestesParser.ID, 0); }
		public TerminalNode ASSIG() { return getToken(EnquestesParser.ASSIG, 0); }
		public QuestionContext question() {
			return getRuleContext(QuestionContext.class,0);
		}
		public AssigsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assigs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterAssigs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitAssigs(this);
		}
	}

	public final AssigsContext assigs() throws RecognitionException {
		AssigsContext _localctx = new AssigsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_assigs);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			match(ID);
			setState(19);
			match(ASSIG);
			setState(20);
			question();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QuestionContext extends ParserRuleContext {
		public TerminalNode QUEST() { return getToken(EnquestesParser.QUEST, 0); }
		public TerminalNode QMARK() { return getToken(EnquestesParser.QMARK, 0); }
		public List<TerminalNode> ID() { return getTokens(EnquestesParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(EnquestesParser.ID, i);
		}
		public QuestionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_question; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterQuestion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitQuestion(this);
		}
	}

	public final QuestionContext question() throws RecognitionException {
		QuestionContext _localctx = new QuestionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_question);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			match(QUEST);
			setState(24); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(23);
				match(ID);
				}
				}
				setState(26); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			setState(28);
			match(QMARK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LinkContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(EnquestesParser.ID, 0); }
		public LinkContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_link; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).enterLink(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof EnquestesListener ) ((EnquestesListener)listener).exitLink(this);
		}
	}

	public final LinkContext link() throws RecognitionException {
		LinkContext _localctx = new LinkContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_link);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26#\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2\3\2\3\3\3\3\5\3\23\n\3\3\4\3\4"+
		"\3\4\3\4\3\5\3\5\6\5\33\n\5\r\5\16\5\34\3\5\3\5\3\6\3\6\3\6\2\2\7\2\4"+
		"\6\b\n\2\2\2\37\2\f\3\2\2\2\4\22\3\2\2\2\6\24\3\2\2\2\b\30\3\2\2\2\n "+
		"\3\2\2\2\f\r\5\4\3\2\r\16\7\21\2\2\16\17\7\2\2\3\17\3\3\2\2\2\20\23\5"+
		"\6\4\2\21\23\5\n\6\2\22\20\3\2\2\2\22\21\3\2\2\2\23\5\3\2\2\2\24\25\7"+
		"\23\2\2\25\26\7\3\2\2\26\27\5\b\5\2\27\7\3\2\2\2\30\32\7\f\2\2\31\33\7"+
		"\23\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\36"+
		"\3\2\2\2\36\37\7\13\2\2\37\t\3\2\2\2 !\7\23\2\2!\13\3\2\2\2\4\22\34";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}