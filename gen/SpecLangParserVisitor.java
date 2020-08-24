// Generated from C:/Users/Emery/PycharmProjects/SpecularLang/SpecularLang\SpecLangParser.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link SpecLangParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface SpecLangParserVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(SpecLangParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#scene_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitScene_statement(SpecLangParser.Scene_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(SpecLangParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#simple_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimple_statement(SpecLangParser.Simple_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#complex_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComplex_statement(SpecLangParser.Complex_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#dialog}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDialog(SpecLangParser.DialogContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#emotion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEmotion(SpecLangParser.EmotionContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#custom_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCustom_statement(SpecLangParser.Custom_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#assignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment(SpecLangParser.AssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#ifstatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfstatement(SpecLangParser.IfstatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#whileLoop}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileLoop(SpecLangParser.WhileLoopContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#else_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElse_statement(SpecLangParser.Else_statementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code add}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdd(SpecLangParser.AddContext ctx);
	/**
	 * Visit a parse tree produced by the {@code paren}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParen(SpecLangParser.ParenContext ctx);
	/**
	 * Visit a parse tree produced by the {@code mult}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMult(SpecLangParser.MultContext ctx);
	/**
	 * Visit a parse tree produced by the {@code or}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOr(SpecLangParser.OrContext ctx);
	/**
	 * Visit a parse tree produced by the {@code greater_than}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGreater_than(SpecLangParser.Greater_thanContext ctx);
	/**
	 * Visit a parse tree produced by the {@code and}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAnd(SpecLangParser.AndContext ctx);
	/**
	 * Visit a parse tree produced by the {@code equals}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEquals(SpecLangParser.EqualsContext ctx);
	/**
	 * Visit a parse tree produced by the {@code less_than}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLess_than(SpecLangParser.Less_thanContext ctx);
	/**
	 * Visit a parse tree produced by the {@code term}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm(SpecLangParser.TermContext ctx);
	/**
	 * Visit a parse tree produced by the {@code unary}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnary(SpecLangParser.UnaryContext ctx);
	/**
	 * Visit a parse tree produced by the {@code choice}
	 * labeled alternative in {@link SpecLangParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChoice(SpecLangParser.ChoiceContext ctx);
	/**
	 * Visit a parse tree produced by {@link SpecLangParser#or_equal_to_modifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOr_equal_to_modifier(SpecLangParser.Or_equal_to_modifierContext ctx);
}