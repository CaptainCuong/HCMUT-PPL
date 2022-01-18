// Generated from BKIT.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.3", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SCI_FLOAT=1, FLOAT=2, REAL=3, DECIMAL=4, WS=5, ERROR_CHAR=6, UNCLOSE_STRING=7, 
		ILLEGAL_ESCAPE=8;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SCI_FLOAT", "FLOAT", "REAL", "DECIMAL", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SCI_FLOAT", "FLOAT", "REAL", "DECIMAL", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE"
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


	public BKITLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BKIT.g4"; }

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
		case 5:
			ERROR_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void ERROR_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			raise ErrorToken(self.text);
			break;
		}
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\nG\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2"+
		"\5\2\30\n\2\3\2\3\2\3\2\3\2\3\2\5\2\37\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\5\2(\n\2\3\3\3\3\5\3,\n\3\3\4\6\4/\n\4\r\4\16\4\60\3\5\3\5\7\5\65\n\5"+
		"\f\5\16\58\13\5\3\6\6\6;\n\6\r\6\16\6<\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t"+
		"\3\t\2\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\3\2\4\3\2\62;\5\2\13\f\17"+
		"\17\"\"\2P\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2"+
		"\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\'\3\2\2\2\5)\3\2\2\2\7.\3\2"+
		"\2\2\t\62\3\2\2\2\13:\3\2\2\2\r@\3\2\2\2\17C\3\2\2\2\21E\3\2\2\2\23(\5"+
		"\5\3\2\24\25\5\5\3\2\25\27\7g\2\2\26\30\7/\2\2\27\26\3\2\2\2\27\30\3\2"+
		"\2\2\30\31\3\2\2\2\31\32\5\7\4\2\32(\3\2\2\2\33\34\5\7\4\2\34\36\7g\2"+
		"\2\35\37\7/\2\2\36\35\3\2\2\2\36\37\3\2\2\2\37 \3\2\2\2 !\5\7\4\2!(\3"+
		"\2\2\2\"#\7g\2\2#$\7/\2\2$(\5\7\4\2%&\7g\2\2&(\5\7\4\2\'\23\3\2\2\2\'"+
		"\24\3\2\2\2\'\33\3\2\2\2\'\"\3\2\2\2\'%\3\2\2\2(\4\3\2\2\2)+\5\7\4\2*"+
		",\5\t\5\2+*\3\2\2\2+,\3\2\2\2,\6\3\2\2\2-/\t\2\2\2.-\3\2\2\2/\60\3\2\2"+
		"\2\60.\3\2\2\2\60\61\3\2\2\2\61\b\3\2\2\2\62\66\7\60\2\2\63\65\t\2\2\2"+
		"\64\63\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67\n\3\2\2\28\66"+
		"\3\2\2\29;\t\3\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=>\3\2\2\2>"+
		"?\b\6\2\2?\f\3\2\2\2@A\13\2\2\2AB\b\7\3\2B\16\3\2\2\2CD\13\2\2\2D\20\3"+
		"\2\2\2EF\13\2\2\2F\22\3\2\2\2\n\2\27\36\'+\60\66<\4\b\2\2\3\7\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}