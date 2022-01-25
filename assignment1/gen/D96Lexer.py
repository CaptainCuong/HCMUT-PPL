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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01ad\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\3")
        buf.write("\2\7\2\u0087\n\2\f\2\16\2\u008a\13\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00f3\n\23\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\5\24\u00fb\n\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\6\33\u011f\n\33\r\33\16\33\u0120")
        buf.write("\3\34\3\34\6\34\u0125\n\34\r\34\16\34\u0126\3\35\3\35")
        buf.write("\5\35\u012b\n\35\3\35\3\35\5\35\u012f\n\35\7\35\u0131")
        buf.write("\n\35\f\35\16\35\u0134\13\35\3\35\3\35\5\35\u0138\n\35")
        buf.write("\3\36\3\36\3\37\3\37\5\37\u013e\n\37\3\37\7\37\u0141\n")
        buf.write("\37\f\37\16\37\u0144\13\37\3\37\3\37\3 \3 \3!\3!\3!\3")
        buf.write("\"\3\"\3\"\7\"\u0150\n\"\f\"\16\"\u0153\13\"\3#\3#\3$")
        buf.write("\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,")
        buf.write("\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\3\67\38\38\38\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3=\3")
        buf.write("=\3=\3=\3>\3>\3>\3?\6?\u0198\n?\r?\16?\u0199\3?\3?\3@")
        buf.write("\3@\3@\3@\5@\u01a2\n@\7@\u01a4\n@\f@\16@\u01a7\13@\3@")
        buf.write("\3@\3@\3@\3@\2\2A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\2=\37? ")
        buf.write("A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60a\61c\62e\63g\64i")
        buf.write("\65k\66m\67o8q9s:u;w<y={>}?\177@\3\2\21\t\2))^^ddhhpp")
        buf.write("ttvv\6\2\13\f\17\17$$^^\4\2ZZzz\4\2\62;CH\3\2\62\63\3")
        buf.write("\2\629\3\2\63;\3\2\62;\5\2C\\aac|\4\2GGgg\4\2--//\5\2")
        buf.write("\13\f\17\17\"\"\t\2$$^^ddhhppttvv\5\2\f\f$$^^\b\2^^dd")
        buf.write("hhppttvv\2\u01bd\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2")
        buf.write("\2\5\u008d\3\2\2\2\7\u0090\3\2\2\2\t\u0094\3\2\2\2\13")
        buf.write("\u009b\3\2\2\2\r\u009e\3\2\2\2\17\u00a0\3\2\2\2\21\u00a6")
        buf.write("\3\2\2\2\23\u00af\3\2\2\2\25\u00b2\3\2\2\2\27\u00b7\3")
        buf.write("\2\2\2\31\u00be\3\2\2\2\33\u00c6\3\2\2\2\35\u00c9\3\2")
        buf.write("\2\2\37\u00d5\3\2\2\2!\u00e0\3\2\2\2#\u00e6\3\2\2\2%\u00f2")
        buf.write("\3\2\2\2\'\u00fa\3\2\2\2)\u00fc\3\2\2\2+\u00fe\3\2\2\2")
        buf.write("-\u0104\3\2\2\2/\u0108\3\2\2\2\61\u010e\3\2\2\2\63\u0116")
        buf.write("\3\2\2\2\65\u011a\3\2\2\2\67\u0122\3\2\2\29\u0137\3\2")
        buf.write("\2\2;\u0139\3\2\2\2=\u013b\3\2\2\2?\u0147\3\2\2\2A\u0149")
        buf.write("\3\2\2\2C\u014c\3\2\2\2E\u0154\3\2\2\2G\u0156\3\2\2\2")
        buf.write("I\u0158\3\2\2\2K\u015a\3\2\2\2M\u015c\3\2\2\2O\u015e\3")
        buf.write("\2\2\2Q\u0160\3\2\2\2S\u0162\3\2\2\2U\u0164\3\2\2\2W\u0166")
        buf.write("\3\2\2\2Y\u0169\3\2\2\2[\u016b\3\2\2\2]\u016d\3\2\2\2")
        buf.write("_\u016f\3\2\2\2a\u0172\3\2\2\2c\u0175\3\2\2\2e\u0177\3")
        buf.write("\2\2\2g\u0179\3\2\2\2i\u017b\3\2\2\2k\u017d\3\2\2\2m\u017f")
        buf.write("\3\2\2\2o\u0182\3\2\2\2q\u0185\3\2\2\2s\u0187\3\2\2\2")
        buf.write("u\u018a\3\2\2\2w\u018d\3\2\2\2y\u018f\3\2\2\2{\u0193\3")
        buf.write("\2\2\2}\u0197\3\2\2\2\177\u019d\3\2\2\2\u0081\u0088\5")
        buf.write("? \2\u0082\u0087\5A!\2\u0083\u0084\7^\2\2\u0084\u0087")
        buf.write("\t\2\2\2\u0085\u0087\n\3\2\2\u0086\u0082\3\2\2\2\u0086")
        buf.write("\u0083\3\2\2\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2")
        buf.write("\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\3")
        buf.write("\2\2\2\u008a\u0088\3\2\2\2\u008b\u008c\5? \2\u008c\4\3")
        buf.write("\2\2\2\u008d\u008e\7<\2\2\u008e\u008f\7<\2\2\u008f\6\3")
        buf.write("\2\2\2\u0090\u0091\7P\2\2\u0091\u0092\7g\2\2\u0092\u0093")
        buf.write("\7y\2\2\u0093\b\3\2\2\2\u0094\u0095\7T\2\2\u0095\u0096")
        buf.write("\7g\2\2\u0096\u0097\7v\2\2\u0097\u0098\7w\2\2\u0098\u0099")
        buf.write("\7t\2\2\u0099\u009a\7p\2\2\u009a\n\3\2\2\2\u009b\u009c")
        buf.write("\7%\2\2\u009c\u009d\7%\2\2\u009d\f\3\2\2\2\u009e\u009f")
        buf.write("\7?\2\2\u009f\16\3\2\2\2\u00a0\u00a1\7D\2\2\u00a1\u00a2")
        buf.write("\7t\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7m\2\2\u00a5\20\3\2\2\2\u00a6\u00a7\7E\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab")
        buf.write("\7k\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\22\3\2\2\2\u00af\u00b0\7K\2\2\u00b0\u00b1")
        buf.write("\7h\2\2\u00b1\24\3\2\2\2\u00b2\u00b3\7G\2\2\u00b3\u00b4")
        buf.write("\7n\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6\7g\2\2\u00b6\26")
        buf.write("\3\2\2\2\u00b7\u00b8\7G\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba")
        buf.write("\7u\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd")
        buf.write("\7h\2\2\u00bd\30\3\2\2\2\u00be\u00bf\7H\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7j\2\2\u00c5\32")
        buf.write("\3\2\2\2\u00c6\u00c7\7K\2\2\u00c7\u00c8\7p\2\2\u00c8\34")
        buf.write("\3\2\2\2\u00c9\u00ca\7E\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf")
        buf.write("\7t\2\2\u00cf\u00d0\7w\2\2\u00d0\u00d1\7e\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7t\2\2\u00d4\36")
        buf.write("\3\2\2\2\u00d5\u00d6\7F\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8")
        buf.write("\7u\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7t\2\2\u00da\u00db")
        buf.write("\7w\2\2\u00db\u00dc\7e\2\2\u00dc\u00dd\7v\2\2\u00dd\u00de")
        buf.write("\7q\2\2\u00de\u00df\7t\2\2\u00df \3\2\2\2\u00e0\u00e1")
        buf.write("\7E\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4")
        buf.write("\7u\2\2\u00e4\u00e5\7u\2\2\u00e5\"\3\2\2\2\u00e6\u00e7")
        buf.write("\7D\2\2\u00e7\u00e8\7{\2\2\u00e8$\3\2\2\2\u00e9\u00ea")
        buf.write("\7V\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7w\2\2\u00ec\u00f3")
        buf.write("\7g\2\2\u00ed\u00ee\7H\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0")
        buf.write("\7n\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f3\7g\2\2\u00f2\u00e9")
        buf.write("\3\2\2\2\u00f2\u00ed\3\2\2\2\u00f3&\3\2\2\2\u00f4\u00f5")
        buf.write("\7X\2\2\u00f5\u00f6\7c\2\2\u00f6\u00fb\7n\2\2\u00f7\u00f8")
        buf.write("\7X\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fb\7t\2\2\u00fa\u00f4")
        buf.write("\3\2\2\2\u00fa\u00f7\3\2\2\2\u00fb(\3\2\2\2\u00fc\u00fd")
        buf.write("\7&\2\2\u00fd*\3\2\2\2\u00fe\u00ff\7C\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7t\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7{\2\2\u0103,\3\2\2\2\u0104\u0105\7K\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106\u0107\7v\2\2\u0107.\3\2\2\2\u0108\u0109")
        buf.write("\7H\2\2\u0109\u010a\7n\2\2\u010a\u010b\7q\2\2\u010b\u010c")
        buf.write("\7c\2\2\u010c\u010d\7v\2\2\u010d\60\3\2\2\2\u010e\u010f")
        buf.write("\7D\2\2\u010f\u0110\7q\2\2\u0110\u0111\7q\2\2\u0111\u0112")
        buf.write("\7n\2\2\u0112\u0113\7g\2\2\u0113\u0114\7c\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115\62\3\2\2\2\u0116\u0117\7\62\2\2\u0117\u0118")
        buf.write("\t\4\2\2\u0118\u0119\t\5\2\2\u0119\64\3\2\2\2\u011a\u011b")
        buf.write("\7\62\2\2\u011b\u011c\7d\2\2\u011c\u011e\3\2\2\2\u011d")
        buf.write("\u011f\t\6\2\2\u011e\u011d\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\66\3\2")
        buf.write("\2\2\u0122\u0124\7\62\2\2\u0123\u0125\t\7\2\2\u0124\u0123")
        buf.write("\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0124\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u01278\3\2\2\2\u0128\u012a\t\b\2\2\u0129")
        buf.write("\u012b\7a\2\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u0132\3\2\2\2\u012c\u012e\t\t\2\2\u012d\u012f\7")
        buf.write("a\2\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0131")
        buf.write("\3\2\2\2\u0130\u012c\3\2\2\2\u0131\u0134\3\2\2\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0135\3\2\2\2")
        buf.write("\u0134\u0132\3\2\2\2\u0135\u0138\t\t\2\2\u0136\u0138\t")
        buf.write("\t\2\2\u0137\u0128\3\2\2\2\u0137\u0136\3\2\2\2\u0138:")
        buf.write("\3\2\2\2\u0139\u013a\t\n\2\2\u013a<\3\2\2\2\u013b\u013d")
        buf.write("\t\13\2\2\u013c\u013e\t\f\2\2\u013d\u013c\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013e\u0142\3\2\2\2\u013f\u0141\7\62\2")
        buf.write("\2\u0140\u013f\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140")
        buf.write("\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0145\u0146\59\35\2\u0146>\3\2\2\2\u0147")
        buf.write("\u0148\7$\2\2\u0148@\3\2\2\2\u0149\u014a\7)\2\2\u014a")
        buf.write("\u014b\7$\2\2\u014bB\3\2\2\2\u014c\u0151\5;\36\2\u014d")
        buf.write("\u0150\t\t\2\2\u014e\u0150\5;\36\2\u014f\u014d\3\2\2\2")
        buf.write("\u014f\u014e\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3")
        buf.write("\2\2\2\u0151\u0152\3\2\2\2\u0152D\3\2\2\2\u0153\u0151")
        buf.write("\3\2\2\2\u0154\u0155\7\62\2\2\u0155F\3\2\2\2\u0156\u0157")
        buf.write("\7\60\2\2\u0157H\3\2\2\2\u0158\u0159\7.\2\2\u0159J\3\2")
        buf.write("\2\2\u015a\u015b\7]\2\2\u015bL\3\2\2\2\u015c\u015d\7_")
        buf.write("\2\2\u015dN\3\2\2\2\u015e\u015f\7*\2\2\u015fP\3\2\2\2")
        buf.write("\u0160\u0161\7+\2\2\u0161R\3\2\2\2\u0162\u0163\7}\2\2")
        buf.write("\u0163T\3\2\2\2\u0164\u0165\7\177\2\2\u0165V\3\2\2\2\u0166")
        buf.write("\u0167\7\60\2\2\u0167\u0168\7\60\2\2\u0168X\3\2\2\2\u0169")
        buf.write("\u016a\7<\2\2\u016aZ\3\2\2\2\u016b\u016c\7=\2\2\u016c")
        buf.write("\\\3\2\2\2\u016d\u016e\7-\2\2\u016e^\3\2\2\2\u016f\u0170")
        buf.write("\7>\2\2\u0170\u0171\7?\2\2\u0171`\3\2\2\2\u0172\u0173")
        buf.write("\7@\2\2\u0173\u0174\7?\2\2\u0174b\3\2\2\2\u0175\u0176")
        buf.write("\7/\2\2\u0176d\3\2\2\2\u0177\u0178\7,\2\2\u0178f\3\2\2")
        buf.write("\2\u0179\u017a\7>\2\2\u017ah\3\2\2\2\u017b\u017c\7\'\2")
        buf.write("\2\u017cj\3\2\2\2\u017d\u017e\7\61\2\2\u017el\3\2\2\2")
        buf.write("\u017f\u0180\7#\2\2\u0180\u0181\7?\2\2\u0181n\3\2\2\2")
        buf.write("\u0182\u0183\7?\2\2\u0183\u0184\7?\2\2\u0184p\3\2\2\2")
        buf.write("\u0185\u0186\7@\2\2\u0186r\3\2\2\2\u0187\u0188\7(\2\2")
        buf.write("\u0188\u0189\7(\2\2\u0189t\3\2\2\2\u018a\u018b\7~\2\2")
        buf.write("\u018b\u018c\7~\2\2\u018cv\3\2\2\2\u018d\u018e\7#\2\2")
        buf.write("\u018ex\3\2\2\2\u018f\u0190\7?\2\2\u0190\u0191\7?\2\2")
        buf.write("\u0191\u0192\7\60\2\2\u0192z\3\2\2\2\u0193\u0194\7-\2")
        buf.write("\2\u0194\u0195\7\60\2\2\u0195|\3\2\2\2\u0196\u0198\t\r")
        buf.write("\2\2\u0197\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\3\2\2\2\u019b")
        buf.write("\u019c\b?\2\2\u019c~\3\2\2\2\u019d\u01a5\7$\2\2\u019e")
        buf.write("\u019f\7^\2\2\u019f\u01a2\t\16\2\2\u01a0\u01a2\n\17\2")
        buf.write("\2\u01a1\u019e\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a4")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a8\3\2\2\2")
        buf.write("\u01a7\u01a5\3\2\2\2\u01a8\u01a9\7^\2\2\u01a9\u01aa\n")
        buf.write("\20\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\b@\3\2\u01ac\u0080")
        buf.write("\3\2\2\2\24\2\u0086\u0088\u00f2\u00fa\u0120\u0126\u012a")
        buf.write("\u012e\u0132\u0137\u013d\u0142\u014f\u0151\u0199\u01a1")
        buf.write("\u01a5\4\b\2\2\3@\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRINGLIT = 1
    MEM_ACCESS_OP = 2
    NEW = 3
    RETURN = 4
    DOUB_HASH_MARK = 5
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
    BY = 17
    BOOLIT = 18
    VAL_VAR = 19
    STATIC = 20
    ARRAY = 21
    INT_TYPE = 22
    FLOAT_TYPE = 23
    BOOL_TYPE = 24
    INTLIT_16 = 25
    INTLIT_2 = 26
    INTLIT_8 = 27
    INTLIT_10 = 28
    EXPONENT = 29
    START_END_STRING = 30
    DOUB_QUOTE = 31
    ID = 32
    ZERO = 33
    DOT = 34
    CM = 35
    LS = 36
    RS = 37
    LB = 38
    RB = 39
    LP = 40
    RP = 41
    RANGE = 42
    CL = 43
    SEMI = 44
    ADDOP = 45
    LESS_EQUAL = 46
    GREAT_EQUAL = 47
    SUBOP = 48
    MULOP = 49
    LESS_THAN = 50
    MODOP = 51
    DIVOP = 52
    NOT_EQUAL = 53
    EQUAL = 54
    GREAT_THAN = 55
    AND = 56
    OR = 57
    NEGATE = 58
    STR_CMP = 59
    STR_CONCAT = 60
    WS = 61
    ILLEGAL_ESCAPE = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'::'", "'New'", "'Return'", "'##'", "'='", "'Break'", "'Continue'", 
            "'If'", "'Else'", "'Elseif'", "'Foreach'", "'In'", "'Constructor'", 
            "'Destructor'", "'Class'", "'By'", "'$'", "'Array'", "'Int'", 
            "'Float'", "'Boolean'", "'\"'", "''\"'", "'0'", "'.'", "','", 
            "'['", "']'", "'('", "')'", "'{'", "'}'", "'..'", "':'", "';'", 
            "'+'", "'<='", "'>='", "'-'", "'*'", "'<'", "'%'", "'/'", "'!='", 
            "'=='", "'>'", "'&&'", "'||'", "'!'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>",
            "STRINGLIT", "MEM_ACCESS_OP", "NEW", "RETURN", "DOUB_HASH_MARK", 
            "ASSIGN_OP", "BREAK", "CONTINUE", "IF", "ELSE", "ELSEIF", "FOREACH", 
            "IN", "CONSTRUCTOR", "DESTRUCTOR", "CLASS", "BY", "BOOLIT", 
            "VAL_VAR", "STATIC", "ARRAY", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
            "INTLIT_16", "INTLIT_2", "INTLIT_8", "INTLIT_10", "EXPONENT", 
            "START_END_STRING", "DOUB_QUOTE", "ID", "ZERO", "DOT", "CM", 
            "LS", "RS", "LB", "RB", "LP", "RP", "RANGE", "CL", "SEMI", "ADDOP", 
            "LESS_EQUAL", "GREAT_EQUAL", "SUBOP", "MULOP", "LESS_THAN", 
            "MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", "GREAT_THAN", "AND", 
            "OR", "NEGATE", "STR_CMP", "STR_CONCAT", "WS", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "STRINGLIT", "MEM_ACCESS_OP", "NEW", "RETURN", "DOUB_HASH_MARK", 
                  "ASSIGN_OP", "BREAK", "CONTINUE", "IF", "ELSE", "ELSEIF", 
                  "FOREACH", "IN", "CONSTRUCTOR", "DESTRUCTOR", "CLASS", 
                  "BY", "BOOLIT", "VAL_VAR", "STATIC", "ARRAY", "INT_TYPE", 
                  "FLOAT_TYPE", "BOOL_TYPE", "INTLIT_16", "INTLIT_2", "INTLIT_8", 
                  "INTLIT_10", "LIT", "EXPONENT", "START_END_STRING", "DOUB_QUOTE", 
                  "ID", "ZERO", "DOT", "CM", "LS", "RS", "LB", "RB", "LP", 
                  "RP", "RANGE", "CL", "SEMI", "ADDOP", "LESS_EQUAL", "GREAT_EQUAL", 
                  "SUBOP", "MULOP", "LESS_THAN", "MODOP", "DIVOP", "NOT_EQUAL", 
                  "EQUAL", "GREAT_THAN", "AND", "OR", "NEGATE", "STR_CMP", 
                  "STR_CONCAT", "WS", "ILLEGAL_ESCAPE" ]

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
            actions[62] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise IllegalEscape(self.text)
     


