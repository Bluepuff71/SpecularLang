# Generated from C:/Users/Emery/PycharmProjects/SpecularLang/SpecularLang\SpecLangLexer.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr_denter.DenterHelper import DenterHelper
from SpecLangParser import SpecLangParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u01c0\b\1\b\1\b\1\b\1\b\1\b\1\b\1\4\2\t\2\4\3\t\3\4\4")
        buf.write("\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4")
        buf.write("\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20")
        buf.write("\4\21\t\21\4\22\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26")
        buf.write("\t\26\4\27\t\27\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33")
        buf.write("\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4")
        buf.write("\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*")
        buf.write("\t*\4+\t+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61")
        buf.write("\4\62\t\62\4\63\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67")
        buf.write("\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?")
        buf.write("\4@\t@\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\6\6\u0091\n")
        buf.write("\6\r\6\16\6\u0092\3\7\5\7\u0096\n\7\3\7\3\7\7\7\u009a")
        buf.write("\n\7\f\7\16\7\u009d\13\7\3\7\7\7\u00a0\n\7\f\7\16\7\u00a3")
        buf.write("\13\7\5\7\u00a5\n\7\3\b\3\b\3\b\3\b\7\b\u00ab\n\b\f\b")
        buf.write("\16\b\u00ae\13\b\3\b\3\b\3\t\3\t\3\n\6\n\u00b5\n\n\r\n")
        buf.write("\16\n\u00b6\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\6\21\u00e1\n\21\r")
        buf.write("\21\16\21\u00e2\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#")
        buf.write("\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\7\'\u0158\n\'\f\'\16\'\u015b\13\'\3(\3(\3(\3")
        buf.write("(\3)\6)\u0162\n)\r)\16)\u0163\3*\3*\3*\3*\3*\3+\3+\3+")
        buf.write("\3+\3,\3,\3,\3,\3-\3-\3.\3.\3.\3.\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\39\39\39\39\39\3:\3:\3:\3:\3;\3;\3<\3<\3=\3=\3=\3")
        buf.write("=\3=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3@\6@\u01bd\n@\r@\16@")
        buf.write("\u01be\4\u00ac\u00b6\2A\t\2\13\2\r\2\17\2\21\2\23\2\25")
        buf.write("\2\27\2\31\2\33\n\35\13\37\f!\r#\16%\17\'\20)\21+\2-\2")
        buf.write("/\22\61\23\63\24\65\25\67\269\27;\30=\31?\32A\33C\34E")
        buf.write("\35G\36I\37K M!O\"Q#S$U\2W%Y\2[&]\'_(a\2c)e\2g\2i*k\2")
        buf.write("m\2o+q,s-u.w\2y/{\60}\61\177\2\u0081\2\u0083\2\u0085\62")
        buf.write("\t\2\3\4\5\6\7\b\t\6\2\62;C\\aac|\3\2\"\"\t\2\"\"))..")
        buf.write("\60\60\62;C\\aa\5\2\62;C\\aa\5\2C\\aac|\3\2\62;\4\2\13")
        buf.write("\f\17\17\2\u01bc\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\3+\3\2\2\2\3-\3\2\2\2\3/\3\2\2\2\3\61\3\2\2\2\3\63")
        buf.write("\3\2\2\2\3\65\3\2\2\2\3\67\3\2\2\2\39\3\2\2\2\3;\3\2\2")
        buf.write("\2\3=\3\2\2\2\3?\3\2\2\2\3A\3\2\2\2\3C\3\2\2\2\3E\3\2")
        buf.write("\2\2\3G\3\2\2\2\3I\3\2\2\2\3K\3\2\2\2\3M\3\2\2\2\3O\3")
        buf.write("\2\2\2\3Q\3\2\2\2\3S\3\2\2\2\3U\3\2\2\2\3W\3\2\2\2\3Y")
        buf.write("\3\2\2\2\3[\3\2\2\2\3]\3\2\2\2\4_\3\2\2\2\4a\3\2\2\2\4")
        buf.write("c\3\2\2\2\4e\3\2\2\2\4g\3\2\2\2\4i\3\2\2\2\5k\3\2\2\2")
        buf.write("\5m\3\2\2\2\5o\3\2\2\2\5q\3\2\2\2\5s\3\2\2\2\6u\3\2\2")
        buf.write("\2\6w\3\2\2\2\6y\3\2\2\2\7{\3\2\2\2\7}\3\2\2\2\7\177\3")
        buf.write("\2\2\2\b\u0081\3\2\2\2\b\u0083\3\2\2\2\b\u0085\3\2\2\2")
        buf.write("\t\u0087\3\2\2\2\13\u0089\3\2\2\2\r\u008b\3\2\2\2\17\u008d")
        buf.write("\3\2\2\2\21\u0090\3\2\2\2\23\u0095\3\2\2\2\25\u00a6\3")
        buf.write("\2\2\2\27\u00b1\3\2\2\2\31\u00b4\3\2\2\2\33\u00b8\3\2")
        buf.write("\2\2\35\u00bf\3\2\2\2\37\u00c7\3\2\2\2!\u00cd\3\2\2\2")
        buf.write("#\u00d2\3\2\2\2%\u00da\3\2\2\2\'\u00e0\3\2\2\2)\u00e8")
        buf.write("\3\2\2\2+\u00ec\3\2\2\2-\u00f0\3\2\2\2/\u00f4\3\2\2\2")
        buf.write("\61\u00f9\3\2\2\2\63\u0102\3\2\2\2\65\u0105\3\2\2\2\67")
        buf.write("\u010f\3\2\2\29\u0113\3\2\2\2;\u0116\3\2\2\2=\u011a\3")
        buf.write("\2\2\2?\u011c\3\2\2\2A\u011e\3\2\2\2C\u0120\3\2\2\2E\u0122")
        buf.write("\3\2\2\2G\u012b\3\2\2\2I\u0138\3\2\2\2K\u0142\3\2\2\2")
        buf.write("M\u0145\3\2\2\2O\u014a\3\2\2\2Q\u0150\3\2\2\2S\u0155\3")
        buf.write("\2\2\2U\u015c\3\2\2\2W\u0161\3\2\2\2Y\u0165\3\2\2\2[\u016a")
        buf.write("\3\2\2\2]\u016e\3\2\2\2_\u0172\3\2\2\2a\u0174\3\2\2\2")
        buf.write("c\u0178\3\2\2\2e\u017a\3\2\2\2g\u017e\3\2\2\2i\u0184\3")
        buf.write("\2\2\2k\u0188\3\2\2\2m\u018c\3\2\2\2o\u0190\3\2\2\2q\u0194")
        buf.write("\3\2\2\2s\u0198\3\2\2\2u\u019c\3\2\2\2w\u01a0\3\2\2\2")
        buf.write("y\u01a5\3\2\2\2{\u01a9\3\2\2\2}\u01ab\3\2\2\2\177\u01ad")
        buf.write("\3\2\2\2\u0081\u01b2\3\2\2\2\u0083\u01b7\3\2\2\2\u0085")
        buf.write("\u01bc\3\2\2\2\u0087\u0088\7*\2\2\u0088\n\3\2\2\2\u0089")
        buf.write("\u008a\7+\2\2\u008a\f\3\2\2\2\u008b\u008c\7]\2\2\u008c")
        buf.write("\16\3\2\2\2\u008d\u008e\7_\2\2\u008e\20\3\2\2\2\u008f")
        buf.write("\u0091\t\2\2\2\u0090\u008f\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\22\3\2")
        buf.write("\2\2\u0094\u0096\7\17\2\2\u0095\u0094\3\2\2\2\u0095\u0096")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u00a4\7\f\2\2\u0098")
        buf.write("\u009a\7\13\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2")
        buf.write("\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u00a5")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a0\7\"\2\2\u009f")
        buf.write("\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2")
        buf.write("\u00a1\u00a2\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3")
        buf.write("\2\2\2\u00a4\u009b\3\2\2\2\u00a4\u00a1\3\2\2\2\u00a5\24")
        buf.write("\3\2\2\2\u00a6\u00ac\7$\2\2\u00a7\u00a8\7^\2\2\u00a8\u00ab")
        buf.write("\7$\2\2\u00a9\u00ab\13\2\2\2\u00aa\u00a7\3\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ac\u00aa\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00ac\3")
        buf.write("\2\2\2\u00af\u00b0\7$\2\2\u00b0\26\3\2\2\2\u00b1\u00b2")
        buf.write("\7.\2\2\u00b2\30\3\2\2\2\u00b3\u00b5\t\3\2\2\u00b4\u00b3")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b7\32\3\2\2\2\u00b8\u00b9\7R\2\2\u00b9")
        buf.write("\u00ba\7n\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7{\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\u00be\b\13\2\2\u00be\34\3\2\2\2\u00bf")
        buf.write("\u00c0\7U\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7c\2\2\u00c2")
        buf.write("\u00c3\7t\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\3\2\2\2\u00c5")
        buf.write("\u00c6\b\f\2\2\u00c6\36\3\2\2\2\u00c7\u00c8\7U\2\2\u00c8")
        buf.write("\u00c9\7g\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\u00cc\b\r\2\2\u00cc \3\2\2\2\u00cd\u00ce\7K\2\2\u00ce")
        buf.write("\u00cf\7h\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\b\16\2\2")
        buf.write("\u00d1\"\3\2\2\2\u00d2\u00d3\7Y\2\2\u00d3\u00d4\7j\2\2")
        buf.write("\u00d4\u00d5\7k\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7\7g")
        buf.write("\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\b\17\2\2\u00d9$\3")
        buf.write("\2\2\2\u00da\u00db\7F\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd\u00de\b\20\3\2\u00de&\3\2\2\2\u00df\u00e1")
        buf.write("\t\4\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4\u00e5\t\5\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\b")
        buf.write("\21\4\2\u00e7(\3\2\2\2\u00e8\u00e9\5\31\n\2\u00e9\u00ea")
        buf.write("\3\2\2\2\u00ea\u00eb\b\22\5\2\u00eb*\3\2\2\2\u00ec\u00ed")
        buf.write("\5\t\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef\b\23\6\2\u00ef")
        buf.write(",\3\2\2\2\u00f0\u00f1\5\13\3\2\u00f1\u00f2\3\2\2\2\u00f2")
        buf.write("\u00f3\b\24\7\2\u00f3.\3\2\2\2\u00f4\u00f5\7u\2\2\u00f5")
        buf.write("\u00f6\7c\2\2\u00f6\u00f7\7{\2\2\u00f7\u00f8\7u\2\2\u00f8")
        buf.write("\60\3\2\2\2\u00f9\u00fa\7i\2\2\u00fa\u00fb\7n\2\2\u00fb")
        buf.write("\u00fc\7q\2\2\u00fc\u00fd\7d\2\2\u00fd\u00fe\7c\2\2\u00fe")
        buf.write("\u00ff\7n\2\2\u00ff\u0100\7n\2\2\u0100\u0101\7{\2\2\u0101")
        buf.write("\62\3\2\2\2\u0102\u0103\7f\2\2\u0103\u0104\7q\2\2\u0104")
        buf.write("\64\3\2\2\2\u0105\u0106\7Q\2\2\u0106\u0107\7v\2\2\u0107")
        buf.write("\u0108\7j\2\2\u0108\u0109\7g\2\2\u0109\u010a\7t\2\2\u010a")
        buf.write("\u010b\7y\2\2\u010b\u010c\7k\2\2\u010c\u010d\7u\2\2\u010d")
        buf.write("\u010e\7g\2\2\u010e\66\3\2\2\2\u010f\u0110\7c\2\2\u0110")
        buf.write("\u0111\7p\2\2\u0111\u0112\7f\2\2\u01128\3\2\2\2\u0113")
        buf.write("\u0114\7q\2\2\u0114\u0115\7t\2\2\u0115:\3\2\2\2\u0116")
        buf.write("\u0117\7p\2\2\u0117\u0118\7q\2\2\u0118\u0119\7v\2\2\u0119")
        buf.write("<\3\2\2\2\u011a\u011b\7,\2\2\u011b>\3\2\2\2\u011c\u011d")
        buf.write("\7\61\2\2\u011d@\3\2\2\2\u011e\u011f\7-\2\2\u011fB\3\2")
        buf.write("\2\2\u0120\u0121\7/\2\2\u0121D\3\2\2\2\u0122\u0123\7g")
        buf.write("\2\2\u0123\u0124\7s\2\2\u0124\u0125\7w\2\2\u0125\u0126")
        buf.write("\7c\2\2\u0126\u0127\7n\2\2\u0127\u0128\7\"\2\2\u0128\u0129")
        buf.write("\7v\2\2\u0129\u012a\7q\2\2\u012aF\3\2\2\2\u012b\u012c")
        buf.write("\7i\2\2\u012c\u012d\7t\2\2\u012d\u012e\7g\2\2\u012e\u012f")
        buf.write("\7c\2\2\u012f\u0130\7v\2\2\u0130\u0131\7g\2\2\u0131\u0132")
        buf.write("\7t\2\2\u0132\u0133\7\"\2\2\u0133\u0134\7v\2\2\u0134\u0135")
        buf.write("\7j\2\2\u0135\u0136\7c\2\2\u0136\u0137\7p\2\2\u0137H\3")
        buf.write("\2\2\2\u0138\u0139\7n\2\2\u0139\u013a\7g\2\2\u013a\u013b")
        buf.write("\7u\2\2\u013b\u013c\7u\2\2\u013c\u013d\7\"\2\2\u013d\u013e")
        buf.write("\7v\2\2\u013e\u013f\7j\2\2\u013f\u0140\7c\2\2\u0140\u0141")
        buf.write("\7p\2\2\u0141J\3\2\2\2\u0142\u0143\7k\2\2\u0143\u0144")
        buf.write("\7u\2\2\u0144L\3\2\2\2\u0145\u0146\7v\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147\u0148\7w\2\2\u0148\u0149\7g\2\2\u0149N\3")
        buf.write("\2\2\2\u014a\u014b\7h\2\2\u014b\u014c\7c\2\2\u014c\u014d")
        buf.write("\7n\2\2\u014d\u014e\7u\2\2\u014e\u014f\7g\2\2\u014fP\3")
        buf.write("\2\2\2\u0150\u0151\7p\2\2\u0151\u0152\7q\2\2\u0152\u0153")
        buf.write("\7p\2\2\u0153\u0154\7g\2\2\u0154R\3\2\2\2\u0155\u0159")
        buf.write("\t\6\2\2\u0156\u0158\t\2\2\2\u0157\u0156\3\2\2\2\u0158")
        buf.write("\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2")
        buf.write("\u015aT\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015d\5\25\b")
        buf.write("\2\u015d\u015e\3\2\2\2\u015e\u015f\b(\b\2\u015fV\3\2\2")
        buf.write("\2\u0160\u0162\t\7\2\2\u0161\u0160\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("X\3\2\2\2\u0165\u0166\5\23\7\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u0168\b*\t\2\u0168\u0169\b*\n\2\u0169Z\3\2\2\2\u016a")
        buf.write("\u016b\5\31\n\2\u016b\u016c\3\2\2\2\u016c\u016d\b+\5\2")
        buf.write("\u016d\\\3\2\2\2\u016e\u016f\5\r\4\2\u016f\u0170\3\2\2")
        buf.write("\2\u0170\u0171\b,\13\2\u0171^\3\2\2\2\u0172\u0173\5\21")
        buf.write("\6\2\u0173`\3\2\2\2\u0174\u0175\5\27\t\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176\u0177\b.\f\2\u0177b\3\2\2\2\u0178\u0179\7")
        buf.write("<\2\2\u0179d\3\2\2\2\u017a\u017b\5\25\b\2\u017b\u017c")
        buf.write("\3\2\2\2\u017c\u017d\b\60\b\2\u017df\3\2\2\2\u017e\u017f")
        buf.write("\5\23\7\2\u017f\u0180\3\2\2\2\u0180\u0181\b\61\n\2\u0181")
        buf.write("\u0182\b\61\t\2\u0182\u0183\b\61\2\2\u0183h\3\2\2\2\u0184")
        buf.write("\u0185\5\31\n\2\u0185\u0186\3\2\2\2\u0186\u0187\b\62\5")
        buf.write("\2\u0187j\3\2\2\2\u0188\u0189\5\25\b\2\u0189\u018a\3\2")
        buf.write("\2\2\u018a\u018b\b\63\b\2\u018bl\3\2\2\2\u018c\u018d\5")
        buf.write("\27\t\2\u018d\u018e\3\2\2\2\u018e\u018f\b\64\f\2\u018f")
        buf.write("n\3\2\2\2\u0190\u0191\5\17\5\2\u0191\u0192\3\2\2\2\u0192")
        buf.write("\u0193\b\65\t\2\u0193p\3\2\2\2\u0194\u0195\5\23\7\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u0197\b\66\5\2\u0197r\3\2\2\2\u0198")
        buf.write("\u0199\5\31\n\2\u0199\u019a\3\2\2\2\u019a\u019b\b\67\5")
        buf.write("\2\u019bt\3\2\2\2\u019c\u019d\5\t\2\2\u019d\u019e\3\2")
        buf.write("\2\2\u019e\u019f\b8\r\2\u019fv\3\2\2\2\u01a0\u01a1\5\23")
        buf.write("\7\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\b9\16\2\u01a3\u01a4")
        buf.write("\b9\n\2\u01a4x\3\2\2\2\u01a5\u01a6\5\31\n\2\u01a6\u01a7")
        buf.write("\3\2\2\2\u01a7\u01a8\b:\5\2\u01a8z\3\2\2\2\u01a9\u01aa")
        buf.write("\5\21\6\2\u01aa|\3\2\2\2\u01ab\u01ac\5\13\3\2\u01ac~\3")
        buf.write("\2\2\2\u01ad\u01ae\5\23\7\2\u01ae\u01af\3\2\2\2\u01af")
        buf.write("\u01b0\b=\16\2\u01b0\u01b1\b=\n\2\u01b1\u0080\3\2\2\2")
        buf.write("\u01b2\u01b3\5\23\7\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5")
        buf.write("\b>\17\2\u01b5\u01b6\b>\n\2\u01b6\u0082\3\2\2\2\u01b7")
        buf.write("\u01b8\5\25\b\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\b?\b\2")
        buf.write("\u01ba\u0084\3\2\2\2\u01bb\u01bd\n\b\2\2\u01bc\u01bb\3")
        buf.write("\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bf\u0086\3\2\2\2\25\2\3\4\5\6\7\b\u0092\u0095")
        buf.write("\u009b\u00a1\u00a4\u00aa\u00ac\u00b6\u00e2\u0159\u0163")
        buf.write("\u01be\20\7\3\2\7\4\2\4\6\2\b\2\2\t\b\2\t\t\2\t\6\2\6")
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
    PLAY = 8
    START = 9
    SET = 10
    IF = 11
    WHILE = 12
    DO_Upper = 13
    ACTOR_NAME = 14
    WS = 15
    SAYS = 16
    GLOBALLY = 17
    DO_Lower = 18
    OTHERWISE = 19
    AND = 20
    OR = 21
    NOT = 22
    MUL = 23
    DIV = 24
    ADD = 25
    SUB = 26
    EQUAL_TO = 27
    GREATER_THAN = 28
    LESS_THAN = 29
    IS = 30
    TRUE = 31
    FALSE = 32
    NONE = 33
    ID = 34
    NUMBER = 35
    C_WS = 36
    PL_START = 37
    CA_CLEAN_WORD = 38
    COLON = 39
    CA_WS = 40
    PL_END = 41
    PL_NEWLINE = 42
    PL_WS = 43
    EMOTION_START = 44
    DS_WS = 45
    EMOTION = 46
    EMOTION_END = 47
    ANYCHAR = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "CODE_MODE", "CUSTOM_ACTION_MODE", "PARAM_LIST_MODE", 
                  "DIALOG_START_MODE", "EMOTION_MODE", "DIALOG_TEXT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Play'", "'Start'", "'Set'", "'If'", "'While'", "'Do'", "'says'", 
            "'globally'", "'do'", "'Otherwise'", "'and'", "'or'", "'not'", 
            "'*'", "'/'", "'+'", "'-'", "'equal to'", "'greater than'", 
            "'less than'", "'is'", "'true'", "'false'", "'none'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "NEWLINE", "STRING", "SEPARATOR", "OPEN", 
            "CLOSE", "PLAY", "START", "SET", "IF", "WHILE", "DO_Upper", 
            "ACTOR_NAME", "WS", "SAYS", "GLOBALLY", "DO_Lower", "OTHERWISE", 
            "AND", "OR", "NOT", "MUL", "DIV", "ADD", "SUB", "EQUAL_TO", 
            "GREATER_THAN", "LESS_THAN", "IS", "TRUE", "FALSE", "NONE", 
            "ID", "NUMBER", "C_WS", "PL_START", "CA_CLEAN_WORD", "COLON", 
            "CA_WS", "PL_END", "PL_NEWLINE", "PL_WS", "EMOTION_START", "DS_WS", 
            "EMOTION", "EMOTION_END", "ANYCHAR" ]

    ruleNames = [ "LEFT_PARAN", "RIGHT_PARAN", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
                  "FR_CLEAN_WORD", "FR_NEWLINE", "FR_STRING", "FR_COMMA", 
                  "WHITESPACE", "PLAY", "START", "SET", "IF", "WHILE", "DO_Upper", 
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



