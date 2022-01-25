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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0255\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\3\2\3\2\3\2\3\3\3\3\7\3\u008e\n\3\f\3\16\3\u0091\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u0099\n\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\7\5\u00a0\n\5\f\5\16\5\u00a3\13\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00af\n\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6\u00b6\n\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00be")
        buf.write("\n\7\3\7\3\7\3\7\3\7\3\7\5\7\u00c5\n\7\3\b\5\b\u00c8\n")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u00d4\n")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\5\n\u00db\n\n\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00e7\n\f\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00ed\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00f8\n\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\7\16\u0108\n\16\f\16\16\16")
        buf.write("\u010b\13\16\3\16\3\16\5\16\u010f\n\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\5\20\u0119\n\20\3\21\3\21\3")
        buf.write("\22\3\22\3\23\3\23\3\23\5\23\u0122\n\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\5\25\u012c\n\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0138\n\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u0144\n\27\3\30\3\30\3\30\3\30\5\30\u014a\n\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u0151\n\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u0163\n\32\3\32\3\32\3\32\3\32\7\32\u0169\n")
        buf.write("\32\f\32\16\32\u016c\13\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u018a\n\36\3\37\3\37\5\37\u018e\n\37\3 \3 ")
        buf.write("\3 \3 \3!\3!\3!\3!\3!\3\"\3\"\5\"\u019b\n\"\3\"\3\"\3")
        buf.write("\"\3\"\6\"\u01a1\n\"\r\"\16\"\u01a2\3#\3#\3#\5#\u01a8")
        buf.write("\n#\3$\3$\3$\5$\u01ad\n$\3%\3%\3%\3%\5%\u01b3\n%\3&\3")
        buf.write("&\3&\3&\3&\5&\u01ba\n&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3(\3)\3)\3)\3)\5)\u01ca\n)\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3/\3/\5/\u01da\n/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u01e1\n\60\3\61\3\61\5\61\u01e5\n\61\3\61\3\61\5")
        buf.write("\61\u01e9\n\61\3\62\3\62\3\62\5\62\u01ee\n\62\3\62\3\62")
        buf.write("\5\62\u01f2\n\62\3\63\3\63\3\63\5\63\u01f7\n\63\3\64\3")
        buf.write("\64\3\64\3\64\5\64\u01fd\n\64\3\65\3\65\3\65\3\65\5\65")
        buf.write("\u0203\n\65\3\66\3\66\3\66\3\66\3\66\5\66\u020a\n\66\3")
        buf.write("\67\3\67\3\67\5\67\u020f\n\67\38\38\38\38\58\u0215\n8")
        buf.write("\39\39\39\39\59\u021b\n9\3:\3:\3:\3:\3:\5:\u0222\n:\3")
        buf.write(";\3;\3;\5;\u0227\n;\3<\3<\3<\3<\5<\u022d\n<\3=\3=\3=\3")
        buf.write("=\5=\u0233\n=\3>\3>\3?\3?\3@\3@\3A\3A\3A\3A\3A\3A\3A\3")
        buf.write("B\3B\3C\3C\3D\3D\3D\7D\u0249\nD\fD\16D\u024c\13D\3D\5")
        buf.write("D\u024f\nD\3D\3D\5D\u0253\nD\3D\3\u008f\3\62E\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\2\f\4\2\20\21\"\"\3\2=>\4\2\678:<\4\2\64\64\67")
        buf.write("9\3\2/8\4\2/\64\67\67\3\2\33\36\3\2\30\32\4\2\62\62<<")
        buf.write("\4\2/;=>\2\u025d\2\u0088\3\2\2\2\4\u008b\3\2\2\2\6\u0094")
        buf.write("\3\2\2\2\b\u009c\3\2\2\2\n\u00b5\3\2\2\2\f\u00c4\3\2\2")
        buf.write("\2\16\u00c7\3\2\2\2\20\u00d3\3\2\2\2\22\u00da\3\2\2\2")
        buf.write("\24\u00dc\3\2\2\2\26\u00ec\3\2\2\2\30\u00ee\3\2\2\2\32")
        buf.write("\u00fc\3\2\2\2\34\u0110\3\2\2\2\36\u0118\3\2\2\2 \u011a")
        buf.write("\3\2\2\2\"\u011c\3\2\2\2$\u0121\3\2\2\2&\u0126\3\2\2\2")
        buf.write("(\u012b\3\2\2\2*\u0137\3\2\2\2,\u0143\3\2\2\2.\u0149\3")
        buf.write("\2\2\2\60\u0150\3\2\2\2\62\u0162\3\2\2\2\64\u016d\3\2")
        buf.write("\2\2\66\u0173\3\2\2\28\u017a\3\2\2\2:\u0189\3\2\2\2<\u018d")
        buf.write("\3\2\2\2>\u018f\3\2\2\2@\u0193\3\2\2\2B\u019a\3\2\2\2")
        buf.write("D\u01a7\3\2\2\2F\u01ac\3\2\2\2H\u01b2\3\2\2\2J\u01b9\3")
        buf.write("\2\2\2L\u01bb\3\2\2\2N\u01c0\3\2\2\2P\u01c9\3\2\2\2R\u01cb")
        buf.write("\3\2\2\2T\u01cd\3\2\2\2V\u01cf\3\2\2\2X\u01d1\3\2\2\2")
        buf.write("Z\u01d3\3\2\2\2\\\u01d9\3\2\2\2^\u01e0\3\2\2\2`\u01e8")
        buf.write("\3\2\2\2b\u01f1\3\2\2\2d\u01f6\3\2\2\2f\u01fc\3\2\2\2")
        buf.write("h\u0202\3\2\2\2j\u0209\3\2\2\2l\u020e\3\2\2\2n\u0214\3")
        buf.write("\2\2\2p\u021a\3\2\2\2r\u0221\3\2\2\2t\u0226\3\2\2\2v\u022c")
        buf.write("\3\2\2\2x\u0232\3\2\2\2z\u0234\3\2\2\2|\u0236\3\2\2\2")
        buf.write("~\u0238\3\2\2\2\u0080\u023a\3\2\2\2\u0082\u0241\3\2\2")
        buf.write("\2\u0084\u0243\3\2\2\2\u0086\u0252\3\2\2\2\u0088\u0089")
        buf.write("\7\3\2\2\u0089\u008a\7\2\2\3\u008a\3\3\2\2\2\u008b\u008f")
        buf.write("\7\7\2\2\u008c\u008e\13\2\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\u0091\3\2\2\2\u008f\u0090\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u0090\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\7")
        buf.write("\7\2\2\u0093\5\3\2\2\2\u0094\u0095\7\22\2\2\u0095\u0098")
        buf.write("\7\"\2\2\u0096\u0097\7-\2\2\u0097\u0099\5d\63\2\u0098")
        buf.write("\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009b\5\b\5\2\u009b\7\3\2\2\2\u009c\u00a1\7*\2")
        buf.write("\2\u009d\u00a0\5\n\6\2\u009e\u00a0\5\16\b\2\u009f\u009d")
        buf.write("\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a4\u00a5\7+\2\2\u00a5\t\3\2\2")
        buf.write("\2\u00a6\u00a7\7\25\2\2\u00a7\u00a8\5`\61\2\u00a8\u00a9")
        buf.write("\7-\2\2\u00a9\u00aa\5|?\2\u00aa\u00ab\7.\2\2\u00ab\u00b6")
        buf.write("\3\2\2\2\u00ac\u00ae\7\25\2\2\u00ad\u00af\7\26\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\3\2\2\2")
        buf.write("\u00b0\u00b1\7\"\2\2\u00b1\u00b2\5\f\7\2\u00b2\u00b3\5")
        buf.write("\62\32\2\u00b3\u00b4\7.\2\2\u00b4\u00b6\3\2\2\2\u00b5")
        buf.write("\u00a6\3\2\2\2\u00b5\u00ac\3\2\2\2\u00b6\13\3\2\2\2\u00b7")
        buf.write("\u00b8\7-\2\2\u00b8\u00b9\5|?\2\u00b9\u00ba\7\b\2\2\u00ba")
        buf.write("\u00c5\3\2\2\2\u00bb\u00bd\7%\2\2\u00bc\u00be\7\26\2\2")
        buf.write("\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\3")
        buf.write("\2\2\2\u00bf\u00c0\7\"\2\2\u00c0\u00c1\5\f\7\2\u00c1\u00c2")
        buf.write("\5\62\32\2\u00c2\u00c3\7%\2\2\u00c3\u00c5\3\2\2\2\u00c4")
        buf.write("\u00b7\3\2\2\2\u00c4\u00bb\3\2\2\2\u00c5\r\3\2\2\2\u00c6")
        buf.write("\u00c8\7\26\2\2\u00c7\u00c6\3\2\2\2\u00c7\u00c8\3\2\2")
        buf.write("\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\t\2\2\2\u00ca\u00cb")
        buf.write("\7(\2\2\u00cb\u00cc\5\22\n\2\u00cc\u00cd\7)\2\2\u00cd")
        buf.write("\u00ce\5\34\17\2\u00ce\17\3\2\2\2\u00cf\u00d4\3\2\2\2")
        buf.write("\u00d0\u00d1\5\24\13\2\u00d1\u00d2\5\22\n\2\u00d2\u00d4")
        buf.write("\3\2\2\2\u00d3\u00cf\3\2\2\2\u00d3\u00d0\3\2\2\2\u00d4")
        buf.write("\21\3\2\2\2\u00d5\u00db\3\2\2\2\u00d6\u00d7\7.\2\2\u00d7")
        buf.write("\u00d8\5\24\13\2\u00d8\u00d9\5\22\n\2\u00d9\u00db\3\2")
        buf.write("\2\2\u00da\u00d5\3\2\2\2\u00da\u00d6\3\2\2\2\u00db\23")
        buf.write("\3\2\2\2\u00dc\u00dd\5d\63\2\u00dd\u00de\7-\2\2\u00de")
        buf.write("\u00df\5|?\2\u00df\25\3\2\2\2\u00e0\u00e7\5$\23\2\u00e1")
        buf.write("\u00e7\5*\26\2\u00e2\u00e7\5\"\22\2\u00e3\u00e7\5 \21")
        buf.write("\2\u00e4\u00e7\5&\24\2\u00e5\u00e7\5(\25\2\u00e6\u00e0")
        buf.write("\3\2\2\2\u00e6\u00e1\3\2\2\2\u00e6\u00e2\3\2\2\2\u00e6")
        buf.write("\u00e3\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\u00e9\7.\2\2\u00e9\u00ed\3")
        buf.write("\2\2\2\u00ea\u00ed\5\32\16\2\u00eb\u00ed\5\30\r\2\u00ec")
        buf.write("\u00e6\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ed\27\3\2\2\2\u00ee\u00ef\7\16\2\2\u00ef\u00f0\7(")
        buf.write("\2\2\u00f0\u00f1\7\"\2\2\u00f1\u00f2\7\17\2\2\u00f2\u00f3")
        buf.write("\5\62\32\2\u00f3\u00f4\7,\2\2\u00f4\u00f7\5\62\32\2\u00f5")
        buf.write("\u00f6\7\23\2\2\u00f6\u00f8\5\62\32\2\u00f7\u00f5\3\2")
        buf.write("\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa")
        buf.write("\7)\2\2\u00fa\u00fb\5\34\17\2\u00fb\31\3\2\2\2\u00fc\u00fd")
        buf.write("\7\13\2\2\u00fd\u00fe\7(\2\2\u00fe\u00ff\5\62\32\2\u00ff")
        buf.write("\u0100\7)\2\2\u0100\u0109\5\34\17\2\u0101\u0102\7\r\2")
        buf.write("\2\u0102\u0103\7(\2\2\u0103\u0104\5\62\32\2\u0104\u0105")
        buf.write("\7)\2\2\u0105\u0106\5\34\17\2\u0106\u0108\3\2\2\2\u0107")
        buf.write("\u0101\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2")
        buf.write("\u0109\u010a\3\2\2\2\u010a\u010e\3\2\2\2\u010b\u0109\3")
        buf.write("\2\2\2\u010c\u010d\7\f\2\2\u010d\u010f\5\34\17\2\u010e")
        buf.write("\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\33\3\2\2\2\u0110")
        buf.write("\u0111\7*\2\2\u0111\u0112\5\36\20\2\u0112\u0113\7+\2\2")
        buf.write("\u0113\35\3\2\2\2\u0114\u0119\3\2\2\2\u0115\u0116\5\26")
        buf.write("\f\2\u0116\u0117\5\36\20\2\u0117\u0119\3\2\2\2\u0118\u0114")
        buf.write("\3\2\2\2\u0118\u0115\3\2\2\2\u0119\37\3\2\2\2\u011a\u011b")
        buf.write("\7\n\2\2\u011b!\3\2\2\2\u011c\u011d\7\t\2\2\u011d#\3\2")
        buf.write("\2\2\u011e\u0122\7\"\2\2\u011f\u0122\5<\37\2\u0120\u0122")
        buf.write("\5B\"\2\u0121\u011e\3\2\2\2\u0121\u011f\3\2\2\2\u0121")
        buf.write("\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\7\b\2\2")
        buf.write("\u0124\u0125\5\62\32\2\u0125%\3\2\2\2\u0126\u0127\7\6")
        buf.write("\2\2\u0127\u0128\5\62\32\2\u0128\'\3\2\2\2\u0129\u012c")
        buf.write("\5\66\34\2\u012a\u012c\58\35\2\u012b\u0129\3\2\2\2\u012b")
        buf.write("\u012a\3\2\2\2\u012c)\3\2\2\2\u012d\u012e\7\25\2\2\u012e")
        buf.write("\u012f\5d\63\2\u012f\u0130\7-\2\2\u0130\u0131\5|?\2\u0131")
        buf.write("\u0138\3\2\2\2\u0132\u0133\7\25\2\2\u0133\u0134\7\"\2")
        buf.write("\2\u0134\u0135\5,\27\2\u0135\u0136\5\62\32\2\u0136\u0138")
        buf.write("\3\2\2\2\u0137\u012d\3\2\2\2\u0137\u0132\3\2\2\2\u0138")
        buf.write("+\3\2\2\2\u0139\u013a\7-\2\2\u013a\u013b\5|?\2\u013b\u013c")
        buf.write("\7\b\2\2\u013c\u0144\3\2\2\2\u013d\u013e\7%\2\2\u013e")
        buf.write("\u013f\7\"\2\2\u013f\u0140\5,\27\2\u0140\u0141\5\62\32")
        buf.write("\2\u0141\u0142\7%\2\2\u0142\u0144\3\2\2\2\u0143\u0139")
        buf.write("\3\2\2\2\u0143\u013d\3\2\2\2\u0144-\3\2\2\2\u0145\u014a")
        buf.write("\3\2\2\2\u0146\u0147\5\62\32\2\u0147\u0148\5\60\31\2\u0148")
        buf.write("\u014a\3\2\2\2\u0149\u0145\3\2\2\2\u0149\u0146\3\2\2\2")
        buf.write("\u014a/\3\2\2\2\u014b\u0151\3\2\2\2\u014c\u014d\7%\2\2")
        buf.write("\u014d\u014e\5\62\32\2\u014e\u014f\5\60\31\2\u014f\u0151")
        buf.write("\3\2\2\2\u0150\u014b\3\2\2\2\u0150\u014c\3\2\2\2\u0151")
        buf.write("\61\3\2\2\2\u0152\u0153\b\32\1\2\u0153\u0163\7\"\2\2\u0154")
        buf.write("\u0163\5B\"\2\u0155\u0163\5\64\33\2\u0156\u0163\5x=\2")
        buf.write("\u0157\u0163\5\66\34\2\u0158\u0163\58\35\2\u0159\u0163")
        buf.write("\5> \2\u015a\u0163\5@!\2\u015b\u015c\5\u0082B\2\u015c")
        buf.write("\u015d\5\62\32\4\u015d\u0163\3\2\2\2\u015e\u015f\7(\2")
        buf.write("\2\u015f\u0160\5\62\32\2\u0160\u0161\7)\2\2\u0161\u0163")
        buf.write("\3\2\2\2\u0162\u0152\3\2\2\2\u0162\u0154\3\2\2\2\u0162")
        buf.write("\u0155\3\2\2\2\u0162\u0156\3\2\2\2\u0162\u0157\3\2\2\2")
        buf.write("\u0162\u0158\3\2\2\2\u0162\u0159\3\2\2\2\u0162\u015a\3")
        buf.write("\2\2\2\u0162\u015b\3\2\2\2\u0162\u015e\3\2\2\2\u0163\u016a")
        buf.write("\3\2\2\2\u0164\u0165\f\5\2\2\u0165\u0166\5\u0084C\2\u0166")
        buf.write("\u0167\5\62\32\6\u0167\u0169\3\2\2\2\u0168\u0164\3\2\2")
        buf.write("\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b")
        buf.write("\3\2\2\2\u016b\63\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016e")
        buf.write("\7\5\2\2\u016e\u016f\7\"\2\2\u016f\u0170\7(\2\2\u0170")
        buf.write("\u0171\5.\30\2\u0171\u0172\7)\2\2\u0172\65\3\2\2\2\u0173")
        buf.write("\u0174\7\"\2\2\u0174\u0175\7$\2\2\u0175\u0176\7\"\2\2")
        buf.write("\u0176\u0177\7(\2\2\u0177\u0178\5:\36\2\u0178\u0179\7")
        buf.write(")\2\2\u0179\67\3\2\2\2\u017a\u017b\7\"\2\2\u017b\u017c")
        buf.write("\7\4\2\2\u017c\u017d\7\26\2\2\u017d\u017e\7\"\2\2\u017e")
        buf.write("\u017f\7(\2\2\u017f\u0180\5:\36\2\u0180\u0181\7)\2\2\u0181")
        buf.write("9\3\2\2\2\u0182\u018a\3\2\2\2\u0183\u018a\5\\/\2\u0184")
        buf.write("\u018a\5d\63\2\u0185\u0186\5\\/\2\u0186\u0187\7%\2\2\u0187")
        buf.write("\u0188\5d\63\2\u0188\u018a\3\2\2\2\u0189\u0182\3\2\2\2")
        buf.write("\u0189\u0183\3\2\2\2\u0189\u0184\3\2\2\2\u0189\u0185\3")
        buf.write("\2\2\2\u018a;\3\2\2\2\u018b\u018e\5> \2\u018c\u018e\5")
        buf.write("@!\2\u018d\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018e=\3")
        buf.write("\2\2\2\u018f\u0190\7\"\2\2\u0190\u0191\7$\2\2\u0191\u0192")
        buf.write("\7\"\2\2\u0192?\3\2\2\2\u0193\u0194\7\"\2\2\u0194\u0195")
        buf.write("\7\4\2\2\u0195\u0196\7\26\2\2\u0196\u0197\7\"\2\2\u0197")
        buf.write("A\3\2\2\2\u0198\u019b\7\"\2\2\u0199\u019b\5<\37\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u0199\3\2\2\2\u019b\u01a0\3\2\2\2")
        buf.write("\u019c\u019d\7&\2\2\u019d\u019e\5D#\2\u019e\u019f\7\'")
        buf.write("\2\2\u019f\u01a1\3\2\2\2\u01a0\u019c\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("C\3\2\2\2\u01a4\u01a8\5z>\2\u01a5\u01a8\7\"\2\2\u01a6")
        buf.write("\u01a8\5<\37\2\u01a7\u01a4\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a7\u01a6\3\2\2\2\u01a8E\3\2\2\2\u01a9\u01ad\5\u0086")
        buf.write("D\2\u01aa\u01ad\7\"\2\2\u01ab\u01ad\5<\37\2\u01ac\u01a9")
        buf.write("\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad")
        buf.write("G\3\2\2\2\u01ae\u01b3\3\2\2\2\u01af\u01b0\5L\'\2\u01b0")
        buf.write("\u01b1\5J&\2\u01b1\u01b3\3\2\2\2\u01b2\u01ae\3\2\2\2\u01b2")
        buf.write("\u01af\3\2\2\2\u01b3I\3\2\2\2\u01b4\u01ba\3\2\2\2\u01b5")
        buf.write("\u01b6\7%\2\2\u01b6\u01b7\5L\'\2\u01b7\u01b8\5J&\2\u01b8")
        buf.write("\u01ba\3\2\2\2\u01b9\u01b4\3\2\2\2\u01b9\u01b5\3\2\2\2")
        buf.write("\u01baK\3\2\2\2\u01bb\u01bc\7\27\2\2\u01bc\u01bd\7(\2")
        buf.write("\2\u01bd\u01be\5P)\2\u01be\u01bf\7)\2\2\u01bfM\3\2\2\2")
        buf.write("\u01c0\u01c1\7\27\2\2\u01c1\u01c2\7(\2\2\u01c2\u01c3\5")
        buf.write("H%\2\u01c3\u01c4\7)\2\2\u01c4O\3\2\2\2\u01c5\u01ca\5h")
        buf.write("\65\2\u01c6\u01ca\5l\67\2\u01c7\u01ca\5p9\2\u01c8\u01ca")
        buf.write("\5t;\2\u01c9\u01c5\3\2\2\2\u01c9\u01c6\3\2\2\2\u01c9\u01c7")
        buf.write("\3\2\2\2\u01c9\u01c8\3\2\2\2\u01caQ\3\2\2\2\u01cb\u01cc")
        buf.write("\t\3\2\2\u01ccS\3\2\2\2\u01cd\u01ce\t\4\2\2\u01ceU\3\2")
        buf.write("\2\2\u01cf\u01d0\t\5\2\2\u01d0W\3\2\2\2\u01d1\u01d2\t")
        buf.write("\6\2\2\u01d2Y\3\2\2\2\u01d3\u01d4\t\7\2\2\u01d4[\3\2\2")
        buf.write("\2\u01d5\u01da\3\2\2\2\u01d6\u01d7\5x=\2\u01d7\u01d8\5")
        buf.write("^\60\2\u01d8\u01da\3\2\2\2\u01d9\u01d5\3\2\2\2\u01d9\u01d6")
        buf.write("\3\2\2\2\u01da]\3\2\2\2\u01db\u01e1\3\2\2\2\u01dc\u01dd")
        buf.write("\7%\2\2\u01dd\u01de\5x=\2\u01de\u01df\5^\60\2\u01df\u01e1")
        buf.write("\3\2\2\2\u01e0\u01db\3\2\2\2\u01e0\u01dc\3\2\2\2\u01e1")
        buf.write("_\3\2\2\2\u01e2\u01e9\3\2\2\2\u01e3\u01e5\7\26\2\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\3\2\2\2")
        buf.write("\u01e6\u01e7\7\"\2\2\u01e7\u01e9\5b\62\2\u01e8\u01e2\3")
        buf.write("\2\2\2\u01e8\u01e4\3\2\2\2\u01e9a\3\2\2\2\u01ea\u01f2")
        buf.write("\3\2\2\2\u01eb\u01ed\7%\2\2\u01ec\u01ee\7\26\2\2\u01ed")
        buf.write("\u01ec\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef\3\2\2\2")
        buf.write("\u01ef\u01f0\7\"\2\2\u01f0\u01f2\5b\62\2\u01f1\u01ea\3")
        buf.write("\2\2\2\u01f1\u01eb\3\2\2\2\u01f2c\3\2\2\2\u01f3\u01f7")
        buf.write("\3\2\2\2\u01f4\u01f5\7\"\2\2\u01f5\u01f7\5f\64\2\u01f6")
        buf.write("\u01f3\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7e\3\2\2\2\u01f8")
        buf.write("\u01fd\3\2\2\2\u01f9\u01fa\7%\2\2\u01fa\u01fb\7\"\2\2")
        buf.write("\u01fb\u01fd\5f\64\2\u01fc\u01f8\3\2\2\2\u01fc\u01f9\3")
        buf.write("\2\2\2\u01fdg\3\2\2\2\u01fe\u0203\3\2\2\2\u01ff\u0200")
        buf.write("\5z>\2\u0200\u0201\5j\66\2\u0201\u0203\3\2\2\2\u0202\u01fe")
        buf.write("\3\2\2\2\u0202\u01ff\3\2\2\2\u0203i\3\2\2\2\u0204\u020a")
        buf.write("\3\2\2\2\u0205\u0206\7%\2\2\u0206\u0207\5z>\2\u0207\u0208")
        buf.write("\5j\66\2\u0208\u020a\3\2\2\2\u0209\u0204\3\2\2\2\u0209")
        buf.write("\u0205\3\2\2\2\u020ak\3\2\2\2\u020b\u020f\3\2\2\2\u020c")
        buf.write("\u020d\7\24\2\2\u020d\u020f\5n8\2\u020e\u020b\3\2\2\2")
        buf.write("\u020e\u020c\3\2\2\2\u020fm\3\2\2\2\u0210\u0215\3\2\2")
        buf.write("\2\u0211\u0212\7%\2\2\u0212\u0213\7\24\2\2\u0213\u0215")
        buf.write("\5n8\2\u0214\u0210\3\2\2\2\u0214\u0211\3\2\2\2\u0215o")
        buf.write("\3\2\2\2\u0216\u021b\3\2\2\2\u0217\u0218\5\u0086D\2\u0218")
        buf.write("\u0219\5r:\2\u0219\u021b\3\2\2\2\u021a\u0216\3\2\2\2\u021a")
        buf.write("\u0217\3\2\2\2\u021bq\3\2\2\2\u021c\u0222\3\2\2\2\u021d")
        buf.write("\u021e\7%\2\2\u021e\u021f\5\u0086D\2\u021f\u0220\5r:\2")
        buf.write("\u0220\u0222\3\2\2\2\u0221\u021c\3\2\2\2\u0221\u021d\3")
        buf.write("\2\2\2\u0222s\3\2\2\2\u0223\u0227\3\2\2\2\u0224\u0225")
        buf.write("\7\3\2\2\u0225\u0227\5v<\2\u0226\u0223\3\2\2\2\u0226\u0224")
        buf.write("\3\2\2\2\u0227u\3\2\2\2\u0228\u022d\3\2\2\2\u0229\u022a")
        buf.write("\7%\2\2\u022a\u022b\7\3\2\2\u022b\u022d\5v<\2\u022c\u0228")
        buf.write("\3\2\2\2\u022c\u0229\3\2\2\2\u022dw\3\2\2\2\u022e\u0233")
        buf.write("\5\u0086D\2\u022f\u0233\7\24\2\2\u0230\u0233\7\3\2\2\u0231")
        buf.write("\u0233\5z>\2\u0232\u022e\3\2\2\2\u0232\u022f\3\2\2\2\u0232")
        buf.write("\u0230\3\2\2\2\u0232\u0231\3\2\2\2\u0233y\3\2\2\2\u0234")
        buf.write("\u0235\t\b\2\2\u0235{\3\2\2\2\u0236\u0237\t\t\2\2\u0237")
        buf.write("}\3\2\2\2\u0238\u0239\5z>\2\u0239\177\3\2\2\2\u023a\u023b")
        buf.write("\7\27\2\2\u023b\u023c\7&\2\2\u023c\u023d\5|?\2\u023d\u023e")
        buf.write("\7%\2\2\u023e\u023f\5~@\2\u023f\u0240\7\'\2\2\u0240\u0081")
        buf.write("\3\2\2\2\u0241\u0242\t\n\2\2\u0242\u0083\3\2\2\2\u0243")
        buf.write("\u0244\t\13\2\2\u0244\u0085\3\2\2\2\u0245\u0246\7\36\2")
        buf.write("\2\u0246\u024e\7$\2\2\u0247\u0249\7#\2\2\u0248\u0247\3")
        buf.write("\2\2\2\u0249\u024c\3\2\2\2\u024a\u0248\3\2\2\2\u024a\u024b")
        buf.write("\3\2\2\2\u024b\u024d\3\2\2\2\u024c\u024a\3\2\2\2\u024d")
        buf.write("\u024f\7\36\2\2\u024e\u024a\3\2\2\2\u024e\u024f\3\2\2")
        buf.write("\2\u024f\u0253\3\2\2\2\u0250\u0251\7\36\2\2\u0251\u0253")
        buf.write("\7\37\2\2\u0252\u0245\3\2\2\2\u0252\u0250\3\2\2\2\u0253")
        buf.write("\u0087\3\2\2\28\u008f\u0098\u009f\u00a1\u00ae\u00b5\u00bd")
        buf.write("\u00c4\u00c7\u00d3\u00da\u00e6\u00ec\u00f7\u0109\u010e")
        buf.write("\u0118\u0121\u012b\u0137\u0143\u0149\u0150\u0162\u016a")
        buf.write("\u0189\u018d\u019a\u01a2\u01a7\u01ac\u01b2\u01b9\u01c9")
        buf.write("\u01d9\u01e0\u01e4\u01e8\u01ed\u01f1\u01f6\u01fc\u0202")
        buf.write("\u0209\u020e\u0214\u021a\u0221\u0226\u022c\u0232\u024a")
        buf.write("\u024e\u0252")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'::'", "'New'", "'Return'", 
                     "'##'", "'='", "'Break'", "'Continue'", "'If'", "'Else'", 
                     "'Elseif'", "'Foreach'", "'In'", "'Constructor'", "'Destructor'", 
                     "'Class'", "'By'", "<INVALID>", "<INVALID>", "'$'", 
                     "'Array'", "'Int'", "'Float'", "'Boolean'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\"'", "''\"'", "<INVALID>", "'0'", "'.'", "','", 
                     "'['", "']'", "'('", "')'", "'{'", "'}'", "'..'", "':'", 
                     "';'", "'+'", "'<='", "'>='", "'-'", "'*'", "'<'", 
                     "'%'", "'/'", "'!='", "'=='", "'>'", "'&&'", "'||'", 
                     "'!'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>", "STRINGLIT", "MEM_ACCESS_OP", "NEW", 
                      "RETURN", "DOUB_HASH_MARK", "ASSIGN_OP", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "ELSEIF", "FOREACH", "IN", 
                      "CONSTRUCTOR", "DESTRUCTOR", "CLASS", "BY", "BOOLIT", 
                      "VAL_VAR", "STATIC", "ARRAY", "INT_TYPE", "FLOAT_TYPE", 
                      "BOOL_TYPE", "INTLIT_16", "INTLIT_2", "INTLIT_8", 
                      "INTLIT_10", "EXPONENT", "START_END_STRING", "DOUB_QUOTE", 
                      "ID", "ZERO", "DOT", "CM", "LS", "RS", "LB", "RB", 
                      "LP", "RP", "RANGE", "CL", "SEMI", "ADDOP", "LESS_EQUAL", 
                      "GREAT_EQUAL", "SUBOP", "MULOP", "LESS_THAN", "MODOP", 
                      "DIVOP", "NOT_EQUAL", "EQUAL", "GREAT_THAN", "AND", 
                      "OR", "NEGATE", "STR_CMP", "STR_CONCAT", "WS", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_comment = 1
    RULE_class_dcl = 2
    RULE_class_body = 3
    RULE_att_dcl = 4
    RULE_att_dcl_list = 5
    RULE_method_dcl = 6
    RULE_para_dcl_list = 7
    RULE_para_dcl_smcllist = 8
    RULE_para_dcl = 9
    RULE_stm = 10
    RULE_for_in_stm = 11
    RULE_if_stm = 12
    RULE_block_stm = 13
    RULE_mn_stm = 14
    RULE_continue_stm = 15
    RULE_break_stm = 16
    RULE_asm_stm = 17
    RULE_return_stm = 18
    RULE_method_invoke_stm = 19
    RULE_var_dcl = 20
    RULE_var_dcl_list = 21
    RULE_expr_list = 22
    RULE_expr_cmlist = 23
    RULE_expr = 24
    RULE_object_ini = 25
    RULE_instance_method_invoke = 26
    RULE_static_mehod_invoke = 27
    RULE_para_pass_list = 28
    RULE_att_access = 29
    RULE_instance_att_access = 30
    RULE_static_att_access = 31
    RULE_index_ele = 32
    RULE_int_object = 33
    RULE_float_object = 34
    RULE_index_arr_list = 35
    RULE_index_arr_cmlist = 36
    RULE_index_arr = 37
    RULE_mul_dim_arr = 38
    RULE_same_type_list = 39
    RULE_string_op = 40
    RULE_bool_op = 41
    RULE_relation_op = 42
    RULE_int_op = 43
    RULE_float_op = 44
    RULE_lit_list = 45
    RULE_lit_cmlist = 46
    RULE_static_id_list = 47
    RULE_static_id_cmlist = 48
    RULE_id_list = 49
    RULE_id_cmlist = 50
    RULE_int_gen_list = 51
    RULE_int_gen_cm = 52
    RULE_bool_list = 53
    RULE_bool_list_cm = 54
    RULE_float_list = 55
    RULE_float_list_cm = 56
    RULE_string_list = 57
    RULE_string_list_cm = 58
    RULE_lit = 59
    RULE_int_gen = 60
    RULE_data_type = 61
    RULE_size = 62
    RULE_array_type = 63
    RULE_unary_op = 64
    RULE_binary_op = 65
    RULE_floatlit = 66

    ruleNames =  [ "program", "comment", "class_dcl", "class_body", "att_dcl", 
                   "att_dcl_list", "method_dcl", "para_dcl_list", "para_dcl_smcllist", 
                   "para_dcl", "stm", "for_in_stm", "if_stm", "block_stm", 
                   "mn_stm", "continue_stm", "break_stm", "asm_stm", "return_stm", 
                   "method_invoke_stm", "var_dcl", "var_dcl_list", "expr_list", 
                   "expr_cmlist", "expr", "object_ini", "instance_method_invoke", 
                   "static_mehod_invoke", "para_pass_list", "att_access", 
                   "instance_att_access", "static_att_access", "index_ele", 
                   "int_object", "float_object", "index_arr_list", "index_arr_cmlist", 
                   "index_arr", "mul_dim_arr", "same_type_list", "string_op", 
                   "bool_op", "relation_op", "int_op", "float_op", "lit_list", 
                   "lit_cmlist", "static_id_list", "static_id_cmlist", "id_list", 
                   "id_cmlist", "int_gen_list", "int_gen_cm", "bool_list", 
                   "bool_list_cm", "float_list", "float_list_cm", "string_list", 
                   "string_list_cm", "lit", "int_gen", "data_type", "size", 
                   "array_type", "unary_op", "binary_op", "floatlit" ]

    EOF = Token.EOF
    STRINGLIT=1
    MEM_ACCESS_OP=2
    NEW=3
    RETURN=4
    DOUB_HASH_MARK=5
    ASSIGN_OP=6
    BREAK=7
    CONTINUE=8
    IF=9
    ELSE=10
    ELSEIF=11
    FOREACH=12
    IN=13
    CONSTRUCTOR=14
    DESTRUCTOR=15
    CLASS=16
    BY=17
    BOOLIT=18
    VAL_VAR=19
    STATIC=20
    ARRAY=21
    INT_TYPE=22
    FLOAT_TYPE=23
    BOOL_TYPE=24
    INTLIT_16=25
    INTLIT_2=26
    INTLIT_8=27
    INTLIT_10=28
    EXPONENT=29
    START_END_STRING=30
    DOUB_QUOTE=31
    ID=32
    ZERO=33
    DOT=34
    CM=35
    LS=36
    RS=37
    LB=38
    RB=39
    LP=40
    RP=41
    RANGE=42
    CL=43
    SEMI=44
    ADDOP=45
    LESS_EQUAL=46
    GREAT_EQUAL=47
    SUBOP=48
    MULOP=49
    LESS_THAN=50
    MODOP=51
    DIVOP=52
    NOT_EQUAL=53
    EQUAL=54
    GREAT_THAN=55
    AND=56
    OR=57
    NEGATE=58
    STR_CMP=59
    STR_CONCAT=60
    WS=61
    ILLEGAL_ESCAPE=62

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

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

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
            self.state = 134
            self.match(D96Parser.STRINGLIT)
            self.state = 135
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUB_HASH_MARK(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOUB_HASH_MARK)
            else:
                return self.getToken(D96Parser.DOUB_HASH_MARK, i)

        def getRuleIndex(self):
            return D96Parser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = D96Parser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(D96Parser.DOUB_HASH_MARK)
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 138
                    self.matchWildcard() 
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 144
            self.match(D96Parser.DOUB_HASH_MARK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_dcl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_dcl" ):
                listener.enterClass_dcl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_dcl" ):
                listener.exitClass_dcl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_dcl" ):
                return visitor.visitClass_dcl(self)
            else:
                return visitor.visitChildren(self)




    def class_dcl(self):

        localctx = D96Parser.Class_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(D96Parser.CLASS)
            self.state = 147
            self.match(D96Parser.ID)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.CL:
                self.state = 148
                self.match(D96Parser.CL)
                self.state = 149
                self.id_list()


            self.state = 152
            self.class_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def att_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Att_dclContext)
            else:
                return self.getTypedRuleContext(D96Parser.Att_dclContext,i)


        def method_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Method_dclContext)
            else:
                return self.getTypedRuleContext(D96Parser.Method_dclContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_body" ):
                listener.enterClass_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_body" ):
                listener.exitClass_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(D96Parser.LP)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.VAL_VAR) | (1 << D96Parser.STATIC) | (1 << D96Parser.ID))) != 0):
                self.state = 157
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL_VAR]:
                    self.state = 155
                    self.att_dcl()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.STATIC, D96Parser.ID]:
                    self.state = 156
                    self.method_dcl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Att_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL_VAR(self):
            return self.getToken(D96Parser.VAL_VAR, 0)

        def static_id_list(self):
            return self.getTypedRuleContext(D96Parser.Static_id_listContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def att_dcl_list(self):
            return self.getTypedRuleContext(D96Parser.Att_dcl_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_att_dcl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtt_dcl" ):
                listener.enterAtt_dcl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtt_dcl" ):
                listener.exitAtt_dcl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_dcl" ):
                return visitor.visitAtt_dcl(self)
            else:
                return visitor.visitChildren(self)




    def att_dcl(self):

        localctx = D96Parser.Att_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_att_dcl)
        self._la = 0 # Token type
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(D96Parser.VAL_VAR)
                self.state = 165
                self.static_id_list()
                self.state = 166
                self.match(D96Parser.CL)
                self.state = 167
                self.data_type()
                self.state = 168
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(D96Parser.VAL_VAR)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 171
                    self.match(D96Parser.STATIC)


                self.state = 174
                self.match(D96Parser.ID)
                self.state = 175
                self.att_dcl_list()
                self.state = 176
                self.expr(0)
                self.state = 177
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Att_dcl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ASSIGN_OP(self):
            return self.getToken(D96Parser.ASSIGN_OP, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def att_dcl_list(self):
            return self.getTypedRuleContext(D96Parser.Att_dcl_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_att_dcl_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtt_dcl_list" ):
                listener.enterAtt_dcl_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtt_dcl_list" ):
                listener.exitAtt_dcl_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_dcl_list" ):
                return visitor.visitAtt_dcl_list(self)
            else:
                return visitor.visitChildren(self)




    def att_dcl_list(self):

        localctx = D96Parser.Att_dcl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_att_dcl_list)
        self._la = 0 # Token type
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(D96Parser.CL)
                self.state = 182
                self.data_type()
                self.state = 183
                self.match(D96Parser.ASSIGN_OP)
                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(D96Parser.CM)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 186
                    self.match(D96Parser.STATIC)


                self.state = 189
                self.match(D96Parser.ID)
                self.state = 190
                self.att_dcl_list()
                self.state = 191
                self.expr(0)
                self.state = 192
                self.match(D96Parser.CM)
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


    class Method_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def para_dcl_smcllist(self):
            return self.getTypedRuleContext(D96Parser.Para_dcl_smcllistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_dcl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_dcl" ):
                listener.enterMethod_dcl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_dcl" ):
                listener.exitMethod_dcl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_dcl" ):
                return visitor.visitMethod_dcl(self)
            else:
                return visitor.visitChildren(self)




    def method_dcl(self):

        localctx = D96Parser.Method_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_method_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC:
                self.state = 196
                self.match(D96Parser.STATIC)


            self.state = 199
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 200
            self.match(D96Parser.LB)
            self.state = 201
            self.para_dcl_smcllist()
            self.state = 202
            self.match(D96Parser.RB)
            self.state = 203
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_dcl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_dcl(self):
            return self.getTypedRuleContext(D96Parser.Para_dclContext,0)


        def para_dcl_smcllist(self):
            return self.getTypedRuleContext(D96Parser.Para_dcl_smcllistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_para_dcl_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara_dcl_list" ):
                listener.enterPara_dcl_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara_dcl_list" ):
                listener.exitPara_dcl_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_dcl_list" ):
                return visitor.visitPara_dcl_list(self)
            else:
                return visitor.visitChildren(self)




    def para_dcl_list(self):

        localctx = D96Parser.Para_dcl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_para_dcl_list)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ID, D96Parser.CL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.para_dcl()
                self.state = 207
                self.para_dcl_smcllist()
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


    class Para_dcl_smcllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def para_dcl(self):
            return self.getTypedRuleContext(D96Parser.Para_dclContext,0)


        def para_dcl_smcllist(self):
            return self.getTypedRuleContext(D96Parser.Para_dcl_smcllistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_para_dcl_smcllist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara_dcl_smcllist" ):
                listener.enterPara_dcl_smcllist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara_dcl_smcllist" ):
                listener.exitPara_dcl_smcllist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_dcl_smcllist" ):
                return visitor.visitPara_dcl_smcllist(self)
            else:
                return visitor.visitChildren(self)




    def para_dcl_smcllist(self):

        localctx = D96Parser.Para_dcl_smcllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_para_dcl_smcllist)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF, D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(D96Parser.SEMI)
                self.state = 213
                self.para_dcl()
                self.state = 214
                self.para_dcl_smcllist()
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


    class Para_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_para_dcl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara_dcl" ):
                listener.enterPara_dcl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara_dcl" ):
                listener.exitPara_dcl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_dcl" ):
                return visitor.visitPara_dcl(self)
            else:
                return visitor.visitChildren(self)




    def para_dcl(self):

        localctx = D96Parser.Para_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_para_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.id_list()
            self.state = 219
            self.match(D96Parser.CL)
            self.state = 220
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def asm_stm(self):
            return self.getTypedRuleContext(D96Parser.Asm_stmContext,0)


        def var_dcl(self):
            return self.getTypedRuleContext(D96Parser.Var_dclContext,0)


        def break_stm(self):
            return self.getTypedRuleContext(D96Parser.Break_stmContext,0)


        def continue_stm(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(D96Parser.Return_stmContext,0)


        def method_invoke_stm(self):
            return self.getTypedRuleContext(D96Parser.Method_invoke_stmContext,0)


        def if_stm(self):
            return self.getTypedRuleContext(D96Parser.If_stmContext,0)


        def for_in_stm(self):
            return self.getTypedRuleContext(D96Parser.For_in_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStm" ):
                listener.enterStm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStm" ):
                listener.exitStm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = D96Parser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stm)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RETURN, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.VAL_VAR, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 222
                    self.asm_stm()
                    pass

                elif la_ == 2:
                    self.state = 223
                    self.var_dcl()
                    pass

                elif la_ == 3:
                    self.state = 224
                    self.break_stm()
                    pass

                elif la_ == 4:
                    self.state = 225
                    self.continue_stm()
                    pass

                elif la_ == 5:
                    self.state = 226
                    self.return_stm()
                    pass

                elif la_ == 6:
                    self.state = 227
                    self.method_invoke_stm()
                    pass


                self.state = 230
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.if_stm()
                pass
            elif token in [D96Parser.FOREACH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.for_in_stm()
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


    class For_in_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RANGE(self):
            return self.getToken(D96Parser.RANGE, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_stm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_in_stm" ):
                listener.enterFor_in_stm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_in_stm" ):
                listener.exitFor_in_stm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_stm" ):
                return visitor.visitFor_in_stm(self)
            else:
                return visitor.visitChildren(self)




    def for_in_stm(self):

        localctx = D96Parser.For_in_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_for_in_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(D96Parser.FOREACH)
            self.state = 237
            self.match(D96Parser.LB)
            self.state = 238
            self.match(D96Parser.ID)
            self.state = 239
            self.match(D96Parser.IN)
            self.state = 240
            self.expr(0)
            self.state = 241
            self.match(D96Parser.RANGE)
            self.state = 242
            self.expr(0)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 243
                self.match(D96Parser.BY)
                self.state = 244
                self.expr(0)


            self.state = 247
            self.match(D96Parser.RB)
            self.state = 248
            self.block_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LB)
            else:
                return self.getToken(D96Parser.LB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RB)
            else:
                return self.getToken(D96Parser.RB, i)

        def block_stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_stmContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_stmContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_stm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stm" ):
                listener.enterIf_stm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stm" ):
                listener.exitIf_stm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = D96Parser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(D96Parser.IF)
            self.state = 251
            self.match(D96Parser.LB)
            self.state = 252
            self.expr(0)
            self.state = 253
            self.match(D96Parser.RB)
            self.state = 254
            self.block_stm()
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 255
                self.match(D96Parser.ELSEIF)
                self.state = 256
                self.match(D96Parser.LB)
                self.state = 257
                self.expr(0)
                self.state = 258
                self.match(D96Parser.RB)
                self.state = 259
                self.block_stm()
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 266
                self.match(D96Parser.ELSE)
                self.state = 267
                self.block_stm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def mn_stm(self):
            return self.getTypedRuleContext(D96Parser.Mn_stmContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_stm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_stm" ):
                listener.enterBlock_stm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_stm" ):
                listener.exitBlock_stm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stm" ):
                return visitor.visitBlock_stm(self)
            else:
                return visitor.visitChildren(self)




    def block_stm(self):

        localctx = D96Parser.Block_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(D96Parser.LP)
            self.state = 271
            self.mn_stm()
            self.state = 272
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mn_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self):
            return self.getTypedRuleContext(D96Parser.StmContext,0)


        def mn_stm(self):
            return self.getTypedRuleContext(D96Parser.Mn_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mn_stm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMn_stm" ):
                listener.enterMn_stm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMn_stm" ):
                listener.exitMn_stm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMn_stm" ):
                return visitor.visitMn_stm(self)
            else:
                return visitor.visitChildren(self)




    def mn_stm(self):

        localctx = D96Parser.Mn_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_mn_stm)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.RETURN, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.VAL_VAR, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.stm()
                self.state = 276
                self.mn_stm()
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


    class Continue_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_stm" ):
                listener.enterContinue_stm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_stm" ):
                listener.exitContinue_stm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = D96Parser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(D96Parser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_stm" ):
                listener.enterBreak_stm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_stm" ):
                listener.exitBreak_stm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = D96Parser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(D96Parser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asm_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_OP(self):
            return self.getToken(D96Parser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def att_access(self):
            return self.getTypedRuleContext(D96Parser.Att_accessContext,0)


        def index_ele(self):
            return self.getTypedRuleContext(D96Parser.Index_eleContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_asm_stm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsm_stm" ):
                listener.enterAsm_stm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsm_stm" ):
                listener.exitAsm_stm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm_stm" ):
                return visitor.visitAsm_stm(self)
            else:
                return visitor.visitChildren(self)




    def asm_stm(self):

        localctx = D96Parser.Asm_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_asm_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 284
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 285
                self.att_access()
                pass

            elif la_ == 3:
                self.state = 286
                self.index_ele()
                pass


            self.state = 289
            self.match(D96Parser.ASSIGN_OP)
            self.state = 290
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stm" ):
                listener.enterReturn_stm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stm" ):
                listener.exitReturn_stm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = D96Parser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_return_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(D96Parser.RETURN)
            self.state = 293
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invoke_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_method_invoke(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_invokeContext,0)


        def static_mehod_invoke(self):
            return self.getTypedRuleContext(D96Parser.Static_mehod_invokeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invoke_stm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_invoke_stm" ):
                listener.enterMethod_invoke_stm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_invoke_stm" ):
                listener.exitMethod_invoke_stm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invoke_stm" ):
                return visitor.visitMethod_invoke_stm(self)
            else:
                return visitor.visitChildren(self)




    def method_invoke_stm(self):

        localctx = D96Parser.Method_invoke_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_method_invoke_stm)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.instance_method_invoke()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.static_mehod_invoke()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL_VAR(self):
            return self.getToken(D96Parser.VAL_VAR, 0)

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_dcl_list(self):
            return self.getTypedRuleContext(D96Parser.Var_dcl_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_dcl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_dcl" ):
                listener.enterVar_dcl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_dcl" ):
                listener.exitVar_dcl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dcl" ):
                return visitor.visitVar_dcl(self)
            else:
                return visitor.visitChildren(self)




    def var_dcl(self):

        localctx = D96Parser.Var_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_dcl)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(D96Parser.VAL_VAR)
                self.state = 300
                self.id_list()
                self.state = 301
                self.match(D96Parser.CL)
                self.state = 302
                self.data_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.match(D96Parser.VAL_VAR)
                self.state = 305
                self.match(D96Parser.ID)
                self.state = 306
                self.var_dcl_list()
                self.state = 307
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dcl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ASSIGN_OP(self):
            return self.getToken(D96Parser.ASSIGN_OP, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_dcl_list(self):
            return self.getTypedRuleContext(D96Parser.Var_dcl_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_dcl_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_dcl_list" ):
                listener.enterVar_dcl_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_dcl_list" ):
                listener.exitVar_dcl_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dcl_list" ):
                return visitor.visitVar_dcl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_dcl_list(self):

        localctx = D96Parser.Var_dcl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_var_dcl_list)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(D96Parser.CL)
                self.state = 312
                self.data_type()
                self.state = 313
                self.match(D96Parser.ASSIGN_OP)
                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(D96Parser.CM)
                self.state = 316
                self.match(D96Parser.ID)
                self.state = 317
                self.var_dcl_list()
                self.state = 318
                self.expr(0)
                self.state = 319
                self.match(D96Parser.CM)
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


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def expr_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Expr_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_list" ):
                listener.enterExpr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_list" ):
                listener.exitExpr_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr_list)
        try:
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT, D96Parser.NEW, D96Parser.BOOLIT, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10, D96Parser.ID, D96Parser.LB, D96Parser.SUBOP, D96Parser.NEGATE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.expr(0)
                self.state = 325
                self.expr_cmlist()
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


    class Expr_cmlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def expr_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Expr_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_cmlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_cmlist" ):
                listener.enterExpr_cmlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_cmlist" ):
                listener.exitExpr_cmlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_cmlist" ):
                return visitor.visitExpr_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def expr_cmlist(self):

        localctx = D96Parser.Expr_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr_cmlist)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(D96Parser.CM)
                self.state = 331
                self.expr(0)
                self.state = 332
                self.expr_cmlist()
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def index_ele(self):
            return self.getTypedRuleContext(D96Parser.Index_eleContext,0)


        def object_ini(self):
            return self.getTypedRuleContext(D96Parser.Object_iniContext,0)


        def lit(self):
            return self.getTypedRuleContext(D96Parser.LitContext,0)


        def instance_method_invoke(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_invokeContext,0)


        def static_mehod_invoke(self):
            return self.getTypedRuleContext(D96Parser.Static_mehod_invokeContext,0)


        def instance_att_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_att_accessContext,0)


        def static_att_access(self):
            return self.getTypedRuleContext(D96Parser.Static_att_accessContext,0)


        def unary_op(self):
            return self.getTypedRuleContext(D96Parser.Unary_opContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def binary_op(self):
            return self.getTypedRuleContext(D96Parser.Binary_opContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 337
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 338
                self.index_ele()
                pass

            elif la_ == 3:
                self.state = 339
                self.object_ini()
                pass

            elif la_ == 4:
                self.state = 340
                self.lit()
                pass

            elif la_ == 5:
                self.state = 341
                self.instance_method_invoke()
                pass

            elif la_ == 6:
                self.state = 342
                self.static_mehod_invoke()
                pass

            elif la_ == 7:
                self.state = 343
                self.instance_att_access()
                pass

            elif la_ == 8:
                self.state = 344
                self.static_att_access()
                pass

            elif la_ == 9:
                self.state = 345
                self.unary_op()
                self.state = 346
                self.expr(2)
                pass

            elif la_ == 10:
                self.state = 348
                self.match(D96Parser.LB)
                self.state = 349
                self.expr(0)
                self.state = 350
                self.match(D96Parser.RB)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 360
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 354
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 355
                    self.binary_op()
                    self.state = 356
                    self.expr(4) 
                self.state = 362
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Object_iniContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_object_ini

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_ini" ):
                listener.enterObject_ini(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_ini" ):
                listener.exitObject_ini(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_ini" ):
                return visitor.visitObject_ini(self)
            else:
                return visitor.visitChildren(self)




    def object_ini(self):

        localctx = D96Parser.Object_iniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_object_ini)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(D96Parser.NEW)
            self.state = 364
            self.match(D96Parser.ID)
            self.state = 365
            self.match(D96Parser.LB)
            self.state = 366
            self.expr_list()
            self.state = 367
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_invokeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def para_pass_list(self):
            return self.getTypedRuleContext(D96Parser.Para_pass_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_method_invoke

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance_method_invoke" ):
                listener.enterInstance_method_invoke(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance_method_invoke" ):
                listener.exitInstance_method_invoke(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invoke" ):
                return visitor.visitInstance_method_invoke(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invoke(self):

        localctx = D96Parser.Instance_method_invokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_instance_method_invoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(D96Parser.ID)
            self.state = 370
            self.match(D96Parser.DOT)
            self.state = 371
            self.match(D96Parser.ID)
            self.state = 372
            self.match(D96Parser.LB)
            self.state = 373
            self.para_pass_list()
            self.state = 374
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_mehod_invokeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def MEM_ACCESS_OP(self):
            return self.getToken(D96Parser.MEM_ACCESS_OP, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def para_pass_list(self):
            return self.getTypedRuleContext(D96Parser.Para_pass_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_mehod_invoke

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic_mehod_invoke" ):
                listener.enterStatic_mehod_invoke(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic_mehod_invoke" ):
                listener.exitStatic_mehod_invoke(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_mehod_invoke" ):
                return visitor.visitStatic_mehod_invoke(self)
            else:
                return visitor.visitChildren(self)




    def static_mehod_invoke(self):

        localctx = D96Parser.Static_mehod_invokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_static_mehod_invoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(D96Parser.ID)
            self.state = 377
            self.match(D96Parser.MEM_ACCESS_OP)
            self.state = 378
            self.match(D96Parser.STATIC)
            self.state = 379
            self.match(D96Parser.ID)
            self.state = 380
            self.match(D96Parser.LB)
            self.state = 381
            self.para_pass_list()
            self.state = 382
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_pass_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit_list(self):
            return self.getTypedRuleContext(D96Parser.Lit_listContext,0)


        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_para_pass_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara_pass_list" ):
                listener.enterPara_pass_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara_pass_list" ):
                listener.exitPara_pass_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_pass_list" ):
                return visitor.visitPara_pass_list(self)
            else:
                return visitor.visitChildren(self)




    def para_pass_list(self):

        localctx = D96Parser.Para_pass_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_para_pass_list)
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.lit_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.id_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.lit_list()
                self.state = 388
                self.match(D96Parser.CM)
                self.state = 389
                self.id_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Att_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_att_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_att_accessContext,0)


        def static_att_access(self):
            return self.getTypedRuleContext(D96Parser.Static_att_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_att_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtt_access" ):
                listener.enterAtt_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtt_access" ):
                listener.exitAtt_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_access" ):
                return visitor.visitAtt_access(self)
            else:
                return visitor.visitChildren(self)




    def att_access(self):

        localctx = D96Parser.Att_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_att_access)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.instance_att_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.static_att_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_att_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_att_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance_att_access" ):
                listener.enterInstance_att_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance_att_access" ):
                listener.exitInstance_att_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_att_access" ):
                return visitor.visitInstance_att_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_att_access(self):

        localctx = D96Parser.Instance_att_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_instance_att_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(D96Parser.ID)
            self.state = 398
            self.match(D96Parser.DOT)
            self.state = 399
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_att_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def MEM_ACCESS_OP(self):
            return self.getToken(D96Parser.MEM_ACCESS_OP, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_att_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic_att_access" ):
                listener.enterStatic_att_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic_att_access" ):
                listener.exitStatic_att_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_att_access" ):
                return visitor.visitStatic_att_access(self)
            else:
                return visitor.visitChildren(self)




    def static_att_access(self):

        localctx = D96Parser.Static_att_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_static_att_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(D96Parser.ID)
            self.state = 402
            self.match(D96Parser.MEM_ACCESS_OP)
            self.state = 403
            self.match(D96Parser.STATIC)
            self.state = 404
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def att_access(self):
            return self.getTypedRuleContext(D96Parser.Att_accessContext,0)


        def LS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LS)
            else:
                return self.getToken(D96Parser.LS, i)

        def int_object(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Int_objectContext)
            else:
                return self.getTypedRuleContext(D96Parser.Int_objectContext,i)


        def RS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RS)
            else:
                return self.getToken(D96Parser.RS, i)

        def getRuleIndex(self):
            return D96Parser.RULE_index_ele

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_ele" ):
                listener.enterIndex_ele(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_ele" ):
                listener.exitIndex_ele(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_ele" ):
                return visitor.visitIndex_ele(self)
            else:
                return visitor.visitChildren(self)




    def index_ele(self):

        localctx = D96Parser.Index_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_index_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 406
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 407
                self.att_access()
                pass


            self.state = 414 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 410
                    self.match(D96Parser.LS)
                    self.state = 411
                    self.int_object()
                    self.state = 412
                    self.match(D96Parser.RS)

                else:
                    raise NoViableAltException(self)
                self.state = 416 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_objectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_gen(self):
            return self.getTypedRuleContext(D96Parser.Int_genContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def att_access(self):
            return self.getTypedRuleContext(D96Parser.Att_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_int_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_object" ):
                listener.enterInt_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_object" ):
                listener.exitInt_object(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_object" ):
                return visitor.visitInt_object(self)
            else:
                return visitor.visitChildren(self)




    def int_object(self):

        localctx = D96Parser.Int_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_int_object)
        try:
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.int_gen()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 420
                self.att_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_objectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def floatlit(self):
            return self.getTypedRuleContext(D96Parser.FloatlitContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def att_access(self):
            return self.getTypedRuleContext(D96Parser.Att_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_float_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_object" ):
                listener.enterFloat_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_object" ):
                listener.exitFloat_object(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_object" ):
                return visitor.visitFloat_object(self)
            else:
                return visitor.visitChildren(self)




    def float_object(self):

        localctx = D96Parser.Float_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_float_object)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.floatlit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.att_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_arr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_arr(self):
            return self.getTypedRuleContext(D96Parser.Index_arrContext,0)


        def index_arr_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Index_arr_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_arr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_arr_list" ):
                listener.enterIndex_arr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_arr_list" ):
                listener.exitIndex_arr_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_arr_list" ):
                return visitor.visitIndex_arr_list(self)
            else:
                return visitor.visitChildren(self)




    def index_arr_list(self):

        localctx = D96Parser.Index_arr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_index_arr_list)
        try:
            self.state = 432
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.index_arr()
                self.state = 430
                self.index_arr_cmlist()
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


    class Index_arr_cmlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def index_arr(self):
            return self.getTypedRuleContext(D96Parser.Index_arrContext,0)


        def index_arr_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Index_arr_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_arr_cmlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_arr_cmlist" ):
                listener.enterIndex_arr_cmlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_arr_cmlist" ):
                listener.exitIndex_arr_cmlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_arr_cmlist" ):
                return visitor.visitIndex_arr_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def index_arr_cmlist(self):

        localctx = D96Parser.Index_arr_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_index_arr_cmlist)
        try:
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.match(D96Parser.CM)
                self.state = 436
                self.index_arr()
                self.state = 437
                self.index_arr_cmlist()
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


    class Index_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def same_type_list(self):
            return self.getTypedRuleContext(D96Parser.Same_type_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_index_arr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_arr" ):
                listener.enterIndex_arr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_arr" ):
                listener.exitIndex_arr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_arr" ):
                return visitor.visitIndex_arr(self)
            else:
                return visitor.visitChildren(self)




    def index_arr(self):

        localctx = D96Parser.Index_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_index_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(D96Parser.ARRAY)
            self.state = 442
            self.match(D96Parser.LB)
            self.state = 443
            self.same_type_list()
            self.state = 444
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_dim_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def index_arr_list(self):
            return self.getTypedRuleContext(D96Parser.Index_arr_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mul_dim_arr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_dim_arr" ):
                listener.enterMul_dim_arr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_dim_arr" ):
                listener.exitMul_dim_arr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_dim_arr" ):
                return visitor.visitMul_dim_arr(self)
            else:
                return visitor.visitChildren(self)




    def mul_dim_arr(self):

        localctx = D96Parser.Mul_dim_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_mul_dim_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(D96Parser.ARRAY)
            self.state = 447
            self.match(D96Parser.LB)
            self.state = 448
            self.index_arr_list()
            self.state = 449
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Same_type_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_gen_list(self):
            return self.getTypedRuleContext(D96Parser.Int_gen_listContext,0)


        def bool_list(self):
            return self.getTypedRuleContext(D96Parser.Bool_listContext,0)


        def float_list(self):
            return self.getTypedRuleContext(D96Parser.Float_listContext,0)


        def string_list(self):
            return self.getTypedRuleContext(D96Parser.String_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_same_type_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSame_type_list" ):
                listener.enterSame_type_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSame_type_list" ):
                listener.exitSame_type_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSame_type_list" ):
                return visitor.visitSame_type_list(self)
            else:
                return visitor.visitChildren(self)




    def same_type_list(self):

        localctx = D96Parser.Same_type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_same_type_list)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.int_gen_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.bool_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 453
                self.float_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 454
                self.string_list()
                pass


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
        self.enterRule(localctx, 80, self.RULE_string_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
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
        self.enterRule(localctx, 82, self.RULE_bool_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
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
        self.enterRule(localctx, 84, self.RULE_relation_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
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
        self.enterRule(localctx, 86, self.RULE_int_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
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
        self.enterRule(localctx, 88, self.RULE_float_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
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


    class Lit_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(D96Parser.LitContext,0)


        def lit_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Lit_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lit_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLit_list" ):
                listener.enterLit_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLit_list" ):
                listener.exitLit_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_list" ):
                return visitor.visitLit_list(self)
            else:
                return visitor.visitChildren(self)




    def lit_list(self):

        localctx = D96Parser.Lit_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_lit_list)
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CM, D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT, D96Parser.BOOLIT, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.lit()
                self.state = 469
                self.lit_cmlist()
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


    class Lit_cmlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def lit(self):
            return self.getTypedRuleContext(D96Parser.LitContext,0)


        def lit_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Lit_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lit_cmlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLit_cmlist" ):
                listener.enterLit_cmlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLit_cmlist" ):
                listener.exitLit_cmlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_cmlist" ):
                return visitor.visitLit_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def lit_cmlist(self):

        localctx = D96Parser.Lit_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_lit_cmlist)
        try:
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.match(D96Parser.CM)
                self.state = 475
                self.lit()
                self.state = 476
                self.lit_cmlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def static_id_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Static_id_cmlistContext,0)


        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_id_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic_id_list" ):
                listener.enterStatic_id_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic_id_list" ):
                listener.exitStatic_id_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_id_list" ):
                return visitor.visitStatic_id_list(self)
            else:
                return visitor.visitChildren(self)




    def static_id_list(self):

        localctx = D96Parser.Static_id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_static_id_list)
        self._la = 0 # Token type
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STATIC, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 481
                    self.match(D96Parser.STATIC)


                self.state = 484
                self.match(D96Parser.ID)
                self.state = 485
                self.static_id_cmlist()
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


    class Static_id_cmlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def static_id_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Static_id_cmlistContext,0)


        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_id_cmlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic_id_cmlist" ):
                listener.enterStatic_id_cmlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic_id_cmlist" ):
                listener.exitStatic_id_cmlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_id_cmlist" ):
                return visitor.visitStatic_id_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def static_id_cmlist(self):

        localctx = D96Parser.Static_id_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_static_id_cmlist)
        self._la = 0 # Token type
        try:
            self.state = 495
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.match(D96Parser.CM)
                self.state = 491
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 490
                    self.match(D96Parser.STATIC)


                self.state = 493
                self.match(D96Parser.ID)
                self.state = 494
                self.static_id_cmlist()
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


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def id_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Id_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_id_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_list" ):
                listener.enterId_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_list" ):
                listener.exitId_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_id_list)
        try:
            self.state = 500
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB, D96Parser.LP, D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.match(D96Parser.ID)
                self.state = 499
                self.id_cmlist()
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


    class Id_cmlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def id_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Id_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_id_cmlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_cmlist" ):
                listener.enterId_cmlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_cmlist" ):
                listener.exitId_cmlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_cmlist" ):
                return visitor.visitId_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def id_cmlist(self):

        localctx = D96Parser.Id_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_id_cmlist)
        try:
            self.state = 506
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB, D96Parser.LP, D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.match(D96Parser.CM)
                self.state = 504
                self.match(D96Parser.ID)
                self.state = 505
                self.id_cmlist()
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
        self.enterRule(localctx, 102, self.RULE_int_gen_list)
        try:
            self.state = 512
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.int_gen()
                self.state = 510
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
        self.enterRule(localctx, 104, self.RULE_int_gen_cm)
        try:
            self.state = 519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.match(D96Parser.CM)
                self.state = 516
                self.int_gen()
                self.state = 517
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
        self.enterRule(localctx, 106, self.RULE_bool_list)
        try:
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(D96Parser.BOOLIT)
                self.state = 523
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
        self.enterRule(localctx, 108, self.RULE_bool_list_cm)
        try:
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.match(D96Parser.CM)
                self.state = 528
                self.match(D96Parser.BOOLIT)
                self.state = 529
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

        def floatlit(self):
            return self.getTypedRuleContext(D96Parser.FloatlitContext,0)


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
        self.enterRule(localctx, 110, self.RULE_float_list)
        try:
            self.state = 536
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.floatlit()
                self.state = 534
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

        def floatlit(self):
            return self.getTypedRuleContext(D96Parser.FloatlitContext,0)


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
        self.enterRule(localctx, 112, self.RULE_float_list_cm)
        try:
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.match(D96Parser.CM)
                self.state = 540
                self.floatlit()
                self.state = 541
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

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

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
        self.enterRule(localctx, 114, self.RULE_string_list)
        try:
            self.state = 548
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
                self.match(D96Parser.STRINGLIT)
                self.state = 547
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

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

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
        self.enterRule(localctx, 116, self.RULE_string_list_cm)
        try:
            self.state = 554
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                self.match(D96Parser.CM)
                self.state = 552
                self.match(D96Parser.STRINGLIT)
                self.state = 553
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

        def floatlit(self):
            return self.getTypedRuleContext(D96Parser.FloatlitContext,0)


        def BOOLIT(self):
            return self.getToken(D96Parser.BOOLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

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
        self.enterRule(localctx, 118, self.RULE_lit)
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.floatlit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
                self.match(D96Parser.BOOLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 558
                self.match(D96Parser.STRINGLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 559
                self.int_gen()
                pass


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
        self.enterRule(localctx, 120, self.RULE_int_gen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
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


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(D96Parser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(D96Parser.FLOAT_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(D96Parser.BOOL_TYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_data_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_type" ):
                listener.enterData_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_type" ):
                listener.exitData_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT_TYPE) | (1 << D96Parser.FLOAT_TYPE) | (1 << D96Parser.BOOL_TYPE))) != 0)):
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


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_gen(self):
            return self.getTypedRuleContext(D96Parser.Int_genContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSize" ):
                listener.enterSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSize" ):
                listener.exitSize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = D96Parser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.int_gen()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def size(self):
            return self.getTypedRuleContext(D96Parser.SizeContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_type" ):
                listener.enterArray_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_type" ):
                listener.exitArray_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(D96Parser.ARRAY)
            self.state = 569
            self.match(D96Parser.LS)
            self.state = 570
            self.data_type()
            self.state = 571
            self.match(D96Parser.CM)
            self.state = 572
            self.size()
            self.state = 573
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBOP(self):
            return self.getToken(D96Parser.SUBOP, 0)

        def NEGATE(self):
            return self.getToken(D96Parser.NEGATE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_unary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_op" ):
                listener.enterUnary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_op" ):
                listener.exitUnary_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_op" ):
                return visitor.visitUnary_op(self)
            else:
                return visitor.visitChildren(self)




    def unary_op(self):

        localctx = D96Parser.Unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            _la = self._input.LA(1)
            if not(_la==D96Parser.SUBOP or _la==D96Parser.NEGATE):
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


    class Binary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADDOP(self):
            return self.getToken(D96Parser.ADDOP, 0)

        def LESS_EQUAL(self):
            return self.getToken(D96Parser.LESS_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(D96Parser.LESS_THAN, 0)

        def GREAT_EQUAL(self):
            return self.getToken(D96Parser.GREAT_EQUAL, 0)

        def GREAT_THAN(self):
            return self.getToken(D96Parser.GREAT_THAN, 0)

        def SUBOP(self):
            return self.getToken(D96Parser.SUBOP, 0)

        def MULOP(self):
            return self.getToken(D96Parser.MULOP, 0)

        def MODOP(self):
            return self.getToken(D96Parser.MODOP, 0)

        def DIVOP(self):
            return self.getToken(D96Parser.DIVOP, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def STR_CMP(self):
            return self.getToken(D96Parser.STR_CMP, 0)

        def STR_CONCAT(self):
            return self.getToken(D96Parser.STR_CONCAT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_binary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_op" ):
                listener.enterBinary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_op" ):
                listener.exitBinary_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_op" ):
                return visitor.visitBinary_op(self)
            else:
                return visitor.visitChildren(self)




    def binary_op(self):

        localctx = D96Parser.Binary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_binary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ADDOP) | (1 << D96Parser.LESS_EQUAL) | (1 << D96Parser.GREAT_EQUAL) | (1 << D96Parser.SUBOP) | (1 << D96Parser.MULOP) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.MODOP) | (1 << D96Parser.DIVOP) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.EQUAL) | (1 << D96Parser.GREAT_THAN) | (1 << D96Parser.AND) | (1 << D96Parser.OR) | (1 << D96Parser.STR_CMP) | (1 << D96Parser.STR_CONCAT))) != 0)):
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


    class FloatlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT_10(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INTLIT_10)
            else:
                return self.getToken(D96Parser.INTLIT_10, i)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ZERO(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ZERO)
            else:
                return self.getToken(D96Parser.ZERO, i)

        def EXPONENT(self):
            return self.getToken(D96Parser.EXPONENT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_floatlit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatlit" ):
                listener.enterFloatlit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatlit" ):
                listener.exitFloatlit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatlit" ):
                return visitor.visitFloatlit(self)
            else:
                return visitor.visitChildren(self)




    def floatlit(self):

        localctx = D96Parser.FloatlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_floatlit)
        self._la = 0 # Token type
        try:
            self.state = 592
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 579
                self.match(D96Parser.INTLIT_10)
                self.state = 580
                self.match(D96Parser.DOT)
                self.state = 588
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 584
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.ZERO:
                        self.state = 581
                        self.match(D96Parser.ZERO)
                        self.state = 586
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 587
                    self.match(D96Parser.INTLIT_10)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 590
                self.match(D96Parser.INTLIT_10)
                self.state = 591
                self.match(D96Parser.EXPONENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




