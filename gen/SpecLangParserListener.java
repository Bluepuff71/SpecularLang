// Generated from C:/Users/Emery/PycharmProjects/SpecularLang/SpecularLang\SpecLangParser.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SpecLangParser}.
 */
public interface SpecLangParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(SpecLangParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(SpecLangParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#scene_statement}.
	 * @param ctx the parse tree
	 */
	void enterScene_statement(SpecLangParser.Scene_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#scene_statement}.
	 * @param ctx the parse tree
	 */
	void exitScene_statement(SpecLangParser.Scene_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(SpecLangParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(SpecLangParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#simple_statement}.
	 * @param ctx the parse tree
	 */
	void enterSimple_statement(SpecLangParser.Simple_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#simple_statement}.
	 * @param ctx the parse tree
	 */
	void exitSimple_statement(SpecLangParser.Simple_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#complex_statement}.
	 * @param ctx the parse tree
	 */
	void enterComplex_statement(SpecLangParser.Complex_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#complex_statement}.
	 * @param ctx the parse tree
	 */
	void exitComplex_statement(SpecLangParser.Complex_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#dialog}.
	 * @param ctx the parse tree
	 */
	void enterDialog(SpecLangParser.DialogContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#dialog}.
	 * @param ctx the parse tree
	 */
	void exitDialog(SpecLangParser.DialogContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#emotion}.
	 * @param ctx the parse tree
	 */
	void enterEmotion(SpecLangParser.EmotionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#emotion}.
	 * @param ctx the parse tree
	 */
	void exitEmotion(SpecLangParser.EmotionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#custom_statement}.
	 * @param ctx the parse tree
	 */
	void enterCustom_statement(SpecLangParser.Custom_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#custom_statement}.
	 * @param ctx the parse tree
	 */
	void exitCustom_statement(SpecLangParser.Custom_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(SpecLangParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(SpecLangParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#ifstatement}.
	 * @param ctx the parse tree
	 */
	void enterIfstatement(SpecLangParser.IfstatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#ifstatement}.
	 * @param ctx the parse tree
	 */
	void exitIfstatement(SpecLangParser.IfstatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void enterWhileLoop(SpecLangParser.WhileLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void exitWhileLoop(SpecLangParser.WhileLoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#else_statement}.
	 * @param ctx the parse tree
	 */
	void enterElse_statement(SpecLangParser.Else_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#else_statement}.
	 * @param ctx the parse tree
	 */
	void exitElse_statement(SpecLangParser.Else_statementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code add}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAdd(SpecLangParser.AddContext ctx);
	/**
	 * Exit a parse tree produced by the {@code add}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAdd(SpecLangParser.AddContext ctx);
	/**
	 * Enter a parse tree produced by the {@code paren}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterParen(SpecLangParser.ParenContext ctx);
	/**
	 * Exit a parse tree produced by the {@code paren}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitParen(SpecLangParser.ParenContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mult}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMult(SpecLangParser.MultContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mult}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMult(SpecLangParser.MultContext ctx);
	/**
	 * Enter a parse tree produced by the {@code or}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterOr(SpecLangParser.OrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code or}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitOr(SpecLangParser.OrContext ctx);
	/**
	 * Enter a parse tree produced by the {@code greater_than}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterGreater_than(SpecLangParser.Greater_thanContext ctx);
	/**
	 * Exit a parse tree produced by the {@code greater_than}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitGreater_than(SpecLangParser.Greater_thanContext ctx);
	/**
	 * Enter a parse tree produced by the {@code and}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAnd(SpecLangParser.AndContext ctx);
	/**
	 * Exit a parse tree produced by the {@code and}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAnd(SpecLangParser.AndContext ctx);
	/**
	 * Enter a parse tree produced by the {@code equals}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterEquals(SpecLangParser.EqualsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code equals}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitEquals(SpecLangParser.EqualsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code less_than}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLess_than(SpecLangParser.Less_thanContext ctx);
	/**
	 * Exit a parse tree produced by the {@code less_than}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLess_than(SpecLangParser.Less_thanContext ctx);
	/**
	 * Enter a parse tree produced by the {@code term}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterTerm(SpecLangParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by the {@code term}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitTerm(SpecLangParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unary}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterUnary(SpecLangParser.UnaryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unary}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitUnary(SpecLangParser.UnaryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code choice}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterChoice(SpecLangParser.ChoiceContext ctx);
	/**
	 * Exit a parse tree produced by the {@code choice}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitChoice(SpecLangParser.ChoiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link SpecLangParser#or_equal_to_modifier}.
	 * @param ctx the parse tree
	 */
	void enterOr_equal_to_modifier(SpecLangParser.Or_equal_to_modifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link SpecLangParser#or_equal_to_modifier}.
	 * @param ctx the parse tree
	 */
	void exitOr_equal_to_modifier(SpecLangParser.Or_equal_to_modifierContext ctx);
}