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
		FLOATLIT=1, BOOLIT=2, ID=3, INTLIT_16=4, INTLIT_2=5, INTLIT_8=6, INTLIT_10=7, 
		CLASS=8, EXPONENT=9, START_STRING=10, ZERO=11, DOT=12, CM=13, LB=14, RB=15, 
		LP=16, RP=17, SEMI=18, ADDOP=19, LESS_EQUAL=20, GREAT_EQUAL=21, SUBOP=22, 
		MULOP=23, LESS_THAN=24, MODOP=25, DIVOP=26, NOT_EQUAL=27, EQUAL=28, GREAT_THAN=29, 
		AND=30, OR=31, NEGATE=32, STR_CMP=33, STR_CONCAT=34, WS=35, ERROR_CHAR=36, 
		UNCLOSE_STRING=37, ILLEGAL_ESCAPE=38, DOUB_QUOTE=39, END_STRING=40, ESCAPE_SEQ=41, 
		STRING_CHAR=42;
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
			"FLOATLIT", "BOOLIT", "ID", "INTLIT_16", "INTLIT_2", "INTLIT_8", "INTLIT_10", 
			"LIT", "CLASS", "EXPONENT", "START_STRING", "ZERO", "DOT", "CM", "LB", 
			"RB", "LP", "RP", "SEMI", "ADDOP", "LESS_EQUAL", "GREAT_EQUAL", "SUBOP", 
			"MULOP", "LESS_THAN", "MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", "GREAT_THAN", 
			"AND", "OR", "NEGATE", "STR_CMP", "STR_CONCAT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE", "DOUB_QUOTE", "END_STRING", "ESCAPE_SEQ", "STRING_CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "'Class'", null, null, 
			"'0'", "'.'", "','", "'('", "')'", "'{'", "'}'", "';'", "'+'", "'<='", 
			"'>='", "'-'", "'*'", "'<'", "'%'", "'/'", "'!='", "'=='", "'>'", "'&&'", 
			"'||'", "'!'", "'==.'", "'+.'", null, null, null, null, "''\"'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "FLOATLIT", "BOOLIT", "ID", "INTLIT_16", "INTLIT_2", "INTLIT_8", 
			"INTLIT_10", "CLASS", "EXPONENT", "START_STRING", "ZERO", "DOT", "CM", 
			"LB", "RB", "LP", "RP", "SEMI", "ADDOP", "LESS_EQUAL", "GREAT_EQUAL", 
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
		case 36:
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,\u00ff\b\1\b\1\4"+
		"\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n"+
		"\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\3\2\3\2\3\2\7\2^\n\2\f\2\16\2a\13\2\3\2\5\2d\n\2\3\2\3\2\3\2\5"+
		"\2i\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3t\n\3\3\4\3\4\3\4\7\4y"+
		"\n\4\f\4\16\4|\13\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\6\6\u0086\n\6\r\6"+
		"\16\6\u0087\3\7\3\7\6\7\u008c\n\7\r\7\16\7\u008d\3\b\3\b\7\b\u0092\n\b"+
		"\f\b\16\b\u0095\13\b\3\b\3\b\5\b\u0099\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\13\3\13\7\13\u00a5\n\13\f\13\16\13\u00a8\13\13\3\f\3\f\3\f\3\f"+
		"\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3"+
		"\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3"+
		"\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3"+
		" \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3%\6%\u00e8\n%\r%\16%\u00e9"+
		"\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3*\3+\3+\3,\3,\2\2-\4"+
		"\3\6\4\b\5\n\6\f\7\16\b\20\t\22\2\24\n\26\13\30\f\32\r\34\16\36\17 \20"+
		"\"\21$\22&\23(\24*\25,\26.\27\60\30\62\31\64\32\66\338\34:\35<\36>\37"+
		"@ B!D\"F#H$J%L&N\'P(R)T*V+X,\4\2\3\16\3\2\62;\4\2ZZzz\4\2\62;CH\3\2\62"+
		"\63\3\2\629\3\2\63;\4\2\62;aa\5\2C\\aac|\4\2GGgg\4\2--//\5\2\13\f\17\17"+
		"\"\"\6\2\n\f\16\17))^^\2\u0108\2\4\3\2\2\2\2\6\3\2\2\2\2\b\3\2\2\2\2\n"+
		"\3\2\2\2\2\f\3\2\2\2\2\16\3\2\2\2\2\20\3\2\2\2\2\24\3\2\2\2\2\26\3\2\2"+
		"\2\2\30\3\2\2\2\2\32\3\2\2\2\2\34\3\2\2\2\2\36\3\2\2\2\2 \3\2\2\2\2\""+
		"\3\2\2\2\2$\3\2\2\2\2&\3\2\2\2\2(\3\2\2\2\2*\3\2\2\2\2,\3\2\2\2\2.\3\2"+
		"\2\2\2\60\3\2\2\2\2\62\3\2\2\2\2\64\3\2\2\2\2\66\3\2\2\2\28\3\2\2\2\2"+
		":\3\2\2\2\2<\3\2\2\2\2>\3\2\2\2\2@\3\2\2\2\2B\3\2\2\2\2D\3\2\2\2\2F\3"+
		"\2\2\2\2H\3\2\2\2\2J\3\2\2\2\2L\3\2\2\2\2N\3\2\2\2\2P\3\2\2\2\3R\3\2\2"+
		"\2\3T\3\2\2\2\3V\3\2\2\2\3X\3\2\2\2\4h\3\2\2\2\6s\3\2\2\2\bu\3\2\2\2\n"+
		"}\3\2\2\2\f\u0081\3\2\2\2\16\u0089\3\2\2\2\20\u0098\3\2\2\2\22\u009a\3"+
		"\2\2\2\24\u009c\3\2\2\2\26\u00a2\3\2\2\2\30\u00a9\3\2\2\2\32\u00ad\3\2"+
		"\2\2\34\u00af\3\2\2\2\36\u00b1\3\2\2\2 \u00b3\3\2\2\2\"\u00b5\3\2\2\2"+
		"$\u00b7\3\2\2\2&\u00b9\3\2\2\2(\u00bb\3\2\2\2*\u00bd\3\2\2\2,\u00bf\3"+
		"\2\2\2.\u00c2\3\2\2\2\60\u00c5\3\2\2\2\62\u00c7\3\2\2\2\64\u00c9\3\2\2"+
		"\2\66\u00cb\3\2\2\28\u00cd\3\2\2\2:\u00cf\3\2\2\2<\u00d2\3\2\2\2>\u00d5"+
		"\3\2\2\2@\u00d7\3\2\2\2B\u00da\3\2\2\2D\u00dd\3\2\2\2F\u00df\3\2\2\2H"+
		"\u00e3\3\2\2\2J\u00e7\3\2\2\2L\u00ed\3\2\2\2N\u00f0\3\2\2\2P\u00f2\3\2"+
		"\2\2R\u00f4\3\2\2\2T\u00f7\3\2\2\2V\u00fb\3\2\2\2X\u00fd\3\2\2\2Z[\5\20"+
		"\b\2[c\5\34\16\2\\^\5\32\r\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2"+
		"`b\3\2\2\2a_\3\2\2\2bd\5\20\b\2c_\3\2\2\2cd\3\2\2\2di\3\2\2\2ef\5\20\b"+
		"\2fg\5\26\13\2gi\3\2\2\2hZ\3\2\2\2he\3\2\2\2i\5\3\2\2\2jk\7V\2\2kl\7t"+
		"\2\2lm\7w\2\2mt\7g\2\2no\7H\2\2op\7c\2\2pq\7n\2\2qr\7u\2\2rt\7g\2\2sj"+
		"\3\2\2\2sn\3\2\2\2t\7\3\2\2\2uz\5\22\t\2vy\t\2\2\2wy\5\22\t\2xv\3\2\2"+
		"\2xw\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\t\3\2\2\2|z\3\2\2\2}~\7\62"+
		"\2\2~\177\t\3\2\2\177\u0080\t\4\2\2\u0080\13\3\2\2\2\u0081\u0082\7\62"+
		"\2\2\u0082\u0083\7d\2\2\u0083\u0085\3\2\2\2\u0084\u0086\t\5\2\2\u0085"+
		"\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2"+
		"\2\2\u0088\r\3\2\2\2\u0089\u008b\7\62\2\2\u008a\u008c\t\6\2\2\u008b\u008a"+
		"\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e"+
		"\17\3\2\2\2\u008f\u0093\t\7\2\2\u0090\u0092\t\b\2\2\u0091\u0090\3\2\2"+
		"\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096"+
		"\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0099\t\2\2\2\u0097\u0099\t\2\2\2\u0098"+
		"\u008f\3\2\2\2\u0098\u0097\3\2\2\2\u0099\21\3\2\2\2\u009a\u009b\t\t\2"+
		"\2\u009b\23\3\2\2\2\u009c\u009d\7E\2\2\u009d\u009e\7n\2\2\u009e\u009f"+
		"\7c\2\2\u009f\u00a0\7u\2\2\u00a0\u00a1\7u\2\2\u00a1\25\3\2\2\2\u00a2\u00a6"+
		"\t\n\2\2\u00a3\u00a5\t\13\2\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2"+
		"\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\27\3\2\2\2\u00a8\u00a6"+
		"\3\2\2\2\u00a9\u00aa\7$\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\b\f\2\2\u00ac"+
		"\31\3\2\2\2\u00ad\u00ae\7\62\2\2\u00ae\33\3\2\2\2\u00af\u00b0\7\60\2\2"+
		"\u00b0\35\3\2\2\2\u00b1\u00b2\7.\2\2\u00b2\37\3\2\2\2\u00b3\u00b4\7*\2"+
		"\2\u00b4!\3\2\2\2\u00b5\u00b6\7+\2\2\u00b6#\3\2\2\2\u00b7\u00b8\7}\2\2"+
		"\u00b8%\3\2\2\2\u00b9\u00ba\7\177\2\2\u00ba\'\3\2\2\2\u00bb\u00bc\7=\2"+
		"\2\u00bc)\3\2\2\2\u00bd\u00be\7-\2\2\u00be+\3\2\2\2\u00bf\u00c0\7>\2\2"+
		"\u00c0\u00c1\7?\2\2\u00c1-\3\2\2\2\u00c2\u00c3\7@\2\2\u00c3\u00c4\7?\2"+
		"\2\u00c4/\3\2\2\2\u00c5\u00c6\7/\2\2\u00c6\61\3\2\2\2\u00c7\u00c8\7,\2"+
		"\2\u00c8\63\3\2\2\2\u00c9\u00ca\7>\2\2\u00ca\65\3\2\2\2\u00cb\u00cc\7"+
		"\'\2\2\u00cc\67\3\2\2\2\u00cd\u00ce\7\61\2\2\u00ce9\3\2\2\2\u00cf\u00d0"+
		"\7#\2\2\u00d0\u00d1\7?\2\2\u00d1;\3\2\2\2\u00d2\u00d3\7?\2\2\u00d3\u00d4"+
		"\7?\2\2\u00d4=\3\2\2\2\u00d5\u00d6\7@\2\2\u00d6?\3\2\2\2\u00d7\u00d8\7"+
		"(\2\2\u00d8\u00d9\7(\2\2\u00d9A\3\2\2\2\u00da\u00db\7~\2\2\u00db\u00dc"+
		"\7~\2\2\u00dcC\3\2\2\2\u00dd\u00de\7#\2\2\u00deE\3\2\2\2\u00df\u00e0\7"+
		"?\2\2\u00e0\u00e1\7?\2\2\u00e1\u00e2\7\60\2\2\u00e2G\3\2\2\2\u00e3\u00e4"+
		"\7-\2\2\u00e4\u00e5\7\60\2\2\u00e5I\3\2\2\2\u00e6\u00e8\t\f\2\2\u00e7"+
		"\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2"+
		"\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\b%\3\2\u00ecK\3\2\2\2\u00ed\u00ee"+
		"\13\2\2\2\u00ee\u00ef\b&\4\2\u00efM\3\2\2\2\u00f0\u00f1\13\2\2\2\u00f1"+
		"O\3\2\2\2\u00f2\u00f3\13\2\2\2\u00f3Q\3\2\2\2\u00f4\u00f5\7)\2\2\u00f5"+
		"\u00f6\7$\2\2\u00f6S\3\2\2\2\u00f7\u00f8\7$\2\2\u00f8\u00f9\3\2\2\2\u00f9"+
		"\u00fa\b*\5\2\u00faU\3\2\2\2\u00fb\u00fc\t\r\2\2\u00fcW\3\2\2\2\u00fd"+
		"\u00fe\13\2\2\2\u00feY\3\2\2\2\20\2\3_chsxz\u0087\u008d\u0093\u0098\u00a6"+
		"\u00e9\6\4\3\2\b\2\2\3&\2\4\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}