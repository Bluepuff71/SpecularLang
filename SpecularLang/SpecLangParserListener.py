# Generated from C:/Users/Emery/PycharmProjects/SpecularLang/SpecularLang\SpecLangParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SpecLangParser import SpecLangParser
else:
    from SpecLangParser import SpecLangParser

# This class defines a complete listener for a parse tree produced by SpecLangParser.
class SpecLangParserListener(ParseTreeListener):

    # Enter a parse tree produced by SpecLangParser#program.
    def enterProgram(self, ctx:SpecLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SpecLangParser#program.
    def exitProgram(self, ctx:SpecLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SpecLangParser#scene_statement.
    def enterScene_statement(self, ctx:SpecLangParser.Scene_statementContext):
        pass

    # Exit a parse tree produced by SpecLangParser#scene_statement.
    def exitScene_statement(self, ctx:SpecLangParser.Scene_statementContext):
        pass


    # Enter a parse tree produced by SpecLangParser#block.
    def enterBlock(self, ctx:SpecLangParser.BlockContext):
        pass

    # Exit a parse tree produced by SpecLangParser#block.
    def exitBlock(self, ctx:SpecLangParser.BlockContext):
        pass


    # Enter a parse tree produced by SpecLangParser#simple_statement.
    def enterSimple_statement(self, ctx:SpecLangParser.Simple_statementContext):
        pass

    # Exit a parse tree produced by SpecLangParser#simple_statement.
    def exitSimple_statement(self, ctx:SpecLangParser.Simple_statementContext):
        pass


    # Enter a parse tree produced by SpecLangParser#complex_statement.
    def enterComplex_statement(self, ctx:SpecLangParser.Complex_statementContext):
        pass

    # Exit a parse tree produced by SpecLangParser#complex_statement.
    def exitComplex_statement(self, ctx:SpecLangParser.Complex_statementContext):
        pass


    # Enter a parse tree produced by SpecLangParser#dialog.
    def enterDialog(self, ctx:SpecLangParser.DialogContext):
        pass

    # Exit a parse tree produced by SpecLangParser#dialog.
    def exitDialog(self, ctx:SpecLangParser.DialogContext):
        pass


    # Enter a parse tree produced by SpecLangParser#dialog_block.
    def enterDialog_block(self, ctx:SpecLangParser.Dialog_blockContext):
        pass

    # Exit a parse tree produced by SpecLangParser#dialog_block.
    def exitDialog_block(self, ctx:SpecLangParser.Dialog_blockContext):
        pass


    # Enter a parse tree produced by SpecLangParser#emotion.
    def enterEmotion(self, ctx:SpecLangParser.EmotionContext):
        pass

    # Exit a parse tree produced by SpecLangParser#emotion.
    def exitEmotion(self, ctx:SpecLangParser.EmotionContext):
        pass


    # Enter a parse tree produced by SpecLangParser#custom_statement.
    def enterCustom_statement(self, ctx:SpecLangParser.Custom_statementContext):
        pass

    # Exit a parse tree produced by SpecLangParser#custom_statement.
    def exitCustom_statement(self, ctx:SpecLangParser.Custom_statementContext):
        pass


    # Enter a parse tree produced by SpecLangParser#custom_param_name_list.
    def enterCustom_param_name_list(self, ctx:SpecLangParser.Custom_param_name_listContext):
        pass

    # Exit a parse tree produced by SpecLangParser#custom_param_name_list.
    def exitCustom_param_name_list(self, ctx:SpecLangParser.Custom_param_name_listContext):
        pass


    # Enter a parse tree produced by SpecLangParser#custom_params_list.
    def enterCustom_params_list(self, ctx:SpecLangParser.Custom_params_listContext):
        pass

    # Exit a parse tree produced by SpecLangParser#custom_params_list.
    def exitCustom_params_list(self, ctx:SpecLangParser.Custom_params_listContext):
        pass


    # Enter a parse tree produced by SpecLangParser#assignment.
    def enterAssignment(self, ctx:SpecLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SpecLangParser#assignment.
    def exitAssignment(self, ctx:SpecLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SpecLangParser#ifstatement.
    def enterIfstatement(self, ctx:SpecLangParser.IfstatementContext):
        pass

    # Exit a parse tree produced by SpecLangParser#ifstatement.
    def exitIfstatement(self, ctx:SpecLangParser.IfstatementContext):
        pass


    # Enter a parse tree produced by SpecLangParser#whileLoop.
    def enterWhileLoop(self, ctx:SpecLangParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by SpecLangParser#whileLoop.
    def exitWhileLoop(self, ctx:SpecLangParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by SpecLangParser#else_statement.
    def enterElse_statement(self, ctx:SpecLangParser.Else_statementContext):
        pass

    # Exit a parse tree produced by SpecLangParser#else_statement.
    def exitElse_statement(self, ctx:SpecLangParser.Else_statementContext):
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


    # Enter a parse tree produced by SpecLangParser#or.
    def enterOr(self, ctx:SpecLangParser.OrContext):
        pass

    # Exit a parse tree produced by SpecLangParser#or.
    def exitOr(self, ctx:SpecLangParser.OrContext):
        pass


    # Enter a parse tree produced by SpecLangParser#greater_than.
    def enterGreater_than(self, ctx:SpecLangParser.Greater_thanContext):
        pass

    # Exit a parse tree produced by SpecLangParser#greater_than.
    def exitGreater_than(self, ctx:SpecLangParser.Greater_thanContext):
        pass


    # Enter a parse tree produced by SpecLangParser#and.
    def enterAnd(self, ctx:SpecLangParser.AndContext):
        pass

    # Exit a parse tree produced by SpecLangParser#and.
    def exitAnd(self, ctx:SpecLangParser.AndContext):
        pass


    # Enter a parse tree produced by SpecLangParser#equals.
    def enterEquals(self, ctx:SpecLangParser.EqualsContext):
        pass

    # Exit a parse tree produced by SpecLangParser#equals.
    def exitEquals(self, ctx:SpecLangParser.EqualsContext):
        pass


    # Enter a parse tree produced by SpecLangParser#less_than.
    def enterLess_than(self, ctx:SpecLangParser.Less_thanContext):
        pass

    # Exit a parse tree produced by SpecLangParser#less_than.
    def exitLess_than(self, ctx:SpecLangParser.Less_thanContext):
        pass


    # Enter a parse tree produced by SpecLangParser#term.
    def enterTerm(self, ctx:SpecLangParser.TermContext):
        pass

    # Exit a parse tree produced by SpecLangParser#term.
    def exitTerm(self, ctx:SpecLangParser.TermContext):
        pass


    # Enter a parse tree produced by SpecLangParser#unary.
    def enterUnary(self, ctx:SpecLangParser.UnaryContext):
        pass

    # Exit a parse tree produced by SpecLangParser#unary.
    def exitUnary(self, ctx:SpecLangParser.UnaryContext):
        pass


    # Enter a parse tree produced by SpecLangParser#choice.
    def enterChoice(self, ctx:SpecLangParser.ChoiceContext):
        pass

    # Exit a parse tree produced by SpecLangParser#choice.
    def exitChoice(self, ctx:SpecLangParser.ChoiceContext):
        pass


    # Enter a parse tree produced by SpecLangParser#param_list.
    def enterParam_list(self, ctx:SpecLangParser.Param_listContext):
        pass

    # Exit a parse tree produced by SpecLangParser#param_list.
    def exitParam_list(self, ctx:SpecLangParser.Param_listContext):
        pass


    # Enter a parse tree produced by SpecLangParser#or_equal_to_modifier.
    def enterOr_equal_to_modifier(self, ctx:SpecLangParser.Or_equal_to_modifierContext):
        pass

    # Exit a parse tree produced by SpecLangParser#or_equal_to_modifier.
    def exitOr_equal_to_modifier(self, ctx:SpecLangParser.Or_equal_to_modifierContext):
        pass



del SpecLangParser