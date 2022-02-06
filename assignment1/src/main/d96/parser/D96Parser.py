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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u027c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\3\2\6\2\u0090\n\2\r\2\16\2\u0091\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\5\3\u009a\n\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\7\4\u00a1\n\4\f\4\16\4\u00a4\13\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\5\5\u00ab\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\5\6\u00b9\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7\u00c5\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\7\t\u00d0\n\t\f\t\16\t\u00d3\13\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u00db\n\n\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00e2\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u00ee\n\r\3\r\3\r\3\r\3\r\3\r\5\r\u00f5\n\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0100\n\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\7\17\u0110\n\17\f\17\16\17\u0113\13\17")
        buf.write("\3\17\3\17\5\17\u0117\n\17\3\20\3\20\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\5\21\u0121\n\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u012b\n\24\3\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\5\25\u0133\n\25\3\26\3\26\5\26\u0137\n\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0143")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u014f\n\30\3\31\3\31\3\31\3\31\5\31\u0155\n\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\5\32\u015c\n\32\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u016e\n\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\5\34\u017b\n\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0190\n\34\f\34\16")
        buf.write("\34\u0193\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\5!\u01ad\n!\3\"\3\"\3\"\3\"\3\"\7\"")
        buf.write("\u01b4\n\"\f\"\16\"\u01b7\13\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\7#\u01c1\n#\f#\16#\u01c4\13#\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\6$\u01ce\n$\r$\16$\u01cf\3%\3%\3%\3%\3%\6%\u01d7")
        buf.write("\n%\r%\16%\u01d8\3&\3&\3&\5&\u01de\n&\3\'\3\'\3\'\5\'")
        buf.write("\u01e3\n\'\3(\3(\3(\3(\5(\u01e9\n(\3)\3)\3)\3)\3)\5)\u01f0")
        buf.write("\n)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\5,\u0200")
        buf.write("\n,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\62\5\62\u0210\n\62\3\63\3\63\3\63\3\63\3\63\5\63")
        buf.write("\u0217\n\63\3\64\3\64\3\64\5\64\u021c\n\64\3\65\3\65\3")
        buf.write("\65\3\65\5\65\u0222\n\65\3\66\3\66\3\66\5\66\u0227\n\66")
        buf.write("\3\67\3\67\3\67\3\67\5\67\u022d\n\67\38\38\38\38\58\u0233")
        buf.write("\n8\39\39\39\39\39\59\u023a\n9\3:\3:\3:\5:\u023f\n:\3")
        buf.write(";\3;\3;\3;\5;\u0245\n;\3<\3<\3<\5<\u024a\n<\3=\3=\3=\3")
        buf.write("=\5=\u0250\n=\3>\3>\3>\5>\u0255\n>\3?\3?\3?\3?\5?\u025b")
        buf.write("\n?\3@\3@\3@\3@\5@\u0261\n@\3A\3A\3B\3B\3B\3B\3B\3B\5")
        buf.write("B\u026b\nB\3C\3C\3D\3D\3D\3D\3D\3D\3D\3E\3E\3F\3F\3G\3")
        buf.write("G\3G\2\3\66H\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\2\16\3\2")
        buf.write("$%\4\2\21\22$%\3\2?@\4\29:<>\4\2\66\669;\3\2\61:\4\2\61")
        buf.write("\6699\4\2\36\36 #\3\2 #\4\2\64\64>>\6\2\5\5&&\61=?@\3")
        buf.write("\2\34\37\2\u028a\2\u008f\3\2\2\2\4\u0095\3\2\2\2\6\u009d")
        buf.write("\3\2\2\2\b\u00aa\3\2\2\2\n\u00b8\3\2\2\2\f\u00c4\3\2\2")
        buf.write("\2\16\u00c6\3\2\2\2\20\u00cc\3\2\2\2\22\u00da\3\2\2\2")
        buf.write("\24\u00e1\3\2\2\2\26\u00e3\3\2\2\2\30\u00f4\3\2\2\2\32")
        buf.write("\u00f6\3\2\2\2\34\u0104\3\2\2\2\36\u0118\3\2\2\2 \u0120")
        buf.write("\3\2\2\2\"\u0122\3\2\2\2$\u0124\3\2\2\2&\u012a\3\2\2\2")
        buf.write("(\u012f\3\2\2\2*\u0136\3\2\2\2,\u0142\3\2\2\2.\u014e\3")
        buf.write("\2\2\2\60\u0154\3\2\2\2\62\u015b\3\2\2\2\64\u015d\3\2")
        buf.write("\2\2\66\u016d\3\2\2\28\u0194\3\2\2\2:\u019a\3\2\2\2<\u01a1")
        buf.write("\3\2\2\2>\u01a8\3\2\2\2@\u01ac\3\2\2\2B\u01ae\3\2\2\2")
        buf.write("D\u01bb\3\2\2\2F\u01c8\3\2\2\2H\u01d1\3\2\2\2J\u01dd\3")
        buf.write("\2\2\2L\u01e2\3\2\2\2N\u01e8\3\2\2\2P\u01ef\3\2\2\2R\u01f1")
        buf.write("\3\2\2\2T\u01f6\3\2\2\2V\u01ff\3\2\2\2X\u0201\3\2\2\2")
        buf.write("Z\u0203\3\2\2\2\\\u0205\3\2\2\2^\u0207\3\2\2\2`\u0209")
        buf.write("\3\2\2\2b\u020f\3\2\2\2d\u0216\3\2\2\2f\u021b\3\2\2\2")
        buf.write("h\u0221\3\2\2\2j\u0226\3\2\2\2l\u022c\3\2\2\2n\u0232\3")
        buf.write("\2\2\2p\u0239\3\2\2\2r\u023e\3\2\2\2t\u0244\3\2\2\2v\u0249")
        buf.write("\3\2\2\2x\u024f\3\2\2\2z\u0254\3\2\2\2|\u025a\3\2\2\2")
        buf.write("~\u0260\3\2\2\2\u0080\u0262\3\2\2\2\u0082\u026a\3\2\2")
        buf.write("\2\u0084\u026c\3\2\2\2\u0086\u026e\3\2\2\2\u0088\u0275")
        buf.write("\3\2\2\2\u008a\u0277\3\2\2\2\u008c\u0279\3\2\2\2\u008e")
        buf.write("\u0090\5\4\3\2\u008f\u008e\3\2\2\2\u0090\u0091\3\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3")
        buf.write("\2\2\2\u0093\u0094\7\2\2\3\u0094\3\3\2\2\2\u0095\u0096")
        buf.write("\7\23\2\2\u0096\u0099\7%\2\2\u0097\u0098\7/\2\2\u0098")
        buf.write("\u009a\5j\66\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\u009c\5\6\4\2\u009c\5\3\2\2")
        buf.write("\2\u009d\u00a2\7,\2\2\u009e\u00a1\5\n\6\2\u009f\u00a1")
        buf.write("\5\16\b\2\u00a0\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1")
        buf.write("\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a6\7")
        buf.write("-\2\2\u00a6\7\3\2\2\2\u00a7\u00ab\5\64\33\2\u00a8\u00ab")
        buf.write("\5H%\2\u00a9\u00ab\5F$\2\u00aa\u00a7\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\t\3\2\2\2\u00ac\u00ad")
        buf.write("\7\27\2\2\u00ad\u00ae\5j\66\2\u00ae\u00af\7/\2\2\u00af")
        buf.write("\u00b0\5\u0082B\2\u00b0\u00b1\7\60\2\2\u00b1\u00b9\3\2")
        buf.write("\2\2\u00b2\u00b3\7\27\2\2\u00b3\u00b4\t\2\2\2\u00b4\u00b5")
        buf.write("\5\f\7\2\u00b5\u00b6\5\b\5\2\u00b6\u00b7\7\60\2\2\u00b7")
        buf.write("\u00b9\3\2\2\2\u00b8\u00ac\3\2\2\2\u00b8\u00b2\3\2\2\2")
        buf.write("\u00b9\13\3\2\2\2\u00ba\u00bb\7/\2\2\u00bb\u00bc\5\u0082")
        buf.write("B\2\u00bc\u00bd\7\t\2\2\u00bd\u00c5\3\2\2\2\u00be\u00bf")
        buf.write("\7\'\2\2\u00bf\u00c0\t\2\2\2\u00c0\u00c1\5\f\7\2\u00c1")
        buf.write("\u00c2\5\b\5\2\u00c2\u00c3\7\'\2\2\u00c3\u00c5\3\2\2\2")
        buf.write("\u00c4\u00ba\3\2\2\2\u00c4\u00be\3\2\2\2\u00c5\r\3\2\2")
        buf.write("\2\u00c6\u00c7\t\3\2\2\u00c7\u00c8\7*\2\2\u00c8\u00c9")
        buf.write("\5\22\n\2\u00c9\u00ca\7+\2\2\u00ca\u00cb\5\20\t\2\u00cb")
        buf.write("\17\3\2\2\2\u00cc\u00d1\7,\2\2\u00cd\u00d0\5\30\r\2\u00ce")
        buf.write("\u00d0\5\36\20\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2")
        buf.write("\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2")
        buf.write("\3\2\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4")
        buf.write("\u00d5\7-\2\2\u00d5\21\3\2\2\2\u00d6\u00db\3\2\2\2\u00d7")
        buf.write("\u00d8\5\26\f\2\u00d8\u00d9\5\24\13\2\u00d9\u00db\3\2")
        buf.write("\2\2\u00da\u00d6\3\2\2\2\u00da\u00d7\3\2\2\2\u00db\23")
        buf.write("\3\2\2\2\u00dc\u00e2\3\2\2\2\u00dd\u00de\7\60\2\2\u00de")
        buf.write("\u00df\5\26\f\2\u00df\u00e0\5\24\13\2\u00e0\u00e2\3\2")
        buf.write("\2\2\u00e1\u00dc\3\2\2\2\u00e1\u00dd\3\2\2\2\u00e2\25")
        buf.write("\3\2\2\2\u00e3\u00e4\5j\66\2\u00e4\u00e5\7/\2\2\u00e5")
        buf.write("\u00e6\5\u0082B\2\u00e6\27\3\2\2\2\u00e7\u00ee\5&\24\2")
        buf.write("\u00e8\u00ee\5,\27\2\u00e9\u00ee\5$\23\2\u00ea\u00ee\5")
        buf.write("\"\22\2\u00eb\u00ee\5(\25\2\u00ec\u00ee\5*\26\2\u00ed")
        buf.write("\u00e7\3\2\2\2\u00ed\u00e8\3\2\2\2\u00ed\u00e9\3\2\2\2")
        buf.write("\u00ed\u00ea\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3")
        buf.write("\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\7\60\2\2\u00f0")
        buf.write("\u00f5\3\2\2\2\u00f1\u00f5\5\34\17\2\u00f2\u00f5\5\32")
        buf.write("\16\2\u00f3\u00f5\5\36\20\2\u00f4\u00ed\3\2\2\2\u00f4")
        buf.write("\u00f1\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2")
        buf.write("\u00f5\31\3\2\2\2\u00f6\u00f7\7\17\2\2\u00f7\u00f8\7*")
        buf.write("\2\2\u00f8\u00f9\7%\2\2\u00f9\u00fa\7\20\2\2\u00fa\u00fb")
        buf.write("\5\b\5\2\u00fb\u00fc\7.\2\2\u00fc\u00ff\5\b\5\2\u00fd")
        buf.write("\u00fe\7\25\2\2\u00fe\u0100\5\b\5\2\u00ff\u00fd\3\2\2")
        buf.write("\2\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102")
        buf.write("\7+\2\2\u0102\u0103\5\36\20\2\u0103\33\3\2\2\2\u0104\u0105")
        buf.write("\7\f\2\2\u0105\u0106\7*\2\2\u0106\u0107\5\b\5\2\u0107")
        buf.write("\u0108\7+\2\2\u0108\u0111\5\36\20\2\u0109\u010a\7\16\2")
        buf.write("\2\u010a\u010b\7*\2\2\u010b\u010c\5\b\5\2\u010c\u010d")
        buf.write("\7+\2\2\u010d\u010e\5\36\20\2\u010e\u0110\3\2\2\2\u010f")
        buf.write("\u0109\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2")
        buf.write("\u0111\u0112\3\2\2\2\u0112\u0116\3\2\2\2\u0113\u0111\3")
        buf.write("\2\2\2\u0114\u0115\7\r\2\2\u0115\u0117\5\36\20\2\u0116")
        buf.write("\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\35\3\2\2\2\u0118")
        buf.write("\u0119\7,\2\2\u0119\u011a\5 \21\2\u011a\u011b\7-\2\2\u011b")
        buf.write("\37\3\2\2\2\u011c\u0121\3\2\2\2\u011d\u011e\5\30\r\2\u011e")
        buf.write("\u011f\5 \21\2\u011f\u0121\3\2\2\2\u0120\u011c\3\2\2\2")
        buf.write("\u0120\u011d\3\2\2\2\u0121!\3\2\2\2\u0122\u0123\7\13\2")
        buf.write("\2\u0123#\3\2\2\2\u0124\u0125\7\n\2\2\u0125%\3\2\2\2\u0126")
        buf.write("\u012b\7%\2\2\u0127\u012b\5@!\2\u0128\u012b\5H%\2\u0129")
        buf.write("\u012b\5F$\2\u012a\u0126\3\2\2\2\u012a\u0127\3\2\2\2\u012a")
        buf.write("\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012b\u012c\3\2\2\2")
        buf.write("\u012c\u012d\7\t\2\2\u012d\u012e\5\b\5\2\u012e\'\3\2\2")
        buf.write("\2\u012f\u0132\7\b\2\2\u0130\u0133\5\b\5\2\u0131\u0133")
        buf.write("\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0133")
        buf.write(")\3\2\2\2\u0134\u0137\5:\36\2\u0135\u0137\5<\37\2\u0136")
        buf.write("\u0134\3\2\2\2\u0136\u0135\3\2\2\2\u0137+\3\2\2\2\u0138")
        buf.write("\u0139\7\27\2\2\u0139\u013a\5f\64\2\u013a\u013b\7/\2\2")
        buf.write("\u013b\u013c\5\u0082B\2\u013c\u0143\3\2\2\2\u013d\u013e")
        buf.write("\7\27\2\2\u013e\u013f\7%\2\2\u013f\u0140\5.\30\2\u0140")
        buf.write("\u0141\5\b\5\2\u0141\u0143\3\2\2\2\u0142\u0138\3\2\2\2")
        buf.write("\u0142\u013d\3\2\2\2\u0143-\3\2\2\2\u0144\u0145\7/\2\2")
        buf.write("\u0145\u0146\5\u0082B\2\u0146\u0147\7\t\2\2\u0147\u014f")
        buf.write("\3\2\2\2\u0148\u0149\7\'\2\2\u0149\u014a\7%\2\2\u014a")
        buf.write("\u014b\5.\30\2\u014b\u014c\5\b\5\2\u014c\u014d\7\'\2\2")
        buf.write("\u014d\u014f\3\2\2\2\u014e\u0144\3\2\2\2\u014e\u0148\3")
        buf.write("\2\2\2\u014f/\3\2\2\2\u0150\u0155\3\2\2\2\u0151\u0152")
        buf.write("\5\b\5\2\u0152\u0153\5\62\32\2\u0153\u0155\3\2\2\2\u0154")
        buf.write("\u0150\3\2\2\2\u0154\u0151\3\2\2\2\u0155\61\3\2\2\2\u0156")
        buf.write("\u015c\3\2\2\2\u0157\u0158\7\'\2\2\u0158\u0159\5\b\5\2")
        buf.write("\u0159\u015a\5\62\32\2\u015a\u015c\3\2\2\2\u015b\u0156")
        buf.write("\3\2\2\2\u015b\u0157\3\2\2\2\u015c\63\3\2\2\2\u015d\u015e")
        buf.write("\5\66\34\2\u015e\65\3\2\2\2\u015f\u0160\b\34\1\2\u0160")
        buf.write("\u016e\7%\2\2\u0161\u016e\7\4\2\2\u0162\u016e\58\35\2")
        buf.write("\u0163\u016e\5~@\2\u0164\u016e\5R*\2\u0165\u016e\5T+\2")
        buf.write("\u0166\u0167\5\u0088E\2\u0167\u0168\5\66\34\5\u0168\u016e")
        buf.write("\3\2\2\2\u0169\u016a\7*\2\2\u016a\u016b\5\66\34\2\u016b")
        buf.write("\u016c\7+\2\2\u016c\u016e\3\2\2\2\u016d\u015f\3\2\2\2")
        buf.write("\u016d\u0161\3\2\2\2\u016d\u0162\3\2\2\2\u016d\u0163\3")
        buf.write("\2\2\2\u016d\u0164\3\2\2\2\u016d\u0165\3\2\2\2\u016d\u0166")
        buf.write("\3\2\2\2\u016d\u0169\3\2\2\2\u016e\u0191\3\2\2\2\u016f")
        buf.write("\u0170\f\7\2\2\u0170\u0171\7&\2\2\u0171\u0190\5\66\34")
        buf.write("\b\u0172\u0173\f\4\2\2\u0173\u0174\5\u008aF\2\u0174\u0175")
        buf.write("\5\66\34\5\u0175\u0190\3\2\2\2\u0176\u0177\f\n\2\2\u0177")
        buf.write("\u017a\7(\2\2\u0178\u017b\5\66\34\2\u0179\u017b\5\u0080")
        buf.write("A\2\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017c\u017d\7)\2\2\u017d\u0190\3\2\2\2\u017e")
        buf.write("\u017f\f\t\2\2\u017f\u0180\7&\2\2\u0180\u0181\7%\2\2\u0181")
        buf.write("\u0182\7*\2\2\u0182\u0183\5> \2\u0183\u0184\7+\2\2\u0184")
        buf.write("\u0190\3\2\2\2\u0185\u0186\f\b\2\2\u0186\u0187\7\5\2\2")
        buf.write("\u0187\u0188\7$\2\2\u0188\u0189\7*\2\2\u0189\u018a\5>")
        buf.write(" \2\u018a\u018b\7+\2\2\u018b\u0190\3\2\2\2\u018c\u018d")
        buf.write("\f\6\2\2\u018d\u018e\7\5\2\2\u018e\u0190\7$\2\2\u018f")
        buf.write("\u016f\3\2\2\2\u018f\u0172\3\2\2\2\u018f\u0176\3\2\2\2")
        buf.write("\u018f\u017e\3\2\2\2\u018f\u0185\3\2\2\2\u018f\u018c\3")
        buf.write("\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192")
        buf.write("\3\2\2\2\u0192\67\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195")
        buf.write("\7\7\2\2\u0195\u0196\7%\2\2\u0196\u0197\7*\2\2\u0197\u0198")
        buf.write("\5\60\31\2\u0198\u0199\7+\2\2\u01999\3\2\2\2\u019a\u019b")
        buf.write("\5\66\34\2\u019b\u019c\7&\2\2\u019c\u019d\7%\2\2\u019d")
        buf.write("\u019e\7*\2\2\u019e\u019f\5> \2\u019f\u01a0\7+\2\2\u01a0")
        buf.write(";\3\2\2\2\u01a1\u01a2\5\66\34\2\u01a2\u01a3\7\5\2\2\u01a3")
        buf.write("\u01a4\7$\2\2\u01a4\u01a5\7*\2\2\u01a5\u01a6\5> \2\u01a6")
        buf.write("\u01a7\7+\2\2\u01a7=\3\2\2\2\u01a8\u01a9\5\60\31\2\u01a9")
        buf.write("?\3\2\2\2\u01aa\u01ad\5B\"\2\u01ab\u01ad\5D#\2\u01ac\u01aa")
        buf.write("\3\2\2\2\u01ac\u01ab\3\2\2\2\u01adA\3\2\2\2\u01ae\u01b5")
        buf.write("\5\66\34\2\u01af\u01b0\7&\2\2\u01b0\u01b4\5\66\34\2\u01b1")
        buf.write("\u01b2\7\5\2\2\u01b2\u01b4\7$\2\2\u01b3\u01af\3\2\2\2")
        buf.write("\u01b3\u01b1\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3")
        buf.write("\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b5")
        buf.write("\3\2\2\2\u01b8\u01b9\7&\2\2\u01b9\u01ba\7%\2\2\u01baC")
        buf.write("\3\2\2\2\u01bb\u01c2\5\66\34\2\u01bc\u01bd\7&\2\2\u01bd")
        buf.write("\u01c1\5\66\34\2\u01be\u01bf\7\5\2\2\u01bf\u01c1\7$\2")
        buf.write("\2\u01c0\u01bc\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c4")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3")
        buf.write("\u01c5\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6\7\5\2\2")
        buf.write("\u01c6\u01c7\7$\2\2\u01c7E\3\2\2\2\u01c8\u01cd\7%\2\2")
        buf.write("\u01c9\u01ca\7(\2\2\u01ca\u01cb\5\b\5\2\u01cb\u01cc\7")
        buf.write(")\2\2\u01cc\u01ce\3\2\2\2\u01cd\u01c9\3\2\2\2\u01ce\u01cf")
        buf.write("\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0")
        buf.write("G\3\2\2\2\u01d1\u01d6\5\64\33\2\u01d2\u01d3\7(\2\2\u01d3")
        buf.write("\u01d4\5\64\33\2\u01d4\u01d5\7)\2\2\u01d5\u01d7\3\2\2")
        buf.write("\2\u01d6\u01d2\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d6")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9I\3\2\2\2\u01da\u01de")
        buf.write("\5\u0080A\2\u01db\u01de\7%\2\2\u01dc\u01de\5@!\2\u01dd")
        buf.write("\u01da\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01dc\3\2\2\2")
        buf.write("\u01deK\3\2\2\2\u01df\u01e3\7\24\2\2\u01e0\u01e3\7%\2")
        buf.write("\2\u01e1\u01e3\5@!\2\u01e2\u01df\3\2\2\2\u01e2\u01e0\3")
        buf.write("\2\2\2\u01e2\u01e1\3\2\2\2\u01e3M\3\2\2\2\u01e4\u01e9")
        buf.write("\3\2\2\2\u01e5\u01e6\5R*\2\u01e6\u01e7\5P)\2\u01e7\u01e9")
        buf.write("\3\2\2\2\u01e8\u01e4\3\2\2\2\u01e8\u01e5\3\2\2\2\u01e9")
        buf.write("O\3\2\2\2\u01ea\u01f0\3\2\2\2\u01eb\u01ec\7\'\2\2\u01ec")
        buf.write("\u01ed\5R*\2\u01ed\u01ee\5P)\2\u01ee\u01f0\3\2\2\2\u01ef")
        buf.write("\u01ea\3\2\2\2\u01ef\u01eb\3\2\2\2\u01f0Q\3\2\2\2\u01f1")
        buf.write("\u01f2\7\30\2\2\u01f2\u01f3\7*\2\2\u01f3\u01f4\5V,\2\u01f4")
        buf.write("\u01f5\7+\2\2\u01f5S\3\2\2\2\u01f6\u01f7\7\30\2\2\u01f7")
        buf.write("\u01f8\7*\2\2\u01f8\u01f9\5N(\2\u01f9\u01fa\7+\2\2\u01fa")
        buf.write("U\3\2\2\2\u01fb\u0200\5n8\2\u01fc\u0200\5r:\2\u01fd\u0200")
        buf.write("\5v<\2\u01fe\u0200\5z>\2\u01ff\u01fb\3\2\2\2\u01ff\u01fc")
        buf.write("\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200")
        buf.write("W\3\2\2\2\u0201\u0202\t\4\2\2\u0202Y\3\2\2\2\u0203\u0204")
        buf.write("\t\5\2\2\u0204[\3\2\2\2\u0205\u0206\t\6\2\2\u0206]\3\2")
        buf.write("\2\2\u0207\u0208\t\7\2\2\u0208_\3\2\2\2\u0209\u020a\t")
        buf.write("\b\2\2\u020aa\3\2\2\2\u020b\u0210\3\2\2\2\u020c\u020d")
        buf.write("\5~@\2\u020d\u020e\5d\63\2\u020e\u0210\3\2\2\2\u020f\u020b")
        buf.write("\3\2\2\2\u020f\u020c\3\2\2\2\u0210c\3\2\2\2\u0211\u0217")
        buf.write("\3\2\2\2\u0212\u0213\7\'\2\2\u0213\u0214\5~@\2\u0214\u0215")
        buf.write("\5d\63\2\u0215\u0217\3\2\2\2\u0216\u0211\3\2\2\2\u0216")
        buf.write("\u0212\3\2\2\2\u0217e\3\2\2\2\u0218\u021c\3\2\2\2\u0219")
        buf.write("\u021a\7%\2\2\u021a\u021c\5h\65\2\u021b\u0218\3\2\2\2")
        buf.write("\u021b\u0219\3\2\2\2\u021cg\3\2\2\2\u021d\u0222\3\2\2")
        buf.write("\2\u021e\u021f\7\'\2\2\u021f\u0220\7%\2\2\u0220\u0222")
        buf.write("\5h\65\2\u0221\u021d\3\2\2\2\u0221\u021e\3\2\2\2\u0222")
        buf.write("i\3\2\2\2\u0223\u0227\3\2\2\2\u0224\u0225\t\2\2\2\u0225")
        buf.write("\u0227\5l\67\2\u0226\u0223\3\2\2\2\u0226\u0224\3\2\2\2")
        buf.write("\u0227k\3\2\2\2\u0228\u022d\3\2\2\2\u0229\u022a\7\'\2")
        buf.write("\2\u022a\u022b\t\2\2\2\u022b\u022d\5l\67\2\u022c\u0228")
        buf.write("\3\2\2\2\u022c\u0229\3\2\2\2\u022dm\3\2\2\2\u022e\u0233")
        buf.write("\3\2\2\2\u022f\u0230\5\u0080A\2\u0230\u0231\5p9\2\u0231")
        buf.write("\u0233\3\2\2\2\u0232\u022e\3\2\2\2\u0232\u022f\3\2\2\2")
        buf.write("\u0233o\3\2\2\2\u0234\u023a\3\2\2\2\u0235\u0236\7\'\2")
        buf.write("\2\u0236\u0237\5\u0080A\2\u0237\u0238\5p9\2\u0238\u023a")
        buf.write("\3\2\2\2\u0239\u0234\3\2\2\2\u0239\u0235\3\2\2\2\u023a")
        buf.write("q\3\2\2\2\u023b\u023f\3\2\2\2\u023c\u023d\7\26\2\2\u023d")
        buf.write("\u023f\5t;\2\u023e\u023b\3\2\2\2\u023e\u023c\3\2\2\2\u023f")
        buf.write("s\3\2\2\2\u0240\u0245\3\2\2\2\u0241\u0242\7\'\2\2\u0242")
        buf.write("\u0243\7\26\2\2\u0243\u0245\5t;\2\u0244\u0240\3\2\2\2")
        buf.write("\u0244\u0241\3\2\2\2\u0245u\3\2\2\2\u0246\u024a\3\2\2")
        buf.write("\2\u0247\u0248\7\24\2\2\u0248\u024a\5x=\2\u0249\u0246")
        buf.write("\3\2\2\2\u0249\u0247\3\2\2\2\u024aw\3\2\2\2\u024b\u0250")
        buf.write("\3\2\2\2\u024c\u024d\7\'\2\2\u024d\u024e\7\24\2\2\u024e")
        buf.write("\u0250\5x=\2\u024f\u024b\3\2\2\2\u024f\u024c\3\2\2\2\u0250")
        buf.write("y\3\2\2\2\u0251\u0255\3\2\2\2\u0252\u0253\7\3\2\2\u0253")
        buf.write("\u0255\5|?\2\u0254\u0251\3\2\2\2\u0254\u0252\3\2\2\2\u0255")
        buf.write("{\3\2\2\2\u0256\u025b\3\2\2\2\u0257\u0258\7\'\2\2\u0258")
        buf.write("\u0259\7\3\2\2\u0259\u025b\5|?\2\u025a\u0256\3\2\2\2\u025a")
        buf.write("\u0257\3\2\2\2\u025b}\3\2\2\2\u025c\u0261\7\24\2\2\u025d")
        buf.write("\u0261\7\26\2\2\u025e\u0261\7\3\2\2\u025f\u0261\5\u0080")
        buf.write("A\2\u0260\u025c\3\2\2\2\u0260\u025d\3\2\2\2\u0260\u025e")
        buf.write("\3\2\2\2\u0260\u025f\3\2\2\2\u0261\177\3\2\2\2\u0262\u0263")
        buf.write("\t\t\2\2\u0263\u0081\3\2\2\2\u0264\u026b\7\31\2\2\u0265")
        buf.write("\u026b\7\32\2\2\u0266\u026b\7\33\2\2\u0267\u026b\7\6\2")
        buf.write("\2\u0268\u026b\5\u0086D\2\u0269\u026b\7%\2\2\u026a\u0264")
        buf.write("\3\2\2\2\u026a\u0265\3\2\2\2\u026a\u0266\3\2\2\2\u026a")
        buf.write("\u0267\3\2\2\2\u026a\u0268\3\2\2\2\u026a\u0269\3\2\2\2")
        buf.write("\u026b\u0083\3\2\2\2\u026c\u026d\t\n\2\2\u026d\u0085\3")
        buf.write("\2\2\2\u026e\u026f\7\30\2\2\u026f\u0270\7(\2\2\u0270\u0271")
        buf.write("\5\u0082B\2\u0271\u0272\7\'\2\2\u0272\u0273\5\u0084C\2")
        buf.write("\u0273\u0274\7)\2\2\u0274\u0087\3\2\2\2\u0275\u0276\t")
        buf.write("\13\2\2\u0276\u0089\3\2\2\2\u0277\u0278\t\f\2\2\u0278")
        buf.write("\u008b\3\2\2\2\u0279\u027a\t\r\2\2\u027a\u008d\3\2\2\2")
        buf.write(":\u0091\u0099\u00a0\u00a2\u00aa\u00b8\u00c4\u00cf\u00d1")
        buf.write("\u00da\u00e1\u00ed\u00f4\u00ff\u0111\u0116\u0120\u012a")
        buf.write("\u0132\u0136\u0142\u014e\u0154\u015b\u016d\u017a\u018f")
        buf.write("\u0191\u01ac\u01b3\u01b5\u01c0\u01c2\u01cf\u01d8\u01dd")
        buf.write("\u01e2\u01e8\u01ef\u01ff\u020f\u0216\u021b\u0221\u0226")
        buf.write("\u022c\u0232\u0239\u023e\u0244\u0249\u024f\u0254\u025a")
        buf.write("\u0260\u026a")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Null'", "'::'", "'String'", 
                     "'New'", "'Return'", "'='", "'Break'", "'Continue'", 
                     "'If'", "'Else'", "'Elseif'", "'Foreach'", "'In'", 
                     "'Constructor'", "'Destructor'", "'Class'", "<INVALID>", 
                     "'By'", "<INVALID>", "<INVALID>", "'Array'", "'Int'", 
                     "'Float'", "'Boolean'", "<INVALID>", "'00'", "'0'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'.'", "','", 
                     "'['", "']'", "'('", "')'", "'{'", "'}'", "'..'", "':'", 
                     "';'", "'+'", "'<='", "'>='", "'-'", "'*'", "'<'", 
                     "'%'", "'/'", "'!='", "'=='", "'>'", "'&&'", "'||'", 
                     "'!'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>", "STRINGLIT", "NULL", "MEM_ACCESS_OP", 
                      "STRING_TYPE", "NEW", "RETURN", "ASSIGN_OP", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "ELSEIF", "FOREACH", "IN", 
                      "CONSTRUCTOR", "DESTRUCTOR", "CLASS", "FLOATLIT", 
                      "BY", "BOOLIT", "VAL_VAR", "ARRAY", "INT_TYPE", "FLOAT_TYPE", 
                      "BOOL_TYPE", "ZERO_2", "ZERO_8", "ZERO_10", "ZERO_16", 
                      "INTLIT_16", "INTLIT_2", "INTLIT_8", "INTLIT_10", 
                      "DOLLAR_ID", "ID", "DOT", "CM", "LS", "RS", "LB", 
                      "RB", "LP", "RP", "RANGE", "CL", "SEMI", "ADDOP", 
                      "LESS_EQUAL", "GREAT_EQUAL", "SUBOP", "MULOP", "LESS_THAN", 
                      "MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", "GREAT_THAN", 
                      "AND", "OR", "NEGATE", "STR_CMP", "STR_CONCAT", "COMMENT", 
                      "WS", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_dcl = 1
    RULE_class_body = 2
    RULE_expr_pro = 3
    RULE_att_dcl = 4
    RULE_att_dcl_list = 5
    RULE_method_dcl = 6
    RULE_method_block = 7
    RULE_para_dcl_list = 8
    RULE_para_dcl_smcllist = 9
    RULE_para_dcl = 10
    RULE_stm = 11
    RULE_for_in_stm = 12
    RULE_if_stm = 13
    RULE_block_stm = 14
    RULE_mn_stm = 15
    RULE_continue_stm = 16
    RULE_break_stm = 17
    RULE_asm_stm = 18
    RULE_return_stm = 19
    RULE_method_invoke_stm = 20
    RULE_var_dcl = 21
    RULE_var_dcl_list = 22
    RULE_expr_pro_list = 23
    RULE_expr_pro_cmlist = 24
    RULE_expr = 25
    RULE_expr_lit = 26
    RULE_object_ini = 27
    RULE_instance_method_invoke = 28
    RULE_static_mehod_invoke = 29
    RULE_para_pass_list = 30
    RULE_att_access = 31
    RULE_instance_att_access = 32
    RULE_static_att_access = 33
    RULE_index_ele_pro = 34
    RULE_index_ele = 35
    RULE_int_object = 36
    RULE_float_object = 37
    RULE_index_arr_list = 38
    RULE_index_arr_cmlist = 39
    RULE_index_arr = 40
    RULE_mul_dim_arr = 41
    RULE_same_type_list = 42
    RULE_string_op = 43
    RULE_bool_op = 44
    RULE_relation_op = 45
    RULE_int_op = 46
    RULE_float_op = 47
    RULE_lit_list = 48
    RULE_lit_cmlist = 49
    RULE_non_static_id_list = 50
    RULE_non_static_id_cmlist = 51
    RULE_id_list = 52
    RULE_id_cmlist = 53
    RULE_int_gen_list = 54
    RULE_int_gen_cm = 55
    RULE_bool_list = 56
    RULE_bool_list_cm = 57
    RULE_float_list = 58
    RULE_float_list_cm = 59
    RULE_string_list = 60
    RULE_string_list_cm = 61
    RULE_lit = 62
    RULE_int_gen = 63
    RULE_data_type = 64
    RULE_size = 65
    RULE_array_type = 66
    RULE_unary_op = 67
    RULE_binary_op = 68
    RULE_zero = 69

    ruleNames =  [ "program", "class_dcl", "class_body", "expr_pro", "att_dcl", 
                   "att_dcl_list", "method_dcl", "method_block", "para_dcl_list", 
                   "para_dcl_smcllist", "para_dcl", "stm", "for_in_stm", 
                   "if_stm", "block_stm", "mn_stm", "continue_stm", "break_stm", 
                   "asm_stm", "return_stm", "method_invoke_stm", "var_dcl", 
                   "var_dcl_list", "expr_pro_list", "expr_pro_cmlist", "expr", 
                   "expr_lit", "object_ini", "instance_method_invoke", "static_mehod_invoke", 
                   "para_pass_list", "att_access", "instance_att_access", 
                   "static_att_access", "index_ele_pro", "index_ele", "int_object", 
                   "float_object", "index_arr_list", "index_arr_cmlist", 
                   "index_arr", "mul_dim_arr", "same_type_list", "string_op", 
                   "bool_op", "relation_op", "int_op", "float_op", "lit_list", 
                   "lit_cmlist", "non_static_id_list", "non_static_id_cmlist", 
                   "id_list", "id_cmlist", "int_gen_list", "int_gen_cm", 
                   "bool_list", "bool_list_cm", "float_list", "float_list_cm", 
                   "string_list", "string_list_cm", "lit", "int_gen", "data_type", 
                   "size", "array_type", "unary_op", "binary_op", "zero" ]

    EOF = Token.EOF
    STRINGLIT=1
    NULL=2
    MEM_ACCESS_OP=3
    STRING_TYPE=4
    NEW=5
    RETURN=6
    ASSIGN_OP=7
    BREAK=8
    CONTINUE=9
    IF=10
    ELSE=11
    ELSEIF=12
    FOREACH=13
    IN=14
    CONSTRUCTOR=15
    DESTRUCTOR=16
    CLASS=17
    FLOATLIT=18
    BY=19
    BOOLIT=20
    VAL_VAR=21
    ARRAY=22
    INT_TYPE=23
    FLOAT_TYPE=24
    BOOL_TYPE=25
    ZERO_2=26
    ZERO_8=27
    ZERO_10=28
    ZERO_16=29
    INTLIT_16=30
    INTLIT_2=31
    INTLIT_8=32
    INTLIT_10=33
    DOLLAR_ID=34
    ID=35
    DOT=36
    CM=37
    LS=38
    RS=39
    LB=40
    RB=41
    LP=42
    RP=43
    RANGE=44
    CL=45
    SEMI=46
    ADDOP=47
    LESS_EQUAL=48
    GREAT_EQUAL=49
    SUBOP=50
    MULOP=51
    LESS_THAN=52
    MODOP=53
    DIVOP=54
    NOT_EQUAL=55
    EQUAL=56
    GREAT_THAN=57
    AND=58
    OR=59
    NEGATE=60
    STR_CMP=61
    STR_CONCAT=62
    COMMENT=63
    WS=64
    ILLEGAL_ESCAPE=65
    UNCLOSED_STRING=66
    ERROR_CHAR=67

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

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_dclContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_dclContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 140
                self.class_dcl()
                self.state = 143 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 145
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
            self.state = 147
            self.match(D96Parser.CLASS)
            self.state = 148
            self.match(D96Parser.ID)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.CL:
                self.state = 149
                self.match(D96Parser.CL)
                self.state = 150
                self.id_list()


            self.state = 153
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
            self.state = 155
            self.match(D96Parser.LP)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.VAL_VAR) | (1 << D96Parser.DOLLAR_ID) | (1 << D96Parser.ID))) != 0):
                self.state = 158
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL_VAR]:
                    self.state = 156
                    self.att_dcl()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.DOLLAR_ID, D96Parser.ID]:
                    self.state = 157
                    self.method_dcl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 163
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_proContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def index_ele(self):
            return self.getTypedRuleContext(D96Parser.Index_eleContext,0)


        def index_ele_pro(self):
            return self.getTypedRuleContext(D96Parser.Index_ele_proContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_pro

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_pro" ):
                return visitor.visitExpr_pro(self)
            else:
                return visitor.visitChildren(self)




    def expr_pro(self):

        localctx = D96Parser.Expr_proContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr_pro)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.index_ele()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.index_ele_pro()
                pass


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

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def att_dcl_list(self):
            return self.getTypedRuleContext(D96Parser.Att_dcl_listContext,0)


        def expr_pro(self):
            return self.getTypedRuleContext(D96Parser.Expr_proContext,0)


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
        self.enterRule(localctx, 8, self.RULE_att_dcl)
        self._la = 0 # Token type
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(D96Parser.VAL_VAR)
                self.state = 171
                self.id_list()
                self.state = 172
                self.match(D96Parser.CL)
                self.state = 173
                self.data_type()
                self.state = 174
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(D96Parser.VAL_VAR)
                self.state = 177
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 178
                self.att_dcl_list()
                self.state = 179
                self.expr_pro()
                self.state = 180
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


        def expr_pro(self):
            return self.getTypedRuleContext(D96Parser.Expr_proContext,0)


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
        self.enterRule(localctx, 10, self.RULE_att_dcl_list)
        self._la = 0 # Token type
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(D96Parser.CL)
                self.state = 185
                self.data_type()
                self.state = 186
                self.match(D96Parser.ASSIGN_OP)
                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(D96Parser.CM)
                self.state = 189
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 190
                self.att_dcl_list()
                self.state = 191
                self.expr_pro()
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

        def para_dcl_list(self):
            return self.getTypedRuleContext(D96Parser.Para_dcl_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def method_block(self):
            return self.getTypedRuleContext(D96Parser.Method_blockContext,0)


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
        self.enterRule(localctx, 12, self.RULE_method_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.DOLLAR_ID) | (1 << D96Parser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 197
            self.match(D96Parser.LB)
            self.state = 198
            self.para_dcl_list()
            self.state = 199
            self.match(D96Parser.RB)
            self.state = 200
            self.method_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmContext,i)


        def block_stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_stmContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_stmContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_method_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_block" ):
                return visitor.visitMethod_block(self)
            else:
                return visitor.visitChildren(self)




    def method_block(self):

        localctx = D96Parser.Method_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(D96Parser.LP)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.STRINGLIT) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.RETURN) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLIT) | (1 << D96Parser.VAL_VAR) | (1 << D96Parser.ARRAY) | (1 << D96Parser.ZERO_10) | (1 << D96Parser.INTLIT_16) | (1 << D96Parser.INTLIT_2) | (1 << D96Parser.INTLIT_8) | (1 << D96Parser.INTLIT_10) | (1 << D96Parser.ID) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NEGATE))) != 0):
                self.state = 205
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 203
                    self.stm()
                    pass

                elif la_ == 2:
                    self.state = 204
                    self.block_stm()
                    pass


                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 210
            self.match(D96Parser.RP)
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
        self.enterRule(localctx, 16, self.RULE_para_dcl_list)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.DOLLAR_ID, D96Parser.ID, D96Parser.CL]:
                self.enterOuterAlt(localctx, 2)
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
        self.enterRule(localctx, 18, self.RULE_para_dcl_smcllist)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(D96Parser.SEMI)
                self.state = 220
                self.para_dcl()
                self.state = 221
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
        self.enterRule(localctx, 20, self.RULE_para_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.id_list()
            self.state = 226
            self.match(D96Parser.CL)
            self.state = 227
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


        def block_stm(self):
            return self.getTypedRuleContext(D96Parser.Block_stmContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = D96Parser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stm)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.STRINGLIT, D96Parser.NULL, D96Parser.NEW, D96Parser.RETURN, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.FLOATLIT, D96Parser.BOOLIT, D96Parser.VAL_VAR, D96Parser.ARRAY, D96Parser.ZERO_10, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10, D96Parser.ID, D96Parser.LB, D96Parser.SUBOP, D96Parser.NEGATE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 229
                    self.asm_stm()
                    pass

                elif la_ == 2:
                    self.state = 230
                    self.var_dcl()
                    pass

                elif la_ == 3:
                    self.state = 231
                    self.break_stm()
                    pass

                elif la_ == 4:
                    self.state = 232
                    self.continue_stm()
                    pass

                elif la_ == 5:
                    self.state = 233
                    self.return_stm()
                    pass

                elif la_ == 6:
                    self.state = 234
                    self.method_invoke_stm()
                    pass


                self.state = 237
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.if_stm()
                pass
            elif token in [D96Parser.FOREACH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.for_in_stm()
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 4)
                self.state = 241
                self.block_stm()
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

        def expr_pro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_proContext)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_proContext,i)


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
        self.enterRule(localctx, 24, self.RULE_for_in_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(D96Parser.FOREACH)
            self.state = 245
            self.match(D96Parser.LB)
            self.state = 246
            self.match(D96Parser.ID)
            self.state = 247
            self.match(D96Parser.IN)
            self.state = 248
            self.expr_pro()
            self.state = 249
            self.match(D96Parser.RANGE)
            self.state = 250
            self.expr_pro()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 251
                self.match(D96Parser.BY)
                self.state = 252
                self.expr_pro()


            self.state = 255
            self.match(D96Parser.RB)
            self.state = 256
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

        def expr_pro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_proContext)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_proContext,i)


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
        self.enterRule(localctx, 26, self.RULE_if_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(D96Parser.IF)
            self.state = 259
            self.match(D96Parser.LB)
            self.state = 260
            self.expr_pro()
            self.state = 261
            self.match(D96Parser.RB)
            self.state = 262
            self.block_stm()
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 263
                self.match(D96Parser.ELSEIF)
                self.state = 264
                self.match(D96Parser.LB)
                self.state = 265
                self.expr_pro()
                self.state = 266
                self.match(D96Parser.RB)
                self.state = 267
                self.block_stm()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 274
                self.match(D96Parser.ELSE)
                self.state = 275
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
        self.enterRule(localctx, 28, self.RULE_block_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(D96Parser.LP)
            self.state = 279
            self.mn_stm()
            self.state = 280
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
        self.enterRule(localctx, 30, self.RULE_mn_stm)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT, D96Parser.NULL, D96Parser.NEW, D96Parser.RETURN, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.FLOATLIT, D96Parser.BOOLIT, D96Parser.VAL_VAR, D96Parser.ARRAY, D96Parser.ZERO_10, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10, D96Parser.ID, D96Parser.LB, D96Parser.LP, D96Parser.SUBOP, D96Parser.NEGATE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.stm()
                self.state = 284
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
        self.enterRule(localctx, 32, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
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
        self.enterRule(localctx, 34, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
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

        def expr_pro(self):
            return self.getTypedRuleContext(D96Parser.Expr_proContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def att_access(self):
            return self.getTypedRuleContext(D96Parser.Att_accessContext,0)


        def index_ele(self):
            return self.getTypedRuleContext(D96Parser.Index_eleContext,0)


        def index_ele_pro(self):
            return self.getTypedRuleContext(D96Parser.Index_ele_proContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_asm_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm_stm" ):
                return visitor.visitAsm_stm(self)
            else:
                return visitor.visitChildren(self)




    def asm_stm(self):

        localctx = D96Parser.Asm_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_asm_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 292
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 293
                self.att_access()
                pass

            elif la_ == 3:
                self.state = 294
                self.index_ele()
                pass

            elif la_ == 4:
                self.state = 295
                self.index_ele_pro()
                pass


            self.state = 298
            self.match(D96Parser.ASSIGN_OP)
            self.state = 299
            self.expr_pro()
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

        def expr_pro(self):
            return self.getTypedRuleContext(D96Parser.Expr_proContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = D96Parser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_return_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(D96Parser.RETURN)
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.STRINGLIT, D96Parser.NULL, D96Parser.NEW, D96Parser.FLOATLIT, D96Parser.BOOLIT, D96Parser.ARRAY, D96Parser.ZERO_10, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10, D96Parser.ID, D96Parser.LB, D96Parser.SUBOP, D96Parser.NEGATE]:
                self.state = 302
                self.expr_pro()
                pass
            elif token in [D96Parser.SEMI]:
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
        self.enterRule(localctx, 40, self.RULE_method_invoke_stm)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.instance_method_invoke()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
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

        def non_static_id_list(self):
            return self.getTypedRuleContext(D96Parser.Non_static_id_listContext,0)


        def CL(self):
            return self.getToken(D96Parser.CL, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def var_dcl_list(self):
            return self.getTypedRuleContext(D96Parser.Var_dcl_listContext,0)


        def expr_pro(self):
            return self.getTypedRuleContext(D96Parser.Expr_proContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_dcl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dcl" ):
                return visitor.visitVar_dcl(self)
            else:
                return visitor.visitChildren(self)




    def var_dcl(self):

        localctx = D96Parser.Var_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_var_dcl)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(D96Parser.VAL_VAR)
                self.state = 311
                self.non_static_id_list()
                self.state = 312
                self.match(D96Parser.CL)
                self.state = 313
                self.data_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(D96Parser.VAL_VAR)
                self.state = 316
                self.match(D96Parser.ID)
                self.state = 317
                self.var_dcl_list()
                self.state = 318
                self.expr_pro()
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


        def expr_pro(self):
            return self.getTypedRuleContext(D96Parser.Expr_proContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_dcl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dcl_list" ):
                return visitor.visitVar_dcl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_dcl_list(self):

        localctx = D96Parser.Var_dcl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_var_dcl_list)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.match(D96Parser.CL)
                self.state = 323
                self.data_type()
                self.state = 324
                self.match(D96Parser.ASSIGN_OP)
                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.match(D96Parser.CM)
                self.state = 327
                self.match(D96Parser.ID)
                self.state = 328
                self.var_dcl_list()
                self.state = 329
                self.expr_pro()
                self.state = 330
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


    class Expr_pro_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_pro(self):
            return self.getTypedRuleContext(D96Parser.Expr_proContext,0)


        def expr_pro_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Expr_pro_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_pro_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_pro_list" ):
                return visitor.visitExpr_pro_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_pro_list(self):

        localctx = D96Parser.Expr_pro_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr_pro_list)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT, D96Parser.NULL, D96Parser.NEW, D96Parser.FLOATLIT, D96Parser.BOOLIT, D96Parser.ARRAY, D96Parser.ZERO_10, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10, D96Parser.ID, D96Parser.LB, D96Parser.SUBOP, D96Parser.NEGATE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.expr_pro()
                self.state = 336
                self.expr_pro_cmlist()
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


    class Expr_pro_cmlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def expr_pro(self):
            return self.getTypedRuleContext(D96Parser.Expr_proContext,0)


        def expr_pro_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Expr_pro_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_pro_cmlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_pro_cmlist" ):
                return visitor.visitExpr_pro_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def expr_pro_cmlist(self):

        localctx = D96Parser.Expr_pro_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr_pro_cmlist)
        try:
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(D96Parser.CM)
                self.state = 342
                self.expr_pro()
                self.state = 343
                self.expr_pro_cmlist()
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

        def expr_lit(self):
            return self.getTypedRuleContext(D96Parser.Expr_litContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.expr_lit(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def object_ini(self):
            return self.getTypedRuleContext(D96Parser.Object_iniContext,0)


        def lit(self):
            return self.getTypedRuleContext(D96Parser.LitContext,0)


        def index_arr(self):
            return self.getTypedRuleContext(D96Parser.Index_arrContext,0)


        def mul_dim_arr(self):
            return self.getTypedRuleContext(D96Parser.Mul_dim_arrContext,0)


        def unary_op(self):
            return self.getTypedRuleContext(D96Parser.Unary_opContext,0)


        def expr_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_litContext)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_litContext,i)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def binary_op(self):
            return self.getTypedRuleContext(D96Parser.Binary_opContext,0)


        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def int_gen(self):
            return self.getTypedRuleContext(D96Parser.Int_genContext,0)


        def para_pass_list(self):
            return self.getTypedRuleContext(D96Parser.Para_pass_listContext,0)


        def MEM_ACCESS_OP(self):
            return self.getToken(D96Parser.MEM_ACCESS_OP, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_lit" ):
                return visitor.visitExpr_lit(self)
            else:
                return visitor.visitChildren(self)



    def expr_lit(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_litContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr_lit, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 350
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 351
                self.match(D96Parser.NULL)
                pass

            elif la_ == 3:
                self.state = 352
                self.object_ini()
                pass

            elif la_ == 4:
                self.state = 353
                self.lit()
                pass

            elif la_ == 5:
                self.state = 354
                self.index_arr()
                pass

            elif la_ == 6:
                self.state = 355
                self.mul_dim_arr()
                pass

            elif la_ == 7:
                self.state = 356
                self.unary_op()
                self.state = 357
                self.expr_lit(3)
                pass

            elif la_ == 8:
                self.state = 359
                self.match(D96Parser.LB)
                self.state = 360
                self.expr_lit(0)
                self.state = 361
                self.match(D96Parser.RB)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 397
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 365
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 366
                        self.match(D96Parser.DOT)
                        self.state = 367
                        self.expr_lit(6)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 368
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 369
                        self.binary_op()
                        self.state = 370
                        self.expr_lit(3)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 372
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 373
                        self.match(D96Parser.LS)
                        self.state = 376
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                        if la_ == 1:
                            self.state = 374
                            self.expr_lit(0)
                            pass

                        elif la_ == 2:
                            self.state = 375
                            self.int_gen()
                            pass


                        self.state = 378
                        self.match(D96Parser.RS)
                        pass

                    elif la_ == 4:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 380
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 381
                        self.match(D96Parser.DOT)
                        self.state = 382
                        self.match(D96Parser.ID)
                        self.state = 383
                        self.match(D96Parser.LB)
                        self.state = 384
                        self.para_pass_list()
                        self.state = 385
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 5:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 387
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 388
                        self.match(D96Parser.MEM_ACCESS_OP)
                        self.state = 389
                        self.match(D96Parser.DOLLAR_ID)
                        self.state = 390
                        self.match(D96Parser.LB)
                        self.state = 391
                        self.para_pass_list()
                        self.state = 392
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 6:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 394
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 395
                        self.match(D96Parser.MEM_ACCESS_OP)
                        self.state = 396
                        self.match(D96Parser.DOLLAR_ID)
                        pass

             
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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

        def expr_pro_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_pro_listContext,0)


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
        self.enterRule(localctx, 54, self.RULE_object_ini)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(D96Parser.NEW)
            self.state = 403
            self.match(D96Parser.ID)
            self.state = 404
            self.match(D96Parser.LB)
            self.state = 405
            self.expr_pro_list()
            self.state = 406
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

        def expr_lit(self):
            return self.getTypedRuleContext(D96Parser.Expr_litContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

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
        self.enterRule(localctx, 56, self.RULE_instance_method_invoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.expr_lit(0)
            self.state = 409
            self.match(D96Parser.DOT)
            self.state = 410
            self.match(D96Parser.ID)
            self.state = 411
            self.match(D96Parser.LB)
            self.state = 412
            self.para_pass_list()
            self.state = 413
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

        def expr_lit(self):
            return self.getTypedRuleContext(D96Parser.Expr_litContext,0)


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
        self.enterRule(localctx, 58, self.RULE_static_mehod_invoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.expr_lit(0)
            self.state = 416
            self.match(D96Parser.MEM_ACCESS_OP)
            self.state = 417
            self.match(D96Parser.DOLLAR_ID)
            self.state = 418
            self.match(D96Parser.LB)
            self.state = 419
            self.para_pass_list()
            self.state = 420
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

        def expr_pro_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_pro_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_para_pass_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_pass_list" ):
                return visitor.visitPara_pass_list(self)
            else:
                return visitor.visitChildren(self)




    def para_pass_list(self):

        localctx = D96Parser.Para_pass_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_para_pass_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.expr_pro_list()
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
        self.enterRule(localctx, 62, self.RULE_att_access)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.instance_att_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
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

        def expr_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_litContext)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_litContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOT)
            else:
                return self.getToken(D96Parser.DOT, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def MEM_ACCESS_OP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.MEM_ACCESS_OP)
            else:
                return self.getToken(D96Parser.MEM_ACCESS_OP, i)

        def DOLLAR_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR_ID)
            else:
                return self.getToken(D96Parser.DOLLAR_ID, i)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_att_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_att_access" ):
                return visitor.visitInstance_att_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_att_access(self):

        localctx = D96Parser.Instance_att_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_instance_att_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.expr_lit(0)
            self.state = 435
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 433
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.DOT]:
                        self.state = 429
                        self.match(D96Parser.DOT)
                        self.state = 430
                        self.expr_lit(0)
                        pass
                    elif token in [D96Parser.MEM_ACCESS_OP]:
                        self.state = 431
                        self.match(D96Parser.MEM_ACCESS_OP)
                        self.state = 432
                        self.match(D96Parser.DOLLAR_ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 437
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 438
            self.match(D96Parser.DOT)
            self.state = 439
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

        def expr_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_litContext)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_litContext,i)


        def MEM_ACCESS_OP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.MEM_ACCESS_OP)
            else:
                return self.getToken(D96Parser.MEM_ACCESS_OP, i)

        def DOLLAR_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR_ID)
            else:
                return self.getToken(D96Parser.DOLLAR_ID, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOT)
            else:
                return self.getToken(D96Parser.DOT, i)

        def getRuleIndex(self):
            return D96Parser.RULE_static_att_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_att_access" ):
                return visitor.visitStatic_att_access(self)
            else:
                return visitor.visitChildren(self)




    def static_att_access(self):

        localctx = D96Parser.Static_att_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_static_att_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.expr_lit(0)
            self.state = 448
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 446
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.DOT]:
                        self.state = 442
                        self.match(D96Parser.DOT)
                        self.state = 443
                        self.expr_lit(0)
                        pass
                    elif token in [D96Parser.MEM_ACCESS_OP]:
                        self.state = 444
                        self.match(D96Parser.MEM_ACCESS_OP)
                        self.state = 445
                        self.match(D96Parser.DOLLAR_ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 450
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 451
            self.match(D96Parser.MEM_ACCESS_OP)
            self.state = 452
            self.match(D96Parser.DOLLAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_ele_proContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LS)
            else:
                return self.getToken(D96Parser.LS, i)

        def expr_pro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_proContext)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_proContext,i)


        def RS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RS)
            else:
                return self.getToken(D96Parser.RS, i)

        def getRuleIndex(self):
            return D96Parser.RULE_index_ele_pro

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_ele_pro" ):
                return visitor.visitIndex_ele_pro(self)
            else:
                return visitor.visitChildren(self)




    def index_ele_pro(self):

        localctx = D96Parser.Index_ele_proContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_index_ele_pro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(D96Parser.ID)
            self.state = 459 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 455
                self.match(D96Parser.LS)
                self.state = 456
                self.expr_pro()
                self.state = 457
                self.match(D96Parser.RS)
                self.state = 461 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.LS):
                    break

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def LS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LS)
            else:
                return self.getToken(D96Parser.LS, i)

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
        self.enterRule(localctx, 70, self.RULE_index_ele)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.expr()
            self.state = 468 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 464
                self.match(D96Parser.LS)
                self.state = 465
                self.expr()
                self.state = 466
                self.match(D96Parser.RS)
                self.state = 470 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.LS):
                    break

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
        self.enterRule(localctx, 72, self.RULE_int_object)
        try:
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.int_gen()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 474
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
        self.enterRule(localctx, 74, self.RULE_float_object)
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 479
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
        self.enterRule(localctx, 76, self.RULE_index_arr_list)
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.index_arr()
                self.state = 484
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
        self.enterRule(localctx, 78, self.RULE_index_arr_cmlist)
        try:
            self.state = 493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.match(D96Parser.CM)
                self.state = 490
                self.index_arr()
                self.state = 491
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
        self.enterRule(localctx, 80, self.RULE_index_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(D96Parser.ARRAY)
            self.state = 496
            self.match(D96Parser.LB)
            self.state = 497
            self.same_type_list()
            self.state = 498
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
        self.enterRule(localctx, 82, self.RULE_mul_dim_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(D96Parser.ARRAY)
            self.state = 501
            self.match(D96Parser.LB)
            self.state = 502
            self.index_arr_list()
            self.state = 503
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
        self.enterRule(localctx, 84, self.RULE_same_type_list)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.int_gen_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                self.bool_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 507
                self.float_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 508
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
        self.enterRule(localctx, 86, self.RULE_string_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
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
        self.enterRule(localctx, 88, self.RULE_bool_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
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
        self.enterRule(localctx, 90, self.RULE_relation_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
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
        self.enterRule(localctx, 92, self.RULE_int_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
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
        self.enterRule(localctx, 94, self.RULE_float_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
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
        self.enterRule(localctx, 96, self.RULE_lit_list)
        try:
            self.state = 525
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.BOOLIT, D96Parser.ZERO_10, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.lit()
                self.state = 523
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
        self.enterRule(localctx, 98, self.RULE_lit_cmlist)
        try:
            self.state = 532
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 528
                self.match(D96Parser.CM)
                self.state = 529
                self.lit()
                self.state = 530
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


    class Non_static_id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def non_static_id_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Non_static_id_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_non_static_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_static_id_list" ):
                return visitor.visitNon_static_id_list(self)
            else:
                return visitor.visitChildren(self)




    def non_static_id_list(self):

        localctx = D96Parser.Non_static_id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_non_static_id_list)
        try:
            self.state = 537
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 535
                self.match(D96Parser.ID)
                self.state = 536
                self.non_static_id_cmlist()
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


    class Non_static_id_cmlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def non_static_id_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Non_static_id_cmlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_non_static_id_cmlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_static_id_cmlist" ):
                return visitor.visitNon_static_id_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def non_static_id_cmlist(self):

        localctx = D96Parser.Non_static_id_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_non_static_id_cmlist)
        try:
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.match(D96Parser.CM)
                self.state = 541
                self.match(D96Parser.ID)
                self.state = 542
                self.non_static_id_cmlist()
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

        def id_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Id_cmlistContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.state = 548
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.DOLLAR_ID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 547
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

        def id_cmlist(self):
            return self.getTypedRuleContext(D96Parser.Id_cmlistContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_id_cmlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_cmlist" ):
                return visitor.visitId_cmlist(self)
            else:
                return visitor.visitChildren(self)




    def id_cmlist(self):

        localctx = D96Parser.Id_cmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_id_cmlist)
        self._la = 0 # Token type
        try:
            self.state = 554
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                self.match(D96Parser.CM)
                self.state = 552
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 553
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
        self.enterRule(localctx, 108, self.RULE_int_gen_list)
        try:
            self.state = 560
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ZERO_10, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
                self.int_gen()
                self.state = 558
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
        self.enterRule(localctx, 110, self.RULE_int_gen_cm)
        try:
            self.state = 567
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 563
                self.match(D96Parser.CM)
                self.state = 564
                self.int_gen()
                self.state = 565
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
        self.enterRule(localctx, 112, self.RULE_bool_list)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 570
                self.match(D96Parser.BOOLIT)
                self.state = 571
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
        self.enterRule(localctx, 114, self.RULE_bool_list_cm)
        try:
            self.state = 578
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 575
                self.match(D96Parser.CM)
                self.state = 576
                self.match(D96Parser.BOOLIT)
                self.state = 577
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
        self.enterRule(localctx, 116, self.RULE_float_list)
        try:
            self.state = 583
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 581
                self.match(D96Parser.FLOATLIT)
                self.state = 582
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
        self.enterRule(localctx, 118, self.RULE_float_list_cm)
        try:
            self.state = 589
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.match(D96Parser.CM)
                self.state = 587
                self.match(D96Parser.FLOATLIT)
                self.state = 588
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
        self.enterRule(localctx, 120, self.RULE_string_list)
        try:
            self.state = 594
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 592
                self.match(D96Parser.STRINGLIT)
                self.state = 593
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
        self.enterRule(localctx, 122, self.RULE_string_list_cm)
        try:
            self.state = 600
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 597
                self.match(D96Parser.CM)
                self.state = 598
                self.match(D96Parser.STRINGLIT)
                self.state = 599
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
        self.enterRule(localctx, 124, self.RULE_lit)
        try:
            self.state = 606
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 602
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 603
                self.match(D96Parser.BOOLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 604
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ZERO_10, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 605
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

        def ZERO_10(self):
            return self.getToken(D96Parser.ZERO_10, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_int_gen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_gen" ):
                return visitor.visitInt_gen(self)
            else:
                return visitor.visitChildren(self)




    def int_gen(self):

        localctx = D96Parser.Int_genContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_int_gen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ZERO_10) | (1 << D96Parser.INTLIT_16) | (1 << D96Parser.INTLIT_2) | (1 << D96Parser.INTLIT_8) | (1 << D96Parser.INTLIT_10))) != 0)):
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

        def STRING_TYPE(self):
            return self.getToken(D96Parser.STRING_TYPE, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_data_type)
        try:
            self.state = 616
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 610
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 611
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.BOOL_TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 612
                self.match(D96Parser.BOOL_TYPE)
                pass
            elif token in [D96Parser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 613
                self.match(D96Parser.STRING_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 614
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 615
                self.match(D96Parser.ID)
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


    class SizeContext(ParserRuleContext):
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
            return D96Parser.RULE_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = D96Parser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_size)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
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
        self.enterRule(localctx, 132, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self.match(D96Parser.ARRAY)
            self.state = 621
            self.match(D96Parser.LS)
            self.state = 622
            self.data_type()
            self.state = 623
            self.match(D96Parser.CM)
            self.state = 624
            self.size()
            self.state = 625
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
        self.enterRule(localctx, 134, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
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

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def MEM_ACCESS_OP(self):
            return self.getToken(D96Parser.MEM_ACCESS_OP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_binary_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_op" ):
                return visitor.visitBinary_op(self)
            else:
                return visitor.visitChildren(self)




    def binary_op(self):

        localctx = D96Parser.Binary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_binary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MEM_ACCESS_OP) | (1 << D96Parser.DOT) | (1 << D96Parser.ADDOP) | (1 << D96Parser.LESS_EQUAL) | (1 << D96Parser.GREAT_EQUAL) | (1 << D96Parser.SUBOP) | (1 << D96Parser.MULOP) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.MODOP) | (1 << D96Parser.DIVOP) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.EQUAL) | (1 << D96Parser.GREAT_THAN) | (1 << D96Parser.AND) | (1 << D96Parser.OR) | (1 << D96Parser.STR_CMP) | (1 << D96Parser.STR_CONCAT))) != 0)):
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


    class ZeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZERO_2(self):
            return self.getToken(D96Parser.ZERO_2, 0)

        def ZERO_8(self):
            return self.getToken(D96Parser.ZERO_8, 0)

        def ZERO_10(self):
            return self.getToken(D96Parser.ZERO_10, 0)

        def ZERO_16(self):
            return self.getToken(D96Parser.ZERO_16, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_zero

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitZero" ):
                return visitor.visitZero(self)
            else:
                return visitor.visitChildren(self)




    def zero(self):

        localctx = D96Parser.ZeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_zero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ZERO_2) | (1 << D96Parser.ZERO_8) | (1 << D96Parser.ZERO_10) | (1 << D96Parser.ZERO_16))) != 0)):
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
        self._predicates[26] = self.expr_lit_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_lit_sempred(self, localctx:Expr_litContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         




