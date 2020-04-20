# Generated from C:/Users/Emery/PycharmProjects/SpecularLang\SpecLang.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from DenterHelper import DenterHelper
from SpecLangParser import SpecLangParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35")
        buf.write("\u00a8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\7\30\u0085\n\30\f\30\16\30\u0088\13\30\3\30")
        buf.write("\3\30\3\31\3\31\7\31\u008e\n\31\f\31\16\31\u0091\13\31")
        buf.write("\3\32\6\32\u0094\n\32\r\32\16\32\u0095\3\33\5\33\u0099")
        buf.write("\n\33\3\33\3\33\7\33\u009d\n\33\f\33\16\33\u00a0\13\33")
        buf.write("\3\34\6\34\u00a3\n\34\r\34\16\34\u00a4\3\34\3\34\4\u0086")
        buf.write("\u00a4\2\35\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\35\3\2\6\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\3\2\62;\3\2\"\"\2\u00ae\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\39\3\2")
        buf.write("\2\2\5;\3\2\2\2\7=\3\2\2\2\t?\3\2\2\2\13A\3\2\2\2\rC\3")
        buf.write("\2\2\2\17E\3\2\2\2\21G\3\2\2\2\23I\3\2\2\2\25K\3\2\2\2")
        buf.write("\27M\3\2\2\2\31O\3\2\2\2\33R\3\2\2\2\35U\3\2\2\2\37Z\3")
        buf.write("\2\2\2!_\3\2\2\2#e\3\2\2\2%h\3\2\2\2\'n\3\2\2\2)u\3\2")
        buf.write("\2\2+y\3\2\2\2-|\3\2\2\2/\u0080\3\2\2\2\61\u008b\3\2\2")
        buf.write("\2\63\u0093\3\2\2\2\65\u0098\3\2\2\2\67\u00a2\3\2\2\2")
        buf.write("9:\7=\2\2:\4\3\2\2\2;<\7B\2\2<\6\3\2\2\2=>\7<\2\2>\b\3")
        buf.write("\2\2\2?@\7?\2\2@\n\3\2\2\2AB\7(\2\2B\f\3\2\2\2CD\7,\2")
        buf.write("\2D\16\3\2\2\2EF\7\61\2\2F\20\3\2\2\2GH\7-\2\2H\22\3\2")
        buf.write("\2\2IJ\7/\2\2J\24\3\2\2\2KL\7*\2\2L\26\3\2\2\2MN\7+\2")
        buf.write("\2N\30\3\2\2\2OP\7?\2\2PQ\7?\2\2Q\32\3\2\2\2RS\7#\2\2")
        buf.write("ST\7?\2\2T\34\3\2\2\2UV\7P\2\2VW\7q\2\2WX\7p\2\2XY\7g")
        buf.write("\2\2Y\36\3\2\2\2Z[\7V\2\2[\\\7t\2\2\\]\7w\2\2]^\7g\2\2")
        buf.write("^ \3\2\2\2_`\7H\2\2`a\7c\2\2ab\7n\2\2bc\7u\2\2cd\7g\2")
        buf.write("\2d\"\3\2\2\2ef\7k\2\2fg\7h\2\2g$\3\2\2\2hi\7u\2\2ij\7")
        buf.write("e\2\2jk\7g\2\2kl\7p\2\2lm\7g\2\2m&\3\2\2\2no\7i\2\2op")
        buf.write("\7n\2\2pq\7q\2\2qr\7d\2\2rs\7c\2\2st\7n\2\2t(\3\2\2\2")
        buf.write("uv\7c\2\2vw\7p\2\2wx\7f\2\2x*\3\2\2\2yz\7q\2\2z{\7t\2")
        buf.write("\2{,\3\2\2\2|}\7p\2\2}~\7q\2\2~\177\7v\2\2\177.\3\2\2")
        buf.write("\2\u0080\u0086\7$\2\2\u0081\u0082\7^\2\2\u0082\u0085\7")
        buf.write("$\2\2\u0083\u0085\13\2\2\2\u0084\u0081\3\2\2\2\u0084\u0083")
        buf.write("\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0087\3\2\2\2\u0086")
        buf.write("\u0084\3\2\2\2\u0087\u0089\3\2\2\2\u0088\u0086\3\2\2\2")
        buf.write("\u0089\u008a\7$\2\2\u008a\60\3\2\2\2\u008b\u008f\t\2\2")
        buf.write("\2\u008c\u008e\t\3\2\2\u008d\u008c\3\2\2\2\u008e\u0091")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\62\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0094\t\4\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\64\3\2\2\2\u0097\u0099\7\17")
        buf.write("\2\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a")
        buf.write("\3\2\2\2\u009a\u009e\7\f\2\2\u009b\u009d\7\13\2\2\u009c")
        buf.write("\u009b\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f\66\3\2\2\2\u00a0\u009e\3\2")
        buf.write("\2\2\u00a1\u00a3\t\5\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5")
        buf.write("\u00a6\3\2\2\2\u00a6\u00a7\b\34\2\2\u00a78\3\2\2\2\n\2")
        buf.write("\u0084\u0086\u008f\u0095\u0098\u009e\u00a4\3\b\2\2")
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
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    IF = 17
    SCENE = 18
    GLOBAL = 19
    AND = 20
    OR = 21
    NOT = 22
    STRING = 23
    ID = 24
    NUMBER = 25
    NEWLINE = 26
    WS = 27

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'@'", "':'", "'='", "'&'", "'*'", "'/'", "'+'", "'-'", 
            "'('", "')'", "'=='", "'!='", "'None'", "'True'", "'False'", 
            "'if'", "'scene'", "'global'", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "SCENE", "GLOBAL", "AND", "OR", "NOT", "STRING", "ID", 
            "NUMBER", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "IF", "SCENE", "GLOBAL", "AND", "OR", 
                  "NOT", "STRING", "ID", "NUMBER", "NEWLINE", "WS" ]

    grammarFileName = "SpecLang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class SpecDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, should_ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, should_ignore_eof)
            self.lexer: SpecLangLexer = lexer

        def pull_token(self):
            return super(SpecLangLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.SpecDenter(self, self.NEWLINE, SpecLangParser.INDENT, SpecLangParser.DEDENT, False)
        return self.denter.next_token()



