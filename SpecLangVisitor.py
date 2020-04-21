# Generated from C:/Users/Emery/PycharmProjects/SpecularLang\SpecLang.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SpecLangParser import SpecLangParser
else:
    from SpecLangParser import SpecLangParser

# This class defines a complete generic visitor for a parse tree produced by SpecLangParser.

class SpecLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SpecLangParser#block.
    def visitBlock(self, ctx:SpecLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#dialog.
    def visitDialog(self, ctx:SpecLangParser.DialogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#assignment.
    def visitAssignment(self, ctx:SpecLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#ifStatement.
    def visitIfStatement(self, ctx:SpecLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#sceneStatement.
    def visitSceneStatement(self, ctx:SpecLangParser.SceneStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#add.
    def visitAdd(self, ctx:SpecLangParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#equal.
    def visitEqual(self, ctx:SpecLangParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#paren.
    def visitParen(self, ctx:SpecLangParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#mult.
    def visitMult(self, ctx:SpecLangParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#or.
    def visitOr(self, ctx:SpecLangParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#and.
    def visitAnd(self, ctx:SpecLangParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#term.
    def visitTerm(self, ctx:SpecLangParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#unary.
    def visitUnary(self, ctx:SpecLangParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#choice.
    def visitChoice(self, ctx:SpecLangParser.ChoiceContext):
        return self.visitChildren(ctx)



del SpecLangParser