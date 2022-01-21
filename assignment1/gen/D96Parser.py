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
        buf.write("\u01d4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\3")
        buf.write("\2\3\2\3\3\3\3\7\3z\n\3\f\3\16\3}\13\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\7\5\u0087\n\5\f\5\16\5\u008a\13\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u0096\n\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u009d\n\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u00a9\n\n\3\n\3\n\3\n\3\n\5\n\u00af")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00b9")
        buf.write("\n\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\7\f\u00c9\n\f\f\f\16\f\u00cc\13\f\3\f\3\f\5")
        buf.write("\f\u00d0\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00da\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3")
        buf.write("\22\3\22\3\22\3\23\3\23\5\23\u00e9\n\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\5\25\u00fa\n\25\3\26\3\26\3\26\3\26\5\26\u0100\n")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\5\27\u0107\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0115\n\30\3\30\3\30\3\30\3\30\7\30\u011b\n\30\f\30\16")
        buf.write("\30\u011e\13\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\5\37\u0145\n\37\3")
        buf.write(" \3 \3 \3 \3 \5 \u014c\n \3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3#\5#\u015c\n#\3$\3$\3$\7$\u0161\n$\f")
        buf.write("$\16$\u0164\13$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)")
        buf.write("\3*\3*\3*\5*\u0175\n*\3+\3+\3+\3+\5+\u017b\n+\3,\3,\3")
        buf.write(",\3,\5,\u0181\n,\3-\3-\3-\3-\3-\5-\u0188\n-\3.\3.\3.\5")
        buf.write(".\u018d\n.\3/\3/\3/\3/\5/\u0193\n/\3\60\3\60\3\60\5\60")
        buf.write("\u0198\n\60\3\61\3\61\3\61\3\61\5\61\u019e\n\61\3\62\3")
        buf.write("\62\3\62\3\62\5\62\u01a4\n\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\5\63\u01ab\n\63\3\64\3\64\3\64\3\64\5\64\u01b1\n\64\3")
        buf.write("\65\3\65\3\66\3\66\3\67\3\67\38\38\38\38\38\38\38\39\3")
        buf.write("9\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u01d2")
        buf.write("\n:\3:\4{\u0162\3.;\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("pr\2\f\4\2\17\20!!\3\2\37\37\3\2=>\4\2\678:<\4\2\64\64")
        buf.write("\679\3\2/8\4\2/\64\67\67\3\2\32\35\3\2\27\31\4\2\62\62")
        buf.write("<<\2\u01d9\2t\3\2\2\2\4w\3\2\2\2\6\u0080\3\2\2\2\b\u0088")
        buf.write("\3\2\2\2\n\u008b\3\2\2\2\f\u0095\3\2\2\2\16\u009c\3\2")
        buf.write("\2\2\20\u009e\3\2\2\2\22\u00ae\3\2\2\2\24\u00b0\3\2\2")
        buf.write("\2\26\u00bd\3\2\2\2\30\u00d1\3\2\2\2\32\u00d9\3\2\2\2")
        buf.write("\34\u00db\3\2\2\2\36\u00dd\3\2\2\2 \u00df\3\2\2\2\"\u00e3")
        buf.write("\3\2\2\2$\u00e8\3\2\2\2&\u00ea\3\2\2\2(\u00f9\3\2\2\2")
        buf.write("*\u00ff\3\2\2\2,\u0106\3\2\2\2.\u0114\3\2\2\2\60\u011f")
        buf.write("\3\2\2\2\62\u0125\3\2\2\2\64\u012c\3\2\2\2\66\u0133\3")
        buf.write("\2\2\28\u0137\3\2\2\2:\u013b\3\2\2\2<\u0144\3\2\2\2>\u014b")
        buf.write("\3\2\2\2@\u014d\3\2\2\2B\u0152\3\2\2\2D\u015b\3\2\2\2")
        buf.write("F\u015d\3\2\2\2H\u0167\3\2\2\2J\u0169\3\2\2\2L\u016b\3")
        buf.write("\2\2\2N\u016d\3\2\2\2P\u016f\3\2\2\2R\u0174\3\2\2\2T\u017a")
        buf.write("\3\2\2\2V\u0180\3\2\2\2X\u0187\3\2\2\2Z\u018c\3\2\2\2")
        buf.write("\\\u0192\3\2\2\2^\u0197\3\2\2\2`\u019d\3\2\2\2b\u01a3")
        buf.write("\3\2\2\2d\u01aa\3\2\2\2f\u01b0\3\2\2\2h\u01b2\3\2\2\2")
        buf.write("j\u01b4\3\2\2\2l\u01b6\3\2\2\2n\u01b8\3\2\2\2p\u01bf\3")
        buf.write("\2\2\2r\u01d1\3\2\2\2tu\5\32\16\2uv\7\2\2\3v\3\3\2\2\2")
        buf.write("w{\7\6\2\2xz\13\2\2\2yx\3\2\2\2z}\3\2\2\2{|\3\2\2\2{y")
        buf.write("\3\2\2\2|~\3\2\2\2}{\3\2\2\2~\177\7\6\2\2\177\5\3\2\2")
        buf.write("\2\u0080\u0081\7\21\2\2\u0081\u0082\7!\2\2\u0082\u0083")
        buf.write("\5\b\5\2\u0083\7\3\2\2\2\u0084\u0087\5&\24\2\u0085\u0087")
        buf.write("\5\n\6\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\t\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008c\t\2\2")
        buf.write("\2\u008c\u008d\7\'\2\2\u008d\u008e\5\16\b\2\u008e\u008f")
        buf.write("\7(\2\2\u008f\u0090\5\30\r\2\u0090\13\3\2\2\2\u0091\u0096")
        buf.write("\3\2\2\2\u0092\u0093\5\20\t\2\u0093\u0094\5\16\b\2\u0094")
        buf.write("\u0096\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0092\3\2\2\2")
        buf.write("\u0096\r\3\2\2\2\u0097\u009d\3\2\2\2\u0098\u0099\7.\2")
        buf.write("\2\u0099\u009a\5\20\t\2\u009a\u009b\5\16\b\2\u009b\u009d")
        buf.write("\3\2\2\2\u009c\u0097\3\2\2\2\u009c\u0098\3\2\2\2\u009d")
        buf.write("\17\3\2\2\2\u009e\u009f\5R*\2\u009f\u00a0\7-\2\2\u00a0")
        buf.write("\u00a1\5j\66\2\u00a1\21\3\2\2\2\u00a2\u00a9\5 \21\2\u00a3")
        buf.write("\u00a9\5&\24\2\u00a4\u00a9\5\36\20\2\u00a5\u00a9\5\34")
        buf.write("\17\2\u00a6\u00a9\5\"\22\2\u00a7\u00a9\5$\23\2\u00a8\u00a2")
        buf.write("\3\2\2\2\u00a8\u00a3\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a8")
        buf.write("\u00a5\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2")
        buf.write("\u00a9\u00aa\3\2\2\2\u00aa\u00ab\7.\2\2\u00ab\u00af\3")
        buf.write("\2\2\2\u00ac\u00af\5\26\f\2\u00ad\u00af\5\24\13\2\u00ae")
        buf.write("\u00a8\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2")
        buf.write("\u00af\23\3\2\2\2\u00b0\u00b1\7\r\2\2\u00b1\u00b2\7\'")
        buf.write("\2\2\u00b2\u00b3\7!\2\2\u00b3\u00b4\5h\65\2\u00b4\u00b5")
        buf.write("\7+\2\2\u00b5\u00b8\5h\65\2\u00b6\u00b7\7,\2\2\u00b7\u00b9")
        buf.write("\5h\65\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\u00bb\7(\2\2\u00bb\u00bc\5\30\r\2")
        buf.write("\u00bc\25\3\2\2\2\u00bd\u00be\7\n\2\2\u00be\u00bf\7\'")
        buf.write("\2\2\u00bf\u00c0\5.\30\2\u00c0\u00c1\7(\2\2\u00c1\u00ca")
        buf.write("\5\30\r\2\u00c2\u00c3\7\f\2\2\u00c3\u00c4\7\'\2\2\u00c4")
        buf.write("\u00c5\5.\30\2\u00c5\u00c6\7(\2\2\u00c6\u00c7\5\30\r\2")
        buf.write("\u00c7\u00c9\3\2\2\2\u00c8\u00c2\3\2\2\2\u00c9\u00cc\3")
        buf.write("\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cf")
        buf.write("\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\7\13\2\2\u00ce")
        buf.write("\u00d0\5\30\r\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2")
        buf.write("\2\u00d0\27\3\2\2\2\u00d1\u00d2\7)\2\2\u00d2\u00d3\5\32")
        buf.write("\16\2\u00d3\u00d4\7*\2\2\u00d4\31\3\2\2\2\u00d5\u00da")
        buf.write("\3\2\2\2\u00d6\u00d7\5\22\n\2\u00d7\u00d8\5\32\16\2\u00d8")
        buf.write("\u00da\3\2\2\2\u00d9\u00d5\3\2\2\2\u00d9\u00d6\3\2\2\2")
        buf.write("\u00da\33\3\2\2\2\u00db\u00dc\7\t\2\2\u00dc\35\3\2\2\2")
        buf.write("\u00dd\u00de\7\b\2\2\u00de\37\3\2\2\2\u00df\u00e0\7!\2")
        buf.write("\2\u00e0\u00e1\7\7\2\2\u00e1\u00e2\5.\30\2\u00e2!\3\2")
        buf.write("\2\2\u00e3\u00e4\7\5\2\2\u00e4\u00e5\5.\30\2\u00e5#\3")
        buf.write("\2\2\2\u00e6\u00e9\5\62\32\2\u00e7\u00e9\5\64\33\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9%\3\2\2\2\u00ea")
        buf.write("\u00eb\7\24\2\2\u00eb\u00ec\7!\2\2\u00ec\u00ed\5(\25\2")
        buf.write("\u00ed\u00ee\5.\30\2\u00ee\'\3\2\2\2\u00ef\u00f0\7-\2")
        buf.write("\2\u00f0\u00f1\5j\66\2\u00f1\u00f2\7\7\2\2\u00f2\u00fa")
        buf.write("\3\2\2\2\u00f3\u00f4\7$\2\2\u00f4\u00f5\7!\2\2\u00f5\u00f6")
        buf.write("\5(\25\2\u00f6\u00f7\5.\30\2\u00f7\u00f8\7$\2\2\u00f8")
        buf.write("\u00fa\3\2\2\2\u00f9\u00ef\3\2\2\2\u00f9\u00f3\3\2\2\2")
        buf.write("\u00fa)\3\2\2\2\u00fb\u0100\3\2\2\2\u00fc\u00fd\5.\30")
        buf.write("\2\u00fd\u00fe\5,\27\2\u00fe\u0100\3\2\2\2\u00ff\u00fb")
        buf.write("\3\2\2\2\u00ff\u00fc\3\2\2\2\u0100+\3\2\2\2\u0101\u0107")
        buf.write("\3\2\2\2\u0102\u0103\7$\2\2\u0103\u0104\5.\30\2\u0104")
        buf.write("\u0105\5,\27\2\u0105\u0107\3\2\2\2\u0106\u0101\3\2\2\2")
        buf.write("\u0106\u0102\3\2\2\2\u0107-\3\2\2\2\u0108\u0109\b\30\1")
        buf.write("\2\u0109\u0115\7!\2\2\u010a\u0115\5:\36\2\u010b\u0115")
        buf.write("\5\60\31\2\u010c\u0115\5f\64\2\u010d\u0115\5\62\32\2\u010e")
        buf.write("\u0115\5\64\33\2\u010f\u0115\5\66\34\2\u0110\u0115\58")
        buf.write("\35\2\u0111\u0112\5p9\2\u0112\u0113\5.\30\3\u0113\u0115")
        buf.write("\3\2\2\2\u0114\u0108\3\2\2\2\u0114\u010a\3\2\2\2\u0114")
        buf.write("\u010b\3\2\2\2\u0114\u010c\3\2\2\2\u0114\u010d\3\2\2\2")
        buf.write("\u0114\u010e\3\2\2\2\u0114\u010f\3\2\2\2\u0114\u0110\3")
        buf.write("\2\2\2\u0114\u0111\3\2\2\2\u0115\u011c\3\2\2\2\u0116\u0117")
        buf.write("\f\4\2\2\u0117\u0118\5r:\2\u0118\u0119\5.\30\5\u0119\u011b")
        buf.write("\3\2\2\2\u011a\u0116\3\2\2\2\u011b\u011e\3\2\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d/\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011f\u0120\7\4\2\2\u0120\u0121\7!\2\2")
        buf.write("\u0121\u0122\7\'\2\2\u0122\u0123\5*\26\2\u0123\u0124\7")
        buf.write("(\2\2\u0124\61\3\2\2\2\u0125\u0126\7!\2\2\u0126\u0127")
        buf.write("\7#\2\2\u0127\u0128\7!\2\2\u0128\u0129\7\'\2\2\u0129\u012a")
        buf.write("\5*\26\2\u012a\u012b\7(\2\2\u012b\63\3\2\2\2\u012c\u012d")
        buf.write("\7!\2\2\u012d\u012e\7\3\2\2\u012e\u012f\7!\2\2\u012f\u0130")
        buf.write("\7\'\2\2\u0130\u0131\5*\26\2\u0131\u0132\7(\2\2\u0132")
        buf.write("\65\3\2\2\2\u0133\u0134\7!\2\2\u0134\u0135\7#\2\2\u0135")
        buf.write("\u0136\7!\2\2\u0136\67\3\2\2\2\u0137\u0138\7!\2\2\u0138")
        buf.write("\u0139\7\3\2\2\u0139\u013a\7!\2\2\u013a9\3\2\2\2\u013b")
        buf.write("\u013c\7!\2\2\u013c\u013d\7%\2\2\u013d\u013e\5V,\2\u013e")
        buf.write("\u013f\7&\2\2\u013f;\3\2\2\2\u0140\u0145\3\2\2\2\u0141")
        buf.write("\u0142\5@!\2\u0142\u0143\5> \2\u0143\u0145\3\2\2\2\u0144")
        buf.write("\u0140\3\2\2\2\u0144\u0141\3\2\2\2\u0145=\3\2\2\2\u0146")
        buf.write("\u0147\7$\2\2\u0147\u0148\5@!\2\u0148\u0149\5<\37\2\u0149")
        buf.write("\u014c\3\2\2\2\u014a\u014c\3\2\2\2\u014b\u0146\3\2\2\2")
        buf.write("\u014b\u014a\3\2\2\2\u014c?\3\2\2\2\u014d\u014e\7\26\2")
        buf.write("\2\u014e\u014f\7\'\2\2\u014f\u0150\5D#\2\u0150\u0151\7")
        buf.write("(\2\2\u0151A\3\2\2\2\u0152\u0153\7\26\2\2\u0153\u0154")
        buf.write("\7\'\2\2\u0154\u0155\5<\37\2\u0155\u0156\7(\2\2\u0156")
        buf.write("C\3\2\2\2\u0157\u015c\5V,\2\u0158\u015c\5Z.\2\u0159\u015c")
        buf.write("\5^\60\2\u015a\u015c\5b\62\2\u015b\u0157\3\2\2\2\u015b")
        buf.write("\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015a\3\2\2\2")
        buf.write("\u015cE\3\2\2\2\u015d\u0162\7\37\2\2\u015e\u0161\7 \2")
        buf.write("\2\u015f\u0161\n\3\2\2\u0160\u015e\3\2\2\2\u0160\u015f")
        buf.write("\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0163\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0163\u0165\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0165\u0166\7\37\2\2\u0166G\3\2\2\2\u0167\u0168\t\4\2")
        buf.write("\2\u0168I\3\2\2\2\u0169\u016a\t\5\2\2\u016aK\3\2\2\2\u016b")
        buf.write("\u016c\t\6\2\2\u016cM\3\2\2\2\u016d\u016e\t\7\2\2\u016e")
        buf.write("O\3\2\2\2\u016f\u0170\t\b\2\2\u0170Q\3\2\2\2\u0171\u0175")
        buf.write("\3\2\2\2\u0172\u0173\7!\2\2\u0173\u0175\5T+\2\u0174\u0171")
        buf.write("\3\2\2\2\u0174\u0172\3\2\2\2\u0175S\3\2\2\2\u0176\u017b")
        buf.write("\3\2\2\2\u0177\u0178\7$\2\2\u0178\u0179\7!\2\2\u0179\u017b")
        buf.write("\5T+\2\u017a\u0176\3\2\2\2\u017a\u0177\3\2\2\2\u017bU")
        buf.write("\3\2\2\2\u017c\u0181\3\2\2\2\u017d\u017e\5h\65\2\u017e")
        buf.write("\u017f\5X-\2\u017f\u0181\3\2\2\2\u0180\u017c\3\2\2\2\u0180")
        buf.write("\u017d\3\2\2\2\u0181W\3\2\2\2\u0182\u0188\3\2\2\2\u0183")
        buf.write("\u0184\7$\2\2\u0184\u0185\5h\65\2\u0185\u0186\5X-\2\u0186")
        buf.write("\u0188\3\2\2\2\u0187\u0182\3\2\2\2\u0187\u0183\3\2\2\2")
        buf.write("\u0188Y\3\2\2\2\u0189\u018d\3\2\2\2\u018a\u018b\7\23\2")
        buf.write("\2\u018b\u018d\5\\/\2\u018c\u0189\3\2\2\2\u018c\u018a")
        buf.write("\3\2\2\2\u018d[\3\2\2\2\u018e\u0193\3\2\2\2\u018f\u0190")
        buf.write("\7$\2\2\u0190\u0191\7\23\2\2\u0191\u0193\5\\/\2\u0192")
        buf.write("\u018e\3\2\2\2\u0192\u018f\3\2\2\2\u0193]\3\2\2\2\u0194")
        buf.write("\u0198\3\2\2\2\u0195\u0196\7\22\2\2\u0196\u0198\5`\61")
        buf.write("\2\u0197\u0194\3\2\2\2\u0197\u0195\3\2\2\2\u0198_\3\2")
        buf.write("\2\2\u0199\u019e\3\2\2\2\u019a\u019b\7$\2\2\u019b\u019c")
        buf.write("\7\22\2\2\u019c\u019e\5`\61\2\u019d\u0199\3\2\2\2\u019d")
        buf.write("\u019a\3\2\2\2\u019ea\3\2\2\2\u019f\u01a4\3\2\2\2\u01a0")
        buf.write("\u01a1\5F$\2\u01a1\u01a2\5d\63\2\u01a2\u01a4\3\2\2\2\u01a3")
        buf.write("\u019f\3\2\2\2\u01a3\u01a0\3\2\2\2\u01a4c\3\2\2\2\u01a5")
        buf.write("\u01ab\3\2\2\2\u01a6\u01a7\7$\2\2\u01a7\u01a8\5F$\2\u01a8")
        buf.write("\u01a9\5d\63\2\u01a9\u01ab\3\2\2\2\u01aa\u01a5\3\2\2\2")
        buf.write("\u01aa\u01a6\3\2\2\2\u01abe\3\2\2\2\u01ac\u01b1\7\22\2")
        buf.write("\2\u01ad\u01b1\7\23\2\2\u01ae\u01b1\5F$\2\u01af\u01b1")
        buf.write("\5h\65\2\u01b0\u01ac\3\2\2\2\u01b0\u01ad\3\2\2\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1g\3\2\2\2\u01b2")
        buf.write("\u01b3\t\t\2\2\u01b3i\3\2\2\2\u01b4\u01b5\t\n\2\2\u01b5")
        buf.write("k\3\2\2\2\u01b6\u01b7\5h\65\2\u01b7m\3\2\2\2\u01b8\u01b9")
        buf.write("\7\26\2\2\u01b9\u01ba\7%\2\2\u01ba\u01bb\5j\66\2\u01bb")
        buf.write("\u01bc\7$\2\2\u01bc\u01bd\5l\67\2\u01bd\u01be\7&\2\2\u01be")
        buf.write("o\3\2\2\2\u01bf\u01c0\t\13\2\2\u01c0q\3\2\2\2\u01c1\u01d2")
        buf.write("\7/\2\2\u01c2\u01d2\7\60\2\2\u01c3\u01d2\7\64\2\2\u01c4")
        buf.write("\u01d2\7\61\2\2\u01c5\u01d2\79\2\2\u01c6\u01d2\7\62\2")
        buf.write("\2\u01c7\u01c8\7\63\2\2\u01c8\u01d2\7\64\2\2\u01c9\u01d2")
        buf.write("\7\65\2\2\u01ca\u01d2\7\66\2\2\u01cb\u01d2\7\67\2\2\u01cc")
        buf.write("\u01d2\78\2\2\u01cd\u01d2\7:\2\2\u01ce\u01d2\7;\2\2\u01cf")
        buf.write("\u01d2\7=\2\2\u01d0\u01d2\7>\2\2\u01d1\u01c1\3\2\2\2\u01d1")
        buf.write("\u01c2\3\2\2\2\u01d1\u01c3\3\2\2\2\u01d1\u01c4\3\2\2\2")
        buf.write("\u01d1\u01c5\3\2\2\2\u01d1\u01c6\3\2\2\2\u01d1\u01c7\3")
        buf.write("\2\2\2\u01d1\u01c9\3\2\2\2\u01d1\u01ca\3\2\2\2\u01d1\u01cb")
        buf.write("\3\2\2\2\u01d1\u01cc\3\2\2\2\u01d1\u01cd\3\2\2\2\u01d1")
        buf.write("\u01ce\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d0\3\2\2\2")
        buf.write("\u01d2s\3\2\2\2${\u0086\u0088\u0095\u009c\u00a8\u00ae")
        buf.write("\u00b8\u00ca\u00cf\u00d9\u00e8\u00f9\u00ff\u0106\u0114")
        buf.write("\u011c\u0144\u014b\u015b\u0160\u0162\u0174\u017a\u0180")
        buf.write("\u0187\u018c\u0192\u0197\u019d\u01a3\u01aa\u01b0\u01d1")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::'", "'New'", "'Return'", "'##'", "'='", 
                     "'Break'", "'Continue'", "'If'", "'Else'", "'Elseif'", 
                     "'Foreach'", "'In'", "'Constructor'", "'Destructor'", 
                     "'Class'", "<INVALID>", "<INVALID>", "<INVALID>", "'$'", 
                     "'Array'", "'Int'", "'Float'", "'Boolean'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\"'", "''\"'", "<INVALID>", "'0'", "'.'", "','", 
                     "'['", "']'", "'('", "')'", "'{'", "'}'", "'..'", "'By'", 
                     "':'", "';'", "'+'", "'<='", "'>='", "'-'", "'*'", 
                     "'<'", "'%'", "'/'", "'!='", "'=='", "'>'", "'&&'", 
                     "'||'", "'!'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>", "MEM_ACCESS_OP", "NEW", "RETURN", "DOUB_HASH_MARK", 
                      "ASSIGN_OP", "BREAK", "CONTINUE", "IF", "ELSE", "ELSEIF", 
                      "FOREACH", "IN", "CONSTRUCTOR", "DESTRUCTOR", "CLASS", 
                      "FLOATLIT", "BOOLIT", "VAL_VAR", "STATIC", "ARRAY", 
                      "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", "INTLIT_16", 
                      "INTLIT_2", "INTLIT_8", "INTLIT_10", "EXPONENT", "START_END_STRING", 
                      "DOUB_QUOTE", "ID", "ZERO", "DOT", "CM", "LS", "RS", 
                      "LB", "RB", "LP", "RP", "RANGE", "BY", "CL", "SEMI", 
                      "ADDOP", "LESS_EQUAL", "GREAT_EQUAL", "SUBOP", "MULOP", 
                      "LESS_THAN", "MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", 
                      "GREAT_THAN", "AND", "OR", "NEGATE", "STR_CMP", "STR_CONCAT", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_comment = 1
    RULE_class_dcl = 2
    RULE_class_body = 3
    RULE_method_dcl = 4
    RULE_para_dcl_list = 5
    RULE_para_dcl_smcllist = 6
    RULE_para_dcl = 7
    RULE_stm = 8
    RULE_for_in_stm = 9
    RULE_if_stm = 10
    RULE_block_stm = 11
    RULE_mn_stm = 12
    RULE_continue_stm = 13
    RULE_break_stm = 14
    RULE_asm_stm = 15
    RULE_return_stm = 16
    RULE_method_invoke_stm = 17
    RULE_var_dcl = 18
    RULE_var_dcl_list = 19
    RULE_expr_list = 20
    RULE_expr_cmlist = 21
    RULE_expr = 22
    RULE_object_ini = 23
    RULE_instance_method_invoke = 24
    RULE_static_mehod_invoke = 25
    RULE_instance_att_access = 26
    RULE_static_att_access = 27
    RULE_index_ele = 28
    RULE_index_arr_list = 29
    RULE_index_arr_cmlist = 30
    RULE_index_arr = 31
    RULE_mul_dim_arr = 32
    RULE_same_type_list = 33
    RULE_string = 34
    RULE_string_op = 35
    RULE_bool_op = 36
    RULE_relation_op = 37
    RULE_int_op = 38
    RULE_float_op = 39
    RULE_id_list = 40
    RULE_id_cmlist = 41
    RULE_int_gen_list = 42
    RULE_int_gen_cm = 43
    RULE_bool_list = 44
    RULE_bool_list_cm = 45
    RULE_float_list = 46
    RULE_float_list_cm = 47
    RULE_string_list = 48
    RULE_string_list_cm = 49
    RULE_lit = 50
    RULE_int_gen = 51
    RULE_data_type = 52
    RULE_size = 53
    RULE_array_type = 54
    RULE_unary_op = 55
    RULE_binary_op = 56

    ruleNames =  [ "program", "comment", "class_dcl", "class_body", "method_dcl", 
                   "para_dcl_list", "para_dcl_smcllist", "para_dcl", "stm", 
                   "for_in_stm", "if_stm", "block_stm", "mn_stm", "continue_stm", 
                   "break_stm", "asm_stm", "return_stm", "method_invoke_stm", 
                   "var_dcl", "var_dcl_list", "expr_list", "expr_cmlist", 
                   "expr", "object_ini", "instance_method_invoke", "static_mehod_invoke", 
                   "instance_att_access", "static_att_access", "index_ele", 
                   "index_arr_list", "index_arr_cmlist", "index_arr", "mul_dim_arr", 
                   "same_type_list", "string", "string_op", "bool_op", "relation_op", 
                   "int_op", "float_op", "id_list", "id_cmlist", "int_gen_list", 
                   "int_gen_cm", "bool_list", "bool_list_cm", "float_list", 
                   "float_list_cm", "string_list", "string_list_cm", "lit", 
                   "int_gen", "data_type", "size", "array_type", "unary_op", 
                   "binary_op" ]

    EOF = Token.EOF
    MEM_ACCESS_OP=1
    NEW=2
    RETURN=3
    DOUB_HASH_MARK=4
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
    BOOLIT=17
    VAL_VAR=18
    STATIC=19
    ARRAY=20
    INT_TYPE=21
    FLOAT_TYPE=22
    BOOL_TYPE=23
    INTLIT_16=24
    INTLIT_2=25
    INTLIT_8=26
    INTLIT_10=27
    EXPONENT=28
    START_END_STRING=29
    DOUB_QUOTE=30
    ID=31
    ZERO=32
    DOT=33
    CM=34
    LS=35
    RS=36
    LB=37
    RB=38
    LP=39
    RP=40
    RANGE=41
    BY=42
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
    ERROR_CHAR=62

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

        def mn_stm(self):
            return self.getTypedRuleContext(D96Parser.Mn_stmContext,0)


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
            self.state = 114
            self.mn_stm()
            self.state = 115
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
            self.state = 117
            self.match(D96Parser.DOUB_HASH_MARK)
            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 118
                    self.matchWildcard() 
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 124
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(D96Parser.CLASS)
            self.state = 127
            self.match(D96Parser.ID)
            self.state = 128
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

        def var_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Var_dclContext)
            else:
                return self.getTypedRuleContext(D96Parser.Var_dclContext,i)


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
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.VAL_VAR) | (1 << D96Parser.ID))) != 0):
                self.state = 132
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL_VAR]:
                    self.state = 130
                    self.var_dcl()
                    pass
                elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID]:
                    self.state = 131
                    self.method_dcl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 8, self.RULE_method_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 138
            self.match(D96Parser.LB)
            self.state = 139
            self.para_dcl_smcllist()
            self.state = 140
            self.match(D96Parser.RB)
            self.state = 141
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
        self.enterRule(localctx, 10, self.RULE_para_dcl_list)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ID, D96Parser.CL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.para_dcl()
                self.state = 145
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
        self.enterRule(localctx, 12, self.RULE_para_dcl_smcllist)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF, D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(D96Parser.SEMI)
                self.state = 151
                self.para_dcl()
                self.state = 152
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
        self.enterRule(localctx, 14, self.RULE_para_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.id_list()
            self.state = 157
            self.match(D96Parser.CL)
            self.state = 158
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
        self.enterRule(localctx, 16, self.RULE_stm)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RETURN, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.VAL_VAR, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 160
                    self.asm_stm()
                    pass

                elif la_ == 2:
                    self.state = 161
                    self.var_dcl()
                    pass

                elif la_ == 3:
                    self.state = 162
                    self.break_stm()
                    pass

                elif la_ == 4:
                    self.state = 163
                    self.continue_stm()
                    pass

                elif la_ == 5:
                    self.state = 164
                    self.return_stm()
                    pass

                elif la_ == 6:
                    self.state = 165
                    self.method_invoke_stm()
                    pass


                self.state = 168
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.if_stm()
                pass
            elif token in [D96Parser.FOREACH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
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

        def int_gen(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Int_genContext)
            else:
                return self.getTypedRuleContext(D96Parser.Int_genContext,i)


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
        self.enterRule(localctx, 18, self.RULE_for_in_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(D96Parser.FOREACH)
            self.state = 175
            self.match(D96Parser.LB)
            self.state = 176
            self.match(D96Parser.ID)
            self.state = 177
            self.int_gen()
            self.state = 178
            self.match(D96Parser.RANGE)
            self.state = 179
            self.int_gen()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 180
                self.match(D96Parser.BY)
                self.state = 181
                self.int_gen()


            self.state = 184
            self.match(D96Parser.RB)
            self.state = 185
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
        self.enterRule(localctx, 20, self.RULE_if_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(D96Parser.IF)
            self.state = 188
            self.match(D96Parser.LB)
            self.state = 189
            self.expr(0)
            self.state = 190
            self.match(D96Parser.RB)
            self.state = 191
            self.block_stm()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 192
                self.match(D96Parser.ELSEIF)
                self.state = 193
                self.match(D96Parser.LB)
                self.state = 194
                self.expr(0)
                self.state = 195
                self.match(D96Parser.RB)
                self.state = 196
                self.block_stm()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 203
                self.match(D96Parser.ELSE)
                self.state = 204
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
        self.enterRule(localctx, 22, self.RULE_block_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(D96Parser.LP)
            self.state = 208
            self.mn_stm()
            self.state = 209
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
        self.enterRule(localctx, 24, self.RULE_mn_stm)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EOF, D96Parser.RP]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.RETURN, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.VAL_VAR, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.stm()
                self.state = 213
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
        self.enterRule(localctx, 26, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
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
        self.enterRule(localctx, 28, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def ASSIGN_OP(self):
            return self.getToken(D96Parser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


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
        self.enterRule(localctx, 30, self.RULE_asm_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(D96Parser.ID)
            self.state = 222
            self.match(D96Parser.ASSIGN_OP)
            self.state = 223
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
        self.enterRule(localctx, 32, self.RULE_return_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(D96Parser.RETURN)
            self.state = 226
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
        self.enterRule(localctx, 34, self.RULE_method_invoke_stm)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.instance_method_invoke()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
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
        self.enterRule(localctx, 36, self.RULE_var_dcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(D96Parser.VAL_VAR)
            self.state = 233
            self.match(D96Parser.ID)
            self.state = 234
            self.var_dcl_list()
            self.state = 235
            self.expr(0)
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
        self.enterRule(localctx, 38, self.RULE_var_dcl_list)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(D96Parser.CL)
                self.state = 238
                self.data_type()
                self.state = 239
                self.match(D96Parser.ASSIGN_OP)
                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(D96Parser.CM)
                self.state = 242
                self.match(D96Parser.ID)
                self.state = 243
                self.var_dcl_list()
                self.state = 244
                self.expr(0)
                self.state = 245
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
        self.enterRule(localctx, 40, self.RULE_expr_list)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.NEW, D96Parser.FLOATLIT, D96Parser.BOOLIT, D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10, D96Parser.START_END_STRING, D96Parser.ID, D96Parser.SUBOP, D96Parser.NEGATE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.expr(0)
                self.state = 251
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
        self.enterRule(localctx, 42, self.RULE_expr_cmlist)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(D96Parser.CM)
                self.state = 257
                self.expr(0)
                self.state = 258
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 263
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 264
                self.index_ele()
                pass

            elif la_ == 3:
                self.state = 265
                self.object_ini()
                pass

            elif la_ == 4:
                self.state = 266
                self.lit()
                pass

            elif la_ == 5:
                self.state = 267
                self.instance_method_invoke()
                pass

            elif la_ == 6:
                self.state = 268
                self.static_mehod_invoke()
                pass

            elif la_ == 7:
                self.state = 269
                self.instance_att_access()
                pass

            elif la_ == 8:
                self.state = 270
                self.static_att_access()
                pass

            elif la_ == 9:
                self.state = 271
                self.unary_op()
                self.state = 272
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 276
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 277
                    self.binary_op()
                    self.state = 278
                    self.expr(3) 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_object_ini)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(D96Parser.NEW)
            self.state = 286
            self.match(D96Parser.ID)
            self.state = 287
            self.match(D96Parser.LB)
            self.state = 288
            self.expr_list()
            self.state = 289
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

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


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
        self.enterRule(localctx, 48, self.RULE_instance_method_invoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(D96Parser.ID)
            self.state = 292
            self.match(D96Parser.DOT)
            self.state = 293
            self.match(D96Parser.ID)
            self.state = 294
            self.match(D96Parser.LB)
            self.state = 295
            self.expr_list()
            self.state = 296
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

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


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
        self.enterRule(localctx, 50, self.RULE_static_mehod_invoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(D96Parser.ID)
            self.state = 299
            self.match(D96Parser.MEM_ACCESS_OP)
            self.state = 300
            self.match(D96Parser.ID)
            self.state = 301
            self.match(D96Parser.LB)
            self.state = 302
            self.expr_list()
            self.state = 303
            self.match(D96Parser.RB)
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
        self.enterRule(localctx, 52, self.RULE_instance_att_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(D96Parser.ID)
            self.state = 306
            self.match(D96Parser.DOT)
            self.state = 307
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
        self.enterRule(localctx, 54, self.RULE_static_att_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(D96Parser.ID)
            self.state = 310
            self.match(D96Parser.MEM_ACCESS_OP)
            self.state = 311
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

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def int_gen_list(self):
            return self.getTypedRuleContext(D96Parser.Int_gen_listContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

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
        self.enterRule(localctx, 56, self.RULE_index_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(D96Parser.ID)
            self.state = 314
            self.match(D96Parser.LS)
            self.state = 315
            self.int_gen_list()
            self.state = 316
            self.match(D96Parser.RS)
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
        self.enterRule(localctx, 58, self.RULE_index_arr_list)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.index_arr()
                self.state = 320
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


        def index_arr_list(self):
            return self.getTypedRuleContext(D96Parser.Index_arr_listContext,0)


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
        self.enterRule(localctx, 60, self.RULE_index_arr_cmlist)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.match(D96Parser.CM)
                self.state = 325
                self.index_arr()
                self.state = 326
                self.index_arr_list()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

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
        self.enterRule(localctx, 62, self.RULE_index_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(D96Parser.ARRAY)
            self.state = 332
            self.match(D96Parser.LB)
            self.state = 333
            self.same_type_list()
            self.state = 334
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
        self.enterRule(localctx, 64, self.RULE_mul_dim_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(D96Parser.ARRAY)
            self.state = 337
            self.match(D96Parser.LB)
            self.state = 338
            self.index_arr_list()
            self.state = 339
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
        self.enterRule(localctx, 66, self.RULE_same_type_list)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.int_gen_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.bool_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.float_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 344
                self.string_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START_END_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.START_END_STRING)
            else:
                return self.getToken(D96Parser.START_END_STRING, i)

        def DOUB_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOUB_QUOTE)
            else:
                return self.getToken(D96Parser.DOUB_QUOTE, i)

        def getRuleIndex(self):
            return D96Parser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = D96Parser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(D96Parser.START_END_STRING)
            self.state = 352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 350
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        self.state = 348
                        self.match(D96Parser.DOUB_QUOTE)
                        pass

                    elif la_ == 2:
                        self.state = 349
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==D96Parser.START_END_STRING:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 354
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 355
            self.match(D96Parser.START_END_STRING)
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
        self.enterRule(localctx, 70, self.RULE_string_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
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
        self.enterRule(localctx, 72, self.RULE_bool_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
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
        self.enterRule(localctx, 74, self.RULE_relation_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
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
        self.enterRule(localctx, 76, self.RULE_int_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
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
        self.enterRule(localctx, 78, self.RULE_float_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
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
        self.enterRule(localctx, 80, self.RULE_id_list)
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.match(D96Parser.ID)
                self.state = 369
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
        self.enterRule(localctx, 82, self.RULE_id_cmlist)
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.match(D96Parser.CM)
                self.state = 374
                self.match(D96Parser.ID)
                self.state = 375
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
        self.enterRule(localctx, 84, self.RULE_int_gen_list)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RS, D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.int_gen()
                self.state = 380
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
        self.enterRule(localctx, 86, self.RULE_int_gen_cm)
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RS, D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.match(D96Parser.CM)
                self.state = 386
                self.int_gen()
                self.state = 387
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
        self.enterRule(localctx, 88, self.RULE_bool_list)
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.match(D96Parser.BOOLIT)
                self.state = 393
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
        self.enterRule(localctx, 90, self.RULE_bool_list_cm)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.match(D96Parser.CM)
                self.state = 398
                self.match(D96Parser.BOOLIT)
                self.state = 399
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
        self.enterRule(localctx, 92, self.RULE_float_list)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.match(D96Parser.FLOATLIT)
                self.state = 404
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
        self.enterRule(localctx, 94, self.RULE_float_list_cm)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.match(D96Parser.CM)
                self.state = 409
                self.match(D96Parser.FLOATLIT)
                self.state = 410
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

        def string(self):
            return self.getTypedRuleContext(D96Parser.StringContext,0)


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
        self.enterRule(localctx, 96, self.RULE_string_list)
        try:
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.START_END_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.string()
                self.state = 415
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

        def string(self):
            return self.getTypedRuleContext(D96Parser.StringContext,0)


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
        self.enterRule(localctx, 98, self.RULE_string_list_cm)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.match(D96Parser.CM)
                self.state = 421
                self.string()
                self.state = 422
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

        def string(self):
            return self.getTypedRuleContext(D96Parser.StringContext,0)


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
        self.enterRule(localctx, 100, self.RULE_lit)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.match(D96Parser.BOOLIT)
                pass
            elif token in [D96Parser.START_END_STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 428
                self.string()
                pass
            elif token in [D96Parser.INTLIT_16, D96Parser.INTLIT_2, D96Parser.INTLIT_8, D96Parser.INTLIT_10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 429
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
        self.enterRule(localctx, 102, self.RULE_int_gen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
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
        self.enterRule(localctx, 104, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
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
        self.enterRule(localctx, 106, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
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
        self.enterRule(localctx, 108, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(D96Parser.ARRAY)
            self.state = 439
            self.match(D96Parser.LS)
            self.state = 440
            self.data_type()
            self.state = 441
            self.match(D96Parser.CM)
            self.state = 442
            self.size()
            self.state = 443
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
        self.enterRule(localctx, 110, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
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
        self.enterRule(localctx, 112, self.RULE_binary_op)
        try:
            self.state = 463
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ADDOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(D96Parser.ADDOP)
                pass
            elif token in [D96Parser.LESS_EQUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(D96Parser.LESS_EQUAL)
                pass
            elif token in [D96Parser.LESS_THAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 449
                self.match(D96Parser.LESS_THAN)
                pass
            elif token in [D96Parser.GREAT_EQUAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 450
                self.match(D96Parser.GREAT_EQUAL)
                pass
            elif token in [D96Parser.GREAT_THAN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 451
                self.match(D96Parser.GREAT_THAN)
                pass
            elif token in [D96Parser.SUBOP]:
                self.enterOuterAlt(localctx, 6)
                self.state = 452
                self.match(D96Parser.SUBOP)
                pass
            elif token in [D96Parser.MULOP]:
                self.enterOuterAlt(localctx, 7)
                self.state = 453
                self.match(D96Parser.MULOP)
                self.state = 454
                self.match(D96Parser.LESS_THAN)
                pass
            elif token in [D96Parser.MODOP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 455
                self.match(D96Parser.MODOP)
                pass
            elif token in [D96Parser.DIVOP]:
                self.enterOuterAlt(localctx, 9)
                self.state = 456
                self.match(D96Parser.DIVOP)
                pass
            elif token in [D96Parser.NOT_EQUAL]:
                self.enterOuterAlt(localctx, 10)
                self.state = 457
                self.match(D96Parser.NOT_EQUAL)
                pass
            elif token in [D96Parser.EQUAL]:
                self.enterOuterAlt(localctx, 11)
                self.state = 458
                self.match(D96Parser.EQUAL)
                pass
            elif token in [D96Parser.AND]:
                self.enterOuterAlt(localctx, 12)
                self.state = 459
                self.match(D96Parser.AND)
                pass
            elif token in [D96Parser.OR]:
                self.enterOuterAlt(localctx, 13)
                self.state = 460
                self.match(D96Parser.OR)
                pass
            elif token in [D96Parser.STR_CMP]:
                self.enterOuterAlt(localctx, 14)
                self.state = 461
                self.match(D96Parser.STR_CMP)
                pass
            elif token in [D96Parser.STR_CONCAT]:
                self.enterOuterAlt(localctx, 15)
                self.state = 462
                self.match(D96Parser.STR_CONCAT)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




