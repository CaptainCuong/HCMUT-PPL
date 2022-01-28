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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0239\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7")
        buf.write("\2\u0096\n\2\f\2\16\2\u0099\13\2\3\2\3\2\3\2\3\2\3\2\5")
        buf.write("\2\u00a0\n\2\3\2\5\2\u00a3\n\2\3\2\3\2\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\5\22\u0106\n\22\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u010c\n\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u0115\n\22\3\22\3\22\3\22\5\22\u011a\n\22\3")
        buf.write("\22\3\22\3\23\3\23\7\23\u0120\n\23\f\23\16\23\u0123\13")
        buf.write("\23\3\23\3\23\5\23\u0127\n\23\5\23\u0129\n\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u0137\n\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u013f\n")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\7\37\u016d\n\37\f\37\16\37\u0170\13\37\3\37\5\37")
        buf.write("\u0173\n\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \7 \u017e\n")
        buf.write(" \f \16 \u0181\13 \3 \5 \u0184\n \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\7!\u018d\n!\f!\16!\u0190\13!\3!\5!\u0193\n!\3!\3!\3")
        buf.write("\"\3\"\5\"\u0199\n\"\3\"\3\"\5\"\u019d\n\"\7\"\u019f\n")
        buf.write("\"\f\"\16\"\u01a2\13\"\3\"\3\"\5\"\u01a6\n\"\3\"\3\"\3")
        buf.write("#\3#\3$\3$\5$\u01ae\n$\3$\7$\u01b1\n$\f$\16$\u01b4\13")
        buf.write("$\3$\3$\5$\u01b8\n$\3%\3%\6%\u01bc\n%\r%\16%\u01bd\3&")
        buf.write("\3&\7&\u01c2\n&\f&\16&\u01c5\13&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\3;\3;\3;\3<")
        buf.write("\3<\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3@\3@\3A\3A\3A\3B\3")
        buf.write("B\3B\3B\7B\u020b\nB\fB\16B\u020e\13B\3B\3B\3B\3B\3B\3")
        buf.write("C\6C\u0216\nC\rC\16C\u0217\3C\3C\3D\3D\3D\3D\7D\u0220")
        buf.write("\nD\fD\16D\u0223\13D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3E")
        buf.write("\7E\u0230\nE\fE\16E\u0233\13E\3E\3E\3F\3F\3F\3\u020c\2")
        buf.write("G\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\2\'\24)\25+\26-\27/\30")
        buf.write("\61\31\63\32\65\33\67\349\35;\36=\37? A!C\"E\2G\2I#K$")
        buf.write("M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\65o\66q\67")
        buf.write("s8u9w:y;{<}=\177>\u0081?\u0083@\u0085A\u0087B\u0089C\u008b")
        buf.write("D\3\2\27\t\2))^^ddhhppttvv\6\2\13\f\17\17$$^^\7\2\13\f")
        buf.write("\17\17$$))^^\4\2DDdd\4\2ZZzz\4\2\63;CH\5\2\62;CHaa\4\2")
        buf.write("\62;CH\4\2\62\63aa\3\2\62\63\3\2\639\4\2\629aa\3\2\62")
        buf.write("9\3\2\63;\3\2\62;\5\2C\\aac|\4\2GGgg\4\2--//\6\2\62;C")
        buf.write("\\aac|\5\2\13\f\17\17\"\"\6\2\f\f\17\17$$^^\2\u025c\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2")
        buf.write("\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2")
        buf.write("\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2")
        buf.write("\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3")
        buf.write("\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w")
        buf.write("\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u00a2\3\2\2")
        buf.write("\2\5\u00a6\3\2\2\2\7\u00a9\3\2\2\2\t\u00b0\3\2\2\2\13")
        buf.write("\u00b4\3\2\2\2\r\u00bb\3\2\2\2\17\u00bd\3\2\2\2\21\u00c3")
        buf.write("\3\2\2\2\23\u00cc\3\2\2\2\25\u00cf\3\2\2\2\27\u00d4\3")
        buf.write("\2\2\2\31\u00db\3\2\2\2\33\u00e3\3\2\2\2\35\u00e6\3\2")
        buf.write("\2\2\37\u00f2\3\2\2\2!\u00fd\3\2\2\2#\u0119\3\2\2\2%\u011d")
        buf.write("\3\2\2\2\'\u012a\3\2\2\2)\u0136\3\2\2\2+\u013e\3\2\2\2")
        buf.write("-\u0140\3\2\2\2/\u0146\3\2\2\2\61\u014a\3\2\2\2\63\u0150")
        buf.write("\3\2\2\2\65\u0158\3\2\2\2\67\u015c\3\2\2\29\u015f\3\2")
        buf.write("\2\2;\u0161\3\2\2\2=\u0172\3\2\2\2?\u0183\3\2\2\2A\u0192")
        buf.write("\3\2\2\2C\u01a5\3\2\2\2E\u01a9\3\2\2\2G\u01ab\3\2\2\2")
        buf.write("I\u01b9\3\2\2\2K\u01bf\3\2\2\2M\u01c6\3\2\2\2O\u01c8\3")
        buf.write("\2\2\2Q\u01ca\3\2\2\2S\u01cc\3\2\2\2U\u01ce\3\2\2\2W\u01d0")
        buf.write("\3\2\2\2Y\u01d2\3\2\2\2[\u01d4\3\2\2\2]\u01d6\3\2\2\2")
        buf.write("_\u01d9\3\2\2\2a\u01db\3\2\2\2c\u01dd\3\2\2\2e\u01df\3")
        buf.write("\2\2\2g\u01e2\3\2\2\2i\u01e5\3\2\2\2k\u01e7\3\2\2\2m\u01e9")
        buf.write("\3\2\2\2o\u01eb\3\2\2\2q\u01ed\3\2\2\2s\u01ef\3\2\2\2")
        buf.write("u\u01f2\3\2\2\2w\u01f5\3\2\2\2y\u01f7\3\2\2\2{\u01fa\3")
        buf.write("\2\2\2}\u01fd\3\2\2\2\177\u01ff\3\2\2\2\u0081\u0203\3")
        buf.write("\2\2\2\u0083\u0206\3\2\2\2\u0085\u0215\3\2\2\2\u0087\u021b")
        buf.write("\3\2\2\2\u0089\u0229\3\2\2\2\u008b\u0236\3\2\2\2\u008d")
        buf.write("\u008e\7$\2\2\u008e\u00a3\7$\2\2\u008f\u0097\7$\2\2\u0090")
        buf.write("\u0091\7)\2\2\u0091\u0096\7$\2\2\u0092\u0093\7^\2\2\u0093")
        buf.write("\u0096\t\2\2\2\u0094\u0096\n\3\2\2\u0095\u0090\3\2\2\2")
        buf.write("\u0095\u0092\3\2\2\2\u0095\u0094\3\2\2\2\u0096\u0099\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009f")
        buf.write("\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009b\7)\2\2\u009b")
        buf.write("\u00a0\7$\2\2\u009c\u009d\7^\2\2\u009d\u00a0\t\2\2\2\u009e")
        buf.write("\u00a0\n\4\2\2\u009f\u009a\3\2\2\2\u009f\u009c\3\2\2\2")
        buf.write("\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\7")
        buf.write("$\2\2\u00a2\u008d\3\2\2\2\u00a2\u008f\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a4\u00a5\b\2\2\2\u00a5\4\3\2\2\2\u00a6\u00a7")
        buf.write("\7<\2\2\u00a7\u00a8\7<\2\2\u00a8\6\3\2\2\2\u00a9\u00aa")
        buf.write("\7U\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad")
        buf.write("\7k\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7i\2\2\u00af\b")
        buf.write("\3\2\2\2\u00b0\u00b1\7P\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3")
        buf.write("\7y\2\2\u00b3\n\3\2\2\2\u00b4\u00b5\7T\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9")
        buf.write("\7t\2\2\u00b9\u00ba\7p\2\2\u00ba\f\3\2\2\2\u00bb\u00bc")
        buf.write("\7?\2\2\u00bc\16\3\2\2\2\u00bd\u00be\7D\2\2\u00be\u00bf")
        buf.write("\7t\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2")
        buf.write("\7m\2\2\u00c2\20\3\2\2\2\u00c3\u00c4\7E\2\2\u00c4\u00c5")
        buf.write("\7q\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8")
        buf.write("\7k\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7w\2\2\u00ca\u00cb")
        buf.write("\7g\2\2\u00cb\22\3\2\2\2\u00cc\u00cd\7K\2\2\u00cd\u00ce")
        buf.write("\7h\2\2\u00ce\24\3\2\2\2\u00cf\u00d0\7G\2\2\u00d0\u00d1")
        buf.write("\7n\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3\7g\2\2\u00d3\26")
        buf.write("\3\2\2\2\u00d4\u00d5\7G\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7")
        buf.write("\7u\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da")
        buf.write("\7h\2\2\u00da\30\3\2\2\2\u00db\u00dc\7H\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u00e1\7e\2\2\u00e1\u00e2\7j\2\2\u00e2\32")
        buf.write("\3\2\2\2\u00e3\u00e4\7K\2\2\u00e4\u00e5\7p\2\2\u00e5\34")
        buf.write("\3\2\2\2\u00e6\u00e7\7E\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee\7e\2\2\u00ee\u00ef")
        buf.write("\7v\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1\7t\2\2\u00f1\36")
        buf.write("\3\2\2\2\u00f2\u00f3\7F\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7u\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8")
        buf.write("\7w\2\2\u00f8\u00f9\7e\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7q\2\2\u00fb\u00fc\7t\2\2\u00fc \3\2\2\2\u00fd\u00fe")
        buf.write("\7E\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100\7c\2\2\u0100\u0101")
        buf.write("\7u\2\2\u0101\u0102\7u\2\2\u0102\"\3\2\2\2\u0103\u0106")
        buf.write("\5C\"\2\u0104\u0106\59\35\2\u0105\u0103\3\2\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\5G$\2\u0108")
        buf.write("\u011a\3\2\2\2\u0109\u010c\5C\"\2\u010a\u010c\59\35\2")
        buf.write("\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c\u010d\3")
        buf.write("\2\2\2\u010d\u010e\5%\23\2\u010e\u011a\3\2\2\2\u010f\u0110")
        buf.write("\5%\23\2\u0110\u0111\5G$\2\u0111\u011a\3\2\2\2\u0112\u0115")
        buf.write("\5C\"\2\u0113\u0115\59\35\2\u0114\u0112\3\2\2\2\u0114")
        buf.write("\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\5%\23\2")
        buf.write("\u0117\u0118\5G$\2\u0118\u011a\3\2\2\2\u0119\u0105\3\2")
        buf.write("\2\2\u0119\u010b\3\2\2\2\u0119\u010f\3\2\2\2\u0119\u0114")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\b\22\3\2\u011c")
        buf.write("$\3\2\2\2\u011d\u0128\5M\'\2\u011e\u0120\59\35\2\u011f")
        buf.write("\u011e\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f\3\2\2\2")
        buf.write("\u0121\u0122\3\2\2\2\u0122\u0126\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0124\u0127\5C\"\2\u0125\u0127\59\35\2\u0126\u0124")
        buf.write("\3\2\2\2\u0126\u0125\3\2\2\2\u0127\u0129\3\2\2\2\u0128")
        buf.write("\u0121\3\2\2\2\u0128\u0129\3\2\2\2\u0129&\3\2\2\2\u012a")
        buf.write("\u012b\7D\2\2\u012b\u012c\7{\2\2\u012c(\3\2\2\2\u012d")
        buf.write("\u012e\7V\2\2\u012e\u012f\7t\2\2\u012f\u0130\7w\2\2\u0130")
        buf.write("\u0137\7g\2\2\u0131\u0132\7H\2\2\u0132\u0133\7c\2\2\u0133")
        buf.write("\u0134\7n\2\2\u0134\u0135\7u\2\2\u0135\u0137\7g\2\2\u0136")
        buf.write("\u012d\3\2\2\2\u0136\u0131\3\2\2\2\u0137*\3\2\2\2\u0138")
        buf.write("\u0139\7X\2\2\u0139\u013a\7c\2\2\u013a\u013f\7n\2\2\u013b")
        buf.write("\u013c\7X\2\2\u013c\u013d\7c\2\2\u013d\u013f\7t\2\2\u013e")
        buf.write("\u0138\3\2\2\2\u013e\u013b\3\2\2\2\u013f,\3\2\2\2\u0140")
        buf.write("\u0141\7C\2\2\u0141\u0142\7t\2\2\u0142\u0143\7t\2\2\u0143")
        buf.write("\u0144\7c\2\2\u0144\u0145\7{\2\2\u0145.\3\2\2\2\u0146")
        buf.write("\u0147\7K\2\2\u0147\u0148\7p\2\2\u0148\u0149\7v\2\2\u0149")
        buf.write("\60\3\2\2\2\u014a\u014b\7H\2\2\u014b\u014c\7n\2\2\u014c")
        buf.write("\u014d\7q\2\2\u014d\u014e\7c\2\2\u014e\u014f\7v\2\2\u014f")
        buf.write("\62\3\2\2\2\u0150\u0151\7D\2\2\u0151\u0152\7q\2\2\u0152")
        buf.write("\u0153\7q\2\2\u0153\u0154\7n\2\2\u0154\u0155\7g\2\2\u0155")
        buf.write("\u0156\7c\2\2\u0156\u0157\7p\2\2\u0157\64\3\2\2\2\u0158")
        buf.write("\u0159\7\62\2\2\u0159\u015a\t\5\2\2\u015a\u015b\7\62\2")
        buf.write("\2\u015b\66\3\2\2\2\u015c\u015d\7\62\2\2\u015d\u015e\7")
        buf.write("\62\2\2\u015e8\3\2\2\2\u015f\u0160\7\62\2\2\u0160:\3\2")
        buf.write("\2\2\u0161\u0162\7\62\2\2\u0162\u0163\t\6\2\2\u0163\u0164")
        buf.write("\7\62\2\2\u0164<\3\2\2\2\u0165\u0166\7\62\2\2\u0166\u0167")
        buf.write("\t\6\2\2\u0167\u0173\t\7\2\2\u0168\u0169\7\62\2\2\u0169")
        buf.write("\u016a\t\6\2\2\u016a\u016e\t\7\2\2\u016b\u016d\t\b\2\2")
        buf.write("\u016c\u016b\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3")
        buf.write("\2\2\2\u016e\u016f\3\2\2\2\u016f\u0171\3\2\2\2\u0170\u016e")
        buf.write("\3\2\2\2\u0171\u0173\t\t\2\2\u0172\u0165\3\2\2\2\u0172")
        buf.write("\u0168\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\b\37\4")
        buf.write("\2\u0175>\3\2\2\2\u0176\u0177\7\62\2\2\u0177\u0178\t\5")
        buf.write("\2\2\u0178\u0184\7\63\2\2\u0179\u017a\7\62\2\2\u017a\u017b")
        buf.write("\t\5\2\2\u017b\u017f\7\63\2\2\u017c\u017e\t\n\2\2\u017d")
        buf.write("\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u017f\3")
        buf.write("\2\2\2\u0182\u0184\t\13\2\2\u0183\u0176\3\2\2\2\u0183")
        buf.write("\u0179\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\b \5\2")
        buf.write("\u0186@\3\2\2\2\u0187\u0188\7\62\2\2\u0188\u0193\t\f\2")
        buf.write("\2\u0189\u018a\7\62\2\2\u018a\u018e\t\f\2\2\u018b\u018d")
        buf.write("\t\r\2\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0191\3\2\2\2")
        buf.write("\u0190\u018e\3\2\2\2\u0191\u0193\t\16\2\2\u0192\u0187")
        buf.write("\3\2\2\2\u0192\u0189\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("\u0195\b!\6\2\u0195B\3\2\2\2\u0196\u0198\t\17\2\2\u0197")
        buf.write("\u0199\7a\2\2\u0198\u0197\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u01a0\3\2\2\2\u019a\u019c\t\20\2\2\u019b\u019d")
        buf.write("\7a\2\2\u019c\u019b\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u019f\3\2\2\2\u019e\u019a\3\2\2\2\u019f\u01a2\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a3\3")
        buf.write("\2\2\2\u01a2\u01a0\3\2\2\2\u01a3\u01a6\t\20\2\2\u01a4")
        buf.write("\u01a6\t\17\2\2\u01a5\u0196\3\2\2\2\u01a5\u01a4\3\2\2")
        buf.write("\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\b\"\7\2\u01a8D\3\2")
        buf.write("\2\2\u01a9\u01aa\t\21\2\2\u01aaF\3\2\2\2\u01ab\u01ad\t")
        buf.write("\22\2\2\u01ac\u01ae\t\23\2\2\u01ad\u01ac\3\2\2\2\u01ad")
        buf.write("\u01ae\3\2\2\2\u01ae\u01b2\3\2\2\2\u01af\u01b1\7\62\2")
        buf.write("\2\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b7\3\2\2\2\u01b4")
        buf.write("\u01b2\3\2\2\2\u01b5\u01b8\5C\"\2\u01b6\u01b8\7\62\2\2")
        buf.write("\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8H\3\2\2")
        buf.write("\2\u01b9\u01bb\7&\2\2\u01ba\u01bc\t\24\2\2\u01bb\u01ba")
        buf.write("\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd")
        buf.write("\u01be\3\2\2\2\u01beJ\3\2\2\2\u01bf\u01c3\t\21\2\2\u01c0")
        buf.write("\u01c2\t\24\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2")
        buf.write("\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4L\3\2")
        buf.write("\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\7\60\2\2\u01c7N\3")
        buf.write("\2\2\2\u01c8\u01c9\7.\2\2\u01c9P\3\2\2\2\u01ca\u01cb\7")
        buf.write("]\2\2\u01cbR\3\2\2\2\u01cc\u01cd\7_\2\2\u01cdT\3\2\2\2")
        buf.write("\u01ce\u01cf\7*\2\2\u01cfV\3\2\2\2\u01d0\u01d1\7+\2\2")
        buf.write("\u01d1X\3\2\2\2\u01d2\u01d3\7}\2\2\u01d3Z\3\2\2\2\u01d4")
        buf.write("\u01d5\7\177\2\2\u01d5\\\3\2\2\2\u01d6\u01d7\7\60\2\2")
        buf.write("\u01d7\u01d8\7\60\2\2\u01d8^\3\2\2\2\u01d9\u01da\7<\2")
        buf.write("\2\u01da`\3\2\2\2\u01db\u01dc\7=\2\2\u01dcb\3\2\2\2\u01dd")
        buf.write("\u01de\7-\2\2\u01ded\3\2\2\2\u01df\u01e0\7>\2\2\u01e0")
        buf.write("\u01e1\7?\2\2\u01e1f\3\2\2\2\u01e2\u01e3\7@\2\2\u01e3")
        buf.write("\u01e4\7?\2\2\u01e4h\3\2\2\2\u01e5\u01e6\7/\2\2\u01e6")
        buf.write("j\3\2\2\2\u01e7\u01e8\7,\2\2\u01e8l\3\2\2\2\u01e9\u01ea")
        buf.write("\7>\2\2\u01ean\3\2\2\2\u01eb\u01ec\7\'\2\2\u01ecp\3\2")
        buf.write("\2\2\u01ed\u01ee\7\61\2\2\u01eer\3\2\2\2\u01ef\u01f0\7")
        buf.write("#\2\2\u01f0\u01f1\7?\2\2\u01f1t\3\2\2\2\u01f2\u01f3\7")
        buf.write("?\2\2\u01f3\u01f4\7?\2\2\u01f4v\3\2\2\2\u01f5\u01f6\7")
        buf.write("@\2\2\u01f6x\3\2\2\2\u01f7\u01f8\7(\2\2\u01f8\u01f9\7")
        buf.write("(\2\2\u01f9z\3\2\2\2\u01fa\u01fb\7~\2\2\u01fb\u01fc\7")
        buf.write("~\2\2\u01fc|\3\2\2\2\u01fd\u01fe\7#\2\2\u01fe~\3\2\2\2")
        buf.write("\u01ff\u0200\7?\2\2\u0200\u0201\7?\2\2\u0201\u0202\7\60")
        buf.write("\2\2\u0202\u0080\3\2\2\2\u0203\u0204\7-\2\2\u0204\u0205")
        buf.write("\7\60\2\2\u0205\u0082\3\2\2\2\u0206\u0207\7%\2\2\u0207")
        buf.write("\u0208\7%\2\2\u0208\u020c\3\2\2\2\u0209\u020b\13\2\2\2")
        buf.write("\u020a\u0209\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020d\3")
        buf.write("\2\2\2\u020c\u020a\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u020c")
        buf.write("\3\2\2\2\u020f\u0210\7%\2\2\u0210\u0211\7%\2\2\u0211\u0212")
        buf.write("\3\2\2\2\u0212\u0213\bB\b\2\u0213\u0084\3\2\2\2\u0214")
        buf.write("\u0216\t\25\2\2\u0215\u0214\3\2\2\2\u0216\u0217\3\2\2")
        buf.write("\2\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0219")
        buf.write("\3\2\2\2\u0219\u021a\bC\b\2\u021a\u0086\3\2\2\2\u021b")
        buf.write("\u0221\7$\2\2\u021c\u021d\7^\2\2\u021d\u0220\t\2\2\2\u021e")
        buf.write("\u0220\n\26\2\2\u021f\u021c\3\2\2\2\u021f\u021e\3\2\2")
        buf.write("\2\u0220\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222\u0224\3\2\2\2\u0223\u0221\3\2\2\2\u0224")
        buf.write("\u0225\7^\2\2\u0225\u0226\n\2\2\2\u0226\u0227\3\2\2\2")
        buf.write("\u0227\u0228\bD\t\2\u0228\u0088\3\2\2\2\u0229\u0231\7")
        buf.write("$\2\2\u022a\u022b\7)\2\2\u022b\u0230\7$\2\2\u022c\u022d")
        buf.write("\7^\2\2\u022d\u0230\t\2\2\2\u022e\u0230\n\3\2\2\u022f")
        buf.write("\u022a\3\2\2\2\u022f\u022c\3\2\2\2\u022f\u022e\3\2\2\2")
        buf.write("\u0230\u0233\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232\3")
        buf.write("\2\2\2\u0232\u0234\3\2\2\2\u0233\u0231\3\2\2\2\u0234\u0235")
        buf.write("\bE\n\2\u0235\u008a\3\2\2\2\u0236\u0237\13\2\2\2\u0237")
        buf.write("\u0238\bF\13\2\u0238\u008c\3\2\2\2%\2\u0095\u0097\u009f")
        buf.write("\u00a2\u0105\u010b\u0114\u0119\u0121\u0126\u0128\u0136")
        buf.write("\u013e\u016e\u0172\u017f\u0183\u018e\u0192\u0198\u019c")
        buf.write("\u01a0\u01a5\u01ad\u01b2\u01b7\u01bd\u01c3\u020c\u0217")
        buf.write("\u021f\u0221\u022f\u0231\f\3\2\2\3\22\3\3\37\4\3 \5\3")
        buf.write("!\6\3\"\7\b\2\2\3D\b\3E\t\3F\n")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRINGLIT = 1
    MEM_ACCESS_OP = 2
    STRING_TYPE = 3
    NEW = 4
    RETURN = 5
    ASSIGN_OP = 6
    BREAK = 7
    CONTINUE = 8
    IF = 9
    ELSE = 10
    ELSEIF = 11
    FOREACH = 12
    IN = 13
    CONSTRUCTOR = 14
    DESTRUCTOR = 15
    CLASS = 16
    FLOATLIT = 17
    BY = 18
    BOOLIT = 19
    VAL_VAR = 20
    ARRAY = 21
    INT_TYPE = 22
    FLOAT_TYPE = 23
    BOOL_TYPE = 24
    ZERO_2 = 25
    ZERO_8 = 26
    ZERO_10 = 27
    ZERO_16 = 28
    INTLIT_16 = 29
    INTLIT_2 = 30
    INTLIT_8 = 31
    INTLIT_10 = 32
    DOLLAR_ID = 33
    ID = 34
    DOT = 35
    CM = 36
    LS = 37
    RS = 38
    LB = 39
    RB = 40
    LP = 41
    RP = 42
    RANGE = 43
    CL = 44
    SEMI = 45
    ADDOP = 46
    LESS_EQUAL = 47
    GREAT_EQUAL = 48
    SUBOP = 49
    MULOP = 50
    LESS_THAN = 51
    MODOP = 52
    DIVOP = 53
    NOT_EQUAL = 54
    EQUAL = 55
    GREAT_THAN = 56
    AND = 57
    OR = 58
    NEGATE = 59
    STR_CMP = 60
    STR_CONCAT = 61
    COMMENT = 62
    WS = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSED_STRING = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'::'", "'String'", "'New'", "'Return'", "'='", "'Break'", "'Continue'", 
            "'If'", "'Else'", "'Elseif'", "'Foreach'", "'In'", "'Constructor'", 
            "'Destructor'", "'Class'", "'By'", "'Array'", "'Int'", "'Float'", 
            "'Boolean'", "'00'", "'0'", "'.'", "','", "'['", "']'", "'('", 
            "')'", "'{'", "'}'", "'..'", "':'", "';'", "'+'", "'<='", "'>='", 
            "'-'", "'*'", "'<'", "'%'", "'/'", "'!='", "'=='", "'>'", "'&&'", 
            "'||'", "'!'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>",
            "STRINGLIT", "MEM_ACCESS_OP", "STRING_TYPE", "NEW", "RETURN", 
            "ASSIGN_OP", "BREAK", "CONTINUE", "IF", "ELSE", "ELSEIF", "FOREACH", 
            "IN", "CONSTRUCTOR", "DESTRUCTOR", "CLASS", "FLOATLIT", "BY", 
            "BOOLIT", "VAL_VAR", "ARRAY", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
            "ZERO_2", "ZERO_8", "ZERO_10", "ZERO_16", "INTLIT_16", "INTLIT_2", 
            "INTLIT_8", "INTLIT_10", "DOLLAR_ID", "ID", "DOT", "CM", "LS", 
            "RS", "LB", "RB", "LP", "RP", "RANGE", "CL", "SEMI", "ADDOP", 
            "LESS_EQUAL", "GREAT_EQUAL", "SUBOP", "MULOP", "LESS_THAN", 
            "MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", "GREAT_THAN", "AND", 
            "OR", "NEGATE", "STR_CMP", "STR_CONCAT", "COMMENT", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSED_STRING", "ERROR_CHAR" ]

    ruleNames = [ "STRINGLIT", "MEM_ACCESS_OP", "STRING_TYPE", "NEW", "RETURN", 
                  "ASSIGN_OP", "BREAK", "CONTINUE", "IF", "ELSE", "ELSEIF", 
                  "FOREACH", "IN", "CONSTRUCTOR", "DESTRUCTOR", "CLASS", 
                  "FLOATLIT", "DECIMAL", "BY", "BOOLIT", "VAL_VAR", "ARRAY", 
                  "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", "ZERO_2", "ZERO_8", 
                  "ZERO_10", "ZERO_16", "INTLIT_16", "INTLIT_2", "INTLIT_8", 
                  "INTLIT_10", "LIT", "EXPONENT", "DOLLAR_ID", "ID", "DOT", 
                  "CM", "LS", "RS", "LB", "RB", "LP", "RP", "RANGE", "CL", 
                  "SEMI", "ADDOP", "LESS_EQUAL", "GREAT_EQUAL", "SUBOP", 
                  "MULOP", "LESS_THAN", "MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", 
                  "GREAT_THAN", "AND", "OR", "NEGATE", "STR_CMP", "STR_CONCAT", 
                  "COMMENT", "WS", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", 
                  "ERROR_CHAR" ]

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
            actions[0] = self.STRINGLIT_action 
            actions[16] = self.FLOATLIT_action 
            actions[29] = self.INTLIT_16_action 
            actions[30] = self.INTLIT_2_action 
            actions[31] = self.INTLIT_8_action 
            actions[32] = self.INTLIT_10_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.UNCLOSED_STRING_action 
            actions[68] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def INTLIT_16_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace("_","")
     

    def INTLIT_2_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text.replace("_","")
     

    def INTLIT_8_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace("_","")
     

    def INTLIT_10_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = self.text.replace("_","")
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            self.text = self.text[1:]; raise UncloseString(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            raise ErrorToken(self.text)
     


