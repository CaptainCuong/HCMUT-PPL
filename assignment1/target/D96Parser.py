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
        buf.write("\u028e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\32\3\32\3\32\3\32\3\32\5\32\u015c\n\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0167\n\33\3\33\3")
        buf.write("\33\3\33\3\33\7\33\u016d\n\33\f\33\16\33\u0170\13\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u0180\n\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u018d\n\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u01a2\n\34\f")
        buf.write("\34\16\34\u01a5\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\5!\u01bf\n!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\7\"\u01c6\n\"\f\"\16\"\u01c9\13\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3#\7#\u01d3\n#\f#\16#\u01d6\13#\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\6$\u01e0\n$\r$\16$\u01e1\3%\3%\3%\3%\3%")
        buf.write("\6%\u01e9\n%\r%\16%\u01ea\3&\3&\3&\5&\u01f0\n&\3\'\3\'")
        buf.write("\3\'\5\'\u01f5\n\'\3(\3(\3(\3(\5(\u01fb\n(\3)\3)\3)\3")
        buf.write(")\3)\5)\u0202\n)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\5,\u0212\n,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\5\62\u0222\n\62\3\63\3\63\3\63\3")
        buf.write("\63\3\63\5\63\u0229\n\63\3\64\3\64\3\64\5\64\u022e\n\64")
        buf.write("\3\65\3\65\3\65\3\65\5\65\u0234\n\65\3\66\3\66\3\66\5")
        buf.write("\66\u0239\n\66\3\67\3\67\3\67\3\67\5\67\u023f\n\67\38")
        buf.write("\38\38\38\58\u0245\n8\39\39\39\39\39\59\u024c\n9\3:\3")
        buf.write(":\3:\5:\u0251\n:\3;\3;\3;\3;\5;\u0257\n;\3<\3<\3<\5<\u025c")
        buf.write("\n<\3=\3=\3=\3=\5=\u0262\n=\3>\3>\3>\5>\u0267\n>\3?\3")
        buf.write("?\3?\3?\5?\u026d\n?\3@\3@\3@\3@\5@\u0273\n@\3A\3A\3B\3")
        buf.write("B\3B\3B\3B\3B\5B\u027d\nB\3C\3C\3D\3D\3D\3D\3D\3D\3D\3")
        buf.write("E\3E\3F\3F\3G\3G\3G\2\4\64\66H\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\2\16\3\2$%\4\2\21\22$%\3\2?@\4\29:<>\4\2\66\66")
        buf.write("9;\3\2\61:\4\2\61\6699\4\2\36\36 #\3\2 #\4\2\64\64>>\6")
        buf.write("\2\5\5&&\61=?@\3\2\34\37\2\u029f\2\u008f\3\2\2\2\4\u0095")
        buf.write("\3\2\2\2\6\u009d\3\2\2\2\b\u00aa\3\2\2\2\n\u00b8\3\2\2")
        buf.write("\2\f\u00c4\3\2\2\2\16\u00c6\3\2\2\2\20\u00cc\3\2\2\2\22")
        buf.write("\u00da\3\2\2\2\24\u00e1\3\2\2\2\26\u00e3\3\2\2\2\30\u00f4")
        buf.write("\3\2\2\2\32\u00f6\3\2\2\2\34\u0104\3\2\2\2\36\u0118\3")
        buf.write("\2\2\2 \u0120\3\2\2\2\"\u0122\3\2\2\2$\u0124\3\2\2\2&")
        buf.write("\u012a\3\2\2\2(\u012f\3\2\2\2*\u0136\3\2\2\2,\u0142\3")
        buf.write("\2\2\2.\u014e\3\2\2\2\60\u0154\3\2\2\2\62\u015b\3\2\2")
        buf.write("\2\64\u0166\3\2\2\2\66\u017f\3\2\2\28\u01a6\3\2\2\2:\u01ac")
        buf.write("\3\2\2\2<\u01b3\3\2\2\2>\u01ba\3\2\2\2@\u01be\3\2\2\2")
        buf.write("B\u01c0\3\2\2\2D\u01cd\3\2\2\2F\u01da\3\2\2\2H\u01e3\3")
        buf.write("\2\2\2J\u01ef\3\2\2\2L\u01f4\3\2\2\2N\u01fa\3\2\2\2P\u0201")
        buf.write("\3\2\2\2R\u0203\3\2\2\2T\u0208\3\2\2\2V\u0211\3\2\2\2")
        buf.write("X\u0213\3\2\2\2Z\u0215\3\2\2\2\\\u0217\3\2\2\2^\u0219")
        buf.write("\3\2\2\2`\u021b\3\2\2\2b\u0221\3\2\2\2d\u0228\3\2\2\2")
        buf.write("f\u022d\3\2\2\2h\u0233\3\2\2\2j\u0238\3\2\2\2l\u023e\3")
        buf.write("\2\2\2n\u0244\3\2\2\2p\u024b\3\2\2\2r\u0250\3\2\2\2t\u0256")
        buf.write("\3\2\2\2v\u025b\3\2\2\2x\u0261\3\2\2\2z\u0266\3\2\2\2")
        buf.write("|\u026c\3\2\2\2~\u0272\3\2\2\2\u0080\u0274\3\2\2\2\u0082")
        buf.write("\u027c\3\2\2\2\u0084\u027e\3\2\2\2\u0086\u0280\3\2\2\2")
        buf.write("\u0088\u0287\3\2\2\2\u008a\u0289\3\2\2\2\u008c\u028b\3")
        buf.write("\2\2\2\u008e\u0090\5\4\3\2\u008f\u008e\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\u0094\7\2\2\3\u0094\3\3\2\2\2\u0095")
        buf.write("\u0096\7\23\2\2\u0096\u0099\7%\2\2\u0097\u0098\7/\2\2")
        buf.write("\u0098\u009a\5j\66\2\u0099\u0097\3\2\2\2\u0099\u009a\3")
        buf.write("\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\5\6\4\2\u009c\5")
        buf.write("\3\2\2\2\u009d\u00a2\7,\2\2\u009e\u00a1\5\n\6\2\u009f")
        buf.write("\u00a1\5\16\b\2\u00a0\u009e\3\2\2\2\u00a0\u009f\3\2\2")
        buf.write("\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5")
        buf.write("\u00a6\7-\2\2\u00a6\7\3\2\2\2\u00a7\u00ab\5\64\33\2\u00a8")
        buf.write("\u00ab\5H%\2\u00a9\u00ab\5F$\2\u00aa\u00a7\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\t\3\2\2\2\u00ac")
        buf.write("\u00ad\7\27\2\2\u00ad\u00ae\5j\66\2\u00ae\u00af\7/\2\2")
        buf.write("\u00af\u00b0\5\u0082B\2\u00b0\u00b1\7\60\2\2\u00b1\u00b9")
        buf.write("\3\2\2\2\u00b2\u00b3\7\27\2\2\u00b3\u00b4\t\2\2\2\u00b4")
        buf.write("\u00b5\5\f\7\2\u00b5\u00b6\5\b\5\2\u00b6\u00b7\7\60\2")
        buf.write("\2\u00b7\u00b9\3\2\2\2\u00b8\u00ac\3\2\2\2\u00b8\u00b2")
        buf.write("\3\2\2\2\u00b9\13\3\2\2\2\u00ba\u00bb\7/\2\2\u00bb\u00bc")
        buf.write("\5\u0082B\2\u00bc\u00bd\7\t\2\2\u00bd\u00c5\3\2\2\2\u00be")
        buf.write("\u00bf\7\'\2\2\u00bf\u00c0\t\2\2\2\u00c0\u00c1\5\f\7\2")
        buf.write("\u00c1\u00c2\5\b\5\2\u00c2\u00c3\7\'\2\2\u00c3\u00c5\3")
        buf.write("\2\2\2\u00c4\u00ba\3\2\2\2\u00c4\u00be\3\2\2\2\u00c5\r")
        buf.write("\3\2\2\2\u00c6\u00c7\t\3\2\2\u00c7\u00c8\7*\2\2\u00c8")
        buf.write("\u00c9\5\22\n\2\u00c9\u00ca\7+\2\2\u00ca\u00cb\5\20\t")
        buf.write("\2\u00cb\17\3\2\2\2\u00cc\u00d1\7,\2\2\u00cd\u00d0\5\30")
        buf.write("\r\2\u00ce\u00d0\5\36\20\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce")
        buf.write("\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d2\3\2\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d4\u00d5\7-\2\2\u00d5\21\3\2\2\2\u00d6\u00db\3\2\2")
        buf.write("\2\u00d7\u00d8\5\26\f\2\u00d8\u00d9\5\24\13\2\u00d9\u00db")
        buf.write("\3\2\2\2\u00da\u00d6\3\2\2\2\u00da\u00d7\3\2\2\2\u00db")
        buf.write("\23\3\2\2\2\u00dc\u00e2\3\2\2\2\u00dd\u00de\7\60\2\2\u00de")
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
        buf.write("\b\33\1\2\u015e\u0167\5\66\34\2\u015f\u0160\5\u0088E\2")
        buf.write("\u0160\u0161\5\64\33\4\u0161\u0167\3\2\2\2\u0162\u0163")
        buf.write("\7*\2\2\u0163\u0164\5\64\33\2\u0164\u0165\7+\2\2\u0165")
        buf.write("\u0167\3\2\2\2\u0166\u015d\3\2\2\2\u0166\u015f\3\2\2\2")
        buf.write("\u0166\u0162\3\2\2\2\u0167\u016e\3\2\2\2\u0168\u0169\f")
        buf.write("\5\2\2\u0169\u016a\5\u008aF\2\u016a\u016b\5\64\33\6\u016b")
        buf.write("\u016d\3\2\2\2\u016c\u0168\3\2\2\2\u016d\u0170\3\2\2\2")
        buf.write("\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\65\3\2")
        buf.write("\2\2\u0170\u016e\3\2\2\2\u0171\u0172\b\34\1\2\u0172\u0180")
        buf.write("\7%\2\2\u0173\u0180\7\4\2\2\u0174\u0180\58\35\2\u0175")
        buf.write("\u0180\5~@\2\u0176\u0180\5R*\2\u0177\u0180\5T+\2\u0178")
        buf.write("\u0179\5\u0088E\2\u0179\u017a\5\66\34\5\u017a\u0180\3")
        buf.write("\2\2\2\u017b\u017c\7*\2\2\u017c\u017d\5\66\34\2\u017d")
        buf.write("\u017e\7+\2\2\u017e\u0180\3\2\2\2\u017f\u0171\3\2\2\2")
        buf.write("\u017f\u0173\3\2\2\2\u017f\u0174\3\2\2\2\u017f\u0175\3")
        buf.write("\2\2\2\u017f\u0176\3\2\2\2\u017f\u0177\3\2\2\2\u017f\u0178")
        buf.write("\3\2\2\2\u017f\u017b\3\2\2\2\u0180\u01a3\3\2\2\2\u0181")
        buf.write("\u0182\f\7\2\2\u0182\u0183\7&\2\2\u0183\u01a2\5\66\34")
        buf.write("\b\u0184\u0185\f\4\2\2\u0185\u0186\5\u008aF\2\u0186\u0187")
        buf.write("\5\66\34\5\u0187\u01a2\3\2\2\2\u0188\u0189\f\n\2\2\u0189")
        buf.write("\u018c\7(\2\2\u018a\u018d\5\66\34\2\u018b\u018d\5\u0080")
        buf.write("A\2\u018c\u018a\3\2\2\2\u018c\u018b\3\2\2\2\u018d\u018e")
        buf.write("\3\2\2\2\u018e\u018f\7)\2\2\u018f\u01a2\3\2\2\2\u0190")
        buf.write("\u0191\f\t\2\2\u0191\u0192\7&\2\2\u0192\u0193\7%\2\2\u0193")
        buf.write("\u0194\7*\2\2\u0194\u0195\5> \2\u0195\u0196\7+\2\2\u0196")
        buf.write("\u01a2\3\2\2\2\u0197\u0198\f\b\2\2\u0198\u0199\7\5\2\2")
        buf.write("\u0199\u019a\7$\2\2\u019a\u019b\7*\2\2\u019b\u019c\5>")
        buf.write(" \2\u019c\u019d\7+\2\2\u019d\u01a2\3\2\2\2\u019e\u019f")
        buf.write("\f\6\2\2\u019f\u01a0\7\5\2\2\u01a0\u01a2\7$\2\2\u01a1")
        buf.write("\u0181\3\2\2\2\u01a1\u0184\3\2\2\2\u01a1\u0188\3\2\2\2")
        buf.write("\u01a1\u0190\3\2\2\2\u01a1\u0197\3\2\2\2\u01a1\u019e\3")
        buf.write("\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4")
        buf.write("\3\2\2\2\u01a4\67\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7")
        buf.write("\7\7\2\2\u01a7\u01a8\7%\2\2\u01a8\u01a9\7*\2\2\u01a9\u01aa")
        buf.write("\5\60\31\2\u01aa\u01ab\7+\2\2\u01ab9\3\2\2\2\u01ac\u01ad")
        buf.write("\5\66\34\2\u01ad\u01ae\7&\2\2\u01ae\u01af\7%\2\2\u01af")
        buf.write("\u01b0\7*\2\2\u01b0\u01b1\5> \2\u01b1\u01b2\7+\2\2\u01b2")
        buf.write(";\3\2\2\2\u01b3\u01b4\5\66\34\2\u01b4\u01b5\7\5\2\2\u01b5")
        buf.write("\u01b6\7$\2\2\u01b6\u01b7\7*\2\2\u01b7\u01b8\5> \2\u01b8")
        buf.write("\u01b9\7+\2\2\u01b9=\3\2\2\2\u01ba\u01bb\5\60\31\2\u01bb")
        buf.write("?\3\2\2\2\u01bc\u01bf\5B\"\2\u01bd\u01bf\5D#\2\u01be\u01bc")
        buf.write("\3\2\2\2\u01be\u01bd\3\2\2\2\u01bfA\3\2\2\2\u01c0\u01c7")
        buf.write("\5\66\34\2\u01c1\u01c2\7&\2\2\u01c2\u01c6\5\66\34\2\u01c3")
        buf.write("\u01c4\7\5\2\2\u01c4\u01c6\7$\2\2\u01c5\u01c1\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3")
        buf.write("\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c7")
        buf.write("\3\2\2\2\u01ca\u01cb\7&\2\2\u01cb\u01cc\7%\2\2\u01ccC")
        buf.write("\3\2\2\2\u01cd\u01d4\5\66\34\2\u01ce\u01cf\7&\2\2\u01cf")
        buf.write("\u01d3\5\66\34\2\u01d0\u01d1\7\5\2\2\u01d1\u01d3\7$\2")
        buf.write("\2\u01d2\u01ce\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d6")
        buf.write("\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5")
        buf.write("\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d8\7\5\2\2")
        buf.write("\u01d8\u01d9\7$\2\2\u01d9E\3\2\2\2\u01da\u01df\7%\2\2")
        buf.write("\u01db\u01dc\7(\2\2\u01dc\u01dd\5\b\5\2\u01dd\u01de\7")
        buf.write(")\2\2\u01de\u01e0\3\2\2\2\u01df\u01db\3\2\2\2\u01e0\u01e1")
        buf.write("\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2")
        buf.write("G\3\2\2\2\u01e3\u01e8\5\64\33\2\u01e4\u01e5\7(\2\2\u01e5")
        buf.write("\u01e6\5\64\33\2\u01e6\u01e7\7)\2\2\u01e7\u01e9\3\2\2")
        buf.write("\2\u01e8\u01e4\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01e8")
        buf.write("\3\2\2\2\u01ea\u01eb\3\2\2\2\u01ebI\3\2\2\2\u01ec\u01f0")
        buf.write("\5\u0080A\2\u01ed\u01f0\7%\2\2\u01ee\u01f0\5@!\2\u01ef")
        buf.write("\u01ec\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2")
        buf.write("\u01f0K\3\2\2\2\u01f1\u01f5\7\24\2\2\u01f2\u01f5\7%\2")
        buf.write("\2\u01f3\u01f5\5@!\2\u01f4\u01f1\3\2\2\2\u01f4\u01f2\3")
        buf.write("\2\2\2\u01f4\u01f3\3\2\2\2\u01f5M\3\2\2\2\u01f6\u01fb")
        buf.write("\3\2\2\2\u01f7\u01f8\5R*\2\u01f8\u01f9\5P)\2\u01f9\u01fb")
        buf.write("\3\2\2\2\u01fa\u01f6\3\2\2\2\u01fa\u01f7\3\2\2\2\u01fb")
        buf.write("O\3\2\2\2\u01fc\u0202\3\2\2\2\u01fd\u01fe\7\'\2\2\u01fe")
        buf.write("\u01ff\5R*\2\u01ff\u0200\5P)\2\u0200\u0202\3\2\2\2\u0201")
        buf.write("\u01fc\3\2\2\2\u0201\u01fd\3\2\2\2\u0202Q\3\2\2\2\u0203")
        buf.write("\u0204\7\30\2\2\u0204\u0205\7*\2\2\u0205\u0206\5V,\2\u0206")
        buf.write("\u0207\7+\2\2\u0207S\3\2\2\2\u0208\u0209\7\30\2\2\u0209")
        buf.write("\u020a\7*\2\2\u020a\u020b\5N(\2\u020b\u020c\7+\2\2\u020c")
        buf.write("U\3\2\2\2\u020d\u0212\5n8\2\u020e\u0212\5r:\2\u020f\u0212")
        buf.write("\5v<\2\u0210\u0212\5z>\2\u0211\u020d\3\2\2\2\u0211\u020e")
        buf.write("\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0210\3\2\2\2\u0212")
        buf.write("W\3\2\2\2\u0213\u0214\t\4\2\2\u0214Y\3\2\2\2\u0215\u0216")
        buf.write("\t\5\2\2\u0216[\3\2\2\2\u0217\u0218\t\6\2\2\u0218]\3\2")
        buf.write("\2\2\u0219\u021a\t\7\2\2\u021a_\3\2\2\2\u021b\u021c\t")
        buf.write("\b\2\2\u021ca\3\2\2\2\u021d\u0222\3\2\2\2\u021e\u021f")
        buf.write("\5~@\2\u021f\u0220\5d\63\2\u0220\u0222\3\2\2\2\u0221\u021d")
        buf.write("\3\2\2\2\u0221\u021e\3\2\2\2\u0222c\3\2\2\2\u0223\u0229")
        buf.write("\3\2\2\2\u0224\u0225\7\'\2\2\u0225\u0226\5~@\2\u0226\u0227")
        buf.write("\5d\63\2\u0227\u0229\3\2\2\2\u0228\u0223\3\2\2\2\u0228")
        buf.write("\u0224\3\2\2\2\u0229e\3\2\2\2\u022a\u022e\3\2\2\2\u022b")
        buf.write("\u022c\7%\2\2\u022c\u022e\5h\65\2\u022d\u022a\3\2\2\2")
        buf.write("\u022d\u022b\3\2\2\2\u022eg\3\2\2\2\u022f\u0234\3\2\2")
        buf.write("\2\u0230\u0231\7\'\2\2\u0231\u0232\7%\2\2\u0232\u0234")
        buf.write("\5h\65\2\u0233\u022f\3\2\2\2\u0233\u0230\3\2\2\2\u0234")
        buf.write("i\3\2\2\2\u0235\u0239\3\2\2\2\u0236\u0237\t\2\2\2\u0237")
        buf.write("\u0239\5l\67\2\u0238\u0235\3\2\2\2\u0238\u0236\3\2\2\2")
        buf.write("\u0239k\3\2\2\2\u023a\u023f\3\2\2\2\u023b\u023c\7\'\2")
        buf.write("\2\u023c\u023d\t\2\2\2\u023d\u023f\5l\67\2\u023e\u023a")
        buf.write("\3\2\2\2\u023e\u023b\3\2\2\2\u023fm\3\2\2\2\u0240\u0245")
        buf.write("\3\2\2\2\u0241\u0242\5\u0080A\2\u0242\u0243\5p9\2\u0243")
        buf.write("\u0245\3\2\2\2\u0244\u0240\3\2\2\2\u0244\u0241\3\2\2\2")
        buf.write("\u0245o\3\2\2\2\u0246\u024c\3\2\2\2\u0247\u0248\7\'\2")
        buf.write("\2\u0248\u0249\5\u0080A\2\u0249\u024a\5p9\2\u024a\u024c")
        buf.write("\3\2\2\2\u024b\u0246\3\2\2\2\u024b\u0247\3\2\2\2\u024c")
        buf.write("q\3\2\2\2\u024d\u0251\3\2\2\2\u024e\u024f\7\26\2\2\u024f")
        buf.write("\u0251\5t;\2\u0250\u024d\3\2\2\2\u0250\u024e\3\2\2\2\u0251")
        buf.write("s\3\2\2\2\u0252\u0257\3\2\2\2\u0253\u0254\7\'\2\2\u0254")
        buf.write("\u0255\7\26\2\2\u0255\u0257\5t;\2\u0256\u0252\3\2\2\2")
        buf.write("\u0256\u0253\3\2\2\2\u0257u\3\2\2\2\u0258\u025c\3\2\2")
        buf.write("\2\u0259\u025a\7\24\2\2\u025a\u025c\5x=\2\u025b\u0258")
        buf.write("\3\2\2\2\u025b\u0259\3\2\2\2\u025cw\3\2\2\2\u025d\u0262")
        buf.write("\3\2\2\2\u025e\u025f\7\'\2\2\u025f\u0260\7\24\2\2\u0260")
        buf.write("\u0262\5x=\2\u0261\u025d\3\2\2\2\u0261\u025e\3\2\2\2\u0262")
        buf.write("y\3\2\2\2\u0263\u0267\3\2\2\2\u0264\u0265\7\3\2\2\u0265")
        buf.write("\u0267\5|?\2\u0266\u0263\3\2\2\2\u0266\u0264\3\2\2\2\u0267")
        buf.write("{\3\2\2\2\u0268\u026d\3\2\2\2\u0269\u026a\7\'\2\2\u026a")
        buf.write("\u026b\7\3\2\2\u026b\u026d\5|?\2\u026c\u0268\3\2\2\2\u026c")
        buf.write("\u0269\3\2\2\2\u026d}\3\2\2\2\u026e\u0273\7\24\2\2\u026f")
        buf.write("\u0273\7\26\2\2\u0270\u0273\7\3\2\2\u0271\u0273\5\u0080")
        buf.write("A\2\u0272\u026e\3\2\2\2\u0272\u026f\3\2\2\2\u0272\u0270")
        buf.write("\3\2\2\2\u0272\u0271\3\2\2\2\u0273\177\3\2\2\2\u0274\u0275")
        buf.write("\t\t\2\2\u0275\u0081\3\2\2\2\u0276\u027d\7\31\2\2\u0277")
        buf.write("\u027d\7\32\2\2\u0278\u027d\7\33\2\2\u0279\u027d\7\6\2")
        buf.write("\2\u027a\u027d\5\u0086D\2\u027b\u027d\7%\2\2\u027c\u0276")
        buf.write("\3\2\2\2\u027c\u0277\3\2\2\2\u027c\u0278\3\2\2\2\u027c")
        buf.write("\u0279\3\2\2\2\u027c\u027a\3\2\2\2\u027c\u027b\3\2\2\2")
        buf.write("\u027d\u0083\3\2\2\2\u027e\u027f\t\n\2\2\u027f\u0085\3")
        buf.write("\2\2\2\u0280\u0281\7\30\2\2\u0281\u0282\7(\2\2\u0282\u0283")
        buf.write("\5\u0082B\2\u0283\u0284\7\'\2\2\u0284\u0285\5\u0084C\2")
        buf.write("\u0285\u0286\7)\2\2\u0286\u0087\3\2\2\2\u0287\u0288\t")
        buf.write("\13\2\2\u0288\u0089\3\2\2\2\u0289\u028a\t\f\2\2\u028a")
        buf.write("\u008b\3\2\2\2\u028b\u028c\t\r\2\2\u028c\u008d\3\2\2\2")
        buf.write("<\u0091\u0099\u00a0\u00a2\u00aa\u00b8\u00c4\u00cf\u00d1")
        buf.write("\u00da\u00e1\u00ed\u00f4\u00ff\u0111\u0116\u0120\u012a")
        buf.write("\u0132\u0136\u0142\u014e\u0154\u015b\u0166\u016e\u017f")
        buf.write("\u018c\u01a1\u01a3\u01be\u01c5\u01c7\u01d2\u01d4\u01e1")
        buf.write("\u01ea\u01ef\u01f4\u01fa\u0201\u0211\u0221\u0228\u022d")
        buf.write("\u0233\u0238\u023e\u0244\u024b\u0250\u0256\u025b\u0261")
        buf.write("\u0266\u026c\u0272\u027c")
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
                self.expr(0)
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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 348
                self.expr_lit(0)
                pass

            elif la_ == 2:
                self.state = 349
                self.unary_op()
                self.state = 350
                self.expr(2)
                pass

            elif la_ == 3:
                self.state = 352
                self.match(D96Parser.LB)
                self.state = 353
                self.expr(0)
                self.state = 354
                self.match(D96Parser.RB)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 364
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 358
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 359
                    self.binary_op()
                    self.state = 360
                    self.expr(4) 
                self.state = 366
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 368
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 369
                self.match(D96Parser.NULL)
                pass

            elif la_ == 3:
                self.state = 370
                self.object_ini()
                pass

            elif la_ == 4:
                self.state = 371
                self.lit()
                pass

            elif la_ == 5:
                self.state = 372
                self.index_arr()
                pass

            elif la_ == 6:
                self.state = 373
                self.mul_dim_arr()
                pass

            elif la_ == 7:
                self.state = 374
                self.unary_op()
                self.state = 375
                self.expr_lit(3)
                pass

            elif la_ == 8:
                self.state = 377
                self.match(D96Parser.LB)
                self.state = 378
                self.expr_lit(0)
                self.state = 379
                self.match(D96Parser.RB)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 417
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 415
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 383
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 384
                        self.match(D96Parser.DOT)
                        self.state = 385
                        self.expr_lit(6)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 386
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 387
                        self.binary_op()
                        self.state = 388
                        self.expr_lit(3)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 390
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 391
                        self.match(D96Parser.LS)
                        self.state = 394
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                        if la_ == 1:
                            self.state = 392
                            self.expr_lit(0)
                            pass

                        elif la_ == 2:
                            self.state = 393
                            self.int_gen()
                            pass


                        self.state = 396
                        self.match(D96Parser.RS)
                        pass

                    elif la_ == 4:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 398
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 399
                        self.match(D96Parser.DOT)
                        self.state = 400
                        self.match(D96Parser.ID)
                        self.state = 401
                        self.match(D96Parser.LB)
                        self.state = 402
                        self.para_pass_list()
                        self.state = 403
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 5:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 405
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 406
                        self.match(D96Parser.MEM_ACCESS_OP)
                        self.state = 407
                        self.match(D96Parser.DOLLAR_ID)
                        self.state = 408
                        self.match(D96Parser.LB)
                        self.state = 409
                        self.para_pass_list()
                        self.state = 410
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 6:
                        localctx = D96Parser.Expr_litContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_lit)
                        self.state = 412
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 413
                        self.match(D96Parser.MEM_ACCESS_OP)
                        self.state = 414
                        self.match(D96Parser.DOLLAR_ID)
                        pass

             
                self.state = 419
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
            self.state = 420
            self.match(D96Parser.NEW)
            self.state = 421
            self.match(D96Parser.ID)
            self.state = 422
            self.match(D96Parser.LB)
            self.state = 423
            self.expr_pro_list()
            self.state = 424
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
            self.state = 426
            self.expr_lit(0)
            self.state = 427
            self.match(D96Parser.DOT)
            self.state = 428
            self.match(D96Parser.ID)
            self.state = 429
            self.match(D96Parser.LB)
            self.state = 430
            self.para_pass_list()
            self.state = 431
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
            self.state = 433
            self.expr_lit(0)
            self.state = 434
            self.match(D96Parser.MEM_ACCESS_OP)
            self.state = 435
            self.match(D96Parser.DOLLAR_ID)
            self.state = 436
            self.match(D96Parser.LB)
            self.state = 437
            self.para_pass_list()
            self.state = 438
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
            self.state = 440
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
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.instance_att_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
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
            self.state = 446
            self.expr_lit(0)
            self.state = 453
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 451
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.DOT]:
                        self.state = 447
                        self.match(D96Parser.DOT)
                        self.state = 448
                        self.expr_lit(0)
                        pass
                    elif token in [D96Parser.MEM_ACCESS_OP]:
                        self.state = 449
                        self.match(D96Parser.MEM_ACCESS_OP)
                        self.state = 450
                        self.match(D96Parser.DOLLAR_ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 455
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 456
            self.match(D96Parser.DOT)
            self.state = 457
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
            self.state = 459
            self.expr_lit(0)
            self.state = 466
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 464
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.DOT]:
                        self.state = 460
                        self.match(D96Parser.DOT)
                        self.state = 461
                        self.expr_lit(0)
                        pass
                    elif token in [D96Parser.MEM_ACCESS_OP]:
                        self.state = 462
                        self.match(D96Parser.MEM_ACCESS_OP)
                        self.state = 463
                        self.match(D96Parser.DOLLAR_ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 468
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 469
            self.match(D96Parser.MEM_ACCESS_OP)
            self.state = 470
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
            self.state = 472
            self.match(D96Parser.ID)
            self.state = 477 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 473
                self.match(D96Parser.LS)
                self.state = 474
                self.expr_pro()
                self.state = 475
                self.match(D96Parser.RS)
                self.state = 479 
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
            self.state = 481
            self.expr(0)
            self.state = 486 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 482
                self.match(D96Parser.LS)
                self.state = 483
                self.expr(0)
                self.state = 484
                self.match(D96Parser.RS)
                self.state = 488 
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
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.int_gen()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 492
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
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 497
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
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.index_arr()
                self.state = 502
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
            self.state = 511
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.match(D96Parser.CM)
                self.state = 508
                self.index_arr()
                self.state = 509
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
            self.state = 513
            self.match(D96Parser.ARRAY)
            self.state = 514
            self.match(D96Parser.LB)
            self.state = 515
            self.same_type_list()
            self.state = 516
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
            self.state = 518
            self.match(D96Parser.ARRAY)
            self.state = 519
            self.match(D96Parser.LB)
            self.state = 520
            self.index_arr_list()
            self.state = 521
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
            self.state = 527
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self.int_gen_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
                self.bool_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 525
                self.float_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 526
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
            self.state = 529
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
            self.state = 531
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
            self.state = 533
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
            self.state = 535
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
            self.state = 537
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
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.BOOLIT, D96Parser.ZERO_10, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.lit()
                self.state = 541
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
            self.state = 550
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
                self.match(D96Parser.CM)
                self.state = 547
                self.lit()
                self.state = 548
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
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 553
                self.match(D96Parser.ID)
                self.state = 554
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
            self.state = 561
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 558
                self.match(D96Parser.CM)
                self.state = 559
                self.match(D96Parser.ID)
                self.state = 560
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
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.DOLLAR_ID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 564
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 565
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
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP, D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 569
                self.match(D96Parser.CM)
                self.state = 570
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 571
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
            self.state = 578
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ZERO_10, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 575
                self.int_gen()
                self.state = 576
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
            self.state = 585
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 581
                self.match(D96Parser.CM)
                self.state = 582
                self.int_gen()
                self.state = 583
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
            self.state = 590
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
                self.match(D96Parser.BOOLIT)
                self.state = 589
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
            self.state = 596
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 593
                self.match(D96Parser.CM)
                self.state = 594
                self.match(D96Parser.BOOLIT)
                self.state = 595
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
            self.state = 601
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 599
                self.match(D96Parser.FLOATLIT)
                self.state = 600
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
            self.state = 607
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 604
                self.match(D96Parser.CM)
                self.state = 605
                self.match(D96Parser.FLOATLIT)
                self.state = 606
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
            self.state = 612
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 610
                self.match(D96Parser.STRINGLIT)
                self.state = 611
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
            self.state = 618
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 615
                self.match(D96Parser.CM)
                self.state = 616
                self.match(D96Parser.STRINGLIT)
                self.state = 617
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
            self.state = 624
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 620
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 621
                self.match(D96Parser.BOOLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 622
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ZERO_10, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 623
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
            self.state = 626
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
            self.state = 634
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 628
                self.match(D96Parser.INT_TYPE)
                pass
            elif token in [D96Parser.FLOAT_TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 629
                self.match(D96Parser.FLOAT_TYPE)
                pass
            elif token in [D96Parser.BOOL_TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 630
                self.match(D96Parser.BOOL_TYPE)
                pass
            elif token in [D96Parser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 631
                self.match(D96Parser.STRING_TYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 632
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 633
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
            self.state = 636
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
            self.state = 638
            self.match(D96Parser.ARRAY)
            self.state = 639
            self.match(D96Parser.LS)
            self.state = 640
            self.data_type()
            self.state = 641
            self.match(D96Parser.CM)
            self.state = 642
            self.size()
            self.state = 643
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
            self.state = 645
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
            self.state = 647
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
            self.state = 649
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
        self._predicates[25] = self.expr_sempred
        self._predicates[26] = self.expr_lit_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def expr_lit_sempred(self, localctx:Expr_litContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         




