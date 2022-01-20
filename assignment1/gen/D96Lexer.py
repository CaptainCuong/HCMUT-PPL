# Generated from C:/Users/ADMIN/Documents/GitHub/HCMUT-PPL/assignment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2)")
        buf.write("\u00ff\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\2\3\2")
        buf.write("\7\2\\\n\2\f\2\16\2_\13\2\3\2\3\2\3\3\3\3\3\3\7\3f\n\3")
        buf.write("\f\3\16\3i\13\3\3\3\5\3l\n\3\3\3\3\3\3\3\5\3q\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4|\n\4\3\5\3\5\3\5")
        buf.write("\7\5\u0081\n\5\f\5\16\5\u0084\13\5\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\6\7\u008e\n\7\r\7\16\7\u008f\3\b\3\b\6\b")
        buf.write("\u0094\n\b\r\b\16\b\u0095\3\t\3\t\7\t\u009a\n\t\f\t\16")
        buf.write("\t\u009d\13\t\3\t\3\t\5\t\u00a1\n\t\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\7\f\u00ad\n\f\f\f\16\f\u00b0")
        buf.write("\13\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\6(\u00f3\n(\r(\16(\u00f4\3(\3(\3)\3)")
        buf.write("\3)\3*\3*\3+\3+\3]\2,\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\2\25\13\27\f\31\2\33\2\35\r\37\16!\17#\20%\21\'")
        buf.write("\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35")
        buf.write("?\36A\37C E!G\"I#K$M%O&Q\'S(U)\3\2\16\3\2\62;\4\2ZZzz")
        buf.write("\4\2\62;CH\3\2\62\63\3\2\629\3\2\63;\4\2\62;aa\5\2C\\")
        buf.write("aac|\4\2GGgg\4\2--//\6\2\n\f\16\17))^^\5\2\13\f\17\17")
        buf.write("\"\"\2\u010a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\3W\3\2\2\2\5p")
        buf.write("\3\2\2\2\7{\3\2\2\2\t}\3\2\2\2\13\u0085\3\2\2\2\r\u0089")
        buf.write("\3\2\2\2\17\u0091\3\2\2\2\21\u00a0\3\2\2\2\23\u00a2\3")
        buf.write("\2\2\2\25\u00a4\3\2\2\2\27\u00aa\3\2\2\2\31\u00b1\3\2")
        buf.write("\2\2\33\u00b4\3\2\2\2\35\u00b6\3\2\2\2\37\u00b8\3\2\2")
        buf.write("\2!\u00ba\3\2\2\2#\u00bc\3\2\2\2%\u00be\3\2\2\2\'\u00c0")
        buf.write("\3\2\2\2)\u00c2\3\2\2\2+\u00c4\3\2\2\2-\u00c6\3\2\2\2")
        buf.write("/\u00c8\3\2\2\2\61\u00ca\3\2\2\2\63\u00cd\3\2\2\2\65\u00d0")
        buf.write("\3\2\2\2\67\u00d2\3\2\2\29\u00d4\3\2\2\2;\u00d6\3\2\2")
        buf.write("\2=\u00d8\3\2\2\2?\u00da\3\2\2\2A\u00dd\3\2\2\2C\u00e0")
        buf.write("\3\2\2\2E\u00e2\3\2\2\2G\u00e5\3\2\2\2I\u00e8\3\2\2\2")
        buf.write("K\u00ea\3\2\2\2M\u00ee\3\2\2\2O\u00f2\3\2\2\2Q\u00f8\3")
        buf.write("\2\2\2S\u00fb\3\2\2\2U\u00fd\3\2\2\2W]\5\33\16\2X\\\5")
        buf.write("\31\r\2Y\\\5\35\17\2Z\\\13\2\2\2[X\3\2\2\2[Y\3\2\2\2[")
        buf.write("Z\3\2\2\2\\_\3\2\2\2]^\3\2\2\2][\3\2\2\2^`\3\2\2\2_]\3")
        buf.write("\2\2\2`a\5\33\16\2a\4\3\2\2\2bc\5\21\t\2ck\5!\21\2df\5")
        buf.write("\37\20\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2hj\3\2")
        buf.write("\2\2ig\3\2\2\2jl\5\21\t\2kg\3\2\2\2kl\3\2\2\2lq\3\2\2")
        buf.write("\2mn\5\21\t\2no\5\27\f\2oq\3\2\2\2pb\3\2\2\2pm\3\2\2\2")
        buf.write("q\6\3\2\2\2rs\7V\2\2st\7t\2\2tu\7w\2\2u|\7g\2\2vw\7H\2")
        buf.write("\2wx\7c\2\2xy\7n\2\2yz\7u\2\2z|\7g\2\2{r\3\2\2\2{v\3\2")
        buf.write("\2\2|\b\3\2\2\2}\u0082\5\23\n\2~\u0081\t\2\2\2\177\u0081")
        buf.write("\5\23\n\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081\u0084")
        buf.write("\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\n\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0086\7\62\2\2\u0086")
        buf.write("\u0087\t\3\2\2\u0087\u0088\t\4\2\2\u0088\f\3\2\2\2\u0089")
        buf.write("\u008a\7\62\2\2\u008a\u008b\7d\2\2\u008b\u008d\3\2\2\2")
        buf.write("\u008c\u008e\t\5\2\2\u008d\u008c\3\2\2\2\u008e\u008f\3")
        buf.write("\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\16")
        buf.write("\3\2\2\2\u0091\u0093\7\62\2\2\u0092\u0094\t\6\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\20\3\2\2\2\u0097\u009b\t\7")
        buf.write("\2\2\u0098\u009a\t\b\2\2\u0099\u0098\3\2\2\2\u009a\u009d")
        buf.write("\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a1\t\2\2\2")
        buf.write("\u009f\u00a1\t\2\2\2\u00a0\u0097\3\2\2\2\u00a0\u009f\3")
        buf.write("\2\2\2\u00a1\22\3\2\2\2\u00a2\u00a3\t\t\2\2\u00a3\24\3")
        buf.write("\2\2\2\u00a4\u00a5\7E\2\2\u00a5\u00a6\7n\2\2\u00a6\u00a7")
        buf.write("\7c\2\2\u00a7\u00a8\7u\2\2\u00a8\u00a9\7u\2\2\u00a9\26")
        buf.write("\3\2\2\2\u00aa\u00ae\t\n\2\2\u00ab\u00ad\t\13\2\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\30\3\2\2\2\u00b0\u00ae\3\2")
        buf.write("\2\2\u00b1\u00b2\7)\2\2\u00b2\u00b3\7$\2\2\u00b3\32\3")
        buf.write("\2\2\2\u00b4\u00b5\7$\2\2\u00b5\34\3\2\2\2\u00b6\u00b7")
        buf.write("\t\f\2\2\u00b7\36\3\2\2\2\u00b8\u00b9\7\62\2\2\u00b9 ")
        buf.write("\3\2\2\2\u00ba\u00bb\7\60\2\2\u00bb\"\3\2\2\2\u00bc\u00bd")
        buf.write("\7.\2\2\u00bd$\3\2\2\2\u00be\u00bf\7*\2\2\u00bf&\3\2\2")
        buf.write("\2\u00c0\u00c1\7+\2\2\u00c1(\3\2\2\2\u00c2\u00c3\7}\2")
        buf.write("\2\u00c3*\3\2\2\2\u00c4\u00c5\7\177\2\2\u00c5,\3\2\2\2")
        buf.write("\u00c6\u00c7\7=\2\2\u00c7.\3\2\2\2\u00c8\u00c9\7-\2\2")
        buf.write("\u00c9\60\3\2\2\2\u00ca\u00cb\7>\2\2\u00cb\u00cc\7?\2")
        buf.write("\2\u00cc\62\3\2\2\2\u00cd\u00ce\7@\2\2\u00ce\u00cf\7?")
        buf.write("\2\2\u00cf\64\3\2\2\2\u00d0\u00d1\7/\2\2\u00d1\66\3\2")
        buf.write("\2\2\u00d2\u00d3\7,\2\2\u00d38\3\2\2\2\u00d4\u00d5\7>")
        buf.write("\2\2\u00d5:\3\2\2\2\u00d6\u00d7\7\'\2\2\u00d7<\3\2\2\2")
        buf.write("\u00d8\u00d9\7\61\2\2\u00d9>\3\2\2\2\u00da\u00db\7#\2")
        buf.write("\2\u00db\u00dc\7?\2\2\u00dc@\3\2\2\2\u00dd\u00de\7?\2")
        buf.write("\2\u00de\u00df\7?\2\2\u00dfB\3\2\2\2\u00e0\u00e1\7@\2")
        buf.write("\2\u00e1D\3\2\2\2\u00e2\u00e3\7(\2\2\u00e3\u00e4\7(\2")
        buf.write("\2\u00e4F\3\2\2\2\u00e5\u00e6\7~\2\2\u00e6\u00e7\7~\2")
        buf.write("\2\u00e7H\3\2\2\2\u00e8\u00e9\7#\2\2\u00e9J\3\2\2\2\u00ea")
        buf.write("\u00eb\7?\2\2\u00eb\u00ec\7?\2\2\u00ec\u00ed\7\60\2\2")
        buf.write("\u00edL\3\2\2\2\u00ee\u00ef\7-\2\2\u00ef\u00f0\7\60\2")
        buf.write("\2\u00f0N\3\2\2\2\u00f1\u00f3\t\r\2\2\u00f2\u00f1\3\2")
        buf.write("\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5")
        buf.write("\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\b(\2\2\u00f7")
        buf.write("P\3\2\2\2\u00f8\u00f9\13\2\2\2\u00f9\u00fa\b)\3\2\u00fa")
        buf.write("R\3\2\2\2\u00fb\u00fc\13\2\2\2\u00fcT\3\2\2\2\u00fd\u00fe")
        buf.write("\13\2\2\2\u00feV\3\2\2\2\21\2[]gkp{\u0080\u0082\u008f")
        buf.write("\u0095\u009b\u00a0\u00ae\u00f4\4\b\2\2\3)\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING = 1
    FLOATLIT = 2
    BOOLIT = 3
    ID = 4
    INTLIT_16 = 5
    INTLIT_2 = 6
    INTLIT_8 = 7
    INTLIT_10 = 8
    CLASS = 9
    EXPONENT = 10
    ESCAPE_SEQ = 11
    ZERO = 12
    DOT = 13
    CM = 14
    LB = 15
    RB = 16
    LP = 17
    RP = 18
    SEMI = 19
    ADDOP = 20
    LESS_EQUAL = 21
    GREAT_EQUAL = 22
    SUBOP = 23
    MULOP = 24
    LESS_THAN = 25
    MODOP = 26
    DIVOP = 27
    NOT_EQUAL = 28
    EQUAL = 29
    GREAT_THAN = 30
    AND = 31
    OR = 32
    NEGATE = 33
    STR_CMP = 34
    STR_CONCAT = 35
    WS = 36
    ERROR_CHAR = 37
    UNCLOSE_STRING = 38
    ILLEGAL_ESCAPE = 39

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Class'", "'0'", "'.'", "','", "'('", "')'", "'{'", "'}'", 
            "';'", "'+'", "'<='", "'>='", "'-'", "'*'", "'<'", "'%'", "'/'", 
            "'!='", "'=='", "'>'", "'&&'", "'||'", "'!'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "FLOATLIT", "BOOLIT", "ID", "INTLIT_16", "INTLIT_2", 
            "INTLIT_8", "INTLIT_10", "CLASS", "EXPONENT", "ESCAPE_SEQ", 
            "ZERO", "DOT", "CM", "LB", "RB", "LP", "RP", "SEMI", "ADDOP", 
            "LESS_EQUAL", "GREAT_EQUAL", "SUBOP", "MULOP", "LESS_THAN", 
            "MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", "GREAT_THAN", "AND", 
            "OR", "NEGATE", "STR_CMP", "STR_CONCAT", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "STRING", "FLOATLIT", "BOOLIT", "ID", "INTLIT_16", "INTLIT_2", 
                  "INTLIT_8", "INTLIT_10", "LIT", "CLASS", "EXPONENT", "ESC_DOUB_QUOTE", 
                  "DOUB_QUOTE", "ESCAPE_SEQ", "ZERO", "DOT", "CM", "LB", 
                  "RB", "LP", "RP", "SEMI", "ADDOP", "LESS_EQUAL", "GREAT_EQUAL", 
                  "SUBOP", "MULOP", "LESS_THAN", "MODOP", "DIVOP", "NOT_EQUAL", 
                  "EQUAL", "GREAT_THAN", "AND", "OR", "NEGATE", "STR_CMP", 
                  "STR_CONCAT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[39] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


