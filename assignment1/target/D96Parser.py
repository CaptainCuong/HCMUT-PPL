# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
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
        buf.write("\u0226\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3\u008c\n\3\3\3\3\3\3\4\3\4\3\4\7")
        buf.write("\4\u0093\n\4\f\4\16\4\u0096\13\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00a6\n\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00b2\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u00be\n\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\5\t\u00c5\n\t\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00d1\n\13\3\13\3\13\3\13\3")
        buf.write("\13\5\13\u00d7\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00e2\n\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\7\r\u00f2\n\r\f\r\16\r\u00f5\13\r\3")
        buf.write("\r\3\r\5\r\u00f9\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u0103\n\17\3\20\3\20\3\21\3\21\3\22\3\22\3")
        buf.write("\22\5\22\u010c\n\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\5\24\u0116\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u0122\n\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u012e\n\26\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u0134\n\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u013b\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u014d")
        buf.write("\n\31\3\31\3\31\3\31\3\31\7\31\u0153\n\31\f\31\16\31\u0156")
        buf.write("\13\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0173\n\35\3")
        buf.write("\36\3\36\5\36\u0177\n\36\3\37\3\37\3\37\3\37\3 \3 \3 ")
        buf.write("\3 \3!\3!\5!\u0183\n!\3!\3!\3!\3!\6!\u0189\n!\r!\16!\u018a")
        buf.write("\3\"\3\"\3\"\5\"\u0190\n\"\3#\3#\3#\5#\u0195\n#\3$\3$")
        buf.write("\3$\3$\5$\u019b\n$\3%\3%\3%\3%\3%\5%\u01a2\n%\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\5(\u01b2\n(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3.\5.\u01c2\n.\3")
        buf.write("/\3/\3/\3/\3/\5/\u01c9\n/\3\60\3\60\3\60\5\60\u01ce\n")
        buf.write("\60\3\61\3\61\3\61\3\61\5\61\u01d4\n\61\3\62\3\62\3\62")
        buf.write("\5\62\u01d9\n\62\3\63\3\63\3\63\3\63\5\63\u01df\n\63\3")
        buf.write("\64\3\64\3\64\3\64\5\64\u01e5\n\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\5\65\u01ec\n\65\3\66\3\66\3\66\5\66\u01f1\n\66\3")
        buf.write("\67\3\67\3\67\3\67\5\67\u01f7\n\67\38\38\38\58\u01fc\n")
        buf.write("8\39\39\39\39\59\u0202\n9\3:\3:\3:\5:\u0207\n:\3;\3;\3")
        buf.write(";\3;\5;\u020d\n;\3<\3<\3<\3<\5<\u0213\n<\3=\3=\3>\3>\3")
        buf.write("?\3?\3@\3@\3@\3@\3@\3@\3@\3A\3A\3B\3B\3B\2\3\60C\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\2\r")
        buf.write("\3\2\36\37\4\2\17\20\36\37\3\2:;\4\2\64\65\679\4\2\61")
        buf.write("\61\64\66\3\2,\65\4\2,\61\64\64\3\2\32\35\3\2\27\31\4")
        buf.write("\2//99\4\2,8:;\2\u0227\2\u0084\3\2\2\2\4\u0087\3\2\2\2")
        buf.write("\6\u008f\3\2\2\2\b\u00a5\3\2\2\2\n\u00b1\3\2\2\2\f\u00b3")
        buf.write("\3\2\2\2\16\u00bd\3\2\2\2\20\u00c4\3\2\2\2\22\u00c6\3")
        buf.write("\2\2\2\24\u00d6\3\2\2\2\26\u00d8\3\2\2\2\30\u00e6\3\2")
        buf.write("\2\2\32\u00fa\3\2\2\2\34\u0102\3\2\2\2\36\u0104\3\2\2")
        buf.write("\2 \u0106\3\2\2\2\"\u010b\3\2\2\2$\u0110\3\2\2\2&\u0115")
        buf.write("\3\2\2\2(\u0121\3\2\2\2*\u012d\3\2\2\2,\u0133\3\2\2\2")
        buf.write(".\u013a\3\2\2\2\60\u014c\3\2\2\2\62\u0157\3\2\2\2\64\u015d")
        buf.write("\3\2\2\2\66\u0164\3\2\2\28\u0172\3\2\2\2:\u0176\3\2\2")
        buf.write("\2<\u0178\3\2\2\2>\u017c\3\2\2\2@\u0182\3\2\2\2B\u018f")
        buf.write("\3\2\2\2D\u0194\3\2\2\2F\u019a\3\2\2\2H\u01a1\3\2\2\2")
        buf.write("J\u01a3\3\2\2\2L\u01a8\3\2\2\2N\u01b1\3\2\2\2P\u01b3\3")
        buf.write("\2\2\2R\u01b5\3\2\2\2T\u01b7\3\2\2\2V\u01b9\3\2\2\2X\u01bb")
        buf.write("\3\2\2\2Z\u01c1\3\2\2\2\\\u01c8\3\2\2\2^\u01cd\3\2\2\2")
        buf.write("`\u01d3\3\2\2\2b\u01d8\3\2\2\2d\u01de\3\2\2\2f\u01e4\3")
        buf.write("\2\2\2h\u01eb\3\2\2\2j\u01f0\3\2\2\2l\u01f6\3\2\2\2n\u01fb")
        buf.write("\3\2\2\2p\u0201\3\2\2\2r\u0206\3\2\2\2t\u020c\3\2\2\2")
        buf.write("v\u0212\3\2\2\2x\u0214\3\2\2\2z\u0216\3\2\2\2|\u0218\3")
        buf.write("\2\2\2~\u021a\3\2\2\2\u0080\u0221\3\2\2\2\u0082\u0223")
        buf.write("\3\2\2\2\u0084\u0085\5\60\31\2\u0085\u0086\7\2\2\3\u0086")
        buf.write("\3\3\2\2\2\u0087\u0088\7\21\2\2\u0088\u008b\7\37\2\2\u0089")
        buf.write("\u008a\7*\2\2\u008a\u008c\5b\62\2\u008b\u0089\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\5")
        buf.write("\6\4\2\u008e\5\3\2\2\2\u008f\u0094\7\'\2\2\u0090\u0093")
        buf.write("\5\b\5\2\u0091\u0093\5\f\7\2\u0092\u0090\3\2\2\2\u0092")
        buf.write("\u0091\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2\u0096\u0094\3")
        buf.write("\2\2\2\u0097\u0098\7(\2\2\u0098\7\3\2\2\2\u0099\u009a")
        buf.write("\7\25\2\2\u009a\u009b\5^\60\2\u009b\u009c\7*\2\2\u009c")
        buf.write("\u009d\5z>\2\u009d\u009e\7+\2\2\u009e\u00a6\3\2\2\2\u009f")
        buf.write("\u00a0\7\25\2\2\u00a0\u00a1\t\2\2\2\u00a1\u00a2\5\n\6")
        buf.write("\2\u00a2\u00a3\5\60\31\2\u00a3\u00a4\7+\2\2\u00a4\u00a6")
        buf.write("\3\2\2\2\u00a5\u0099\3\2\2\2\u00a5\u009f\3\2\2\2\u00a6")
        buf.write("\t\3\2\2\2\u00a7\u00a8\7*\2\2\u00a8\u00a9\5z>\2\u00a9")
        buf.write("\u00aa\7\7\2\2\u00aa\u00b2\3\2\2\2\u00ab\u00ac\7\"\2\2")
        buf.write("\u00ac\u00ad\t\2\2\2\u00ad\u00ae\5\n\6\2\u00ae\u00af\5")
        buf.write("\60\31\2\u00af\u00b0\7\"\2\2\u00b0\u00b2\3\2\2\2\u00b1")
        buf.write("\u00a7\3\2\2\2\u00b1\u00ab\3\2\2\2\u00b2\13\3\2\2\2\u00b3")
        buf.write("\u00b4\t\3\2\2\u00b4\u00b5\7%\2\2\u00b5\u00b6\5\20\t\2")
        buf.write("\u00b6\u00b7\7&\2\2\u00b7\u00b8\5\32\16\2\u00b8\r\3\2")
        buf.write("\2\2\u00b9\u00be\3\2\2\2\u00ba\u00bb\5\22\n\2\u00bb\u00bc")
        buf.write("\5\20\t\2\u00bc\u00be\3\2\2\2\u00bd\u00b9\3\2\2\2\u00bd")
        buf.write("\u00ba\3\2\2\2\u00be\17\3\2\2\2\u00bf\u00c5\3\2\2\2\u00c0")
        buf.write("\u00c1\7+\2\2\u00c1\u00c2\5\22\n\2\u00c2\u00c3\5\20\t")
        buf.write("\2\u00c3\u00c5\3\2\2\2\u00c4\u00bf\3\2\2\2\u00c4\u00c0")
        buf.write("\3\2\2\2\u00c5\21\3\2\2\2\u00c6\u00c7\5b\62\2\u00c7\u00c8")
        buf.write("\7*\2\2\u00c8\u00c9\5z>\2\u00c9\23\3\2\2\2\u00ca\u00d1")
        buf.write("\5\"\22\2\u00cb\u00d1\5(\25\2\u00cc\u00d1\5 \21\2\u00cd")
        buf.write("\u00d1\5\36\20\2\u00ce\u00d1\5$\23\2\u00cf\u00d1\5&\24")
        buf.write("\2\u00d0\u00ca\3\2\2\2\u00d0\u00cb\3\2\2\2\u00d0\u00cc")
        buf.write("\3\2\2\2\u00d0\u00cd\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\7+\2\2")
        buf.write("\u00d3\u00d7\3\2\2\2\u00d4\u00d7\5\30\r\2\u00d5\u00d7")
        buf.write("\5\26\f\2\u00d6\u00d0\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d5\3\2\2\2\u00d7\25\3\2\2\2\u00d8\u00d9\7\r\2\2\u00d9")
        buf.write("\u00da\7%\2\2\u00da\u00db\7\37\2\2\u00db\u00dc\7\16\2")
        buf.write("\2\u00dc\u00dd\5\60\31\2\u00dd\u00de\7)\2\2\u00de\u00e1")
        buf.write("\5\60\31\2\u00df\u00e0\7\23\2\2\u00e0\u00e2\5\60\31\2")
        buf.write("\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\3")
        buf.write("\2\2\2\u00e3\u00e4\7&\2\2\u00e4\u00e5\5\32\16\2\u00e5")
        buf.write("\27\3\2\2\2\u00e6\u00e7\7\n\2\2\u00e7\u00e8\7%\2\2\u00e8")
        buf.write("\u00e9\5\60\31\2\u00e9\u00ea\7&\2\2\u00ea\u00f3\5\32\16")
        buf.write("\2\u00eb\u00ec\7\f\2\2\u00ec\u00ed\7%\2\2\u00ed\u00ee")
        buf.write("\5\60\31\2\u00ee\u00ef\7&\2\2\u00ef\u00f0\5\32\16\2\u00f0")
        buf.write("\u00f2\3\2\2\2\u00f1\u00eb\3\2\2\2\u00f2\u00f5\3\2\2\2")
        buf.write("\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f8\3")
        buf.write("\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7\7\13\2\2\u00f7")
        buf.write("\u00f9\5\32\16\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2")
        buf.write("\2\u00f9\31\3\2\2\2\u00fa\u00fb\7\'\2\2\u00fb\u00fc\5")
        buf.write("\34\17\2\u00fc\u00fd\7(\2\2\u00fd\33\3\2\2\2\u00fe\u0103")
        buf.write("\3\2\2\2\u00ff\u0100\5\24\13\2\u0100\u0101\5\34\17\2\u0101")
        buf.write("\u0103\3\2\2\2\u0102\u00fe\3\2\2\2\u0102\u00ff\3\2\2\2")
        buf.write("\u0103\35\3\2\2\2\u0104\u0105\7\t\2\2\u0105\37\3\2\2\2")
        buf.write("\u0106\u0107\7\b\2\2\u0107!\3\2\2\2\u0108\u010c\7\37\2")
        buf.write("\2\u0109\u010c\5:\36\2\u010a\u010c\5@!\2\u010b\u0108\3")
        buf.write("\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u010e\7\7\2\2\u010e\u010f\5\60\31\2\u010f")
        buf.write("#\3\2\2\2\u0110\u0111\7\6\2\2\u0111\u0112\5\60\31\2\u0112")
        buf.write("%\3\2\2\2\u0113\u0116\5\64\33\2\u0114\u0116\5\66\34\2")
        buf.write("\u0115\u0113\3\2\2\2\u0115\u0114\3\2\2\2\u0116\'\3\2\2")
        buf.write("\2\u0117\u0118\7\25\2\2\u0118\u0119\5b\62\2\u0119\u011a")
        buf.write("\7*\2\2\u011a\u011b\5z>\2\u011b\u0122\3\2\2\2\u011c\u011d")
        buf.write("\7\25\2\2\u011d\u011e\7\37\2\2\u011e\u011f\5*\26\2\u011f")
        buf.write("\u0120\5\60\31\2\u0120\u0122\3\2\2\2\u0121\u0117\3\2\2")
        buf.write("\2\u0121\u011c\3\2\2\2\u0122)\3\2\2\2\u0123\u0124\7*\2")
        buf.write("\2\u0124\u0125\5z>\2\u0125\u0126\7\7\2\2\u0126\u012e\3")
        buf.write("\2\2\2\u0127\u0128\7\"\2\2\u0128\u0129\7\37\2\2\u0129")
        buf.write("\u012a\5*\26\2\u012a\u012b\5\60\31\2\u012b\u012c\7\"\2")
        buf.write("\2\u012c\u012e\3\2\2\2\u012d\u0123\3\2\2\2\u012d\u0127")
        buf.write("\3\2\2\2\u012e+\3\2\2\2\u012f\u0134\3\2\2\2\u0130\u0131")
        buf.write("\5\60\31\2\u0131\u0132\5.\30\2\u0132\u0134\3\2\2\2\u0133")
        buf.write("\u012f\3\2\2\2\u0133\u0130\3\2\2\2\u0134-\3\2\2\2\u0135")
        buf.write("\u013b\3\2\2\2\u0136\u0137\7\"\2\2\u0137\u0138\5\60\31")
        buf.write("\2\u0138\u0139\5.\30\2\u0139\u013b\3\2\2\2\u013a\u0135")
        buf.write("\3\2\2\2\u013a\u0136\3\2\2\2\u013b/\3\2\2\2\u013c\u013d")
        buf.write("\b\31\1\2\u013d\u014d\7\37\2\2\u013e\u014d\5@!\2\u013f")
        buf.write("\u014d\5\62\32\2\u0140\u014d\5v<\2\u0141\u014d\5\64\33")
        buf.write("\2\u0142\u014d\5\66\34\2\u0143\u014d\5<\37\2\u0144\u014d")
        buf.write("\5> \2\u0145\u0146\5\u0080A\2\u0146\u0147\5\60\31\4\u0147")
        buf.write("\u014d\3\2\2\2\u0148\u0149\7%\2\2\u0149\u014a\5\60\31")
        buf.write("\2\u014a\u014b\7&\2\2\u014b\u014d\3\2\2\2\u014c\u013c")
        buf.write("\3\2\2\2\u014c\u013e\3\2\2\2\u014c\u013f\3\2\2\2\u014c")
        buf.write("\u0140\3\2\2\2\u014c\u0141\3\2\2\2\u014c\u0142\3\2\2\2")
        buf.write("\u014c\u0143\3\2\2\2\u014c\u0144\3\2\2\2\u014c\u0145\3")
        buf.write("\2\2\2\u014c\u0148\3\2\2\2\u014d\u0154\3\2\2\2\u014e\u014f")
        buf.write("\f\5\2\2\u014f\u0150\5\u0082B\2\u0150\u0151\5\60\31\6")
        buf.write("\u0151\u0153\3\2\2\2\u0152\u014e\3\2\2\2\u0153\u0156\3")
        buf.write("\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\61")
        buf.write("\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\7\5\2\2\u0158")
        buf.write("\u0159\7\37\2\2\u0159\u015a\7%\2\2\u015a\u015b\5,\27\2")
        buf.write("\u015b\u015c\7&\2\2\u015c\63\3\2\2\2\u015d\u015e\7\37")
        buf.write("\2\2\u015e\u015f\7!\2\2\u015f\u0160\7\37\2\2\u0160\u0161")
        buf.write("\7%\2\2\u0161\u0162\58\35\2\u0162\u0163\7&\2\2\u0163\65")
        buf.write("\3\2\2\2\u0164\u0165\7\37\2\2\u0165\u0166\7\4\2\2\u0166")
        buf.write("\u0167\7\36\2\2\u0167\u0168\7%\2\2\u0168\u0169\58\35\2")
        buf.write("\u0169\u016a\7&\2\2\u016a\67\3\2\2\2\u016b\u0173\3\2\2")
        buf.write("\2\u016c\u0173\5Z.\2\u016d\u0173\5b\62\2\u016e\u016f\5")
        buf.write("Z.\2\u016f\u0170\7\"\2\2\u0170\u0171\5b\62\2\u0171\u0173")
        buf.write("\3\2\2\2\u0172\u016b\3\2\2\2\u0172\u016c\3\2\2\2\u0172")
        buf.write("\u016d\3\2\2\2\u0172\u016e\3\2\2\2\u01739\3\2\2\2\u0174")
        buf.write("\u0177\5<\37\2\u0175\u0177\5> \2\u0176\u0174\3\2\2\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177;\3\2\2\2\u0178\u0179\7\37\2\2\u0179")
        buf.write("\u017a\7!\2\2\u017a\u017b\7\37\2\2\u017b=\3\2\2\2\u017c")
        buf.write("\u017d\7\37\2\2\u017d\u017e\7\4\2\2\u017e\u017f\7\36\2")
        buf.write("\2\u017f?\3\2\2\2\u0180\u0183\7\37\2\2\u0181\u0183\5:")
        buf.write("\36\2\u0182\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183\u0188")
        buf.write("\3\2\2\2\u0184\u0185\7#\2\2\u0185\u0186\5B\"\2\u0186\u0187")
        buf.write("\7$\2\2\u0187\u0189\3\2\2\2\u0188\u0184\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018bA\3\2\2\2\u018c\u0190\5x=\2\u018d\u0190\7\37\2\2")
        buf.write("\u018e\u0190\5:\36\2\u018f\u018c\3\2\2\2\u018f\u018d\3")
        buf.write("\2\2\2\u018f\u018e\3\2\2\2\u0190C\3\2\2\2\u0191\u0195")
        buf.write("\7\22\2\2\u0192\u0195\7\37\2\2\u0193\u0195\5:\36\2\u0194")
        buf.write("\u0191\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0193\3\2\2\2")
        buf.write("\u0195E\3\2\2\2\u0196\u019b\3\2\2\2\u0197\u0198\5J&\2")
        buf.write("\u0198\u0199\5H%\2\u0199\u019b\3\2\2\2\u019a\u0196\3\2")
        buf.write("\2\2\u019a\u0197\3\2\2\2\u019bG\3\2\2\2\u019c\u01a2\3")
        buf.write("\2\2\2\u019d\u019e\7\"\2\2\u019e\u019f\5J&\2\u019f\u01a0")
        buf.write("\5H%\2\u01a0\u01a2\3\2\2\2\u01a1\u019c\3\2\2\2\u01a1\u019d")
        buf.write("\3\2\2\2\u01a2I\3\2\2\2\u01a3\u01a4\7\26\2\2\u01a4\u01a5")
        buf.write("\7%\2\2\u01a5\u01a6\5N(\2\u01a6\u01a7\7&\2\2\u01a7K\3")
        buf.write("\2\2\2\u01a8\u01a9\7\26\2\2\u01a9\u01aa\7%\2\2\u01aa\u01ab")
        buf.write("\5F$\2\u01ab\u01ac\7&\2\2\u01acM\3\2\2\2\u01ad\u01b2\5")
        buf.write("f\64\2\u01ae\u01b2\5j\66\2\u01af\u01b2\5n8\2\u01b0\u01b2")
        buf.write("\5r:\2\u01b1\u01ad\3\2\2\2\u01b1\u01ae\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2O\3\2\2\2\u01b3\u01b4")
        buf.write("\t\4\2\2\u01b4Q\3\2\2\2\u01b5\u01b6\t\5\2\2\u01b6S\3\2")
        buf.write("\2\2\u01b7\u01b8\t\6\2\2\u01b8U\3\2\2\2\u01b9\u01ba\t")
        buf.write("\7\2\2\u01baW\3\2\2\2\u01bb\u01bc\t\b\2\2\u01bcY\3\2\2")
        buf.write("\2\u01bd\u01c2\3\2\2\2\u01be\u01bf\5v<\2\u01bf\u01c0\5")
        buf.write("\\/\2\u01c0\u01c2\3\2\2\2\u01c1\u01bd\3\2\2\2\u01c1\u01be")
        buf.write("\3\2\2\2\u01c2[\3\2\2\2\u01c3\u01c9\3\2\2\2\u01c4\u01c5")
        buf.write("\7\"\2\2\u01c5\u01c6\5v<\2\u01c6\u01c7\5\\/\2\u01c7\u01c9")
        buf.write("\3\2\2\2\u01c8\u01c3\3\2\2\2\u01c8\u01c4\3\2\2\2\u01c9")
        buf.write("]\3\2\2\2\u01ca\u01ce\3\2\2\2\u01cb\u01cc\7\36\2\2\u01cc")
        buf.write("\u01ce\5`\61\2\u01cd\u01ca\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01ce_\3\2\2\2\u01cf\u01d4\3\2\2\2\u01d0\u01d1\7\"\2")
        buf.write("\2\u01d1\u01d2\7\36\2\2\u01d2\u01d4\5`\61\2\u01d3\u01cf")
        buf.write("\3\2\2\2\u01d3\u01d0\3\2\2\2\u01d4a\3\2\2\2\u01d5\u01d9")
        buf.write("\3\2\2\2\u01d6\u01d7\7\37\2\2\u01d7\u01d9\5d\63\2\u01d8")
        buf.write("\u01d5\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9c\3\2\2\2\u01da")
        buf.write("\u01df\3\2\2\2\u01db\u01dc\7\"\2\2\u01dc\u01dd\7\37\2")
        buf.write("\2\u01dd\u01df\5d\63\2\u01de\u01da\3\2\2\2\u01de\u01db")
        buf.write("\3\2\2\2\u01dfe\3\2\2\2\u01e0\u01e5\3\2\2\2\u01e1\u01e2")
        buf.write("\5x=\2\u01e2\u01e3\5h\65\2\u01e3\u01e5\3\2\2\2\u01e4\u01e0")
        buf.write("\3\2\2\2\u01e4\u01e1\3\2\2\2\u01e5g\3\2\2\2\u01e6\u01ec")
        buf.write("\3\2\2\2\u01e7\u01e8\7\"\2\2\u01e8\u01e9\5x=\2\u01e9\u01ea")
        buf.write("\5h\65\2\u01ea\u01ec\3\2\2\2\u01eb\u01e6\3\2\2\2\u01eb")
        buf.write("\u01e7\3\2\2\2\u01eci\3\2\2\2\u01ed\u01f1\3\2\2\2\u01ee")
        buf.write("\u01ef\7\24\2\2\u01ef\u01f1\5l\67\2\u01f0\u01ed\3\2\2")
        buf.write("\2\u01f0\u01ee\3\2\2\2\u01f1k\3\2\2\2\u01f2\u01f7\3\2")
        buf.write("\2\2\u01f3\u01f4\7\"\2\2\u01f4\u01f5\7\24\2\2\u01f5\u01f7")
        buf.write("\5l\67\2\u01f6\u01f2\3\2\2\2\u01f6\u01f3\3\2\2\2\u01f7")
        buf.write("m\3\2\2\2\u01f8\u01fc\3\2\2\2\u01f9\u01fa\7\22\2\2\u01fa")
        buf.write("\u01fc\5p9\2\u01fb\u01f8\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc")
        buf.write("o\3\2\2\2\u01fd\u0202\3\2\2\2\u01fe\u01ff\7\"\2\2\u01ff")
        buf.write("\u0200\7\22\2\2\u0200\u0202\5p9\2\u0201\u01fd\3\2\2\2")
        buf.write("\u0201\u01fe\3\2\2\2\u0202q\3\2\2\2\u0203\u0207\3\2\2")
        buf.write("\2\u0204\u0205\7\3\2\2\u0205\u0207\5t;\2\u0206\u0203\3")
        buf.write("\2\2\2\u0206\u0204\3\2\2\2\u0207s\3\2\2\2\u0208\u020d")
        buf.write("\3\2\2\2\u0209\u020a\7\"\2\2\u020a\u020b\7\3\2\2\u020b")
        buf.write("\u020d\5t;\2\u020c\u0208\3\2\2\2\u020c\u0209\3\2\2\2\u020d")
        buf.write("u\3\2\2\2\u020e\u0213\7\22\2\2\u020f\u0213\7\24\2\2\u0210")
        buf.write("\u0213\7\3\2\2\u0211\u0213\5x=\2\u0212\u020e\3\2\2\2\u0212")
        buf.write("\u020f\3\2\2\2\u0212\u0210\3\2\2\2\u0212\u0211\3\2\2\2")
        buf.write("\u0213w\3\2\2\2\u0214\u0215\t\t\2\2\u0215y\3\2\2\2\u0216")
        buf.write("\u0217\t\n\2\2\u0217{\3\2\2\2\u0218\u0219\5x=\2\u0219")
        buf.write("}\3\2\2\2\u021a\u021b\7\26\2\2\u021b\u021c\7#\2\2\u021c")
        buf.write("\u021d\5z>\2\u021d\u021e\7\"\2\2\u021e\u021f\5|?\2\u021f")
        buf.write("\u0220\7$\2\2\u0220\177\3\2\2\2\u0221\u0222\t\13\2\2\u0222")
        buf.write("\u0081\3\2\2\2\u0223\u0224\t\f\2\2\u0224\u0083\3\2\2\2")
        buf.write("/\u008b\u0092\u0094\u00a5\u00b1\u00bd\u00c4\u00d0\u00d6")
        buf.write("\u00e1\u00f3\u00f8\u0102\u010b\u0115\u0121\u012d\u0133")
        buf.write("\u013a\u014c\u0154\u0172\u0176\u0182\u018a\u018f\u0194")
        buf.write("\u019a\u01a1\u01b1\u01c1\u01c8\u01cd\u01d3\u01d8\u01de")
        buf.write("\u01e4\u01eb\u01f0\u01f6\u01fb\u0201\u0206\u020c\u0212")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'::'", "'New'", "'Return'", 
                     "'='", "'Break'", "'Continue'", "'If'", "'Else'", "'Elseif'", 
                     "'Foreach'", "'In'", "'Constructor'", "'Destructor'", 
                     "'Class'", "<INVALID>", "'By'", "<INVALID>", "<INVALID>", 
                     "'Array'", "'Int'", "'Float'", "'Boolean'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'0'", "'.'", "','", "'['", "']'", "'('", 
                     "')'", "'{'", "'}'", "'..'", "':'", "';'", "'+'", "'<='", 
                     "'>='", "'-'", "'*'", "'<'", "'%'", "'/'", "'!='", 
                     "'=='", "'>'", "'&&'", "'||'", "'!'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>", "STRINGLIT", "MEM_ACCESS_OP", "NEW", 
                      "RETURN", "ASSIGN_OP", "BREAK", "CONTINUE", "IF", 
                      "ELSE", "ELSEIF", "FOREACH", "IN", "CONSTRUCTOR", 
                      "DESTRUCTOR", "CLASS", "FLOATLIT", "BY", "BOOLIT", 
                      "VAL_VAR", "ARRAY", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
                      "INTLIT_16", "INTLIT_2", "INTLIT_8", "INTLIT_10", 
                      "DOLLAR_ID", "ID", "ZERO", "DOT", "CM", "LS", "RS", 
                      "LB", "RB", "LP", "RP", "RANGE", "CL", "SEMI", "ADDOP", 
                      "LESS_EQUAL", "GREAT_EQUAL", "SUBOP", "MULOP", "LESS_THAN", 
                      "MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", "GREAT_THAN", 
                      "AND", "OR", "NEGATE", "STR_CMP", "STR_CONCAT", "COMMENT", 
                      "WS", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_dcl = 1
    RULE_class_body = 2
    RULE_att_dcl = 3
    RULE_att_dcl_list = 4
    RULE_method_dcl = 5
    RULE_para_dcl_list = 6
    RULE_para_dcl_smcllist = 7
    RULE_para_dcl = 8
    RULE_stm = 9
    RULE_for_in_stm = 10
    RULE_if_stm = 11
    RULE_block_stm = 12
    RULE_mn_stm = 13
    RULE_continue_stm = 14
    RULE_break_stm = 15
    RULE_asm_stm = 16
    RULE_return_stm = 17
    RULE_method_invoke_stm = 18
    RULE_var_dcl = 19
    RULE_var_dcl_list = 20
    RULE_expr_list = 21
    RULE_expr_cmlist = 22
    RULE_expr = 23
    RULE_object_ini = 24
    RULE_instance_method_invoke = 25
    RULE_static_mehod_invoke = 26
    RULE_para_pass_list = 27
    RULE_att_access = 28
    RULE_instance_att_access = 29
    RULE_static_att_access = 30
    RULE_index_ele = 31
    RULE_int_object = 32
    RULE_float_object = 33
    RULE_index_arr_list = 34
    RULE_index_arr_cmlist = 35
    RULE_index_arr = 36
    RULE_mul_dim_arr = 37
    RULE_same_type_list = 38
    RULE_string_op = 39
    RULE_bool_op = 40
    RULE_relation_op = 41
    RULE_int_op = 42
    RULE_float_op = 43
    RULE_lit_list = 44
    RULE_lit_cmlist = 45
    RULE_static_id_list = 46
    RULE_static_id_cmlist = 47
    RULE_id_list = 48
    RULE_id_cmlist = 49
    RULE_int_gen_list = 50
    RULE_int_gen_cm = 51
    RULE_bool_list = 52
    RULE_bool_list_cm = 53
    RULE_float_list = 54
    RULE_float_list_cm = 55
    RULE_string_list = 56
    RULE_string_list_cm = 57
    RULE_lit = 58
    RULE_int_gen = 59
    RULE_data_type = 60
    RULE_size = 61
    RULE_array_type = 62
    RULE_unary_op = 63
    RULE_binary_op = 64

    ruleNames =  [ "program", "class_dcl", "class_body", "att_dcl", "att_dcl_list", 
                   "method_dcl", "para_dcl_list", "para_dcl_smcllist", "para_dcl", 
                   "stm", "for_in_stm", "if_stm", "block_stm", "mn_stm", 
                   "continue_stm", "break_stm", "asm_stm", "return_stm", 
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
                   "array_type", "unary_op", "binary_op" ]

    EOF = Token.EOF
    STRINGLIT=1
    MEM_ACCESS_OP=2
    NEW=3
    RETURN=4
    ASSIGN_OP=5
    BREAK=6
    CONTINUE=7
    IF=8
    ELSE=9
    ELSEIF=10
    FOREACH=11
    IN=12
    CONSTRUCTOR=13
    DESTRUCTOR=14
    CLASS=15
    FLOATLIT=16
    BY=17
    BOOLIT=18
    VAL_VAR=19
    ARRAY=20
    INT_TYPE=21
    FLOAT_TYPE=22
    BOOL_TYPE=23
    INTLIT_16=24
    INTLIT_2=25
    INTLIT_8=26
    INTLIT_10=27
    DOLLAR_ID=28
    ID=29
    ZERO=30
    DOT=31
    CM=32
    LS=33
    RS=34
    LB=35
    RB=36
    LP=37
    RP=38
    RANGE=39
    CL=40
    SEMI=41
    ADDOP=42
    LESS_EQUAL=43
    GREAT_EQUAL=44
    SUBOP=45
    MULOP=46
    LESS_THAN=47
    MODOP=48
    DIVOP=49
    NOT_EQUAL=50
    EQUAL=51
    GREAT_THAN=52
    AND=53
    OR=54
    NEGATE=55
    STR_CMP=56
    STR_CONCAT=57
    COMMENT=58
    WS=59
    ILLEGAL_ESCAPE=60
    UNCLOSED_STRING=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

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
            self.state = 130
            self.expr(0)
            self.state = 131
            self.match(D96Parser.EOF)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_dcl" ):
                return visitor.visitClass_dcl(self)
            else:
                return visitor.visitChildren(self)




    def class_dcl(self):

        localctx = D96Parser.Class_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(D96Parser.CLASS)
            self.state = 134
            self.match(D96Parser.ID)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.CL:
                self.state = 135
                self.match(D96Parser.CL)
                self.state = 136
                self.id_list()


            self.state = 139
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(D96Parser.LP)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.VAL_VAR) | (1 << D96Parser.DOLLAR_ID) | (1 << D96Parser.ID))) != 0):
                self.state = 144
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL_VAR]:
                    self.state = 142
                    self.att_dcl()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.DOLLAR_ID, D96Parser.ID]:
                    self.state = 143
                    self.method_dcl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
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

        def att_dcl_list(self):
            return self.getTypedRuleContext(D96Parser.Att_dcl_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_att_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_dcl" ):
                return visitor.visitAtt_dcl(self)
            else:
                return visitor.visitChildren(self)




    def att_dcl(self):

        localctx = D96Parser.Att_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_att_dcl)
        self._la = 0 # Token type
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(D96Parser.VAL_VAR)
                self.state = 152
                self.static_id_list()
                self.state = 153
                self.match(D96Parser.CL)
                self.state = 154
                self.data_type()
                self.state = 155
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(D96Parser.VAL_VAR)
                self.state = 158
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 159
                self.att_dcl_list()
                self.state = 160
                self.expr(0)
                self.state = 161
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

        def att_dcl_list(self):
            return self.getTypedRuleContext(D96Parser.Att_dcl_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_att_dcl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_dcl_list" ):
                return visitor.visitAtt_dcl_list(self)
            else:
                return visitor.visitChildren(self)




    def att_dcl_list(self):

        localctx = D96Parser.Att_dcl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_att_dcl_list)
        self._la = 0 # Token type
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(D96Parser.CL)
                self.state = 166
                self.data_type()
                self.state = 167
                self.match(D96Parser.ASSIGN_OP)
                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(D96Parser.CM)
                self.state = 170
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 171
                self.att_dcl_list()
                self.state = 172
                self.expr(0)
                self.state = 173
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

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_dcl" ):
                return visitor.visitMethod_dcl(self)
            else:
                return visitor.visitChildren(self)




    def method_dcl(self):

        localctx = D96Parser.Method_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_method_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.DOLLAR_ID) | (1 << D96Parser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 178
            self.match(D96Parser.LB)
            self.state = 179
            self.para_dcl_smcllist()
            self.state = 180
            self.match(D96Parser.RB)
            self.state = 181
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_dcl_list" ):
                return visitor.visitPara_dcl_list(self)
            else:
                return visitor.visitChildren(self)




    def para_dcl_list(self):

        localctx = D96Parser.Para_dcl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_para_dcl_list)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ID, D96Parser.CL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.para_dcl()
                self.state = 185
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_dcl_smcllist" ):
                return visitor.visitPara_dcl_smcllist(self)
            else:
                return visitor.visitChildren(self)




    def para_dcl_smcllist(self):

        localctx = D96Parser.Para_dcl_smcllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_para_dcl_smcllist)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF, D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(D96Parser.SEMI)
                self.state = 191
                self.para_dcl()
                self.state = 192
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_dcl" ):
                return visitor.visitPara_dcl(self)
            else:
                return visitor.visitChildren(self)




    def para_dcl(self):

        localctx = D96Parser.Para_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_para_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.id_list()
            self.state = 197
            self.match(D96Parser.CL)
            self.state = 198
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = D96Parser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stm)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RETURN, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.VAL_VAR, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 200
                    self.asm_stm()
                    pass

                elif la_ == 2:
                    self.state = 201
                    self.var_dcl()
                    pass

                elif la_ == 3:
                    self.state = 202
                    self.break_stm()
                    pass

                elif la_ == 4:
                    self.state = 203
                    self.continue_stm()
                    pass

                elif la_ == 5:
                    self.state = 204
                    self.return_stm()
                    pass

                elif la_ == 6:
                    self.state = 205
                    self.method_invoke_stm()
                    pass


                self.state = 208
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.if_stm()
                pass
            elif token in [D96Parser.FOREACH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_stm" ):
                return visitor.visitFor_in_stm(self)
            else:
                return visitor.visitChildren(self)




    def for_in_stm(self):

        localctx = D96Parser.For_in_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_for_in_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(D96Parser.FOREACH)
            self.state = 215
            self.match(D96Parser.LB)
            self.state = 216
            self.match(D96Parser.ID)
            self.state = 217
            self.match(D96Parser.IN)
            self.state = 218
            self.expr(0)
            self.state = 219
            self.match(D96Parser.RANGE)
            self.state = 220
            self.expr(0)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 221
                self.match(D96Parser.BY)
                self.state = 222
                self.expr(0)


            self.state = 225
            self.match(D96Parser.RB)
            self.state = 226
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = D96Parser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(D96Parser.IF)
            self.state = 229
            self.match(D96Parser.LB)
            self.state = 230
            self.expr(0)
            self.state = 231
            self.match(D96Parser.RB)
            self.state = 232
            self.block_stm()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 233
                self.match(D96Parser.ELSEIF)
                self.state = 234
                self.match(D96Parser.LB)
                self.state = 235
                self.expr(0)
                self.state = 236
                self.match(D96Parser.RB)
                self.state = 237
                self.block_stm()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 244
                self.match(D96Parser.ELSE)
                self.state = 245
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stm" ):
                return visitor.visitBlock_stm(self)
            else:
                return visitor.visitChildren(self)




    def block_stm(self):

        localctx = D96Parser.Block_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(D96Parser.LP)
            self.state = 249
            self.mn_stm()
            self.state = 250
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMn_stm" ):
                return visitor.visitMn_stm(self)
            else:
                return visitor.visitChildren(self)




    def mn_stm(self):

        localctx = D96Parser.Mn_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_mn_stm)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.RETURN, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.VAL_VAR, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.stm()
                self.state = 254
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = D96Parser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = D96Parser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm_stm" ):
                return visitor.visitAsm_stm(self)
            else:
                return visitor.visitChildren(self)




    def asm_stm(self):

        localctx = D96Parser.Asm_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_asm_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 262
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 263
                self.att_access()
                pass

            elif la_ == 3:
                self.state = 264
                self.index_ele()
                pass


            self.state = 267
            self.match(D96Parser.ASSIGN_OP)
            self.state = 268
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = D96Parser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(D96Parser.RETURN)
            self.state = 271
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invoke_stm" ):
                return visitor.visitMethod_invoke_stm(self)
            else:
                return visitor.visitChildren(self)




    def method_invoke_stm(self):

        localctx = D96Parser.Method_invoke_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_method_invoke_stm)
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.instance_method_invoke()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dcl" ):
                return visitor.visitVar_dcl(self)
            else:
                return visitor.visitChildren(self)




    def var_dcl(self):

        localctx = D96Parser.Var_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_dcl)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(D96Parser.VAL_VAR)
                self.state = 278
                self.id_list()
                self.state = 279
                self.match(D96Parser.CL)
                self.state = 280
                self.data_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(D96Parser.VAL_VAR)
                self.state = 283
                self.match(D96Parser.ID)
                self.state = 284
                self.var_dcl_list()
                self.state = 285
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dcl_list" ):
                return visitor.visitVar_dcl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_dcl_list(self):

        localctx = D96Parser.Var_dcl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_dcl_list)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(D96Parser.CL)
                self.state = 290
                self.data_type()
                self.state = 291
                self.match(D96Parser.ASSIGN_OP)
                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.match(D96Parser.CM)
                self.state = 294
                self.match(D96Parser.ID)
                self.state = 295
                self.var_dcl_list()
                self.state = 296
                self.expr(0)
                self.state = 297
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr_list)
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT, D96Parser.NEW, D96Parser.FLOATLIT, D96Parser.BOOLIT, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10, D96Parser.ID, D96Parser.LB, D96Parser.SUBOP, D96Parser.NEGATE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.expr(0)
                self.state = 303
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_cmlist" ):
                return visitor.visitExpr_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def expr_cmlist(self):

        localctx = D96Parser.Expr_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr_cmlist)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(D96Parser.CM)
                self.state = 309
                self.expr(0)
                self.state = 310
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 315
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 316
                self.index_ele()
                pass

            elif la_ == 3:
                self.state = 317
                self.object_ini()
                pass

            elif la_ == 4:
                self.state = 318
                self.lit()
                pass

            elif la_ == 5:
                self.state = 319
                self.instance_method_invoke()
                pass

            elif la_ == 6:
                self.state = 320
                self.static_mehod_invoke()
                pass

            elif la_ == 7:
                self.state = 321
                self.instance_att_access()
                pass

            elif la_ == 8:
                self.state = 322
                self.static_att_access()
                pass

            elif la_ == 9:
                self.state = 323
                self.unary_op()
                self.state = 324
                self.expr(2)
                pass

            elif la_ == 10:
                self.state = 326
                self.match(D96Parser.LB)
                self.state = 327
                self.expr(0)
                self.state = 328
                self.match(D96Parser.RB)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 332
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 333
                    self.binary_op()
                    self.state = 334
                    self.expr(4) 
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_ini" ):
                return visitor.visitObject_ini(self)
            else:
                return visitor.visitChildren(self)




    def object_ini(self):

        localctx = D96Parser.Object_iniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_object_ini)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(D96Parser.NEW)
            self.state = 342
            self.match(D96Parser.ID)
            self.state = 343
            self.match(D96Parser.LB)
            self.state = 344
            self.expr_list()
            self.state = 345
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invoke" ):
                return visitor.visitInstance_method_invoke(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invoke(self):

        localctx = D96Parser.Instance_method_invokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_instance_method_invoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(D96Parser.ID)
            self.state = 348
            self.match(D96Parser.DOT)
            self.state = 349
            self.match(D96Parser.ID)
            self.state = 350
            self.match(D96Parser.LB)
            self.state = 351
            self.para_pass_list()
            self.state = 352
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def MEM_ACCESS_OP(self):
            return self.getToken(D96Parser.MEM_ACCESS_OP, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def para_pass_list(self):
            return self.getTypedRuleContext(D96Parser.Para_pass_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_mehod_invoke

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_mehod_invoke" ):
                return visitor.visitStatic_mehod_invoke(self)
            else:
                return visitor.visitChildren(self)




    def static_mehod_invoke(self):

        localctx = D96Parser.Static_mehod_invokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_static_mehod_invoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(D96Parser.ID)
            self.state = 355
            self.match(D96Parser.MEM_ACCESS_OP)
            self.state = 356
            self.match(D96Parser.DOLLAR_ID)
            self.state = 357
            self.match(D96Parser.LB)
            self.state = 358
            self.para_pass_list()
            self.state = 359
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_pass_list" ):
                return visitor.visitPara_pass_list(self)
            else:
                return visitor.visitChildren(self)




    def para_pass_list(self):

        localctx = D96Parser.Para_pass_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_para_pass_list)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.lit_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 363
                self.id_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 364
                self.lit_list()
                self.state = 365
                self.match(D96Parser.CM)
                self.state = 366
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_access" ):
                return visitor.visitAtt_access(self)
            else:
                return visitor.visitChildren(self)




    def att_access(self):

        localctx = D96Parser.Att_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_att_access)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.instance_att_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_att_access" ):
                return visitor.visitInstance_att_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_att_access(self):

        localctx = D96Parser.Instance_att_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_instance_att_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(D96Parser.ID)
            self.state = 375
            self.match(D96Parser.DOT)
            self.state = 376
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def MEM_ACCESS_OP(self):
            return self.getToken(D96Parser.MEM_ACCESS_OP, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_att_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_att_access" ):
                return visitor.visitStatic_att_access(self)
            else:
                return visitor.visitChildren(self)




    def static_att_access(self):

        localctx = D96Parser.Static_att_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_static_att_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(D96Parser.ID)
            self.state = 379
            self.match(D96Parser.MEM_ACCESS_OP)
            self.state = 380
            self.match(D96Parser.DOLLAR_ID)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_ele" ):
                return visitor.visitIndex_ele(self)
            else:
                return visitor.visitChildren(self)




    def index_ele(self):

        localctx = D96Parser.Index_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_index_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 382
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 383
                self.att_access()
                pass


            self.state = 390 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 386
                    self.match(D96Parser.LS)
                    self.state = 387
                    self.int_object()
                    self.state = 388
                    self.match(D96Parser.RS)

                else:
                    raise NoViableAltException(self)
                self.state = 392 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_object" ):
                return visitor.visitInt_object(self)
            else:
                return visitor.visitChildren(self)




    def int_object(self):

        localctx = D96Parser.Int_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_int_object)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.int_gen()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
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

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def att_access(self):
            return self.getTypedRuleContext(D96Parser.Att_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_float_object

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_object" ):
                return visitor.visitFloat_object(self)
            else:
                return visitor.visitChildren(self)




    def float_object(self):

        localctx = D96Parser.Float_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_float_object)
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 401
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_arr_list" ):
                return visitor.visitIndex_arr_list(self)
            else:
                return visitor.visitChildren(self)




    def index_arr_list(self):

        localctx = D96Parser.Index_arr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_index_arr_list)
        try:
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.index_arr()
                self.state = 406
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_arr_cmlist" ):
                return visitor.visitIndex_arr_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def index_arr_cmlist(self):

        localctx = D96Parser.Index_arr_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_index_arr_cmlist)
        try:
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.match(D96Parser.CM)
                self.state = 412
                self.index_arr()
                self.state = 413
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_arr" ):
                return visitor.visitIndex_arr(self)
            else:
                return visitor.visitChildren(self)




    def index_arr(self):

        localctx = D96Parser.Index_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_index_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(D96Parser.ARRAY)
            self.state = 418
            self.match(D96Parser.LB)
            self.state = 419
            self.same_type_list()
            self.state = 420
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_dim_arr" ):
                return visitor.visitMul_dim_arr(self)
            else:
                return visitor.visitChildren(self)




    def mul_dim_arr(self):

        localctx = D96Parser.Mul_dim_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_mul_dim_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(D96Parser.ARRAY)
            self.state = 423
            self.match(D96Parser.LB)
            self.state = 424
            self.index_arr_list()
            self.state = 425
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSame_type_list" ):
                return visitor.visitSame_type_list(self)
            else:
                return visitor.visitChildren(self)




    def same_type_list(self):

        localctx = D96Parser.Same_type_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_same_type_list)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.int_gen_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.bool_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.float_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_op" ):
                return visitor.visitString_op(self)
            else:
                return visitor.visitChildren(self)




    def string_op(self):

        localctx = D96Parser.String_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_string_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_op" ):
                return visitor.visitBool_op(self)
            else:
                return visitor.visitChildren(self)




    def bool_op(self):

        localctx = D96Parser.Bool_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_bool_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_op" ):
                return visitor.visitRelation_op(self)
            else:
                return visitor.visitChildren(self)




    def relation_op(self):

        localctx = D96Parser.Relation_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_relation_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_op" ):
                return visitor.visitInt_op(self)
            else:
                return visitor.visitChildren(self)




    def int_op(self):

        localctx = D96Parser.Int_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_int_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_op" ):
                return visitor.visitFloat_op(self)
            else:
                return visitor.visitChildren(self)




    def float_op(self):

        localctx = D96Parser.Float_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_float_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_list" ):
                return visitor.visitLit_list(self)
            else:
                return visitor.visitChildren(self)




    def lit_list(self):

        localctx = D96Parser.Lit_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_lit_list)
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CM, D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.BOOLIT, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.lit()
                self.state = 445
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_cmlist" ):
                return visitor.visitLit_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def lit_cmlist(self):

        localctx = D96Parser.Lit_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_lit_cmlist)
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.match(D96Parser.CM)
                self.state = 451
                self.lit()
                self.state = 452
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

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def static_id_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Static_id_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_id_list" ):
                return visitor.visitStatic_id_list(self)
            else:
                return visitor.visitChildren(self)




    def static_id_list(self):

        localctx = D96Parser.Static_id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_static_id_list)
        try:
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.match(D96Parser.DOLLAR_ID)
                self.state = 458
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

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def static_id_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Static_id_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_id_cmlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_id_cmlist" ):
                return visitor.visitStatic_id_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def static_id_cmlist(self):

        localctx = D96Parser.Static_id_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_static_id_cmlist)
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.match(D96Parser.CM)
                self.state = 463
                self.match(D96Parser.DOLLAR_ID)
                self.state = 464
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_id_list)
        try:
            self.state = 470
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB, D96Parser.LP, D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.match(D96Parser.ID)
                self.state = 469
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_cmlist" ):
                return visitor.visitId_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def id_cmlist(self):

        localctx = D96Parser.Id_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_id_cmlist)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB, D96Parser.LP, D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.match(D96Parser.CM)
                self.state = 474
                self.match(D96Parser.ID)
                self.state = 475
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_gen_list" ):
                return visitor.visitInt_gen_list(self)
            else:
                return visitor.visitChildren(self)




    def int_gen_list(self):

        localctx = D96Parser.Int_gen_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_int_gen_list)
        try:
            self.state = 482
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.int_gen()
                self.state = 480
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_gen_cm" ):
                return visitor.visitInt_gen_cm(self)
            else:
                return visitor.visitChildren(self)




    def int_gen_cm(self):

        localctx = D96Parser.Int_gen_cmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_int_gen_cm)
        try:
            self.state = 489
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.match(D96Parser.CM)
                self.state = 486
                self.int_gen()
                self.state = 487
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_list" ):
                return visitor.visitBool_list(self)
            else:
                return visitor.visitChildren(self)




    def bool_list(self):

        localctx = D96Parser.Bool_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_bool_list)
        try:
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.match(D96Parser.BOOLIT)
                self.state = 493
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_list_cm" ):
                return visitor.visitBool_list_cm(self)
            else:
                return visitor.visitChildren(self)




    def bool_list_cm(self):

        localctx = D96Parser.Bool_list_cmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_bool_list_cm)
        try:
            self.state = 500
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
                self.match(D96Parser.CM)
                self.state = 498
                self.match(D96Parser.BOOLIT)
                self.state = 499
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_list" ):
                return visitor.visitFloat_list(self)
            else:
                return visitor.visitChildren(self)




    def float_list(self):

        localctx = D96Parser.Float_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_float_list)
        try:
            self.state = 505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.match(D96Parser.FLOATLIT)
                self.state = 504
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_list_cm" ):
                return visitor.visitFloat_list_cm(self)
            else:
                return visitor.visitChildren(self)




    def float_list_cm(self):

        localctx = D96Parser.Float_list_cmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_float_list_cm)
        try:
            self.state = 511
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.match(D96Parser.CM)
                self.state = 509
                self.match(D96Parser.FLOATLIT)
                self.state = 510
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_list" ):
                return visitor.visitString_list(self)
            else:
                return visitor.visitChildren(self)




    def string_list(self):

        localctx = D96Parser.String_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_string_list)
        try:
            self.state = 516
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 514
                self.match(D96Parser.STRINGLIT)
                self.state = 515
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_list_cm" ):
                return visitor.visitString_list_cm(self)
            else:
                return visitor.visitChildren(self)




    def string_list_cm(self):

        localctx = D96Parser.String_list_cmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_string_list_cm)
        try:
            self.state = 522
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
                self.match(D96Parser.CM)
                self.state = 520
                self.match(D96Parser.STRINGLIT)
                self.state = 521
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

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def int_gen(self):
            return self.getTypedRuleContext(D96Parser.Int_genContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = D96Parser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_lit)
        try:
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.match(D96Parser.BOOLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 526
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 527
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_gen" ):
                return visitor.visitInt_gen(self)
            else:
                return visitor.visitChildren(self)




    def int_gen(self):

        localctx = D96Parser.Int_genContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_int_gen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = D96Parser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(D96Parser.ARRAY)
            self.state = 537
            self.match(D96Parser.LS)
            self.state = 538
            self.data_type()
            self.state = 539
            self.match(D96Parser.CM)
            self.state = 540
            self.size()
            self.state = 541
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_op" ):
                return visitor.visitUnary_op(self)
            else:
                return visitor.visitChildren(self)




    def unary_op(self):

        localctx = D96Parser.Unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_op" ):
                return visitor.visitBinary_op(self)
            else:
                return visitor.visitChildren(self)




    def binary_op(self):

        localctx = D96Parser.Binary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_binary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




