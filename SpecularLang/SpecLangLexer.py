# Generated from C:/Users/Emery/PycharmProjects/SpecularLang/SpecularLang\SpecLangLexer.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr_denter.DenterHelper import DenterHelper
from SpecLangParser import SpecLangParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u01b7\b\1\b\1\b\1\b\1\b\1\b\1\b\1\4\2\t\2\4\3\t\3\4\4")
        buf.write("\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4")
        buf.write("\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20")
        buf.write("\4\21\t\21\4\22\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26")
        buf.write("\t\26\4\27\t\27\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33")
        buf.write("\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4")
        buf.write("\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*")
        buf.write("\t*\4+\t+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61")
        buf.write("\4\62\t\62\4\63\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67")
        buf.write("\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\6\6\u008f\n\6\r\6")
        buf.write("\16\6\u0090\3\7\5\7\u0094\n\7\3\7\3\7\7\7\u0098\n\7\f")
        buf.write("\7\16\7\u009b\13\7\3\7\7\7\u009e\n\7\f\7\16\7\u00a1\13")
        buf.write("\7\5\7\u00a3\n\7\3\b\3\b\3\b\3\b\7\b\u00a9\n\b\f\b\16")
        buf.write("\b\u00ac\13\b\3\b\3\b\3\t\3\t\3\n\6\n\u00b3\n\n\r\n\16")
        buf.write("\n\u00b4\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\6\20\u00d8\n\20\r\20\16\20\u00d9\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\7&\u014f\n&\f&\16&")
        buf.write("\u0152\13&\3\'\3\'\3\'\3\'\3(\6(\u0159\n(\r(\16(\u015a")
        buf.write("\3)\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3-\3-\3")
        buf.write("-\3-\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\38\38\39\39\3")
        buf.write("9\39\3:\3:\3;\3;\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3>\3>\3")
        buf.write(">\3>\3?\6?\u01b4\n?\r?\16?\u01b5\4\u00aa\u00b4\2@\t\2")
        buf.write("\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\n\35\13\37")
        buf.write("\f!\r#\16%\17\'\20)\2+\2-\21/\22\61\23\63\24\65\25\67")
        buf.write("\269\27;\30=\31?\32A\33C\34E\35G\36I\37K M!O\"Q#S\2U$")
        buf.write("W\2Y%[&]\'_\2a(c\2e\2g)i\2k\2m*o+q,s-u\2w.y/{\60}\2\177")
        buf.write("\2\u0081\2\u0083\61\t\2\3\4\5\6\7\b\t\6\2\62;C\\aac|\3")
        buf.write("\2\"\"\t\2\"\"))..\60\60\62;C\\aa\5\2\62;C\\aa\5\2C\\")
        buf.write("aac|\3\2\62;\4\2\13\f\17\17\2\u01b3\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\3)\3\2\2\2\3+\3\2\2\2\3-\3\2\2\2\3/\3\2\2")
        buf.write("\2\3\61\3\2\2\2\3\63\3\2\2\2\3\65\3\2\2\2\3\67\3\2\2\2")
        buf.write("\39\3\2\2\2\3;\3\2\2\2\3=\3\2\2\2\3?\3\2\2\2\3A\3\2\2")
        buf.write("\2\3C\3\2\2\2\3E\3\2\2\2\3G\3\2\2\2\3I\3\2\2\2\3K\3\2")
        buf.write("\2\2\3M\3\2\2\2\3O\3\2\2\2\3Q\3\2\2\2\3S\3\2\2\2\3U\3")
        buf.write("\2\2\2\3W\3\2\2\2\3Y\3\2\2\2\3[\3\2\2\2\4]\3\2\2\2\4_")
        buf.write("\3\2\2\2\4a\3\2\2\2\4c\3\2\2\2\4e\3\2\2\2\4g\3\2\2\2\5")
        buf.write("i\3\2\2\2\5k\3\2\2\2\5m\3\2\2\2\5o\3\2\2\2\5q\3\2\2\2")
        buf.write("\6s\3\2\2\2\6u\3\2\2\2\6w\3\2\2\2\7y\3\2\2\2\7{\3\2\2")
        buf.write("\2\7}\3\2\2\2\b\177\3\2\2\2\b\u0081\3\2\2\2\b\u0083\3")
        buf.write("\2\2\2\t\u0085\3\2\2\2\13\u0087\3\2\2\2\r\u0089\3\2\2")
        buf.write("\2\17\u008b\3\2\2\2\21\u008e\3\2\2\2\23\u0093\3\2\2\2")
        buf.write("\25\u00a4\3\2\2\2\27\u00af\3\2\2\2\31\u00b2\3\2\2\2\33")
        buf.write("\u00b6\3\2\2\2\35\u00be\3\2\2\2\37\u00c4\3\2\2\2!\u00c9")
        buf.write("\3\2\2\2#\u00d1\3\2\2\2%\u00d7\3\2\2\2\'\u00df\3\2\2\2")
        buf.write(")\u00e3\3\2\2\2+\u00e7\3\2\2\2-\u00eb\3\2\2\2/\u00f0\3")
        buf.write("\2\2\2\61\u00f9\3\2\2\2\63\u00fc\3\2\2\2\65\u0106\3\2")
        buf.write("\2\2\67\u010a\3\2\2\29\u010d\3\2\2\2;\u0111\3\2\2\2=\u0113")
        buf.write("\3\2\2\2?\u0115\3\2\2\2A\u0117\3\2\2\2C\u0119\3\2\2\2")
        buf.write("E\u0122\3\2\2\2G\u012f\3\2\2\2I\u0139\3\2\2\2K\u013c\3")
        buf.write("\2\2\2M\u0141\3\2\2\2O\u0147\3\2\2\2Q\u014c\3\2\2\2S\u0153")
        buf.write("\3\2\2\2U\u0158\3\2\2\2W\u015c\3\2\2\2Y\u0161\3\2\2\2")
        buf.write("[\u0165\3\2\2\2]\u0169\3\2\2\2_\u016b\3\2\2\2a\u016f\3")
        buf.write("\2\2\2c\u0171\3\2\2\2e\u0175\3\2\2\2g\u017b\3\2\2\2i\u017f")
        buf.write("\3\2\2\2k\u0183\3\2\2\2m\u0187\3\2\2\2o\u018b\3\2\2\2")
        buf.write("q\u018f\3\2\2\2s\u0193\3\2\2\2u\u0197\3\2\2\2w\u019c\3")
        buf.write("\2\2\2y\u01a0\3\2\2\2{\u01a2\3\2\2\2}\u01a4\3\2\2\2\177")
        buf.write("\u01a9\3\2\2\2\u0081\u01ae\3\2\2\2\u0083\u01b3\3\2\2\2")
        buf.write("\u0085\u0086\7*\2\2\u0086\n\3\2\2\2\u0087\u0088\7+\2\2")
        buf.write("\u0088\f\3\2\2\2\u0089\u008a\7]\2\2\u008a\16\3\2\2\2\u008b")
        buf.write("\u008c\7_\2\2\u008c\20\3\2\2\2\u008d\u008f\t\2\2\2\u008e")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\22\3\2\2\2\u0092\u0094\7\17")
        buf.write("\2\2\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u00a2\7\f\2\2\u0096\u0098\7\13\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u00a3\3\2\2\2\u009b\u0099\3")
        buf.write("\2\2\2\u009c\u009e\7\"\2\2\u009d\u009c\3\2\2\2\u009e\u00a1")
        buf.write("\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u0099\3\2\2\2")
        buf.write("\u00a2\u009f\3\2\2\2\u00a3\24\3\2\2\2\u00a4\u00aa\7$\2")
        buf.write("\2\u00a5\u00a6\7^\2\2\u00a6\u00a9\7$\2\2\u00a7\u00a9\13")
        buf.write("\2\2\2\u00a8\u00a5\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac")
        buf.write("\3\2\2\2\u00aa\u00ab\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab")
        buf.write("\u00ad\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\7$\2\2")
        buf.write("\u00ae\26\3\2\2\2\u00af\u00b0\7.\2\2\u00b0\30\3\2\2\2")
        buf.write("\u00b1\u00b3\t\3\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3")
        buf.write("\2\2\2\u00b4\u00b5\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\32")
        buf.write("\3\2\2\2\u00b6\u00b7\7U\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9")
        buf.write("\7c\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc")
        buf.write("\3\2\2\2\u00bc\u00bd\b\13\2\2\u00bd\34\3\2\2\2\u00be\u00bf")
        buf.write("\7U\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\u00c3\b\f\2\2\u00c3\36\3\2\2\2\u00c4\u00c5")
        buf.write("\7K\2\2\u00c5\u00c6\7h\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8")
        buf.write("\b\r\2\2\u00c8 \3\2\2\2\u00c9\u00ca\7Y\2\2\u00ca\u00cb")
        buf.write("\7j\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\b\16\2\2\u00d0")
        buf.write("\"\3\2\2\2\u00d1\u00d2\7F\2\2\u00d2\u00d3\7q\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00d5\b\17\3\2\u00d5$\3\2\2\2\u00d6")
        buf.write("\u00d8\t\4\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\3")
        buf.write("\2\2\2\u00db\u00dc\t\5\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de")
        buf.write("\b\20\4\2\u00de&\3\2\2\2\u00df\u00e0\5\31\n\2\u00e0\u00e1")
        buf.write("\3\2\2\2\u00e1\u00e2\b\21\5\2\u00e2(\3\2\2\2\u00e3\u00e4")
        buf.write("\5\t\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\b\22\6\2\u00e6")
        buf.write("*\3\2\2\2\u00e7\u00e8\5\13\3\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write("\u00ea\b\23\7\2\u00ea,\3\2\2\2\u00eb\u00ec\7u\2\2\u00ec")
        buf.write("\u00ed\7c\2\2\u00ed\u00ee\7{\2\2\u00ee\u00ef\7u\2\2\u00ef")
        buf.write(".\3\2\2\2\u00f0\u00f1\7i\2\2\u00f1\u00f2\7n\2\2\u00f2")
        buf.write("\u00f3\7q\2\2\u00f3\u00f4\7d\2\2\u00f4\u00f5\7c\2\2\u00f5")
        buf.write("\u00f6\7n\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8\7{\2\2\u00f8")
        buf.write("\60\3\2\2\2\u00f9\u00fa\7f\2\2\u00fa\u00fb\7q\2\2\u00fb")
        buf.write("\62\3\2\2\2\u00fc\u00fd\7Q\2\2\u00fd\u00fe\7v\2\2\u00fe")
        buf.write("\u00ff\7j\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7t\2\2\u0101")
        buf.write("\u0102\7y\2\2\u0102\u0103\7k\2\2\u0103\u0104\7u\2\2\u0104")
        buf.write("\u0105\7g\2\2\u0105\64\3\2\2\2\u0106\u0107\7c\2\2\u0107")
        buf.write("\u0108\7p\2\2\u0108\u0109\7f\2\2\u0109\66\3\2\2\2\u010a")
        buf.write("\u010b\7q\2\2\u010b\u010c\7t\2\2\u010c8\3\2\2\2\u010d")
        buf.write("\u010e\7p\2\2\u010e\u010f\7q\2\2\u010f\u0110\7v\2\2\u0110")
        buf.write(":\3\2\2\2\u0111\u0112\7,\2\2\u0112<\3\2\2\2\u0113\u0114")
        buf.write("\7\61\2\2\u0114>\3\2\2\2\u0115\u0116\7-\2\2\u0116@\3\2")
        buf.write("\2\2\u0117\u0118\7/\2\2\u0118B\3\2\2\2\u0119\u011a\7g")
        buf.write("\2\2\u011a\u011b\7s\2\2\u011b\u011c\7w\2\2\u011c\u011d")
        buf.write("\7c\2\2\u011d\u011e\7n\2\2\u011e\u011f\7\"\2\2\u011f\u0120")
        buf.write("\7v\2\2\u0120\u0121\7q\2\2\u0121D\3\2\2\2\u0122\u0123")
        buf.write("\7i\2\2\u0123\u0124\7t\2\2\u0124\u0125\7g\2\2\u0125\u0126")
        buf.write("\7c\2\2\u0126\u0127\7v\2\2\u0127\u0128\7g\2\2\u0128\u0129")
        buf.write("\7t\2\2\u0129\u012a\7\"\2\2\u012a\u012b\7v\2\2\u012b\u012c")
        buf.write("\7j\2\2\u012c\u012d\7c\2\2\u012d\u012e\7p\2\2\u012eF\3")
        buf.write("\2\2\2\u012f\u0130\7n\2\2\u0130\u0131\7g\2\2\u0131\u0132")
        buf.write("\7u\2\2\u0132\u0133\7u\2\2\u0133\u0134\7\"\2\2\u0134\u0135")
        buf.write("\7v\2\2\u0135\u0136\7j\2\2\u0136\u0137\7c\2\2\u0137\u0138")
        buf.write("\7p\2\2\u0138H\3\2\2\2\u0139\u013a\7k\2\2\u013a\u013b")
        buf.write("\7u\2\2\u013bJ\3\2\2\2\u013c\u013d\7v\2\2\u013d\u013e")
        buf.write("\7t\2\2\u013e\u013f\7w\2\2\u013f\u0140\7g\2\2\u0140L\3")
        buf.write("\2\2\2\u0141\u0142\7h\2\2\u0142\u0143\7c\2\2\u0143\u0144")
        buf.write("\7n\2\2\u0144\u0145\7u\2\2\u0145\u0146\7g\2\2\u0146N\3")
        buf.write("\2\2\2\u0147\u0148\7p\2\2\u0148\u0149\7q\2\2\u0149\u014a")
        buf.write("\7p\2\2\u014a\u014b\7g\2\2\u014bP\3\2\2\2\u014c\u0150")
        buf.write("\t\6\2\2\u014d\u014f\t\2\2\2\u014e\u014d\3\2\2\2\u014f")
        buf.write("\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151R\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0154\5\25\b")
        buf.write("\2\u0154\u0155\3\2\2\2\u0155\u0156\b\'\b\2\u0156T\3\2")
        buf.write("\2\2\u0157\u0159\t\7\2\2\u0158\u0157\3\2\2\2\u0159\u015a")
        buf.write("\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b")
        buf.write("V\3\2\2\2\u015c\u015d\5\23\7\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("\u015f\b)\t\2\u015f\u0160\b)\n\2\u0160X\3\2\2\2\u0161")
        buf.write("\u0162\5\31\n\2\u0162\u0163\3\2\2\2\u0163\u0164\b*\5\2")
        buf.write("\u0164Z\3\2\2\2\u0165\u0166\5\r\4\2\u0166\u0167\3\2\2")
        buf.write("\2\u0167\u0168\b+\13\2\u0168\\\3\2\2\2\u0169\u016a\5\21")
        buf.write("\6\2\u016a^\3\2\2\2\u016b\u016c\5\27\t\2\u016c\u016d\3")
        buf.write("\2\2\2\u016d\u016e\b-\f\2\u016e`\3\2\2\2\u016f\u0170\7")
        buf.write("<\2\2\u0170b\3\2\2\2\u0171\u0172\5\25\b\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u0174\b/\b\2\u0174d\3\2\2\2\u0175\u0176")
        buf.write("\5\23\7\2\u0176\u0177\3\2\2\2\u0177\u0178\b\60\n\2\u0178")
        buf.write("\u0179\b\60\t\2\u0179\u017a\b\60\2\2\u017af\3\2\2\2\u017b")
        buf.write("\u017c\5\31\n\2\u017c\u017d\3\2\2\2\u017d\u017e\b\61\5")
        buf.write("\2\u017eh\3\2\2\2\u017f\u0180\5\25\b\2\u0180\u0181\3\2")
        buf.write("\2\2\u0181\u0182\b\62\b\2\u0182j\3\2\2\2\u0183\u0184\5")
        buf.write("\27\t\2\u0184\u0185\3\2\2\2\u0185\u0186\b\63\f\2\u0186")
        buf.write("l\3\2\2\2\u0187\u0188\5\17\5\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u018a\b\64\t\2\u018an\3\2\2\2\u018b\u018c\5\23\7\2\u018c")
        buf.write("\u018d\3\2\2\2\u018d\u018e\b\65\5\2\u018ep\3\2\2\2\u018f")
        buf.write("\u0190\5\31\n\2\u0190\u0191\3\2\2\2\u0191\u0192\b\66\5")
        buf.write("\2\u0192r\3\2\2\2\u0193\u0194\5\t\2\2\u0194\u0195\3\2")
        buf.write("\2\2\u0195\u0196\b\67\r\2\u0196t\3\2\2\2\u0197\u0198\5")
        buf.write("\23\7\2\u0198\u0199\3\2\2\2\u0199\u019a\b8\16\2\u019a")
        buf.write("\u019b\b8\n\2\u019bv\3\2\2\2\u019c\u019d\5\31\n\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e\u019f\b9\5\2\u019fx\3\2\2\2\u01a0")
        buf.write("\u01a1\5\21\6\2\u01a1z\3\2\2\2\u01a2\u01a3\5\13\3\2\u01a3")
        buf.write("|\3\2\2\2\u01a4\u01a5\5\23\7\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01a7\b<\16\2\u01a7\u01a8\b<\n\2\u01a8~\3\2\2\2\u01a9")
        buf.write("\u01aa\5\23\7\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\b=\17")
        buf.write("\2\u01ac\u01ad\b=\n\2\u01ad\u0080\3\2\2\2\u01ae\u01af")
        buf.write("\5\25\b\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\b>\b\2\u01b1")
        buf.write("\u0082\3\2\2\2\u01b2\u01b4\n\b\2\2\u01b3\u01b2\3\2\2\2")
        buf.write("\u01b4\u01b5\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3")
        buf.write("\2\2\2\u01b6\u0084\3\2\2\2\25\2\3\4\5\6\7\b\u0090\u0093")
        buf.write("\u0099\u009f\u00a2\u00a8\u00aa\u00b4\u00d9\u0150\u015a")
        buf.write("\u01b5\20\7\3\2\7\4\2\4\6\2\b\2\2\t\b\2\t\t\2\t\6\2\6")
        buf.write("\2\2\t\5\2\7\5\2\t\7\2\4\7\2\4\b\2\4\2\2")
        return buf.getvalue()


class SpecLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CODE_MODE = 1
    CUSTOM_ACTION_MODE = 2
    PARAM_LIST_MODE = 3
    DIALOG_START_MODE = 4
    EMOTION_MODE = 5
    DIALOG_TEXT_MODE = 6

    INDENT = 1
    DEDENT = 2
    NEWLINE = 3
    STRING = 4
    SEPARATOR = 5
    OPEN = 6
    CLOSE = 7
    START = 8
    SET = 9
    IF = 10
    WHILE = 11
    DO_Upper = 12
    ACTOR_NAME = 13
    WS = 14
    SAYS = 15
    GLOBALLY = 16
    DO_Lower = 17
    OTHERWISE = 18
    AND = 19
    OR = 20
    NOT = 21
    MUL = 22
    DIV = 23
    ADD = 24
    SUB = 25
    EQUAL_TO = 26
    GREATER_THAN = 27
    LESS_THAN = 28
    IS = 29
    TRUE = 30
    FALSE = 31
    NONE = 32
    ID = 33
    NUMBER = 34
    C_WS = 35
    PL_START = 36
    CA_CLEAN_WORD = 37
    COLON = 38
    CA_WS = 39
    PL_END = 40
    PL_NEWLINE = 41
    PL_WS = 42
    EMOTION_START = 43
    DS_WS = 44
    EMOTION = 45
    EMOTION_END = 46
    ANYCHAR = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "CODE_MODE", "CUSTOM_ACTION_MODE", "PARAM_LIST_MODE", 
                  "DIALOG_START_MODE", "EMOTION_MODE", "DIALOG_TEXT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Start'", "'Set'", "'If'", "'While'", "'Do'", "'says'", "'globally'", 
            "'do'", "'Otherwise'", "'and'", "'or'", "'not'", "'*'", "'/'", 
            "'+'", "'-'", "'equal to'", "'greater than'", "'less than'", 
            "'is'", "'true'", "'false'", "'none'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NEWLINE", "STRING", "SEPARATOR", "OPEN", 
            "CLOSE", "START", "SET", "IF", "WHILE", "DO_Upper", "ACTOR_NAME", 
            "WS", "SAYS", "GLOBALLY", "DO_Lower", "OTHERWISE", "AND", "OR", 
            "NOT", "MUL", "DIV", "ADD", "SUB", "EQUAL_TO", "GREATER_THAN", 
            "LESS_THAN", "IS", "TRUE", "FALSE", "NONE", "ID", "NUMBER", 
            "C_WS", "PL_START", "CA_CLEAN_WORD", "COLON", "CA_WS", "PL_END", 
            "PL_NEWLINE", "PL_WS", "EMOTION_START", "DS_WS", "EMOTION", 
            "EMOTION_END", "ANYCHAR" ]

    ruleNames = [ "LEFT_PARAN", "RIGHT_PARAN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "FR_CLEAN_WORD", "FR_NEWLINE", "FR_STRING", "FR_COMMA", 
                  "WHITESPACE", "START", "SET", "IF", "WHILE", "DO_Upper", 
                  "ACTOR_NAME", "WS", "OPEN_PARAN", "CLOSE_PARAN", "SAYS", 
                  "GLOBALLY", "DO_Lower", "OTHERWISE", "AND", "OR", "NOT", 
                  "MUL", "DIV", "ADD", "SUB", "EQUAL_TO", "GREATER_THAN", 
                  "LESS_THAN", "IS", "TRUE", "FALSE", "NONE", "ID", "C_STRING", 
                  "NUMBER", "C_NEWLINE", "C_WS", "PL_START", "CA_CLEAN_WORD", 
                  "CA_COMMA", "COLON", "CA_STRING", "CA_NEWLINE", "CA_WS", 
                  "PL_STRING", "PL_COMMA", "PL_END", "PL_NEWLINE", "PL_WS", 
                  "EMOTION_START", "DS_NEWLINE", "DS_WS", "EMOTION", "EMOTION_END", 
                  "E_NEWLINE", "DT_NEWLINE", "DT_STRING", "ANYCHAR" ]

    grammarFileName = "SpecLangLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class SpecDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: SpecLangLexer = lexer

        def pull_token(self):
            return super(SpecLangLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.SpecDenter(self, self.NEWLINE, SpecLangParser.INDENT, SpecLangParser.DEDENT, False)
        return self.denter.next_token()



