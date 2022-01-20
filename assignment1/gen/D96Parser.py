# Generated from C:/Users/ADMIN/Documents/GitHub/HCMUT-PPL/assignment1/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3)")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\5\b\64")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\t\5\t;\n\t\3\n\3\n\3\n\5\n@\n\n")
        buf.write("\3\13\3\13\3\13\3\13\5\13F\n\13\3\f\3\f\3\f\5\fK\n\f\3")
        buf.write("\r\3\r\3\r\3\r\5\rQ\n\r\3\16\3\16\3\16\5\16V\n\16\3\17")
        buf.write("\3\17\3\17\3\17\5\17\\\n\17\3\20\3\20\3\20\3\20\5\20b")
        buf.write("\n\20\3\21\3\21\3\21\2\2\22\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \2\b\3\2$%\4\2\36\37!#\4\2\33\33\36 \3\2")
        buf.write("\26\37\4\2\26\33\36\36\3\2\7\n\2`\2\"\3\2\2\2\4%\3\2\2")
        buf.write("\2\6\'\3\2\2\2\b)\3\2\2\2\n+\3\2\2\2\f-\3\2\2\2\16\63")
        buf.write("\3\2\2\2\20:\3\2\2\2\22?\3\2\2\2\24E\3\2\2\2\26J\3\2\2")
        buf.write("\2\30P\3\2\2\2\32U\3\2\2\2\34[\3\2\2\2\36a\3\2\2\2 c\3")
        buf.write("\2\2\2\"#\7\3\2\2#$\7\2\2\3$\3\3\2\2\2%&\t\2\2\2&\5\3")
        buf.write("\2\2\2\'(\t\3\2\2(\7\3\2\2\2)*\t\4\2\2*\t\3\2\2\2+,\t")
        buf.write("\5\2\2,\13\3\2\2\2-.\t\6\2\2.\r\3\2\2\2/\64\3\2\2\2\60")
        buf.write("\61\5 \21\2\61\62\5\20\t\2\62\64\3\2\2\2\63/\3\2\2\2\63")
        buf.write("\60\3\2\2\2\64\17\3\2\2\2\65;\3\2\2\2\66\67\7\20\2\2\67")
        buf.write("8\5 \21\289\5\20\t\29;\3\2\2\2:\65\3\2\2\2:\66\3\2\2\2")
        buf.write(";\21\3\2\2\2<@\3\2\2\2=>\7\5\2\2>@\5\24\13\2?<\3\2\2\2")
        buf.write("?=\3\2\2\2@\23\3\2\2\2AF\3\2\2\2BC\7\20\2\2CD\7\5\2\2")
        buf.write("DF\5\24\13\2EA\3\2\2\2EB\3\2\2\2F\25\3\2\2\2GK\3\2\2\2")
        buf.write("HI\7\4\2\2IK\5\30\r\2JG\3\2\2\2JH\3\2\2\2K\27\3\2\2\2")
        buf.write("LQ\3\2\2\2MN\7\20\2\2NO\7\4\2\2OQ\5\30\r\2PL\3\2\2\2P")
        buf.write("M\3\2\2\2Q\31\3\2\2\2RV\3\2\2\2ST\7\3\2\2TV\5\34\17\2")
        buf.write("UR\3\2\2\2US\3\2\2\2V\33\3\2\2\2W\\\3\2\2\2XY\7\20\2\2")
        buf.write("YZ\7\3\2\2Z\\\5\34\17\2[W\3\2\2\2[X\3\2\2\2\\\35\3\2\2")
        buf.write("\2]b\7\4\2\2^b\7\5\2\2_b\7\3\2\2`b\5 \21\2a]\3\2\2\2a")
        buf.write("^\3\2\2\2a_\3\2\2\2a`\3\2\2\2b\37\3\2\2\2cd\t\7\2\2d!")
        buf.write("\3\2\2\2\13\63:?EJPU[a")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Class'", "<INVALID>", "<INVALID>", "'0'", 
                     "'.'", "','", "'('", "')'", "'{'", "'}'", "';'", "'+'", 
                     "'<='", "'>='", "'-'", "'*'", "'<'", "'%'", "'/'", 
                     "'!='", "'=='", "'>'", "'&&'", "'||'", "'!'", "'==.'", 
                     "'+.'" ]

    symbolicNames = [ "<INVALID>", "STRING", "FLOATLIT", "BOOLIT", "ID", 
                      "INTLIT_16", "INTLIT_2", "INTLIT_8", "INTLIT_10", 
                      "CLASS", "EXPONENT", "ESCAPE_SEQ", "ZERO", "DOT", 
                      "CM", "LB", "RB", "LP", "RP", "SEMI", "ADDOP", "LESS_EQUAL", 
                      "GREAT_EQUAL", "SUBOP", "MULOP", "LESS_THAN", "MODOP", 
                      "DIVOP", "NOT_EQUAL", "EQUAL", "GREAT_THAN", "AND", 
                      "OR", "NEGATE", "STR_CMP", "STR_CONCAT", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_string_op = 1
    RULE_bool_op = 2
    RULE_relation_op = 3
    RULE_int_op = 4
    RULE_float_op = 5
    RULE_int_gen_list = 6
    RULE_int_gen_cm = 7
    RULE_bool_list = 8
    RULE_bool_list_cm = 9
    RULE_float_list = 10
    RULE_float_list_cm = 11
    RULE_string_list = 12
    RULE_string_list_cm = 13
    RULE_lit = 14
    RULE_int_gen = 15

    ruleNames =  [ "program", "string_op", "bool_op", "relation_op", "int_op", 
                   "float_op", "int_gen_list", "int_gen_cm", "bool_list", 
                   "bool_list_cm", "float_list", "float_list_cm", "string_list", 
                   "string_list_cm", "lit", "int_gen" ]

    EOF = Token.EOF
    STRING=1
    FLOATLIT=2
    BOOLIT=3
    ID=4
    INTLIT_16=5
    INTLIT_2=6
    INTLIT_8=7
    INTLIT_10=8
    CLASS=9
    EXPONENT=10
    ESCAPE_SEQ=11
    ZERO=12
    DOT=13
    CM=14
    LB=15
    RB=16
    LP=17
    RP=18
    SEMI=19
    ADDOP=20
    LESS_EQUAL=21
    GREAT_EQUAL=22
    SUBOP=23
    MULOP=24
    LESS_THAN=25
    MODOP=26
    DIVOP=27
    NOT_EQUAL=28
    EQUAL=29
    GREAT_THAN=30
    AND=31
    OR=32
    NEGATE=33
    STR_CMP=34
    STR_CONCAT=35
    WS=36
    ERROR_CHAR=37
    UNCLOSE_STRING=38
    ILLEGAL_ESCAPE=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(D96Parser.STRING)
            self.state = 33
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR_CMP(self):
            return self.getToken(D96Parser.STR_CMP, 0)

        def STR_CONCAT(self):
            return self.getToken(D96Parser.STR_CONCAT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_string_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_op" ):
                listener.enterString_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_op" ):
                listener.exitString_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_op" ):
                return visitor.visitString_op(self)
            else:
                return visitor.visitChildren(self)




    def string_op(self):

        localctx = D96Parser.String_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_string_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            _la = self._input.LA(1)
            if not(_la==D96Parser.STR_CMP or _la==D96Parser.STR_CONCAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEGATE(self):
            return self.getToken(D96Parser.NEGATE, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_bool_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_op" ):
                listener.enterBool_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_op" ):
                listener.exitBool_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_op" ):
                return visitor.visitBool_op(self)
            else:
                return visitor.visitChildren(self)




    def bool_op(self):

        localctx = D96Parser.Bool_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bool_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.EQUAL) | (1 << D96Parser.AND) | (1 << D96Parser.OR) | (1 << D96Parser.NEGATE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relation_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS_THAN(self):
            return self.getToken(D96Parser.LESS_THAN, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def GREAT_THAN(self):
            return self.getToken(D96Parser.GREAT_THAN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relation_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation_op" ):
                listener.enterRelation_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation_op" ):
                listener.exitRelation_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_op" ):
                return visitor.visitRelation_op(self)
            else:
                return visitor.visitChildren(self)




    def relation_op(self):

        localctx = D96Parser.Relation_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_relation_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.LESS_THAN) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.EQUAL) | (1 << D96Parser.GREAT_THAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADDOP(self):
            return self.getToken(D96Parser.ADDOP, 0)

        def LESS_EQUAL(self):
            return self.getToken(D96Parser.LESS_EQUAL, 0)

        def GREAT_EQUAL(self):
            return self.getToken(D96Parser.GREAT_EQUAL, 0)

        def SUBOP(self):
            return self.getToken(D96Parser.SUBOP, 0)

        def MULOP(self):
            return self.getToken(D96Parser.MULOP, 0)

        def LESS_THAN(self):
            return self.getToken(D96Parser.LESS_THAN, 0)

        def MODOP(self):
            return self.getToken(D96Parser.MODOP, 0)

        def DIVOP(self):
            return self.getToken(D96Parser.DIVOP, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_int_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_op" ):
                listener.enterInt_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_op" ):
                listener.exitInt_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_op" ):
                return visitor.visitInt_op(self)
            else:
                return visitor.visitChildren(self)




    def int_op(self):

        localctx = D96Parser.Int_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_int_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ADDOP) | (1 << D96Parser.LESS_EQUAL) | (1 << D96Parser.GREAT_EQUAL) | (1 << D96Parser.SUBOP) | (1 << D96Parser.MULOP) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.MODOP) | (1 << D96Parser.DIVOP) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADDOP(self):
            return self.getToken(D96Parser.ADDOP, 0)

        def LESS_EQUAL(self):
            return self.getToken(D96Parser.LESS_EQUAL, 0)

        def GREAT_EQUAL(self):
            return self.getToken(D96Parser.GREAT_EQUAL, 0)

        def SUBOP(self):
            return self.getToken(D96Parser.SUBOP, 0)

        def MULOP(self):
            return self.getToken(D96Parser.MULOP, 0)

        def LESS_THAN(self):
            return self.getToken(D96Parser.LESS_THAN, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_float_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_op" ):
                listener.enterFloat_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_op" ):
                listener.exitFloat_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_op" ):
                return visitor.visitFloat_op(self)
            else:
                return visitor.visitChildren(self)




    def float_op(self):

        localctx = D96Parser.Float_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_float_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ADDOP) | (1 << D96Parser.LESS_EQUAL) | (1 << D96Parser.GREAT_EQUAL) | (1 << D96Parser.SUBOP) | (1 << D96Parser.MULOP) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.NOT_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_gen_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_gen(self):
            return self.getTypedRuleContext(D96Parser.Int_genContext,0)


        def int_gen_cm(self):
            return self.getTypedRuleContext(D96Parser.Int_gen_cmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_int_gen_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_gen_list" ):
                listener.enterInt_gen_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_gen_list" ):
                listener.exitInt_gen_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_gen_list" ):
                return visitor.visitInt_gen_list(self)
            else:
                return visitor.visitChildren(self)




    def int_gen_list(self):

        localctx = D96Parser.Int_gen_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_int_gen_list)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.int_gen()
                self.state = 47
                self.int_gen_cm()
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


    class Int_gen_cmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def int_gen(self):
            return self.getTypedRuleContext(D96Parser.Int_genContext,0)


        def int_gen_cm(self):
            return self.getTypedRuleContext(D96Parser.Int_gen_cmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_int_gen_cm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_gen_cm" ):
                listener.enterInt_gen_cm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_gen_cm" ):
                listener.exitInt_gen_cm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_gen_cm" ):
                return visitor.visitInt_gen_cm(self)
            else:
                return visitor.visitChildren(self)




    def int_gen_cm(self):

        localctx = D96Parser.Int_gen_cmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_int_gen_cm)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(D96Parser.CM)
                self.state = 53
                self.int_gen()
                self.state = 54
                self.int_gen_cm()
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


    class Bool_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLIT(self):
            return self.getToken(D96Parser.BOOLIT, 0)

        def bool_list_cm(self):
            return self.getTypedRuleContext(D96Parser.Bool_list_cmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_bool_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_list" ):
                listener.enterBool_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_list" ):
                listener.exitBool_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_list" ):
                return visitor.visitBool_list(self)
            else:
                return visitor.visitChildren(self)




    def bool_list(self):

        localctx = D96Parser.Bool_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bool_list)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(D96Parser.BOOLIT)
                self.state = 60
                self.bool_list_cm()
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


    class Bool_list_cmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def BOOLIT(self):
            return self.getToken(D96Parser.BOOLIT, 0)

        def bool_list_cm(self):
            return self.getTypedRuleContext(D96Parser.Bool_list_cmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_bool_list_cm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_list_cm" ):
                listener.enterBool_list_cm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_list_cm" ):
                listener.exitBool_list_cm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_list_cm" ):
                return visitor.visitBool_list_cm(self)
            else:
                return visitor.visitChildren(self)




    def bool_list_cm(self):

        localctx = D96Parser.Bool_list_cmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bool_list_cm)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(D96Parser.CM)
                self.state = 65
                self.match(D96Parser.BOOLIT)
                self.state = 66
                self.bool_list_cm()
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


    class Float_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def float_list_cm(self):
            return self.getTypedRuleContext(D96Parser.Float_list_cmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_float_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_list" ):
                listener.enterFloat_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_list" ):
                listener.exitFloat_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_list" ):
                return visitor.visitFloat_list(self)
            else:
                return visitor.visitChildren(self)




    def float_list(self):

        localctx = D96Parser.Float_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_float_list)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(D96Parser.FLOATLIT)
                self.state = 71
                self.float_list_cm()
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


    class Float_list_cmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def float_list_cm(self):
            return self.getTypedRuleContext(D96Parser.Float_list_cmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_float_list_cm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_list_cm" ):
                listener.enterFloat_list_cm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_list_cm" ):
                listener.exitFloat_list_cm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_list_cm" ):
                return visitor.visitFloat_list_cm(self)
            else:
                return visitor.visitChildren(self)




    def float_list_cm(self):

        localctx = D96Parser.Float_list_cmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_float_list_cm)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(D96Parser.CM)
                self.state = 76
                self.match(D96Parser.FLOATLIT)
                self.state = 77
                self.float_list_cm()
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


    class String_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def string_list_cm(self):
            return self.getTypedRuleContext(D96Parser.String_list_cmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_string_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_list" ):
                listener.enterString_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_list" ):
                listener.exitString_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_list" ):
                return visitor.visitString_list(self)
            else:
                return visitor.visitChildren(self)




    def string_list(self):

        localctx = D96Parser.String_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_string_list)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(D96Parser.STRING)
                self.state = 82
                self.string_list_cm()
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


    class String_list_cmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def string_list_cm(self):
            return self.getTypedRuleContext(D96Parser.String_list_cmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_string_list_cm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_list_cm" ):
                listener.enterString_list_cm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_list_cm" ):
                listener.exitString_list_cm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_list_cm" ):
                return visitor.visitString_list_cm(self)
            else:
                return visitor.visitChildren(self)




    def string_list_cm(self):

        localctx = D96Parser.String_list_cmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_string_list_cm)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(D96Parser.CM)
                self.state = 87
                self.match(D96Parser.STRING)
                self.state = 88
                self.string_list_cm()
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


    class LitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def BOOLIT(self):
            return self.getToken(D96Parser.BOOLIT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def int_gen(self):
            return self.getTypedRuleContext(D96Parser.Int_genContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLit" ):
                listener.enterLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLit" ):
                listener.exitLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = D96Parser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_lit)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(D96Parser.BOOLIT)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.int_gen()
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


    class Int_genContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT_16(self):
            return self.getToken(D96Parser.INTLIT_16, 0)

        def INTLIT_2(self):
            return self.getToken(D96Parser.INTLIT_2, 0)

        def INTLIT_8(self):
            return self.getToken(D96Parser.INTLIT_8, 0)

        def INTLIT_10(self):
            return self.getToken(D96Parser.INTLIT_10, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_int_gen

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_gen" ):
                listener.enterInt_gen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_gen" ):
                listener.exitInt_gen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_gen" ):
                return visitor.visitInt_gen(self)
            else:
                return visitor.visitChildren(self)




    def int_gen(self):

        localctx = D96Parser.Int_genContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_int_gen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT_16) | (1 << D96Parser.INTLIT_2) | (1 << D96Parser.INTLIT_8) | (1 << D96Parser.INTLIT_10))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





