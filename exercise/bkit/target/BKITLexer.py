# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("\61\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4\3\5\6\5")
        buf.write(")\n\5\r\5\16\5*\3\5\3\5\3\6\3\6\3\6\2\2\7\3\3\5\2\7\2")
        buf.write("\t\4\13\5\3\2\6\3\2\63;\3\2\62\67\3\2\62;\5\2\13\f\17")
        buf.write("\17\"\"\2\63\2\3\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\r")
        buf.write("\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t(\3\2\2\2\13.\3\2\2\2")
        buf.write("\r\16\5\5\3\2\16\17\7\60\2\2\17\20\5\5\3\2\20\21\7\60")
        buf.write("\2\2\21\22\5\5\3\2\22\23\7\60\2\2\23\24\5\5\3\2\24\4\3")
        buf.write("\2\2\2\25$\5\7\4\2\26\27\t\2\2\2\27$\5\7\4\2\30\31\7\63")
        buf.write("\2\2\31\32\5\7\4\2\32\33\5\7\4\2\33$\3\2\2\2\34\35\7\64")
        buf.write("\2\2\35\36\t\3\2\2\36$\5\7\4\2\37 \7\64\2\2 !\7\67\2\2")
        buf.write("!\"\3\2\2\2\"$\t\3\2\2#\25\3\2\2\2#\26\3\2\2\2#\30\3\2")
        buf.write("\2\2#\34\3\2\2\2#\37\3\2\2\2$\6\3\2\2\2%&\t\4\2\2&\b\3")
        buf.write("\2\2\2\')\t\5\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2")
        buf.write("\2\2+,\3\2\2\2,-\b\5\2\2-\n\3\2\2\2./\13\2\2\2/\60\b\6")
        buf.write("\3\2\60\f\3\2\2\2\5\2#*\4\b\2\2\3\6\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADDRS = 1
    WS = 2
    ERROR_CHAR = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ADDRS", "WS", "ERROR_CHAR" ]

    ruleNames = [ "ADDRS", "NUM", "DIGIT", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


