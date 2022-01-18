# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u0082\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\6\4>\n\4")
        buf.write("\r\4\16\4?\3\4\3\4\6\4D\n\4\r\4\16\4E\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\5\17i\n\17\3\20\3\20\3\21\6\21n\n")
        buf.write("\21\r\21\16\21o\3\22\6\22s\n\22\r\22\16\22t\3\23\3\23")
        buf.write("\3\24\6\24z\n\24\r\24\16\24{\3\24\3\24\3\25\3\25\3\25")
        buf.write("\2\2\26\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26\3\2")
        buf.write("\5\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\2\u0087\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2\5\63\3\2\2\2\7=\3\2")
        buf.write("\2\2\tG\3\2\2\2\13N\3\2\2\2\rP\3\2\2\2\17R\3\2\2\2\21")
        buf.write("T\3\2\2\2\23V\3\2\2\2\25X\3\2\2\2\27Z\3\2\2\2\31\\\3\2")
        buf.write("\2\2\33^\3\2\2\2\35h\3\2\2\2\37j\3\2\2\2!m\3\2\2\2#r\3")
        buf.write("\2\2\2%v\3\2\2\2\'y\3\2\2\2)\177\3\2\2\2+,\7x\2\2,-\7")
        buf.write("c\2\2-.\7t\2\2./\7f\2\2/\60\7g\2\2\60\61\7e\2\2\61\62")
        buf.write("\7n\2\2\62\4\3\2\2\2\63\64\7h\2\2\64\65\7w\2\2\65\66\7")
        buf.write("p\2\2\66\67\7e\2\2\678\7f\2\289\7g\2\29:\7e\2\2:;\7n\2")
        buf.write("\2;\6\3\2\2\2<>\t\2\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2")
        buf.write("?@\3\2\2\2@A\3\2\2\2AC\7\60\2\2BD\t\2\2\2CB\3\2\2\2DE")
        buf.write("\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\b\3\2\2\2GH\7t\2\2HI\7g")
        buf.write("\2\2IJ\7v\2\2JK\7w\2\2KL\7t\2\2LM\7p\2\2M\n\3\2\2\2NO")
        buf.write("\7\61\2\2O\f\3\2\2\2PQ\7,\2\2Q\16\3\2\2\2RS\7-\2\2S\20")
        buf.write("\3\2\2\2TU\7/\2\2U\22\3\2\2\2VW\7?\2\2W\24\3\2\2\2XY\7")
        buf.write("*\2\2Y\26\3\2\2\2Z[\7+\2\2[\30\3\2\2\2\\]\7}\2\2]\32\3")
        buf.write("\2\2\2^_\7\177\2\2_\34\3\2\2\2`a\7k\2\2ab\7p\2\2bi\7v")
        buf.write("\2\2cd\7h\2\2de\7n\2\2ef\7q\2\2fg\7c\2\2gi\7v\2\2h`\3")
        buf.write("\2\2\2hc\3\2\2\2i\36\3\2\2\2jk\7.\2\2k \3\2\2\2ln\t\3")
        buf.write("\2\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2p\"\3\2\2")
        buf.write("\2qs\t\2\2\2rq\3\2\2\2st\3\2\2\2tr\3\2\2\2tu\3\2\2\2u")
        buf.write("$\3\2\2\2vw\7=\2\2w&\3\2\2\2xz\t\4\2\2yx\3\2\2\2z{\3\2")
        buf.write("\2\2{y\3\2\2\2{|\3\2\2\2|}\3\2\2\2}~\b\24\2\2~(\3\2\2")
        buf.write("\2\177\u0080\13\2\2\2\u0080\u0081\b\25\3\2\u0081*\3\2")
        buf.write("\2\2\t\2?Ehot{\4\b\2\2\3\25\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    FLOATLIT = 3
    RET = 4
    DIVOP = 5
    MULOP = 6
    ADDOP = 7
    MINOP = 8
    EQUAL = 9
    LB = 10
    RB = 11
    LP = 12
    RP = 13
    VARTYPE = 14
    CM = 15
    ID = 16
    INTLIT = 17
    SEMI = 18
    WS = 19
    ERROR_CHAR = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'vardecl'", "'funcdecl'", "'return'", "'/'", "'*'", "'+'", 
            "'-'", "'='", "'('", "')'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "FLOATLIT", "RET", "DIVOP", "MULOP", "ADDOP", "MINOP", "EQUAL", 
            "LB", "RB", "LP", "RP", "VARTYPE", "CM", "ID", "INTLIT", "SEMI", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "FLOATLIT", "RET", "DIVOP", "MULOP", "ADDOP", 
                  "MINOP", "EQUAL", "LB", "RB", "LP", "RP", "VARTYPE", "CM", 
                  "ID", "INTLIT", "SEMI", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[19] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


