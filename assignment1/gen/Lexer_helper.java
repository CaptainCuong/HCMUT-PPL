// Generated from C:/Users/ADMIN/Documents/GitHub/HCMUT-PPL/assignment1/src/main/d96/parser\Lexer_helper.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class Lexer_helper extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		FLOATLIT=1, BOOLIT=2, ID=3, ARRAY=4, INT_TYPE=5, FLOAT_TYPE=6, BOOL_TYPE=7, 
		INTLIT_16=8, INTLIT_2=9, INTLIT_8=10, INTLIT_10=11, CLASS=12, EXPONENT=13, 
		START_STRING=14, ZERO=15, DOT=16, CM=17, LS=18, RS=19, LB=20, RB=21, LP=22, 
		RP=23, SEMI=24, ADDOP=25, LESS_EQUAL=26, GREAT_EQUAL=27, SUBOP=28, MULOP=29, 
		LESS_THAN=30, MODOP=31, DIVOP=32, NOT_EQUAL=33, EQUAL=34, GREAT_THAN=35, 
		AND=36, OR=37, NEGATE=38, STR_CMP=39, STR_CONCAT=40, WS=41, ERROR_CHAR=42, 
		UNCLOSE_STRING=43, ILLEGAL_ESCAPE=44, DOUB_QUOTE=45, END_STRING=46, ESCAPE_SEQ=47, 
		STRING_CHAR=48;
	public static final int
		STRING_INSIDE=1;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE", "STRING_INSIDE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"FLOATLIT", "BOOLIT", "ID", "ARRAY", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
			"INTLIT_16", "INTLIT_2", "INTLIT_8", "INTLIT_10", "LIT", "CLASS", "EXPONENT", 
			"START_STRING", "ZERO", "DOT", "CM", "LS", "RS", "LB", "RB", "LP", "RP", 
			"SEMI", "ADDOP", "LESS_EQUAL", "GREAT_EQUAL", "SUBOP", "MULOP", "LESS_THAN", 
			"MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", "GREAT_THAN", "AND", "OR", "NEGATE", 
			"STR_CMP", "STR_CONCAT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
			"DOUB_QUOTE", "END_STRING", "ESCAPE_SEQ", "STRING_CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, "'Array'", "'Int'", "'Float'", "'Boolean'", null, 
			null, null, null, "'Class'", null, null, "'0'", "'.'", "','", "'['", 
			"']'", "'('", "')'", "'{'", "'}'", "';'", "'+'", "'<='", "'>='", "'-'", 
			"'*'", "'<'", "'%'", "'/'", "'!='", "'=='", "'>'", "'&&'", "'||'", "'!'", 
			"'==.'", "'+.'", null, null, null, null, "''\"'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "FLOATLIT", "BOOLIT", "ID", "ARRAY", "INT_TYPE", "FLOAT_TYPE", 
			"BOOL_TYPE", "INTLIT_16", "INTLIT_2", "INTLIT_8", "INTLIT_10", "CLASS", 
			"EXPONENT", "START_STRING", "ZERO", "DOT", "CM", "LS", "RS", "LB", "RB", 
			"LP", "RP", "SEMI", "ADDOP", "LESS_EQUAL", "GREAT_EQUAL", "SUBOP", "MULOP", 
			"LESS_THAN", "MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", "GREAT_THAN", "AND", 
			"OR", "NEGATE", "STR_CMP", "STR_CONCAT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE", "DOUB_QUOTE", "END_STRING", "ESCAPE_SEQ", "STRING_CHAR"
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


	public Lexer_helper(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Lexer_helper.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 42:
			ERROR_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void ERROR_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			raise ErrorToken(self.text)
			break;
		}
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62\u0127\b\1\b\1"+
		"\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t"+
		"\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4"+
		"\22\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4"+
		"\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4"+
		" \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4"+
		"+\t+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2"+
		"\7\2j\n\2\f\2\16\2m\13\2\3\2\5\2p\n\2\3\2\3\2\3\2\5\2u\n\2\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0080\n\3\3\4\3\4\3\4\7\4\u0085\n\4\f\4\16"+
		"\4\u0088\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3"+
		"\n\6\n\u00aa\n\n\r\n\16\n\u00ab\3\13\3\13\6\13\u00b0\n\13\r\13\16\13\u00b1"+
		"\3\f\3\f\7\f\u00b6\n\f\f\f\16\f\u00b9\13\f\3\f\3\f\5\f\u00bd\n\f\3\r\3"+
		"\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\7\17\u00c9\n\17\f\17\16\17"+
		"\u00cc\13\17\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3"+
		"\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3"+
		"\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\""+
		"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3)\3"+
		"*\3*\3*\3+\6+\u0110\n+\r+\16+\u0111\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3"+
		"/\3\60\3\60\3\60\3\60\3\61\3\61\3\62\3\62\2\2\63\4\3\6\4\b\5\n\6\f\7\16"+
		"\b\20\t\22\n\24\13\26\f\30\r\32\2\34\16\36\17 \20\"\21$\22&\23(\24*\25"+
		",\26.\27\60\30\62\31\64\32\66\338\34:\35<\36>\37@ B!D\"F#H$J%L&N\'P(R"+
		")T*V+X,Z-\\.^/`\60b\61d\62\4\2\3\16\3\2\62;\4\2ZZzz\4\2\62;CH\3\2\62\63"+
		"\3\2\629\3\2\63;\4\2\62;aa\5\2C\\aac|\4\2GGgg\4\2--//\5\2\13\f\17\17\""+
		"\"\6\2\n\f\16\17))^^\2\u0130\2\4\3\2\2\2\2\6\3\2\2\2\2\b\3\2\2\2\2\n\3"+
		"\2\2\2\2\f\3\2\2\2\2\16\3\2\2\2\2\20\3\2\2\2\2\22\3\2\2\2\2\24\3\2\2\2"+
		"\2\26\3\2\2\2\2\30\3\2\2\2\2\34\3\2\2\2\2\36\3\2\2\2\2 \3\2\2\2\2\"\3"+
		"\2\2\2\2$\3\2\2\2\2&\3\2\2\2\2(\3\2\2\2\2*\3\2\2\2\2,\3\2\2\2\2.\3\2\2"+
		"\2\2\60\3\2\2\2\2\62\3\2\2\2\2\64\3\2\2\2\2\66\3\2\2\2\28\3\2\2\2\2:\3"+
		"\2\2\2\2<\3\2\2\2\2>\3\2\2\2\2@\3\2\2\2\2B\3\2\2\2\2D\3\2\2\2\2F\3\2\2"+
		"\2\2H\3\2\2\2\2J\3\2\2\2\2L\3\2\2\2\2N\3\2\2\2\2P\3\2\2\2\2R\3\2\2\2\2"+
		"T\3\2\2\2\2V\3\2\2\2\2X\3\2\2\2\2Z\3\2\2\2\2\\\3\2\2\2\3^\3\2\2\2\3`\3"+
		"\2\2\2\3b\3\2\2\2\3d\3\2\2\2\4t\3\2\2\2\6\177\3\2\2\2\b\u0081\3\2\2\2"+
		"\n\u0089\3\2\2\2\f\u008f\3\2\2\2\16\u0093\3\2\2\2\20\u0099\3\2\2\2\22"+
		"\u00a1\3\2\2\2\24\u00a5\3\2\2\2\26\u00ad\3\2\2\2\30\u00bc\3\2\2\2\32\u00be"+
		"\3\2\2\2\34\u00c0\3\2\2\2\36\u00c6\3\2\2\2 \u00cd\3\2\2\2\"\u00d1\3\2"+
		"\2\2$\u00d3\3\2\2\2&\u00d5\3\2\2\2(\u00d7\3\2\2\2*\u00d9\3\2\2\2,\u00db"+
		"\3\2\2\2.\u00dd\3\2\2\2\60\u00df\3\2\2\2\62\u00e1\3\2\2\2\64\u00e3\3\2"+
		"\2\2\66\u00e5\3\2\2\28\u00e7\3\2\2\2:\u00ea\3\2\2\2<\u00ed\3\2\2\2>\u00ef"+
		"\3\2\2\2@\u00f1\3\2\2\2B\u00f3\3\2\2\2D\u00f5\3\2\2\2F\u00f7\3\2\2\2H"+
		"\u00fa\3\2\2\2J\u00fd\3\2\2\2L\u00ff\3\2\2\2N\u0102\3\2\2\2P\u0105\3\2"+
		"\2\2R\u0107\3\2\2\2T\u010b\3\2\2\2V\u010f\3\2\2\2X\u0115\3\2\2\2Z\u0118"+
		"\3\2\2\2\\\u011a\3\2\2\2^\u011c\3\2\2\2`\u011f\3\2\2\2b\u0123\3\2\2\2"+
		"d\u0125\3\2\2\2fg\5\30\f\2go\5$\22\2hj\5\"\21\2ih\3\2\2\2jm\3\2\2\2ki"+
		"\3\2\2\2kl\3\2\2\2ln\3\2\2\2mk\3\2\2\2np\5\30\f\2ok\3\2\2\2op\3\2\2\2"+
		"pu\3\2\2\2qr\5\30\f\2rs\5\36\17\2su\3\2\2\2tf\3\2\2\2tq\3\2\2\2u\5\3\2"+
		"\2\2vw\7V\2\2wx\7t\2\2xy\7w\2\2y\u0080\7g\2\2z{\7H\2\2{|\7c\2\2|}\7n\2"+
		"\2}~\7u\2\2~\u0080\7g\2\2\177v\3\2\2\2\177z\3\2\2\2\u0080\7\3\2\2\2\u0081"+
		"\u0086\5\32\r\2\u0082\u0085\t\2\2\2\u0083\u0085\5\32\r\2\u0084\u0082\3"+
		"\2\2\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086"+
		"\u0087\3\2\2\2\u0087\t\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008a\7C\2\2"+
		"\u008a\u008b\7t\2\2\u008b\u008c\7t\2\2\u008c\u008d\7c\2\2\u008d\u008e"+
		"\7{\2\2\u008e\13\3\2\2\2\u008f\u0090\7K\2\2\u0090\u0091\7p\2\2\u0091\u0092"+
		"\7v\2\2\u0092\r\3\2\2\2\u0093\u0094\7H\2\2\u0094\u0095\7n\2\2\u0095\u0096"+
		"\7q\2\2\u0096\u0097\7c\2\2\u0097\u0098\7v\2\2\u0098\17\3\2\2\2\u0099\u009a"+
		"\7D\2\2\u009a\u009b\7q\2\2\u009b\u009c\7q\2\2\u009c\u009d\7n\2\2\u009d"+
		"\u009e\7g\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7p\2\2\u00a0\21\3\2\2\2\u00a1"+
		"\u00a2\7\62\2\2\u00a2\u00a3\t\3\2\2\u00a3\u00a4\t\4\2\2\u00a4\23\3\2\2"+
		"\2\u00a5\u00a6\7\62\2\2\u00a6\u00a7\7d\2\2\u00a7\u00a9\3\2\2\2\u00a8\u00aa"+
		"\t\5\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab"+
		"\u00ac\3\2\2\2\u00ac\25\3\2\2\2\u00ad\u00af\7\62\2\2\u00ae\u00b0\t\6\2"+
		"\2\u00af\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2"+
		"\3\2\2\2\u00b2\27\3\2\2\2\u00b3\u00b7\t\7\2\2\u00b4\u00b6\t\b\2\2\u00b5"+
		"\u00b4\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2"+
		"\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bd\t\2\2\2\u00bb"+
		"\u00bd\t\2\2\2\u00bc\u00b3\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\31\3\2\2"+
		"\2\u00be\u00bf\t\t\2\2\u00bf\33\3\2\2\2\u00c0\u00c1\7E\2\2\u00c1\u00c2"+
		"\7n\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5\7u\2\2\u00c5"+
		"\35\3\2\2\2\u00c6\u00ca\t\n\2\2\u00c7\u00c9\t\13\2\2\u00c8\u00c7\3\2\2"+
		"\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\37"+
		"\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\7$\2\2\u00ce\u00cf\3\2\2\2\u00cf"+
		"\u00d0\b\20\2\2\u00d0!\3\2\2\2\u00d1\u00d2\7\62\2\2\u00d2#\3\2\2\2\u00d3"+
		"\u00d4\7\60\2\2\u00d4%\3\2\2\2\u00d5\u00d6\7.\2\2\u00d6\'\3\2\2\2\u00d7"+
		"\u00d8\7]\2\2\u00d8)\3\2\2\2\u00d9\u00da\7_\2\2\u00da+\3\2\2\2\u00db\u00dc"+
		"\7*\2\2\u00dc-\3\2\2\2\u00dd\u00de\7+\2\2\u00de/\3\2\2\2\u00df\u00e0\7"+
		"}\2\2\u00e0\61\3\2\2\2\u00e1\u00e2\7\177\2\2\u00e2\63\3\2\2\2\u00e3\u00e4"+
		"\7=\2\2\u00e4\65\3\2\2\2\u00e5\u00e6\7-\2\2\u00e6\67\3\2\2\2\u00e7\u00e8"+
		"\7>\2\2\u00e8\u00e9\7?\2\2\u00e99\3\2\2\2\u00ea\u00eb\7@\2\2\u00eb\u00ec"+
		"\7?\2\2\u00ec;\3\2\2\2\u00ed\u00ee\7/\2\2\u00ee=\3\2\2\2\u00ef\u00f0\7"+
		",\2\2\u00f0?\3\2\2\2\u00f1\u00f2\7>\2\2\u00f2A\3\2\2\2\u00f3\u00f4\7\'"+
		"\2\2\u00f4C\3\2\2\2\u00f5\u00f6\7\61\2\2\u00f6E\3\2\2\2\u00f7\u00f8\7"+
		"#\2\2\u00f8\u00f9\7?\2\2\u00f9G\3\2\2\2\u00fa\u00fb\7?\2\2\u00fb\u00fc"+
		"\7?\2\2\u00fcI\3\2\2\2\u00fd\u00fe\7@\2\2\u00feK\3\2\2\2\u00ff\u0100\7"+
		"(\2\2\u0100\u0101\7(\2\2\u0101M\3\2\2\2\u0102\u0103\7~\2\2\u0103\u0104"+
		"\7~\2\2\u0104O\3\2\2\2\u0105\u0106\7#\2\2\u0106Q\3\2\2\2\u0107\u0108\7"+
		"?\2\2\u0108\u0109\7?\2\2\u0109\u010a\7\60\2\2\u010aS\3\2\2\2\u010b\u010c"+
		"\7-\2\2\u010c\u010d\7\60\2\2\u010dU\3\2\2\2\u010e\u0110\t\f\2\2\u010f"+
		"\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2"+
		"\2\2\u0112\u0113\3\2\2\2\u0113\u0114\b+\3\2\u0114W\3\2\2\2\u0115\u0116"+
		"\13\2\2\2\u0116\u0117\b,\4\2\u0117Y\3\2\2\2\u0118\u0119\13\2\2\2\u0119"+
		"[\3\2\2\2\u011a\u011b\13\2\2\2\u011b]\3\2\2\2\u011c\u011d\7)\2\2\u011d"+
		"\u011e\7$\2\2\u011e_\3\2\2\2\u011f\u0120\7$\2\2\u0120\u0121\3\2\2\2\u0121"+
		"\u0122\b\60\5\2\u0122a\3\2\2\2\u0123\u0124\t\r\2\2\u0124c\3\2\2\2\u0125"+
		"\u0126\13\2\2\2\u0126e\3\2\2\2\20\2\3kot\177\u0084\u0086\u00ab\u00b1\u00b7"+
		"\u00bc\u00ca\u0111\6\4\3\2\b\2\2\3,\2\4\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}