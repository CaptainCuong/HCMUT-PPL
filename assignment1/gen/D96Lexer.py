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
        buf.write("\u019e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\7\21\u00de\n\21\f\21\16\21\u00e1\13\21\3\21")
        buf.write("\5\21\u00e4\n\21\3\21\3\21\3\21\5\21\u00e9\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00f4\n\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00fc\n\23\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\6\32\u0120\n\32\r\32\16\32\u0121\3\33\3\33\6\33\u0126")
        buf.write("\n\33\r\33\16\33\u0127\3\34\3\34\7\34\u012c\n\34\f\34")
        buf.write("\16\34\u012f\13\34\3\34\3\34\5\34\u0133\n\34\3\35\3\35")
        buf.write("\3\36\3\36\5\36\u0139\n\36\3\36\7\36\u013c\n\36\f\36\16")
        buf.write("\36\u013f\13\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\7!\u014b\n!\f!\16!\u014e\13!\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\38\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3=\3=\3=")
        buf.write("\3=\3>\3>\3>\3?\6?\u0196\n?\r?\16?\u0197\3?\3?\3@\3@\3")
        buf.write("@\2\2A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\2;\36=\37? A!C\"E#G$I%K")
        buf.write("&M\'O(Q)S*U+W,Y-[.]/_\60a\61c\62e\63g\64i\65k\66m\67o")
        buf.write("8q9s:u;w<y={>}?\177@\3\2\r\4\2ZZzz\4\2\62;CH\3\2\62\63")
        buf.write("\3\2\629\3\2\63;\4\2\62;aa\3\2\62;\5\2C\\aac|\4\2GGgg")
        buf.write("\4\2--//\5\2\13\f\17\17\"\"\2\u01aa\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\3\u0081\3\2\2\2\5\u0084\3\2\2\2\7\u0088\3\2\2\2")
        buf.write("\t\u008f\3\2\2\2\13\u0092\3\2\2\2\r\u0094\3\2\2\2\17\u009a")
        buf.write("\3\2\2\2\21\u00a3\3\2\2\2\23\u00a6\3\2\2\2\25\u00ab\3")
        buf.write("\2\2\2\27\u00b2\3\2\2\2\31\u00ba\3\2\2\2\33\u00bd\3\2")
        buf.write("\2\2\35\u00c9\3\2\2\2\37\u00d4\3\2\2\2!\u00e8\3\2\2\2")
        buf.write("#\u00f3\3\2\2\2%\u00fb\3\2\2\2\'\u00fd\3\2\2\2)\u00ff")
        buf.write("\3\2\2\2+\u0105\3\2\2\2-\u0109\3\2\2\2/\u010f\3\2\2\2")
        buf.write("\61\u0117\3\2\2\2\63\u011b\3\2\2\2\65\u0123\3\2\2\2\67")
        buf.write("\u0132\3\2\2\29\u0134\3\2\2\2;\u0136\3\2\2\2=\u0142\3")
        buf.write("\2\2\2?\u0144\3\2\2\2A\u0147\3\2\2\2C\u014f\3\2\2\2E\u0151")
        buf.write("\3\2\2\2G\u0153\3\2\2\2I\u0155\3\2\2\2K\u0157\3\2\2\2")
        buf.write("M\u0159\3\2\2\2O\u015b\3\2\2\2Q\u015d\3\2\2\2S\u015f\3")
        buf.write("\2\2\2U\u0161\3\2\2\2W\u0164\3\2\2\2Y\u0167\3\2\2\2[\u0169")
        buf.write("\3\2\2\2]\u016b\3\2\2\2_\u016d\3\2\2\2a\u0170\3\2\2\2")
        buf.write("c\u0173\3\2\2\2e\u0175\3\2\2\2g\u0177\3\2\2\2i\u0179\3")
        buf.write("\2\2\2k\u017b\3\2\2\2m\u017d\3\2\2\2o\u0180\3\2\2\2q\u0183")
        buf.write("\3\2\2\2s\u0185\3\2\2\2u\u0188\3\2\2\2w\u018b\3\2\2\2")
        buf.write("y\u018d\3\2\2\2{\u0191\3\2\2\2}\u0195\3\2\2\2\177\u019b")
        buf.write("\3\2\2\2\u0081\u0082\7<\2\2\u0082\u0083\7<\2\2\u0083\4")
        buf.write("\3\2\2\2\u0084\u0085\7P\2\2\u0085\u0086\7g\2\2\u0086\u0087")
        buf.write("\7y\2\2\u0087\6\3\2\2\2\u0088\u0089\7T\2\2\u0089\u008a")
        buf.write("\7g\2\2\u008a\u008b\7v\2\2\u008b\u008c\7w\2\2\u008c\u008d")
        buf.write("\7t\2\2\u008d\u008e\7p\2\2\u008e\b\3\2\2\2\u008f\u0090")
        buf.write("\7%\2\2\u0090\u0091\7%\2\2\u0091\n\3\2\2\2\u0092\u0093")
        buf.write("\7?\2\2\u0093\f\3\2\2\2\u0094\u0095\7D\2\2\u0095\u0096")
        buf.write("\7t\2\2\u0096\u0097\7g\2\2\u0097\u0098\7c\2\2\u0098\u0099")
        buf.write("\7m\2\2\u0099\16\3\2\2\2\u009a\u009b\7E\2\2\u009b\u009c")
        buf.write("\7q\2\2\u009c\u009d\7p\2\2\u009d\u009e\7v\2\2\u009e\u009f")
        buf.write("\7k\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\20\3\2\2\2\u00a3\u00a4\7K\2\2\u00a4\u00a5")
        buf.write("\7h\2\2\u00a5\22\3\2\2\2\u00a6\u00a7\7G\2\2\u00a7\u00a8")
        buf.write("\7n\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa\7g\2\2\u00aa\24")
        buf.write("\3\2\2\2\u00ab\u00ac\7G\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae")
        buf.write("\7u\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1")
        buf.write("\7h\2\2\u00b1\26\3\2\2\2\u00b2\u00b3\7H\2\2\u00b3\u00b4")
        buf.write("\7q\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7")
        buf.write("\7c\2\2\u00b7\u00b8\7e\2\2\u00b8\u00b9\7j\2\2\u00b9\30")
        buf.write("\3\2\2\2\u00ba\u00bb\7K\2\2\u00bb\u00bc\7p\2\2\u00bc\32")
        buf.write("\3\2\2\2\u00bd\u00be\7E\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0")
        buf.write("\7p\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3")
        buf.write("\7t\2\2\u00c3\u00c4\7w\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7t\2\2\u00c8\34")
        buf.write("\3\2\2\2\u00c9\u00ca\7F\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc")
        buf.write("\7u\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf")
        buf.write("\7w\2\2\u00cf\u00d0\7e\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2")
        buf.write("\7q\2\2\u00d2\u00d3\7t\2\2\u00d3\36\3\2\2\2\u00d4\u00d5")
        buf.write("\7E\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8")
        buf.write("\7u\2\2\u00d8\u00d9\7u\2\2\u00d9 \3\2\2\2\u00da\u00db")
        buf.write("\5\67\34\2\u00db\u00e3\5E#\2\u00dc\u00de\5C\"\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2")
        buf.write("\u00df\u00e0\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00df\3")
        buf.write("\2\2\2\u00e2\u00e4\5\67\34\2\u00e3\u00df\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\u00e9\3\2\2\2\u00e5\u00e6\5\67\34")
        buf.write("\2\u00e6\u00e7\5;\36\2\u00e7\u00e9\3\2\2\2\u00e8\u00da")
        buf.write("\3\2\2\2\u00e8\u00e5\3\2\2\2\u00e9\"\3\2\2\2\u00ea\u00eb")
        buf.write("\7V\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7w\2\2\u00ed\u00f4")
        buf.write("\7g\2\2\u00ee\u00ef\7H\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1")
        buf.write("\7n\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f4\7g\2\2\u00f3\u00ea")
        buf.write("\3\2\2\2\u00f3\u00ee\3\2\2\2\u00f4$\3\2\2\2\u00f5\u00f6")
        buf.write("\7X\2\2\u00f6\u00f7\7c\2\2\u00f7\u00fc\7n\2\2\u00f8\u00f9")
        buf.write("\7X\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fc\7t\2\2\u00fb\u00f5")
        buf.write("\3\2\2\2\u00fb\u00f8\3\2\2\2\u00fc&\3\2\2\2\u00fd\u00fe")
        buf.write("\7&\2\2\u00fe(\3\2\2\2\u00ff\u0100\7C\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7t\2\2\u0102\u0103\7c\2\2\u0103\u0104")
        buf.write("\7{\2\2\u0104*\3\2\2\2\u0105\u0106\7K\2\2\u0106\u0107")
        buf.write("\7p\2\2\u0107\u0108\7v\2\2\u0108,\3\2\2\2\u0109\u010a")
        buf.write("\7H\2\2\u010a\u010b\7n\2\2\u010b\u010c\7q\2\2\u010c\u010d")
        buf.write("\7c\2\2\u010d\u010e\7v\2\2\u010e.\3\2\2\2\u010f\u0110")
        buf.write("\7D\2\2\u0110\u0111\7q\2\2\u0111\u0112\7q\2\2\u0112\u0113")
        buf.write("\7n\2\2\u0113\u0114\7g\2\2\u0114\u0115\7c\2\2\u0115\u0116")
        buf.write("\7p\2\2\u0116\60\3\2\2\2\u0117\u0118\7\62\2\2\u0118\u0119")
        buf.write("\t\2\2\2\u0119\u011a\t\3\2\2\u011a\62\3\2\2\2\u011b\u011c")
        buf.write("\7\62\2\2\u011c\u011d\7d\2\2\u011d\u011f\3\2\2\2\u011e")
        buf.write("\u0120\t\4\2\2\u011f\u011e\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122\64\3\2")
        buf.write("\2\2\u0123\u0125\7\62\2\2\u0124\u0126\t\5\2\2\u0125\u0124")
        buf.write("\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0125\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128\66\3\2\2\2\u0129\u012d\t\6\2\2\u012a")
        buf.write("\u012c\t\7\2\2\u012b\u012a\3\2\2\2\u012c\u012f\3\2\2\2")
        buf.write("\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0130\3")
        buf.write("\2\2\2\u012f\u012d\3\2\2\2\u0130\u0133\t\b\2\2\u0131\u0133")
        buf.write("\t\b\2\2\u0132\u0129\3\2\2\2\u0132\u0131\3\2\2\2\u0133")
        buf.write("8\3\2\2\2\u0134\u0135\t\t\2\2\u0135:\3\2\2\2\u0136\u0138")
        buf.write("\t\n\2\2\u0137\u0139\t\13\2\2\u0138\u0137\3\2\2\2\u0138")
        buf.write("\u0139\3\2\2\2\u0139\u013d\3\2\2\2\u013a\u013c\7\62\2")
        buf.write("\2\u013b\u013a\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f")
        buf.write("\u013d\3\2\2\2\u0140\u0141\5\67\34\2\u0141<\3\2\2\2\u0142")
        buf.write("\u0143\7$\2\2\u0143>\3\2\2\2\u0144\u0145\7)\2\2\u0145")
        buf.write("\u0146\7$\2\2\u0146@\3\2\2\2\u0147\u014c\59\35\2\u0148")
        buf.write("\u014b\t\b\2\2\u0149\u014b\59\35\2\u014a\u0148\3\2\2\2")
        buf.write("\u014a\u0149\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3")
        buf.write("\2\2\2\u014c\u014d\3\2\2\2\u014dB\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014f\u0150\7\62\2\2\u0150D\3\2\2\2\u0151\u0152")
        buf.write("\7\60\2\2\u0152F\3\2\2\2\u0153\u0154\7.\2\2\u0154H\3\2")
        buf.write("\2\2\u0155\u0156\7]\2\2\u0156J\3\2\2\2\u0157\u0158\7_")
        buf.write("\2\2\u0158L\3\2\2\2\u0159\u015a\7*\2\2\u015aN\3\2\2\2")
        buf.write("\u015b\u015c\7+\2\2\u015cP\3\2\2\2\u015d\u015e\7}\2\2")
        buf.write("\u015eR\3\2\2\2\u015f\u0160\7\177\2\2\u0160T\3\2\2\2\u0161")
        buf.write("\u0162\7\60\2\2\u0162\u0163\7\60\2\2\u0163V\3\2\2\2\u0164")
        buf.write("\u0165\7D\2\2\u0165\u0166\7{\2\2\u0166X\3\2\2\2\u0167")
        buf.write("\u0168\7<\2\2\u0168Z\3\2\2\2\u0169\u016a\7=\2\2\u016a")
        buf.write("\\\3\2\2\2\u016b\u016c\7-\2\2\u016c^\3\2\2\2\u016d\u016e")
        buf.write("\7>\2\2\u016e\u016f\7?\2\2\u016f`\3\2\2\2\u0170\u0171")
        buf.write("\7@\2\2\u0171\u0172\7?\2\2\u0172b\3\2\2\2\u0173\u0174")
        buf.write("\7/\2\2\u0174d\3\2\2\2\u0175\u0176\7,\2\2\u0176f\3\2\2")
        buf.write("\2\u0177\u0178\7>\2\2\u0178h\3\2\2\2\u0179\u017a\7\'\2")
        buf.write("\2\u017aj\3\2\2\2\u017b\u017c\7\61\2\2\u017cl\3\2\2\2")
        buf.write("\u017d\u017e\7#\2\2\u017e\u017f\7?\2\2\u017fn\3\2\2\2")
        buf.write("\u0180\u0181\7?\2\2\u0181\u0182\7?\2\2\u0182p\3\2\2\2")
        buf.write("\u0183\u0184\7@\2\2\u0184r\3\2\2\2\u0185\u0186\7(\2\2")
        buf.write("\u0186\u0187\7(\2\2\u0187t\3\2\2\2\u0188\u0189\7~\2\2")
        buf.write("\u0189\u018a\7~\2\2\u018av\3\2\2\2\u018b\u018c\7#\2\2")
        buf.write("\u018cx\3\2\2\2\u018d\u018e\7?\2\2\u018e\u018f\7?\2\2")
        buf.write("\u018f\u0190\7\60\2\2\u0190z\3\2\2\2\u0191\u0192\7-\2")
        buf.write("\2\u0192\u0193\7\60\2\2\u0193|\3\2\2\2\u0194\u0196\t\f")
        buf.write("\2\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("\u019a\b?\2\2\u019a~\3\2\2\2\u019b\u019c\13\2\2\2\u019c")
        buf.write("\u019d\b@\3\2\u019d\u0080\3\2\2\2\21\2\u00df\u00e3\u00e8")
        buf.write("\u00f3\u00fb\u0121\u0127\u012d\u0132\u0138\u013d\u014a")
        buf.write("\u014c\u0197\4\b\2\2\3@\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MEM_ACCESS_OP = 1
    NEW = 2
    RETURN = 3
    DOUB_HASH_MARK = 4
    ASSIGN_OP = 5
    BREAK = 6
    CONTINUE = 7
    IF = 8
    ELSE = 9
    ELSEIF = 10
    FOREACH = 11
    IN = 12
    CONSTRUCTOR = 13
    DESTRUCTOR = 14
    CLASS = 15
    FLOATLIT = 16
    BOOLIT = 17
    VAL_VAR = 18
    STATIC = 19
    ARRAY = 20
    INT_TYPE = 21
    FLOAT_TYPE = 22
    BOOL_TYPE = 23
    INTLIT_16 = 24
    INTLIT_2 = 25
    INTLIT_8 = 26
    INTLIT_10 = 27
    EXPONENT = 28
    START_END_STRING = 29
    DOUB_QUOTE = 30
    ID = 31
    ZERO = 32
    DOT = 33
    CM = 34
    LS = 35
    RS = 36
    LB = 37
    RB = 38
    LP = 39
    RP = 40
    RANGE = 41
    BY = 42
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
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'::'", "'New'", "'Return'", "'##'", "'='", "'Break'", "'Continue'", 
            "'If'", "'Else'", "'Elseif'", "'Foreach'", "'In'", "'Constructor'", 
            "'Destructor'", "'Class'", "'$'", "'Array'", "'Int'", "'Float'", 
            "'Boolean'", "'\"'", "''\"'", "'0'", "'.'", "','", "'['", "']'", 
            "'('", "')'", "'{'", "'}'", "'..'", "'By'", "':'", "';'", "'+'", 
            "'<='", "'>='", "'-'", "'*'", "'<'", "'%'", "'/'", "'!='", "'=='", 
            "'>'", "'&&'", "'||'", "'!'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>",
            "MEM_ACCESS_OP", "NEW", "RETURN", "DOUB_HASH_MARK", "ASSIGN_OP", 
            "BREAK", "CONTINUE", "IF", "ELSE", "ELSEIF", "FOREACH", "IN", 
            "CONSTRUCTOR", "DESTRUCTOR", "CLASS", "FLOATLIT", "BOOLIT", 
            "VAL_VAR", "STATIC", "ARRAY", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", 
            "INTLIT_16", "INTLIT_2", "INTLIT_8", "INTLIT_10", "EXPONENT", 
            "START_END_STRING", "DOUB_QUOTE", "ID", "ZERO", "DOT", "CM", 
            "LS", "RS", "LB", "RB", "LP", "RP", "RANGE", "BY", "CL", "SEMI", 
            "ADDOP", "LESS_EQUAL", "GREAT_EQUAL", "SUBOP", "MULOP", "LESS_THAN", 
            "MODOP", "DIVOP", "NOT_EQUAL", "EQUAL", "GREAT_THAN", "AND", 
            "OR", "NEGATE", "STR_CMP", "STR_CONCAT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "MEM_ACCESS_OP", "NEW", "RETURN", "DOUB_HASH_MARK", "ASSIGN_OP", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELSEIF", "FOREACH", 
                  "IN", "CONSTRUCTOR", "DESTRUCTOR", "CLASS", "FLOATLIT", 
                  "BOOLIT", "VAL_VAR", "STATIC", "ARRAY", "INT_TYPE", "FLOAT_TYPE", 
                  "BOOL_TYPE", "INTLIT_16", "INTLIT_2", "INTLIT_8", "INTLIT_10", 
                  "LIT", "EXPONENT", "START_END_STRING", "DOUB_QUOTE", "ID", 
                  "ZERO", "DOT", "CM", "LS", "RS", "LB", "RB", "LP", "RP", 
                  "RANGE", "BY", "CL", "SEMI", "ADDOP", "LESS_EQUAL", "GREAT_EQUAL", 
                  "SUBOP", "MULOP", "LESS_THAN", "MODOP", "DIVOP", "NOT_EQUAL", 
                  "EQUAL", "GREAT_THAN", "AND", "OR", "NEGATE", "STR_CMP", 
                  "STR_CONCAT", "WS", "ERROR_CHAR" ]

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
            actions[62] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


