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
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\5\2\20\n\2\6\2\22\n\2\r\2\16\2\23\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\'")
        buf.write("\n\3\3\3\3\3\3\3\5\3,\n\3\3\4\3\4\3\4\3\4\3\4\7\4\63\n")
        buf.write("\4\f\4\16\4\66\13\4\3\4\3\4\3\4\3\4\3\4\5\4=\n\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\7\4E\n\4\f\4\16\4H\13\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5R\n\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\7\5]\n\5\f\5\16\5`\13\5\3\6\3\6\3\6\4\23")
        buf.write("\64\4\6\b\7\2\4\6\b\n\2\6\3\2\b\t\3\2\n\13\3\2\16\17\4")
        buf.write("\2\20\22\31\33\2n\2\f\3\2\2\2\4+\3\2\2\2\6<\3\2\2\2\b")
        buf.write("Q\3\2\2\2\na\3\2\2\2\f\21\7\36\2\2\r\17\5\4\3\2\16\20")
        buf.write("\7\34\2\2\17\16\3\2\2\2\17\20\3\2\2\2\20\22\3\2\2\2\21")
        buf.write("\r\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\23\21\3\2\2\2\24")
        buf.write("\25\3\2\2\2\25\26\7\37\2\2\26\3\3\2\2\2\27\30\7\23\2\2")
        buf.write("\30\31\5\b\5\2\31\32\7\3\2\2\32\33\5\2\2\2\33,\3\2\2\2")
        buf.write("\34\35\7\24\2\2\35\36\7\31\2\2\36\37\7\3\2\2\37,\5\2\2")
        buf.write("\2 !\7\4\2\2!\"\5\n\6\2\"#\7\5\2\2#$\5\n\6\2$,\3\2\2\2")
        buf.write("%\'\7\25\2\2&%\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2()\7\32\2")
        buf.write("\2)*\7\6\2\2*,\5\6\4\2+\27\3\2\2\2+\34\3\2\2\2+ \3\2\2")
        buf.write("\2+&\3\2\2\2,\5\3\2\2\2-.\b\4\1\2./\7\7\2\2/\64\7\31\2")
        buf.write("\2\60\61\7\5\2\2\61\63\7\31\2\2\62\60\3\2\2\2\63\66\3")
        buf.write("\2\2\2\64\65\3\2\2\2\64\62\3\2\2\2\65=\3\2\2\2\66\64\3")
        buf.write("\2\2\2\678\7\f\2\289\5\6\4\29:\7\r\2\2:=\3\2\2\2;=\5\n")
        buf.write("\6\2<-\3\2\2\2<\67\3\2\2\2<;\3\2\2\2=F\3\2\2\2>?\f\6\2")
        buf.write("\2?@\t\2\2\2@E\5\6\4\7AB\f\5\2\2BC\t\3\2\2CE\5\6\4\6D")
        buf.write(">\3\2\2\2DA\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\7\3")
        buf.write("\2\2\2HF\3\2\2\2IJ\b\5\1\2JK\7\30\2\2KR\5\b\5\bLM\7\f")
        buf.write("\2\2MN\5\b\5\2NO\7\r\2\2OR\3\2\2\2PR\5\6\4\2QI\3\2\2\2")
        buf.write("QL\3\2\2\2QP\3\2\2\2R^\3\2\2\2ST\f\7\2\2TU\t\4\2\2U]\5")
        buf.write("\b\5\bVW\f\6\2\2WX\7\26\2\2X]\5\b\5\7YZ\f\5\2\2Z[\7\27")
        buf.write("\2\2[]\5\b\5\6\\S\3\2\2\2\\V\3\2\2\2\\Y\3\2\2\2]`\3\2")
        buf.write("\2\2^\\\3\2\2\2^_\3\2\2\2_\t\3\2\2\2`^\3\2\2\2ab\t\5\2")
        buf.write("\2b\13\3\2\2\2\r\17\23&+\64<DFQ\\^")
        return buf.getvalue()


class SpecLangParser ( Parser ):

    grammarFileName = "SpecLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'@'", "':'", "'='", "'&'", "'*'", 
                     "'/'", "'+'", "'-'", "'('", "')'", "'=='", "'!='", 
                     "'None'", "'True'", "'False'", "'if'", "'scene'", "'global'", 
                     "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IF", "SCENE", "GLOBAL", "AND", "OR", 
                      "NOT", "STRING", "ID", "NUMBER", "NEWLINE", "WS", 
                      "INDENT", "DEDENT" ]

    RULE_block = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_condition = 3
    RULE_term = 4

    ruleNames =  [ "block", "statement", "expression", "condition", "term" ]

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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    IF=17
    SCENE=18
    GLOBAL=19
    AND=20
    OR=21
    NOT=22
    STRING=23
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

        def INDENT(self):
            return self.getToken(SpecLangParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(SpecLangParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SpecLangParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(SpecLangParser.NEWLINE)
            else:
                return self.getToken(SpecLangParser.NEWLINE, i)

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
            self.state = 10
            self.match(SpecLangParser.INDENT)
            self.state = 15 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 11
                    self.statement()
                    self.state = 13
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SpecLangParser.NEWLINE:
                        self.state = 12
                        self.match(SpecLangParser.NEWLINE)



                else:
                    raise NoViableAltException(self)
                self.state = 17 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 19
            self.match(SpecLangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SpecLangParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DialogContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecLangParser.TermContext)
            else:
                return self.getTypedRuleContext(SpecLangParser.TermContext,i)


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


    class AssignmentContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.StatementContext
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


    class SceneStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SCENE(self):
            return self.getToken(SpecLangParser.SCENE, 0)
        def STRING(self):
            return self.getToken(SpecLangParser.STRING, 0)
        def block(self):
            return self.getTypedRuleContext(SpecLangParser.BlockContext,0)


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


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(SpecLangParser.IF, 0)
        def condition(self):
            return self.getTypedRuleContext(SpecLangParser.ConditionContext,0)

        def block(self):
            return self.getTypedRuleContext(SpecLangParser.BlockContext,0)


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



    def statement(self):

        localctx = SpecLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SpecLangParser.IF]:
                localctx = SpecLangParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(SpecLangParser.IF)
                self.state = 22
                self.condition(0)
                self.state = 23
                self.match(SpecLangParser.T__0)
                self.state = 24
                self.block()
                pass
            elif token in [SpecLangParser.SCENE]:
                localctx = SpecLangParser.SceneStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(SpecLangParser.SCENE)
                self.state = 27
                self.match(SpecLangParser.STRING)
                self.state = 28
                self.match(SpecLangParser.T__0)
                self.state = 29
                self.block()
                pass
            elif token in [SpecLangParser.T__1]:
                localctx = SpecLangParser.DialogContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(SpecLangParser.T__1)
                self.state = 31
                self.term()
                self.state = 32
                self.match(SpecLangParser.T__2)
                self.state = 33
                self.term()
                pass
            elif token in [SpecLangParser.GLOBAL, SpecLangParser.ID]:
                localctx = SpecLangParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SpecLangParser.GLOBAL:
                    self.state = 35
                    self.match(SpecLangParser.GLOBAL)


                self.state = 38
                self.match(SpecLangParser.ID)
                self.state = 39
                self.match(SpecLangParser.T__3)
                self.state = 40
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


    class Expr_termContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(SpecLangParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term" ):
                listener.enterExpr_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term" ):
                listener.exitExpr_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term" ):
                return visitor.visitExpr_term(self)
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SpecLangParser.T__4]:
                localctx = SpecLangParser.ChoiceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 44
                self.match(SpecLangParser.T__4)
                self.state = 45
                self.match(SpecLangParser.STRING)
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 46
                        self.match(SpecLangParser.T__2)
                        self.state = 47
                        self.match(SpecLangParser.STRING) 
                    self.state = 52
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass
            elif token in [SpecLangParser.T__9]:
                localctx = SpecLangParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(SpecLangParser.T__9)
                self.state = 54
                self.expression(0)
                self.state = 55
                self.match(SpecLangParser.T__10)
                pass
            elif token in [SpecLangParser.T__13, SpecLangParser.T__14, SpecLangParser.T__15, SpecLangParser.STRING, SpecLangParser.ID, SpecLangParser.NUMBER]:
                localctx = SpecLangParser.Expr_termContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 57
                self.term()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 66
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = SpecLangParser.MultContext(self, SpecLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 60
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 61
                        _la = self._input.LA(1)
                        if not(_la==SpecLangParser.T__5 or _la==SpecLangParser.T__6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = SpecLangParser.AddContext(self, SpecLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 63
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 64
                        _la = self._input.LA(1)
                        if not(_la==SpecLangParser.T__7 or _la==SpecLangParser.T__8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        self.expression(4)
                        pass

             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(SpecLangParser.NOT, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecLangParser.ConditionContext)
            else:
                return self.getTypedRuleContext(SpecLangParser.ConditionContext,i)


        def expression(self):
            return self.getTypedRuleContext(SpecLangParser.ExpressionContext,0)


        def AND(self):
            return self.getToken(SpecLangParser.AND, 0)

        def OR(self):
            return self.getToken(SpecLangParser.OR, 0)

        def getRuleIndex(self):
            return SpecLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SpecLangParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_condition, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 72
                self.match(SpecLangParser.NOT)
                self.state = 73
                self.condition(6)
                pass

            elif la_ == 2:
                self.state = 74
                self.match(SpecLangParser.T__9)
                self.state = 75
                self.condition(0)
                self.state = 76
                self.match(SpecLangParser.T__10)
                pass

            elif la_ == 3:
                self.state = 78
                self.expression(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 90
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = SpecLangParser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 81
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 82
                        _la = self._input.LA(1)
                        if not(_la==SpecLangParser.T__11 or _la==SpecLangParser.T__12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 83
                        self.condition(6)
                        pass

                    elif la_ == 2:
                        localctx = SpecLangParser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 84
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 85
                        self.match(SpecLangParser.AND)
                        self.state = 86
                        self.condition(5)
                        pass

                    elif la_ == 3:
                        localctx = SpecLangParser.ConditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                        self.state = 87
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 88
                        self.match(SpecLangParser.OR)
                        self.state = 89
                        self.condition(4)
                        pass

             
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SpecLangParser.ID, 0)

        def STRING(self):
            return self.getToken(SpecLangParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(SpecLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return SpecLangParser.RULE_term

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




    def term(self):

        localctx = SpecLangParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SpecLangParser.T__13) | (1 << SpecLangParser.T__14) | (1 << SpecLangParser.T__15) | (1 << SpecLangParser.STRING) | (1 << SpecLangParser.ID) | (1 << SpecLangParser.NUMBER))) != 0)):
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
        self._predicates[2] = self.expression_sempred
        self._predicates[3] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




