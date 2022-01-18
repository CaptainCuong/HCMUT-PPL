# Generated from BKIT.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("G\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\5\2\30\n\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\5\2\37\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2")
        buf.write("(\n\2\3\3\3\3\5\3,\n\3\3\4\6\4/\n\4\r\4\16\4\60\3\5\3")
        buf.write("\5\7\5\65\n\5\f\5\16\58\13\5\3\6\6\6;\n\6\r\6\16\6<\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\2\2\n\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\3\2\4\3\2\62;\5\2\13\f\17\17\"\"")
        buf.write("\2P\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\'")
        buf.write("\3\2\2\2\5)\3\2\2\2\7.\3\2\2\2\t\62\3\2\2\2\13:\3\2\2")
        buf.write("\2\r@\3\2\2\2\17C\3\2\2\2\21E\3\2\2\2\23(\5\5\3\2\24\25")
        buf.write("\5\5\3\2\25\27\7g\2\2\26\30\7/\2\2\27\26\3\2\2\2\27\30")
        buf.write("\3\2\2\2\30\31\3\2\2\2\31\32\5\7\4\2\32(\3\2\2\2\33\34")
        buf.write("\5\7\4\2\34\36\7g\2\2\35\37\7/\2\2\36\35\3\2\2\2\36\37")
        buf.write("\3\2\2\2\37 \3\2\2\2 !\5\7\4\2!(\3\2\2\2\"#\7g\2\2#$\7")
        buf.write("/\2\2$(\5\7\4\2%&\7g\2\2&(\5\7\4\2\'\23\3\2\2\2\'\24\3")
        buf.write("\2\2\2\'\33\3\2\2\2\'\"\3\2\2\2\'%\3\2\2\2(\4\3\2\2\2")
        buf.write(")+\5\7\4\2*,\5\t\5\2+*\3\2\2\2+,\3\2\2\2,\6\3\2\2\2-/")
        buf.write("\t\2\2\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2")
        buf.write("\2\61\b\3\2\2\2\62\66\7\60\2\2\63\65\t\2\2\2\64\63\3\2")
        buf.write("\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67\n\3\2")
        buf.write("\2\28\66\3\2\2\29;\t\3\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2")
        buf.write("\2<=\3\2\2\2=>\3\2\2\2>?\b\6\2\2?\f\3\2\2\2@A\13\2\2\2")
        buf.write("AB\b\7\3\2B\16\3\2\2\2CD\13\2\2\2D\20\3\2\2\2EF\13\2\2")
        buf.write("\2F\22\3\2\2\2\n\2\27\36\'+\60\66<\4\b\2\2\3\7\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SCI_FLOAT = 1
    FLOAT = 2
    REAL = 3
    DECIMAL = 4
    WS = 5
    ERROR_CHAR = 6
    UNCLOSE_STRING = 7
    ILLEGAL_ESCAPE = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "SCI_FLOAT", "FLOAT", "REAL", "DECIMAL", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "SCI_FLOAT", "FLOAT", "REAL", "DECIMAL", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[5] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


