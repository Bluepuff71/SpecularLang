# Generated from C:/Users/Emery/PycharmProjects/SpecularLang/SpecularLang\SpecLangParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SpecLangParser import SpecLangParser
else:
    from SpecLangParser import SpecLangParser

# This class defines a complete generic visitor for a parse tree produced by SpecLangParser.

class SpecLangParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SpecLangParser#program.
    def visitProgram(self, ctx:SpecLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#scene_statement.
    def visitScene_statement(self, ctx:SpecLangParser.Scene_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#block.
    def visitBlock(self, ctx:SpecLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#simple_statement.
    def visitSimple_statement(self, ctx:SpecLangParser.Simple_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#complex_statement.
    def visitComplex_statement(self, ctx:SpecLangParser.Complex_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#dialog.
    def visitDialog(self, ctx:SpecLangParser.DialogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#emotion.
    def visitEmotion(self, ctx:SpecLangParser.EmotionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#custom_statement.
    def visitCustom_statement(self, ctx:SpecLangParser.Custom_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#assignment.
    def visitAssignment(self, ctx:SpecLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#ifstatement.
    def visitIfstatement(self, ctx:SpecLangParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#whileLoop.
    def visitWhileLoop(self, ctx:SpecLangParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#else_statement.
    def visitElse_statement(self, ctx:SpecLangParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#add.
    def visitAdd(self, ctx:SpecLangParser.AddContext):
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


    # Visit a parse tree produced by SpecLangParser#greater_than.
    def visitGreater_than(self, ctx:SpecLangParser.Greater_thanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#and.
    def visitAnd(self, ctx:SpecLangParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#equals.
    def visitEquals(self, ctx:SpecLangParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecLangParser#less_than.
    def visitLess_than(self, ctx:SpecLangParser.Less_thanContext):
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


    # Visit a parse tree produced by SpecLangParser#or_equal_to_modifier.
    def visitOr_equal_to_modifier(self, ctx:SpecLangParser.Or_equal_to_modifierContext):
        return self.visitChildren(ctx)



del SpecLangParser