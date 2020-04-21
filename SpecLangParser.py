# Generated from C:/Users/Emery/PycharmProjects/SpecularLang\SpecLang.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\5\2")
        buf.write("\17\n\2\3\2\5\2\22\n\2\3\3\3\3\3\3\3\3\3\3\5\3\31\n\3")
        buf.write("\3\3\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4.\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\7\5\67\n\5\f\5\16\5:\13\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5A\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\7\5R\n\5\f\5\16\5U\13\5\3\5\38\3\b")
        buf.write("\6\2\4\6\b\2\b\4\2\26\26\32\32\4\2\21\21\25\25\3\2\26")
        buf.write("\33\3\2\22\23\3\2\24\25\3\2\b\t\2`\2\16\3\2\2\2\4\35\3")
        buf.write("\2\2\2\6-\3\2\2\2\b@\3\2\2\2\n\13\5\4\3\2\13\f\7\34\2")
        buf.write("\2\f\17\3\2\2\2\r\17\5\6\4\2\16\n\3\2\2\2\16\r\3\2\2\2")
        buf.write("\17\21\3\2\2\2\20\22\5\2\2\2\21\20\3\2\2\2\21\22\3\2\2")
        buf.write("\2\22\3\3\2\2\2\23\24\7\3\2\2\24\25\t\2\2\2\25\26\7\4")
        buf.write("\2\2\26\36\7\26\2\2\27\31\7\16\2\2\30\27\3\2\2\2\30\31")
        buf.write("\3\2\2\2\31\32\3\2\2\2\32\33\7\32\2\2\33\34\7\5\2\2\34")
        buf.write("\36\5\b\5\2\35\23\3\2\2\2\35\30\3\2\2\2\36\5\3\2\2\2\37")
        buf.write(" \7\f\2\2 !\5\b\5\2!\"\7\6\2\2\"#\7\36\2\2#$\5\2\2\2$")
        buf.write("%\7\37\2\2%.\3\2\2\2&\'\7\r\2\2\'(\7\26\2\2()\7\6\2\2")
        buf.write(")*\7\36\2\2*+\5\2\2\2+,\7\37\2\2,.\3\2\2\2-\37\3\2\2\2")
        buf.write("-&\3\2\2\2.\7\3\2\2\2/\60\b\5\1\2\60\61\t\3\2\2\61A\5")
        buf.write("\b\5\13\62\63\7\7\2\2\638\7\26\2\2\64\65\7\4\2\2\65\67")
        buf.write("\7\26\2\2\66\64\3\2\2\2\67:\3\2\2\289\3\2\2\28\66\3\2")
        buf.write("\2\29A\3\2\2\2:8\3\2\2\2;<\7\n\2\2<=\5\b\5\2=>\7\13\2")
        buf.write("\2>A\3\2\2\2?A\t\4\2\2@/\3\2\2\2@\62\3\2\2\2@;\3\2\2\2")
        buf.write("@?\3\2\2\2AS\3\2\2\2BC\f\t\2\2CD\t\5\2\2DR\5\b\5\nEF\f")
        buf.write("\b\2\2FG\t\6\2\2GR\5\b\5\tHI\f\7\2\2IJ\t\7\2\2JR\5\b\5")
        buf.write("\bKL\f\6\2\2LM\7\17\2\2MR\5\b\5\7NO\f\5\2\2OP\7\20\2\2")
        buf.write("PR\5\b\5\6QB\3\2\2\2QE\3\2\2\2QH\3\2\2\2QK\3\2\2\2QN\3")
        buf.write("\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\t\3\2\2\2US\3\2")
        buf.write("\2\2\13\16\21\30\35-8@QS")
        return buf.getvalue()


class SpecLangParser ( Parser ):

    grammarFileName = "SpecLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@'", "':'", "'='", "';'", "'&'", "'=='", 
                     "'!='", "'('", "')'", "'if'", "'scene'", "'global'", 
                     "'and'", "'or'", "'not'", "'*'", "'/'", "'+'", "'-'", 
                     "<INVALID>", "'True'", "'False'", "'None'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IF", "SCENE", "GLOBAL", 
                      "AND", "OR", "NOT", "MUL", "DIV", "ADD", "SUB", "STRING", 
                      "TRUE", "FALSE", "NONE", "ID", "NUMBER", "NEWLINE", 
                      "WS", "INDENT", "DEDENT" ]

    RULE_block = 0
    RULE_simple_statement = 1
    RULE_complex_statement = 2
    RULE_expression = 3

    ruleNames =  [ "block", "simple_statement", "complex_statement", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    IF=10
    SCENE=11
    GLOBAL=12
    AND=13
    OR=14
    NOT=15
    MUL=16
    DIV=17
    ADD=18
    SUB=19
    STRING=20
    TRUE=21
    FALSE=22
    NONE=23
    ID=24
    NUMBER=25
    NEWLINE=26
    WS=27
    INDENT=28
    DEDENT=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_statement(self):
            return self.getTypedRuleContext(SpecLangParser.Simple_statementContext,0)


        def NEWLINE(self):
            return self.getToken(SpecLangParser.NEWLINE, 0)

        def complex_statement(self):
            return self.getTypedRuleContext(SpecLangParser.Complex_statementContext,0)


        def block(self):
            return self.getTypedRuleContext(SpecLangParser.BlockContext,0)


        def getRuleIndex(self):
            return SpecLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SpecLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SpecLangParser.T__0, SpecLangParser.GLOBAL, SpecLangParser.ID]:
                self.state = 8
                self.simple_statement()
                self.state = 9
                self.match(SpecLangParser.NEWLINE)
                pass
            elif token in [SpecLangParser.IF, SpecLangParser.SCENE]:
                self.state = 11
                self.complex_statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SpecLangParser.T__0) | (1 << SpecLangParser.IF) | (1 << SpecLangParser.SCENE) | (1 << SpecLangParser.GLOBAL) | (1 << SpecLangParser.ID))) != 0):
                self.state = 14
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SpecLangParser.RULE_simple_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DialogContext(Simple_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.Simple_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SpecLangParser.STRING)
            else:
                return self.getToken(SpecLangParser.STRING, i)
        def ID(self):
            return self.getToken(SpecLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDialog" ):
                listener.enterDialog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDialog" ):
                listener.exitDialog(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDialog" ):
                return visitor.visitDialog(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(Simple_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.Simple_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SpecLangParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(SpecLangParser.ExpressionContext,0)

        def GLOBAL(self):
            return self.getToken(SpecLangParser.GLOBAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)



    def simple_statement(self):

        localctx = SpecLangParser.Simple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_simple_statement)
        self._la = 0 # Token type
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SpecLangParser.T__0]:
                localctx = SpecLangParser.DialogContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(SpecLangParser.T__0)
                self.state = 18
                _la = self._input.LA(1)
                if not(_la==SpecLangParser.STRING or _la==SpecLangParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 19
                self.match(SpecLangParser.T__1)
                self.state = 20
                self.match(SpecLangParser.STRING)
                pass
            elif token in [SpecLangParser.GLOBAL, SpecLangParser.ID]:
                localctx = SpecLangParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SpecLangParser.GLOBAL:
                    self.state = 21
                    self.match(SpecLangParser.GLOBAL)


                self.state = 24
                self.match(SpecLangParser.ID)
                self.state = 25
                self.match(SpecLangParser.T__2)
                self.state = 26
                self.expression(0)
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


    class Complex_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SpecLangParser.RULE_complex_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SceneStatementContext(Complex_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.Complex_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SCENE(self):
            return self.getToken(SpecLangParser.SCENE, 0)
        def STRING(self):
            return self.getToken(SpecLangParser.STRING, 0)
        def INDENT(self):
            return self.getToken(SpecLangParser.INDENT, 0)
        def block(self):
            return self.getTypedRuleContext(SpecLangParser.BlockContext,0)

        def DEDENT(self):
            return self.getToken(SpecLangParser.DEDENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSceneStatement" ):
                listener.enterSceneStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSceneStatement" ):
                listener.exitSceneStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSceneStatement" ):
                return visitor.visitSceneStatement(self)
            else:
                return visitor.visitChildren(self)


    class IfStatementContext(Complex_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.Complex_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(SpecLangParser.IF, 0)
        def expression(self):
            return self.getTypedRuleContext(SpecLangParser.ExpressionContext,0)

        def INDENT(self):
            return self.getToken(SpecLangParser.INDENT, 0)
        def block(self):
            return self.getTypedRuleContext(SpecLangParser.BlockContext,0)

        def DEDENT(self):
            return self.getToken(SpecLangParser.DEDENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)



    def complex_statement(self):

        localctx = SpecLangParser.Complex_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_complex_statement)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SpecLangParser.IF]:
                localctx = SpecLangParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(SpecLangParser.IF)
                self.state = 30
                self.expression(0)
                self.state = 31
                self.match(SpecLangParser.T__3)
                self.state = 32
                self.match(SpecLangParser.INDENT)
                self.state = 33
                self.block()
                self.state = 34
                self.match(SpecLangParser.DEDENT)
                pass
            elif token in [SpecLangParser.SCENE]:
                localctx = SpecLangParser.SceneStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(SpecLangParser.SCENE)
                self.state = 37
                self.match(SpecLangParser.STRING)
                self.state = 38
                self.match(SpecLangParser.T__3)
                self.state = 39
                self.match(SpecLangParser.INDENT)
                self.state = 40
                self.block()
                self.state = 41
                self.match(SpecLangParser.DEDENT)
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


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SpecLangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SpecLangParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(SpecLangParser.ADD, 0)
        def SUB(self):
            return self.getToken(SpecLangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class EqualContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SpecLangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SpecLangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SpecLangParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(SpecLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(SpecLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SpecLangParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(SpecLangParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SpecLangParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(SpecLangParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class TermContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NONE(self):
            return self.getToken(SpecLangParser.NONE, 0)
        def TRUE(self):
            return self.getToken(SpecLangParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(SpecLangParser.FALSE, 0)
        def ID(self):
            return self.getToken(SpecLangParser.ID, 0)
        def STRING(self):
            return self.getToken(SpecLangParser.STRING, 0)
        def NUMBER(self):
            return self.getToken(SpecLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)


    class UnaryContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SpecLangParser.ExpressionContext,0)

        def NOT(self):
            return self.getToken(SpecLangParser.NOT, 0)
        def SUB(self):
            return self.getToken(SpecLangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)


    class ChoiceContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SpecLangParser.STRING)
            else:
                return self.getToken(SpecLangParser.STRING, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChoice" ):
                listener.enterChoice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChoice" ):
                listener.exitChoice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChoice" ):
                return visitor.visitChoice(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SpecLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SpecLangParser.NOT, SpecLangParser.SUB]:
                localctx = SpecLangParser.UnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 46
                _la = self._input.LA(1)
                if not(_la==SpecLangParser.NOT or _la==SpecLangParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 47
                self.expression(9)
                pass
            elif token in [SpecLangParser.T__4]:
                localctx = SpecLangParser.ChoiceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(SpecLangParser.T__4)
                self.state = 49
                self.match(SpecLangParser.STRING)
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 50
                        self.match(SpecLangParser.T__1)
                        self.state = 51
                        self.match(SpecLangParser.STRING) 
                    self.state = 56
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass
            elif token in [SpecLangParser.T__7]:
                localctx = SpecLangParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 57
                self.match(SpecLangParser.T__7)
                self.state = 58
                self.expression(0)
                self.state = 59
                self.match(SpecLangParser.T__8)
                pass
            elif token in [SpecLangParser.STRING, SpecLangParser.TRUE, SpecLangParser.FALSE, SpecLangParser.NONE, SpecLangParser.ID, SpecLangParser.NUMBER]:
                localctx = SpecLangParser.TermContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SpecLangParser.STRING) | (1 << SpecLangParser.TRUE) | (1 << SpecLangParser.FALSE) | (1 << SpecLangParser.NONE) | (1 << SpecLangParser.ID) | (1 << SpecLangParser.NUMBER))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 79
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = SpecLangParser.MultContext(self, SpecLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 64
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 65
                        _la = self._input.LA(1)
                        if not(_la==SpecLangParser.MUL or _la==SpecLangParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 66
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = SpecLangParser.AddContext(self, SpecLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 67
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 68
                        _la = self._input.LA(1)
                        if not(_la==SpecLangParser.ADD or _la==SpecLangParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 69
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = SpecLangParser.EqualContext(self, SpecLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 70
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 71
                        _la = self._input.LA(1)
                        if not(_la==SpecLangParser.T__5 or _la==SpecLangParser.T__6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 72
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = SpecLangParser.AndContext(self, SpecLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 73
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 74
                        self.match(SpecLangParser.AND)
                        self.state = 75
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = SpecLangParser.OrContext(self, SpecLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 76
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 77
                        self.match(SpecLangParser.OR)
                        self.state = 78
                        self.expression(4)
                        pass

             
                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




