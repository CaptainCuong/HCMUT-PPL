// Generated from C:/Users/ADMIN/Documents/GitHub/HCMUT-PPL/assignment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class D96 extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		FLOATLIT=1, BOOLIT=2, ID=3, INTLIT_16=4, INTLIT_2=5, INTLIT_8=6, INTLIT_10=7, 
		CLASS=8, EXPONENT=9, START_STRING=10, STRING=11, ZERO=12, DOT=13, CM=14, 
		LB=15, RB=16, LP=17, RP=18, SEMI=19, ADDOP=20, LESS_EQUAL=21, GREAT_EQUAL=22, 
		SUBOP=23, MULOP=24, LESS_THAN=25, MODOP=26, DIVOP=27, NOT_EQUAL=28, EQUAL=29, 
		GREAT_THAN=30, AND=31, OR=32, NEGATE=33, STR_CMP=34, STR_CONCAT=35, WS=36, 
		ERROR_CHAR=37, UNCLOSE_STRING=38, ILLEGAL_ESCAPE=39, DOUB_QUOTE=40, END_STRING=41, 
		ESCAPE_SEQ=42, STRING_CHAR=43;
	public static final int
		RULE_program = 0, RULE_string = 1, RULE_string_op = 2, RULE_bool_op = 3, 
		RULE_relation_op = 4, RULE_int_op = 5, RULE_float_op = 6, RULE_int_gen_list = 7, 
		RULE_int_gen_cm = 8, RULE_bool_list = 9, RULE_bool_list_cm = 10, RULE_float_list = 11, 
		RULE_float_list_cm = 12, RULE_string_list = 13, RULE_string_list_cm = 14, 
		RULE_lit = 15, RULE_int_gen = 16;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "string", "string_op", "bool_op", "relation_op", "int_op", 
			"float_op", "int_gen_list", "int_gen_cm", "bool_list", "bool_list_cm", 
			"float_list", "float_list_cm", "string_list", "string_list_cm", "lit", 
			"int_gen"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "'Class'", null, null, 
			null, "'0'", "'.'", "','", "'('", "')'", "'{'", "'}'", "';'", "'+'", 
			"'<='", "'>='", "'-'", "'*'", "'<'", "'%'", "'/'", "'!='", "'=='", "'>'", 
			"'&&'", "'||'", "'!'", "'==.'", "'+.'", null, null, null, null, "''\"'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "FLOATLIT", "BOOLIT", "ID", "INTLIT_16", "INTLIT_2", "INTLIT_8", 
			"INTLIT_10", "CLASS", "EXPONENT", "START_STRING", "STRING", "ZERO", "DOT", 
			"CM", "LB", "RB", "LP", "RP", "SEMI", "ADDOP", "LESS_EQUAL", "GREAT_EQUAL", 
			"SUBOP", "MULOP", "LESS_THAN", "MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", 
			"GREAT_THAN", "AND", "OR", "NEGATE", "STR_CMP", "STR_CONCAT", "WS", "ERROR_CHAR", 
			"UNCLOSE_STRING", "ILLEGAL_ESCAPE", "DOUB_QUOTE", "END_STRING", "ESCAPE_SEQ", 
			"STRING_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
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
	public String getGrammarFileName() { return "D96.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public D96(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public TerminalNode EOF() { return getToken(D96.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			string();
			setState(35);
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

	public static class StringContext extends ParserRuleContext {
		public TerminalNode START_STRING() { return getToken(D96.START_STRING, 0); }
		public TerminalNode END_STRING() { return getToken(D96.END_STRING, 0); }
		public List<TerminalNode> DOUB_QUOTE() { return getTokens(D96.DOUB_QUOTE); }
		public TerminalNode DOUB_QUOTE(int i) {
			return getToken(D96.DOUB_QUOTE, i);
		}
		public List<TerminalNode> ESCAPE_SEQ() { return getTokens(D96.ESCAPE_SEQ); }
		public TerminalNode ESCAPE_SEQ(int i) {
			return getToken(D96.ESCAPE_SEQ, i);
		}
		public List<TerminalNode> STRING_CHAR() { return getTokens(D96.STRING_CHAR); }
		public TerminalNode STRING_CHAR(int i) {
			return getToken(D96.STRING_CHAR, i);
		}
		public StringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitString(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitString(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_string);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			match(START_STRING);
			setState(41);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(38);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DOUB_QUOTE) | (1L << ESCAPE_SEQ) | (1L << STRING_CHAR))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					} 
				}
				setState(43);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(44);
			match(END_STRING);
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

	public static class String_opContext extends ParserRuleContext {
		public TerminalNode STR_CMP() { return getToken(D96.STR_CMP, 0); }
		public TerminalNode STR_CONCAT() { return getToken(D96.STR_CONCAT, 0); }
		public String_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterString_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitString_op(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitString_op(this);
			else return visitor.visitChildren(this);
		}
	}

	public final String_opContext string_op() throws RecognitionException {
		String_opContext _localctx = new String_opContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_string_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			_la = _input.LA(1);
			if ( !(_la==STR_CMP || _la==STR_CONCAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class Bool_opContext extends ParserRuleContext {
		public TerminalNode NEGATE() { return getToken(D96.NEGATE, 0); }
		public TerminalNode OR() { return getToken(D96.OR, 0); }
		public TerminalNode AND() { return getToken(D96.AND, 0); }
		public TerminalNode EQUAL() { return getToken(D96.EQUAL, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(D96.NOT_EQUAL, 0); }
		public Bool_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterBool_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitBool_op(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitBool_op(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Bool_opContext bool_op() throws RecognitionException {
		Bool_opContext _localctx = new Bool_opContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_bool_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NOT_EQUAL) | (1L << EQUAL) | (1L << AND) | (1L << OR) | (1L << NEGATE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class Relation_opContext extends ParserRuleContext {
		public TerminalNode LESS_THAN() { return getToken(D96.LESS_THAN, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(D96.NOT_EQUAL, 0); }
		public TerminalNode EQUAL() { return getToken(D96.EQUAL, 0); }
		public TerminalNode GREAT_THAN() { return getToken(D96.GREAT_THAN, 0); }
		public Relation_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relation_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterRelation_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitRelation_op(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitRelation_op(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Relation_opContext relation_op() throws RecognitionException {
		Relation_opContext _localctx = new Relation_opContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_relation_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS_THAN) | (1L << NOT_EQUAL) | (1L << EQUAL) | (1L << GREAT_THAN))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class Int_opContext extends ParserRuleContext {
		public TerminalNode ADDOP() { return getToken(D96.ADDOP, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(D96.LESS_EQUAL, 0); }
		public TerminalNode GREAT_EQUAL() { return getToken(D96.GREAT_EQUAL, 0); }
		public TerminalNode SUBOP() { return getToken(D96.SUBOP, 0); }
		public TerminalNode MULOP() { return getToken(D96.MULOP, 0); }
		public TerminalNode LESS_THAN() { return getToken(D96.LESS_THAN, 0); }
		public TerminalNode MODOP() { return getToken(D96.MODOP, 0); }
		public TerminalNode DIVOP() { return getToken(D96.DIVOP, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(D96.NOT_EQUAL, 0); }
		public TerminalNode EQUAL() { return getToken(D96.EQUAL, 0); }
		public Int_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterInt_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitInt_op(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitInt_op(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Int_opContext int_op() throws RecognitionException {
		Int_opContext _localctx = new Int_opContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_int_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADDOP) | (1L << LESS_EQUAL) | (1L << GREAT_EQUAL) | (1L << SUBOP) | (1L << MULOP) | (1L << LESS_THAN) | (1L << MODOP) | (1L << DIVOP) | (1L << NOT_EQUAL) | (1L << EQUAL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class Float_opContext extends ParserRuleContext {
		public TerminalNode ADDOP() { return getToken(D96.ADDOP, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(D96.LESS_EQUAL, 0); }
		public TerminalNode GREAT_EQUAL() { return getToken(D96.GREAT_EQUAL, 0); }
		public TerminalNode SUBOP() { return getToken(D96.SUBOP, 0); }
		public TerminalNode MULOP() { return getToken(D96.MULOP, 0); }
		public TerminalNode LESS_THAN() { return getToken(D96.LESS_THAN, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(D96.NOT_EQUAL, 0); }
		public Float_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_float_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterFloat_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitFloat_op(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitFloat_op(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Float_opContext float_op() throws RecognitionException {
		Float_opContext _localctx = new Float_opContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_float_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADDOP) | (1L << LESS_EQUAL) | (1L << GREAT_EQUAL) | (1L << SUBOP) | (1L << MULOP) | (1L << LESS_THAN) | (1L << NOT_EQUAL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class Int_gen_listContext extends ParserRuleContext {
		public Int_genContext int_gen() {
			return getRuleContext(Int_genContext.class,0);
		}
		public Int_gen_cmContext int_gen_cm() {
			return getRuleContext(Int_gen_cmContext.class,0);
		}
		public Int_gen_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_gen_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterInt_gen_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitInt_gen_list(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitInt_gen_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Int_gen_listContext int_gen_list() throws RecognitionException {
		Int_gen_listContext _localctx = new Int_gen_listContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_int_gen_list);
		try {
			setState(60);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EOF:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case INTLIT_16:
			case INTLIT_2:
			case INTLIT_8:
			case INTLIT_10:
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				int_gen();
				setState(58);
				int_gen_cm();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Int_gen_cmContext extends ParserRuleContext {
		public TerminalNode CM() { return getToken(D96.CM, 0); }
		public Int_genContext int_gen() {
			return getRuleContext(Int_genContext.class,0);
		}
		public Int_gen_cmContext int_gen_cm() {
			return getRuleContext(Int_gen_cmContext.class,0);
		}
		public Int_gen_cmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_gen_cm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterInt_gen_cm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitInt_gen_cm(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitInt_gen_cm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Int_gen_cmContext int_gen_cm() throws RecognitionException {
		Int_gen_cmContext _localctx = new Int_gen_cmContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_int_gen_cm);
		try {
			setState(67);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EOF:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case CM:
				enterOuterAlt(_localctx, 2);
				{
				setState(63);
				match(CM);
				setState(64);
				int_gen();
				setState(65);
				int_gen_cm();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Bool_listContext extends ParserRuleContext {
		public TerminalNode BOOLIT() { return getToken(D96.BOOLIT, 0); }
		public Bool_list_cmContext bool_list_cm() {
			return getRuleContext(Bool_list_cmContext.class,0);
		}
		public Bool_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterBool_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitBool_list(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitBool_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Bool_listContext bool_list() throws RecognitionException {
		Bool_listContext _localctx = new Bool_listContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_bool_list);
		try {
			setState(72);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EOF:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case BOOLIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				match(BOOLIT);
				setState(71);
				bool_list_cm();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Bool_list_cmContext extends ParserRuleContext {
		public TerminalNode CM() { return getToken(D96.CM, 0); }
		public TerminalNode BOOLIT() { return getToken(D96.BOOLIT, 0); }
		public Bool_list_cmContext bool_list_cm() {
			return getRuleContext(Bool_list_cmContext.class,0);
		}
		public Bool_list_cmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_list_cm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterBool_list_cm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitBool_list_cm(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitBool_list_cm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Bool_list_cmContext bool_list_cm() throws RecognitionException {
		Bool_list_cmContext _localctx = new Bool_list_cmContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_bool_list_cm);
		try {
			setState(78);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EOF:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case CM:
				enterOuterAlt(_localctx, 2);
				{
				setState(75);
				match(CM);
				setState(76);
				match(BOOLIT);
				setState(77);
				bool_list_cm();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Float_listContext extends ParserRuleContext {
		public TerminalNode FLOATLIT() { return getToken(D96.FLOATLIT, 0); }
		public Float_list_cmContext float_list_cm() {
			return getRuleContext(Float_list_cmContext.class,0);
		}
		public Float_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_float_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterFloat_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitFloat_list(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitFloat_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Float_listContext float_list() throws RecognitionException {
		Float_listContext _localctx = new Float_listContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_float_list);
		try {
			setState(83);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EOF:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case FLOATLIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(81);
				match(FLOATLIT);
				setState(82);
				float_list_cm();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Float_list_cmContext extends ParserRuleContext {
		public TerminalNode CM() { return getToken(D96.CM, 0); }
		public TerminalNode FLOATLIT() { return getToken(D96.FLOATLIT, 0); }
		public Float_list_cmContext float_list_cm() {
			return getRuleContext(Float_list_cmContext.class,0);
		}
		public Float_list_cmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_float_list_cm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterFloat_list_cm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitFloat_list_cm(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitFloat_list_cm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Float_list_cmContext float_list_cm() throws RecognitionException {
		Float_list_cmContext _localctx = new Float_list_cmContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_float_list_cm);
		try {
			setState(89);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EOF:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case CM:
				enterOuterAlt(_localctx, 2);
				{
				setState(86);
				match(CM);
				setState(87);
				match(FLOATLIT);
				setState(88);
				float_list_cm();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class String_listContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(D96.STRING, 0); }
		public String_list_cmContext string_list_cm() {
			return getRuleContext(String_list_cmContext.class,0);
		}
		public String_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterString_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitString_list(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitString_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final String_listContext string_list() throws RecognitionException {
		String_listContext _localctx = new String_listContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_string_list);
		try {
			setState(94);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EOF:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(92);
				match(STRING);
				setState(93);
				string_list_cm();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class String_list_cmContext extends ParserRuleContext {
		public TerminalNode CM() { return getToken(D96.CM, 0); }
		public TerminalNode STRING() { return getToken(D96.STRING, 0); }
		public String_list_cmContext string_list_cm() {
			return getRuleContext(String_list_cmContext.class,0);
		}
		public String_list_cmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_list_cm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterString_list_cm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitString_list_cm(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitString_list_cm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final String_list_cmContext string_list_cm() throws RecognitionException {
		String_list_cmContext _localctx = new String_list_cmContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_string_list_cm);
		try {
			setState(100);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EOF:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case CM:
				enterOuterAlt(_localctx, 2);
				{
				setState(97);
				match(CM);
				setState(98);
				match(STRING);
				setState(99);
				string_list_cm();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class LitContext extends ParserRuleContext {
		public TerminalNode FLOATLIT() { return getToken(D96.FLOATLIT, 0); }
		public TerminalNode BOOLIT() { return getToken(D96.BOOLIT, 0); }
		public TerminalNode STRING() { return getToken(D96.STRING, 0); }
		public Int_genContext int_gen() {
			return getRuleContext(Int_genContext.class,0);
		}
		public LitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterLit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitLit(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitLit(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LitContext lit() throws RecognitionException {
		LitContext _localctx = new LitContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_lit);
		try {
			setState(106);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FLOATLIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(102);
				match(FLOATLIT);
				}
				break;
			case BOOLIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(103);
				match(BOOLIT);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(104);
				match(STRING);
				}
				break;
			case INTLIT_16:
			case INTLIT_2:
			case INTLIT_8:
			case INTLIT_10:
				enterOuterAlt(_localctx, 4);
				{
				setState(105);
				int_gen();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Int_genContext extends ParserRuleContext {
		public TerminalNode INTLIT_16() { return getToken(D96.INTLIT_16, 0); }
		public TerminalNode INTLIT_2() { return getToken(D96.INTLIT_2, 0); }
		public TerminalNode INTLIT_8() { return getToken(D96.INTLIT_8, 0); }
		public TerminalNode INTLIT_10() { return getToken(D96.INTLIT_10, 0); }
		public Int_genContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_gen; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).enterInt_gen(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof D96Listener ) ((D96Listener)listener).exitInt_gen(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof D96Visitor ) return ((D96Visitor<? extends T>)visitor).visitInt_gen(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Int_genContext int_gen() throws RecognitionException {
		Int_genContext _localctx = new Int_genContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_int_gen);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTLIT_16) | (1L << INTLIT_2) | (1L << INTLIT_8) | (1L << INTLIT_10))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-q\4\2\t\2\4\3\t\3"+
		"\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f"+
		"\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2"+
		"\3\2\3\3\3\3\7\3*\n\3\f\3\16\3-\13\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3"+
		"\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\5\t?\n\t\3\n\3\n\3\n\3\n\3\n\5\nF\n\n\3"+
		"\13\3\13\3\13\5\13K\n\13\3\f\3\f\3\f\3\f\5\fQ\n\f\3\r\3\r\3\r\5\rV\n\r"+
		"\3\16\3\16\3\16\3\16\5\16\\\n\16\3\17\3\17\3\17\5\17a\n\17\3\20\3\20\3"+
		"\20\3\20\5\20g\n\20\3\21\3\21\3\21\3\21\5\21m\n\21\3\22\3\22\3\22\3+\2"+
		"\23\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"\2\t\4\2**,-\3\2$%\4\2\36"+
		"\37!#\4\2\33\33\36 \3\2\26\37\4\2\26\33\36\36\3\2\6\t\2k\2$\3\2\2\2\4"+
		"\'\3\2\2\2\6\60\3\2\2\2\b\62\3\2\2\2\n\64\3\2\2\2\f\66\3\2\2\2\168\3\2"+
		"\2\2\20>\3\2\2\2\22E\3\2\2\2\24J\3\2\2\2\26P\3\2\2\2\30U\3\2\2\2\32[\3"+
		"\2\2\2\34`\3\2\2\2\36f\3\2\2\2 l\3\2\2\2\"n\3\2\2\2$%\5\4\3\2%&\7\2\2"+
		"\3&\3\3\2\2\2\'+\7\f\2\2(*\t\2\2\2)(\3\2\2\2*-\3\2\2\2+,\3\2\2\2+)\3\2"+
		"\2\2,.\3\2\2\2-+\3\2\2\2./\7+\2\2/\5\3\2\2\2\60\61\t\3\2\2\61\7\3\2\2"+
		"\2\62\63\t\4\2\2\63\t\3\2\2\2\64\65\t\5\2\2\65\13\3\2\2\2\66\67\t\6\2"+
		"\2\67\r\3\2\2\289\t\7\2\29\17\3\2\2\2:?\3\2\2\2;<\5\"\22\2<=\5\22\n\2"+
		"=?\3\2\2\2>:\3\2\2\2>;\3\2\2\2?\21\3\2\2\2@F\3\2\2\2AB\7\20\2\2BC\5\""+
		"\22\2CD\5\22\n\2DF\3\2\2\2E@\3\2\2\2EA\3\2\2\2F\23\3\2\2\2GK\3\2\2\2H"+
		"I\7\4\2\2IK\5\26\f\2JG\3\2\2\2JH\3\2\2\2K\25\3\2\2\2LQ\3\2\2\2MN\7\20"+
		"\2\2NO\7\4\2\2OQ\5\26\f\2PL\3\2\2\2PM\3\2\2\2Q\27\3\2\2\2RV\3\2\2\2ST"+
		"\7\3\2\2TV\5\32\16\2UR\3\2\2\2US\3\2\2\2V\31\3\2\2\2W\\\3\2\2\2XY\7\20"+
		"\2\2YZ\7\3\2\2Z\\\5\32\16\2[W\3\2\2\2[X\3\2\2\2\\\33\3\2\2\2]a\3\2\2\2"+
		"^_\7\r\2\2_a\5\36\20\2`]\3\2\2\2`^\3\2\2\2a\35\3\2\2\2bg\3\2\2\2cd\7\20"+
		"\2\2de\7\r\2\2eg\5\36\20\2fb\3\2\2\2fc\3\2\2\2g\37\3\2\2\2hm\7\3\2\2i"+
		"m\7\4\2\2jm\7\r\2\2km\5\"\22\2lh\3\2\2\2li\3\2\2\2lj\3\2\2\2lk\3\2\2\2"+
		"m!\3\2\2\2no\t\b\2\2o#\3\2\2\2\f+>EJPU[`fl";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}