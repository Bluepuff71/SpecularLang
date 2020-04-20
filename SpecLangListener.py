# Generated from C:/Users/Emery/PycharmProjects/SpecularLang\SpecLang.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SpecLangParser import SpecLangParser
else:
    from SpecLangParser import SpecLangParser

# This class defines a complete listener for a parse tree produced by SpecLangParser.
class SpecLangListener(ParseTreeListener):

    # Enter a parse tree produced by SpecLangParser#block.
    def enterBlock(self, ctx:SpecLangParser.BlockContext):
        pass

    # Exit a parse tree produced by SpecLangParser#block.
    def exitBlock(self, ctx:SpecLangParser.BlockContext):
        pass


    # Enter a parse tree produced by SpecLangParser#ifStatement.
    def enterIfStatement(self, ctx:SpecLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SpecLangParser#ifStatement.
    def exitIfStatement(self, ctx:SpecLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SpecLangParser#sceneStatement.
    def enterSceneStatement(self, ctx:SpecLangParser.SceneStatementContext):
        pass

    # Exit a parse tree produced by SpecLangParser#sceneStatement.
    def exitSceneStatement(self, ctx:SpecLangParser.SceneStatementContext):
        pass


    # Enter a parse tree produced by SpecLangParser#dialog.
    def enterDialog(self, ctx:SpecLangParser.DialogContext):
        pass

    # Exit a parse tree produced by SpecLangParser#dialog.
    def exitDialog(self, ctx:SpecLangParser.DialogContext):
        pass


    # Enter a parse tree produced by SpecLangParser#assignment.
    def enterAssignment(self, ctx:SpecLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SpecLangParser#assignment.
    def exitAssignment(self, ctx:SpecLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SpecLangParser#add.
    def enterAdd(self, ctx:SpecLangParser.AddContext):
        pass

    # Exit a parse tree produced by SpecLangParser#add.
    def exitAdd(self, ctx:SpecLangParser.AddContext):
        pass


    # Enter a parse tree produced by SpecLangParser#paren.
    def enterParen(self, ctx:SpecLangParser.ParenContext):
        pass

    # Exit a parse tree produced by SpecLangParser#paren.
    def exitParen(self, ctx:SpecLangParser.ParenContext):
        pass


    # Enter a parse tree produced by SpecLangParser#mult.
    def enterMult(self, ctx:SpecLangParser.MultContext):
        pass

    # Exit a parse tree produced by SpecLangParser#mult.
    def exitMult(self, ctx:SpecLangParser.MultContext):
        pass


    # Enter a parse tree produced by SpecLangParser#expr_term.
    def enterExpr_term(self, ctx:SpecLangParser.Expr_termContext):
        pass

    # Exit a parse tree produced by SpecLangParser#expr_term.
    def exitExpr_term(self, ctx:SpecLangParser.Expr_termContext):
        pass


    # Enter a parse tree produced by SpecLangParser#choice.
    def enterChoice(self, ctx:SpecLangParser.ChoiceContext):
        pass

    # Exit a parse tree produced by SpecLangParser#choice.
    def exitChoice(self, ctx:SpecLangParser.ChoiceContext):
        pass


    # Enter a parse tree produced by SpecLangParser#condition.
    def enterCondition(self, ctx:SpecLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by SpecLangParser#condition.
    def exitCondition(self, ctx:SpecLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by SpecLangParser#term.
    def enterTerm(self, ctx:SpecLangParser.TermContext):
        pass

    # Exit a parse tree produced by SpecLangParser#term.
    def exitTerm(self, ctx:SpecLangParser.TermContext):
        pass



del SpecLangParser