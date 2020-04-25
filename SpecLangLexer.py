# Generated from C:/Users/Emery/PycharmProjects/SpecularLang\SpecLang.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr_denter.DenterHelper import DenterHelper
from SpecLangParser import SpecLangParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2(")
        buf.write("\u00f4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \3 \7 \u00b9\n \f \16 \u00bc\13 \3 \3 \3")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write("$\3$\7$\u00d2\n$\f$\16$\u00d5\13$\3%\6%\u00d8\n%\r%\16")
        buf.write("%\u00d9\3&\5&\u00dd\n&\3&\3&\7&\u00e1\n&\f&\16&\u00e4")
        buf.write("\13&\3&\7&\u00e7\n&\f&\16&\u00ea\13&\5&\u00ec\n&\3\'\6")
        buf.write("\'\u00ef\n\'\r\'\16\'\u00f0\3\'\3\'\4\u00ba\u00f0\2(\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(\3\2")
        buf.write("\6\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\"\"\2\u00fc\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\3O\3\2\2\2\5Q\3\2\2\2\7S\3\2\2")
        buf.write("\2\tU\3\2\2\2\13W\3\2\2\2\rZ\3\2\2\2\17]\3\2\2\2\21_\3")
        buf.write("\2\2\2\23a\3\2\2\2\25c\3\2\2\2\27e\3\2\2\2\31g\3\2\2\2")
        buf.write("\33j\3\2\2\2\35p\3\2\2\2\37v\3\2\2\2!|\3\2\2\2#\u0081")
        buf.write("\3\2\2\2%\u0084\3\2\2\2\'\u0087\3\2\2\2)\u008a\3\2\2\2")
        buf.write("+\u008f\3\2\2\2-\u0094\3\2\2\2/\u009a\3\2\2\2\61\u00a1")
        buf.write("\3\2\2\2\63\u00a5\3\2\2\2\65\u00a8\3\2\2\2\67\u00ac\3")
        buf.write("\2\2\29\u00ae\3\2\2\2;\u00b0\3\2\2\2=\u00b2\3\2\2\2?\u00b4")
        buf.write("\3\2\2\2A\u00bf\3\2\2\2C\u00c4\3\2\2\2E\u00ca\3\2\2\2")
        buf.write("G\u00cf\3\2\2\2I\u00d7\3\2\2\2K\u00dc\3\2\2\2M\u00ee\3")
        buf.write("\2\2\2OP\7?\2\2P\4\3\2\2\2QR\7B\2\2R\6\3\2\2\2ST\7<\2")
        buf.write("\2T\b\3\2\2\2UV\7=\2\2V\n\3\2\2\2WX\7?\2\2XY\7?\2\2Y\f")
        buf.write("\3\2\2\2Z[\7#\2\2[\\\7?\2\2\\\16\3\2\2\2]^\7*\2\2^\20")
        buf.write("\3\2\2\2_`\7+\2\2`\22\3\2\2\2ab\7]\2\2b\24\3\2\2\2cd\7")
        buf.write(".\2\2d\26\3\2\2\2ef\7_\2\2f\30\3\2\2\2gh\7/\2\2hi\7@\2")
        buf.write("\2i\32\3\2\2\2jk\7y\2\2kl\7j\2\2lm\7k\2\2mn\7n\2\2no\7")
        buf.write("g\2\2o\34\3\2\2\2pq\7g\2\2qr\7p\2\2rs\7v\2\2st\7g\2\2")
        buf.write("tu\7t\2\2u\36\3\2\2\2vw\7g\2\2wx\7z\2\2xy\7k\2\2yz\7v")
        buf.write("\2\2z{\7u\2\2{ \3\2\2\2|}\7o\2\2}~\7q\2\2~\177\7x\2\2")
        buf.write("\177\u0080\7g\2\2\u0080\"\3\2\2\2\u0081\u0082\7v\2\2\u0082")
        buf.write("\u0083\7q\2\2\u0083$\3\2\2\2\u0084\u0085\7f\2\2\u0085")
        buf.write("\u0086\7q\2\2\u0086&\3\2\2\2\u0087\u0088\7k\2\2\u0088")
        buf.write("\u0089\7h\2\2\u0089(\3\2\2\2\u008a\u008b\7g\2\2\u008b")
        buf.write("\u008c\7n\2\2\u008c\u008d\7k\2\2\u008d\u008e\7h\2\2\u008e")
        buf.write("*\3\2\2\2\u008f\u0090\7g\2\2\u0090\u0091\7n\2\2\u0091")
        buf.write("\u0092\7u\2\2\u0092\u0093\7g\2\2\u0093,\3\2\2\2\u0094")
        buf.write("\u0095\7u\2\2\u0095\u0096\7e\2\2\u0096\u0097\7g\2\2\u0097")
        buf.write("\u0098\7p\2\2\u0098\u0099\7g\2\2\u0099.\3\2\2\2\u009a")
        buf.write("\u009b\7i\2\2\u009b\u009c\7n\2\2\u009c\u009d\7q\2\2\u009d")
        buf.write("\u009e\7d\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7n\2\2\u00a0")
        buf.write("\60\3\2\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7p\2\2\u00a3")
        buf.write("\u00a4\7f\2\2\u00a4\62\3\2\2\2\u00a5\u00a6\7q\2\2\u00a6")
        buf.write("\u00a7\7t\2\2\u00a7\64\3\2\2\2\u00a8\u00a9\7p\2\2\u00a9")
        buf.write("\u00aa\7q\2\2\u00aa\u00ab\7v\2\2\u00ab\66\3\2\2\2\u00ac")
        buf.write("\u00ad\7,\2\2\u00ad8\3\2\2\2\u00ae\u00af\7\61\2\2\u00af")
        buf.write(":\3\2\2\2\u00b0\u00b1\7-\2\2\u00b1<\3\2\2\2\u00b2\u00b3")
        buf.write("\7/\2\2\u00b3>\3\2\2\2\u00b4\u00ba\7$\2\2\u00b5\u00b6")
        buf.write("\7^\2\2\u00b6\u00b9\7$\2\2\u00b7\u00b9\13\2\2\2\u00b8")
        buf.write("\u00b5\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2")
        buf.write("\u00ba\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bd\3")
        buf.write("\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00be\7$\2\2\u00be@\3")
        buf.write("\2\2\2\u00bf\u00c0\7V\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2")
        buf.write("\7w\2\2\u00c2\u00c3\7g\2\2\u00c3B\3\2\2\2\u00c4\u00c5")
        buf.write("\7H\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8")
        buf.write("\7u\2\2\u00c8\u00c9\7g\2\2\u00c9D\3\2\2\2\u00ca\u00cb")
        buf.write("\7P\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ceF\3\2\2\2\u00cf\u00d3\t\2\2\2\u00d0\u00d2")
        buf.write("\t\3\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4H\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d6\u00d8\t\4\2\2\u00d7\u00d6\3\2\2\2")
        buf.write("\u00d8\u00d9\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00daJ\3\2\2\2\u00db\u00dd\7\17\2\2\u00dc\u00db")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00eb\7\f\2\2\u00df\u00e1\7\13\2\2\u00e0\u00df\3\2\2")
        buf.write("\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\u00ec\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5")
        buf.write("\u00e7\7\"\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00ea\3\2\2\2")
        buf.write("\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ec\3")
        buf.write("\2\2\2\u00ea\u00e8\3\2\2\2\u00eb\u00e2\3\2\2\2\u00eb\u00e8")
        buf.write("\3\2\2\2\u00ecL\3\2\2\2\u00ed\u00ef\t\5\2\2\u00ee\u00ed")
        buf.write("\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\b\'\2\2")
        buf.write("\u00f3N\3\2\2\2\f\2\u00b8\u00ba\u00d3\u00d9\u00dc\u00e2")
        buf.write("\u00e8\u00eb\u00f0\3\b\2\2")
        return buf.getvalue()


class SpecLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    NEXT = 12
    WHILE = 13
    ENTER = 14
    EXITS = 15
    MOVE = 16
    TO = 17
    DO = 18
    IF = 19
    ELIF = 20
    ELSE = 21
    SCENE = 22
    GLOBAL = 23
    AND = 24
    OR = 25
    NOT = 26
    MUL = 27
    DIV = 28
    ADD = 29
    SUB = 30
    STRING = 31
    TRUE = 32
    FALSE = 33
    NONE = 34
    ID = 35
    NUMBER = 36
    NEWLINE = 37
    WS = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'@'", "':'", "';'", "'=='", "'!='", "'('", "')'", "'['", 
            "','", "']'", "'->'", "'while'", "'enter'", "'exits'", "'move'", 
            "'to'", "'do'", "'if'", "'elif'", "'else'", "'scene'", "'global'", 
            "'and'", "'or'", "'not'", "'*'", "'/'", "'+'", "'-'", "'True'", 
            "'False'", "'None'" ]

    symbolicNames = [ "<INVALID>",
            "NEXT", "WHILE", "ENTER", "EXITS", "MOVE", "TO", "DO", "IF", 
            "ELIF", "ELSE", "SCENE", "GLOBAL", "AND", "OR", "NOT", "MUL", 
            "DIV", "ADD", "SUB", "STRING", "TRUE", "FALSE", "NONE", "ID", 
            "NUMBER", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "NEXT", "WHILE", "ENTER", 
                  "EXITS", "MOVE", "TO", "DO", "IF", "ELIF", "ELSE", "SCENE", 
                  "GLOBAL", "AND", "OR", "NOT", "MUL", "DIV", "ADD", "SUB", 
                  "STRING", "TRUE", "FALSE", "NONE", "ID", "NUMBER", "NEWLINE", 
                  "WS" ]

    grammarFileName = "SpecLang.g4"

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



