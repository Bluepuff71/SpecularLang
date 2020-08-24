// Generated from C:/Users/Emery/PycharmProjects/SpecularLang/SpecularLang\SpecLangParser.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SpecLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INDENT=1, DEDENT=2, NEWLINE=3, LEFT_BRACKET=4, RIGHT_BRACKET=5, COMMA=6, 
		START=7, SET=8, IF=9, WHILE=10, DO_Upper=11, ACTOR_NAME=12, WS=13, OPEN_PARAN=14, 
		CLOSE_PARAN=15, SAYS=16, GLOBALLY=17, DO_Lower=18, OTHERWISE=19, AND=20, 
		OR=21, NOT=22, MUL=23, DIV=24, ADD=25, SUB=26, EQUAL_TO=27, GREATER_THAN=28, 
		LESS_THAN=29, IS=30, TRUE=31, FALSE=32, NONE=33, ID=34, STRING=35, NUMBER=36, 
		C_WS=37, EMOTION_START=38, DS_WS=39, EMOTION=40, EMOTION_END=41, ANYCHAR=42;
	public static final int
		RULE_program = 0, RULE_scene_statement = 1, RULE_block = 2, RULE_simple_statement = 3, 
		RULE_complex_statement = 4, RULE_dialog = 5, RULE_emotion = 6, RULE_custom_statement = 7, 
		RULE_assignment = 8, RULE_ifstatement = 9, RULE_whileLoop = 10, RULE_else_statement = 11, 
		RULE_expression = 12, RULE_or_equal_to_modifier = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "scene_statement", "block", "simple_statement", "complex_statement", 
			"dialog", "emotion", "custom_statement", "assignment", "ifstatement", 
			"whileLoop", "else_statement", "expression", "or_equal_to_modifier"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, "'{'", "'}'", "','", "'Start'", "'Set'", "'If'", 
			"'While'", "'Do'", null, null, null, null, "'says'", "'globally'", "'do'", 
			"'Otherwise'", "'and'", "'or'", "'not'", "'*'", "'/'", "'+'", "'-'", 
			"'equal to'", "'greater than'", "'less than'", "'is'", "'true'", "'false'", 
			"'none'", null, null, null, null, null, null, null, null, "'Hello World'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INDENT", "DEDENT", "NEWLINE", "LEFT_BRACKET", "RIGHT_BRACKET", 
			"COMMA", "START", "SET", "IF", "WHILE", "DO_Upper", "ACTOR_NAME", "WS", 
			"OPEN_PARAN", "CLOSE_PARAN", "SAYS", "GLOBALLY", "DO_Lower", "OTHERWISE", 
			"AND", "OR", "NOT", "MUL", "DIV", "ADD", "SUB", "EQUAL_TO", "GREATER_THAN", 
			"LESS_THAN", "IS", "TRUE", "FALSE", "NONE", "ID", "STRING", "NUMBER", 
			"C_WS", "EMOTION_START", "DS_WS", "EMOTION", "EMOTION_END", "ANYCHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "SpecLangParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SpecLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public List<Scene_statementContext> scene_statement() {
			return getRuleContexts(Scene_statementContext.class);
		}
		public Scene_statementContext scene_statement(int i) {
			return getRuleContext(Scene_statementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(29); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(28);
				scene_statement();
				}
				}
				setState(31); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==START );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Scene_statementContext extends ParserRuleContext {
		public TerminalNode START() { return getToken(SpecLangParser.START, 0); }
		public TerminalNode ID() { return getToken(SpecLangParser.ID, 0); }
		public TerminalNode INDENT() { return getToken(SpecLangParser.INDENT, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode DEDENT() { return getToken(SpecLangParser.DEDENT, 0); }
		public Scene_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scene_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterScene_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitScene_statement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitScene_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Scene_statementContext scene_statement() throws RecognitionException {
		Scene_statementContext _localctx = new Scene_statementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_scene_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(START);
			setState(34);
			match(ID);
			setState(35);
			match(INDENT);
			setState(36);
			block();
			setState(37);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public Simple_statementContext simple_statement() {
			return getRuleContext(Simple_statementContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(SpecLangParser.NEWLINE, 0); }
		public Complex_statementContext complex_statement() {
			return getRuleContext(Complex_statementContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitBlock(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitBlock(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SET:
			case DO_Upper:
			case ACTOR_NAME:
				{
				setState(39);
				simple_statement();
				setState(40);
				match(NEWLINE);
				}
				break;
			case IF:
			case WHILE:
				{
				setState(42);
				complex_statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SET) | (1L << IF) | (1L << WHILE) | (1L << DO_Upper) | (1L << ACTOR_NAME))) != 0)) {
				{
				setState(45);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_statementContext extends ParserRuleContext {
		public DialogContext dialog() {
			return getRuleContext(DialogContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public Custom_statementContext custom_statement() {
			return getRuleContext(Custom_statementContext.class,0);
		}
		public Simple_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterSimple_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitSimple_statement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitSimple_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Simple_statementContext simple_statement() throws RecognitionException {
		Simple_statementContext _localctx = new Simple_statementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_simple_statement);
		try {
			setState(51);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ACTOR_NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(48);
				dialog();
				}
				break;
			case SET:
				enterOuterAlt(_localctx, 2);
				{
				setState(49);
				assignment();
				}
				break;
			case DO_Upper:
				enterOuterAlt(_localctx, 3);
				{
				setState(50);
				custom_statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Complex_statementContext extends ParserRuleContext {
		public IfstatementContext ifstatement() {
			return getRuleContext(IfstatementContext.class,0);
		}
		public WhileLoopContext whileLoop() {
			return getRuleContext(WhileLoopContext.class,0);
		}
		public Complex_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_complex_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterComplex_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitComplex_statement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitComplex_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Complex_statementContext complex_statement() throws RecognitionException {
		Complex_statementContext _localctx = new Complex_statementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_complex_statement);
		try {
			setState(55);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(53);
				ifstatement();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(54);
				whileLoop();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DialogContext extends ParserRuleContext {
		public TerminalNode ACTOR_NAME() { return getToken(SpecLangParser.ACTOR_NAME, 0); }
		public EmotionContext emotion() {
			return getRuleContext(EmotionContext.class,0);
		}
		public TerminalNode INDENT() { return getToken(SpecLangParser.INDENT, 0); }
		public TerminalNode ANYCHAR() { return getToken(SpecLangParser.ANYCHAR, 0); }
		public TerminalNode DEDENT() { return getToken(SpecLangParser.DEDENT, 0); }
		public DialogContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dialog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterDialog(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitDialog(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitDialog(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DialogContext dialog() throws RecognitionException {
		DialogContext _localctx = new DialogContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_dialog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(ACTOR_NAME);
			setState(58);
			emotion();
			setState(59);
			match(INDENT);
			setState(60);
			match(ANYCHAR);
			setState(61);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EmotionContext extends ParserRuleContext {
		public TerminalNode EMOTION_START() { return getToken(SpecLangParser.EMOTION_START, 0); }
		public TerminalNode EMOTION() { return getToken(SpecLangParser.EMOTION, 0); }
		public TerminalNode EMOTION_END() { return getToken(SpecLangParser.EMOTION_END, 0); }
		public EmotionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_emotion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterEmotion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitEmotion(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitEmotion(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EmotionContext emotion() throws RecognitionException {
		EmotionContext _localctx = new EmotionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_emotion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(EMOTION_START);
			setState(64);
			match(EMOTION);
			setState(65);
			match(EMOTION_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Custom_statementContext extends ParserRuleContext {
		public TerminalNode DO_Upper() { return getToken(SpecLangParser.DO_Upper, 0); }
		public List<TerminalNode> STRING() { return getTokens(SpecLangParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(SpecLangParser.STRING, i);
		}
		public TerminalNode INDENT() { return getToken(SpecLangParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(SpecLangParser.DEDENT, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(SpecLangParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(SpecLangParser.NEWLINE, i);
		}
		public Custom_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_custom_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterCustom_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitCustom_statement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitCustom_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Custom_statementContext custom_statement() throws RecognitionException {
		Custom_statementContext _localctx = new Custom_statementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_custom_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(DO_Upper);
			setState(68);
			match(STRING);
			setState(79);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INDENT) {
				{
				setState(69);
				match(INDENT);
				setState(70);
				match(STRING);
				setState(75);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NEWLINE) {
					{
					{
					setState(71);
					match(NEWLINE);
					setState(72);
					match(STRING);
					}
					}
					setState(77);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(78);
				match(DEDENT);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode SET() { return getToken(SpecLangParser.SET, 0); }
		public TerminalNode ID() { return getToken(SpecLangParser.ID, 0); }
		public TerminalNode EQUAL_TO() { return getToken(SpecLangParser.EQUAL_TO, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode GLOBALLY() { return getToken(SpecLangParser.GLOBALLY, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitAssignment(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitAssignment(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(SET);
			setState(82);
			match(ID);
			setState(83);
			match(EQUAL_TO);
			setState(84);
			expression(0);
			setState(86);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==GLOBALLY) {
				{
				setState(85);
				match(GLOBALLY);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfstatementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(SpecLangParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode INDENT() { return getToken(SpecLangParser.INDENT, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode DEDENT() { return getToken(SpecLangParser.DEDENT, 0); }
		public Else_statementContext else_statement() {
			return getRuleContext(Else_statementContext.class,0);
		}
		public IfstatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifstatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterIfstatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitIfstatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitIfstatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IfstatementContext ifstatement() throws RecognitionException {
		IfstatementContext _localctx = new IfstatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_ifstatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(IF);
			setState(89);
			expression(0);
			setState(90);
			match(INDENT);
			setState(91);
			block();
			setState(92);
			match(DEDENT);
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OTHERWISE) {
				{
				setState(93);
				else_statement();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhileLoopContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(SpecLangParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode INDENT() { return getToken(SpecLangParser.INDENT, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode DEDENT() { return getToken(SpecLangParser.DEDENT, 0); }
		public WhileLoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileLoop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterWhileLoop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitWhileLoop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitWhileLoop(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WhileLoopContext whileLoop() throws RecognitionException {
		WhileLoopContext _localctx = new WhileLoopContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_whileLoop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(WHILE);
			setState(97);
			expression(0);
			setState(98);
			match(INDENT);
			setState(99);
			block();
			setState(100);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Else_statementContext extends ParserRuleContext {
		public TerminalNode OTHERWISE() { return getToken(SpecLangParser.OTHERWISE, 0); }
		public TerminalNode INDENT() { return getToken(SpecLangParser.INDENT, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode DEDENT() { return getToken(SpecLangParser.DEDENT, 0); }
		public Else_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterElse_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitElse_statement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitElse_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Else_statementContext else_statement() throws RecognitionException {
		Else_statementContext _localctx = new Else_statementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_else_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(OTHERWISE);
			setState(103);
			match(INDENT);
			setState(104);
			block();
			setState(105);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AddContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode ADD() { return getToken(SpecLangParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(SpecLangParser.SUB, 0); }
		public AddContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterAdd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitAdd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitAdd(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class ParenContext extends ExpressionContext {
		public TerminalNode OPEN_PARAN() { return getToken(SpecLangParser.OPEN_PARAN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode CLOSE_PARAN() { return getToken(SpecLangParser.CLOSE_PARAN, 0); }
		public ParenContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterParen(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitParen(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitParen(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class MultContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MUL() { return getToken(SpecLangParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(SpecLangParser.DIV, 0); }
		public MultContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterMult(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitMult(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitMult(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class OrContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OR() { return getToken(SpecLangParser.OR, 0); }
		public OrContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterOr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitOr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitOr(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class Greater_thanContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode IS() { return getToken(SpecLangParser.IS, 0); }
		public TerminalNode GREATER_THAN() { return getToken(SpecLangParser.GREATER_THAN, 0); }
		public Or_equal_to_modifierContext or_equal_to_modifier() {
			return getRuleContext(Or_equal_to_modifierContext.class,0);
		}
		public Greater_thanContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterGreater_than(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitGreater_than(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitGreater_than(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class AndContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode AND() { return getToken(SpecLangParser.AND, 0); }
		public AndContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterAnd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitAnd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitAnd(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class EqualsContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode IS() { return getToken(SpecLangParser.IS, 0); }
		public TerminalNode NOT() { return getToken(SpecLangParser.NOT, 0); }
		public TerminalNode EQUAL_TO() { return getToken(SpecLangParser.EQUAL_TO, 0); }
		public EqualsContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterEquals(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitEquals(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitEquals(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class Less_thanContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode IS() { return getToken(SpecLangParser.IS, 0); }
		public TerminalNode LESS_THAN() { return getToken(SpecLangParser.LESS_THAN, 0); }
		public Or_equal_to_modifierContext or_equal_to_modifier() {
			return getRuleContext(Or_equal_to_modifierContext.class,0);
		}
		public Less_thanContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterLess_than(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitLess_than(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitLess_than(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class TermContext extends ExpressionContext {
		public TerminalNode NONE() { return getToken(SpecLangParser.NONE, 0); }
		public TerminalNode TRUE() { return getToken(SpecLangParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(SpecLangParser.FALSE, 0); }
		public TerminalNode ID() { return getToken(SpecLangParser.ID, 0); }
		public TerminalNode STRING() { return getToken(SpecLangParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(SpecLangParser.NUMBER, 0); }
		public TermContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitTerm(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitTerm(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class UnaryContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NOT() { return getToken(SpecLangParser.NOT, 0); }
		public TerminalNode SUB() { return getToken(SpecLangParser.SUB, 0); }
		public UnaryContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterUnary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitUnary(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitUnary(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class ChoiceContext extends ExpressionContext {
		public TerminalNode LEFT_BRACKET() { return getToken(SpecLangParser.LEFT_BRACKET, 0); }
		public List<TerminalNode> STRING() { return getTokens(SpecLangParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(SpecLangParser.STRING, i);
		}
		public TerminalNode RIGHT_BRACKET() { return getToken(SpecLangParser.RIGHT_BRACKET, 0); }
		public List<TerminalNode> COMMA() { return getTokens(SpecLangParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(SpecLangParser.COMMA, i);
		}
		public ChoiceContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterChoice(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitChoice(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitChoice(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
			case SUB:
				{
				_localctx = new UnaryContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(108);
				_la = _input.LA(1);
				if ( !(_la==NOT || _la==SUB) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(109);
				expression(11);
				}
				break;
			case OPEN_PARAN:
				{
				_localctx = new ParenContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(110);
				match(OPEN_PARAN);
				setState(111);
				expression(0);
				setState(112);
				match(CLOSE_PARAN);
				}
				break;
			case LEFT_BRACKET:
				{
				_localctx = new ChoiceContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(114);
				match(LEFT_BRACKET);
				setState(115);
				match(STRING);
				setState(120);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(116);
						match(COMMA);
						setState(117);
						match(STRING);
						}
						} 
					}
					setState(122);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
				}
				setState(123);
				match(RIGHT_BRACKET);
				}
				break;
			case TRUE:
			case FALSE:
			case NONE:
			case ID:
			case STRING:
			case NUMBER:
				{
				_localctx = new TermContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(124);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TRUE) | (1L << FALSE) | (1L << NONE) | (1L << ID) | (1L << STRING) | (1L << NUMBER))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(164);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(162);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
					case 1:
						{
						_localctx = new MultContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(127);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(128);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(129);
						expression(11);
						}
						break;
					case 2:
						{
						_localctx = new AddContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(130);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(131);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(132);
						expression(10);
						}
						break;
					case 3:
						{
						_localctx = new EqualsContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(133);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(134);
						match(IS);
						setState(136);
						_errHandler.sync(this);
						switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
						case 1:
							{
							setState(135);
							match(NOT);
							}
							break;
						}
						setState(139);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==EQUAL_TO) {
							{
							setState(138);
							match(EQUAL_TO);
							}
						}

						setState(141);
						expression(9);
						}
						break;
					case 4:
						{
						_localctx = new Greater_thanContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(142);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(143);
						match(IS);
						setState(144);
						match(GREATER_THAN);
						setState(146);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==OR) {
							{
							setState(145);
							or_equal_to_modifier();
							}
						}

						setState(148);
						expression(8);
						}
						break;
					case 5:
						{
						_localctx = new Less_thanContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(149);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(150);
						match(IS);
						setState(151);
						match(LESS_THAN);
						setState(153);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==OR) {
							{
							setState(152);
							or_equal_to_modifier();
							}
						}

						setState(155);
						expression(7);
						}
						break;
					case 6:
						{
						_localctx = new AndContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(156);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(157);
						match(AND);
						setState(158);
						expression(6);
						}
						break;
					case 7:
						{
						_localctx = new OrContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(159);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(160);
						match(OR);
						setState(161);
						expression(5);
						}
						break;
					}
					} 
				}
				setState(166);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Or_equal_to_modifierContext extends ParserRuleContext {
		public TerminalNode OR() { return getToken(SpecLangParser.OR, 0); }
		public TerminalNode EQUAL_TO() { return getToken(SpecLangParser.EQUAL_TO, 0); }
		public Or_equal_to_modifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_or_equal_to_modifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).enterOr_equal_to_modifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SpecLangParserListener ) ((SpecLangParserListener)listener).exitOr_equal_to_modifier(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof SpecLangParserVisitor ) return ((SpecLangParserVisitor<? extends T>)visitor).visitOr_equal_to_modifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Or_equal_to_modifierContext or_equal_to_modifier() throws RecognitionException {
		Or_equal_to_modifierContext _localctx = new Or_equal_to_modifierContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_or_equal_to_modifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(OR);
			setState(168);
			match(EQUAL_TO);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 12:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 10);
		case 1:
			return precpred(_ctx, 9);
		case 2:
			return precpred(_ctx, 8);
		case 3:
			return precpred(_ctx, 7);
		case 4:
			return precpred(_ctx, 6);
		case 5:
			return precpred(_ctx, 5);
		case 6:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,\u00ad\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\6\2 \n\2\r\2\16\2!\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4.\n\4\3\4\5\4\61\n\4\3\5\3\5\3\5\5"+
		"\5\66\n\5\3\6\3\6\5\6:\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\7\tL\n\t\f\t\16\tO\13\t\3\t\5\tR\n\t\3\n\3\n\3\n"+
		"\3\n\3\n\5\nY\n\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13a\n\13\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3"+
		"\16\3\16\3\16\3\16\7\16y\n\16\f\16\16\16|\13\16\3\16\3\16\5\16\u0080\n"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u008b\n\16\3\16"+
		"\5\16\u008e\n\16\3\16\3\16\3\16\3\16\3\16\5\16\u0095\n\16\3\16\3\16\3"+
		"\16\3\16\3\16\5\16\u009c\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16"+
		"\u00a5\n\16\f\16\16\16\u00a8\13\16\3\17\3\17\3\17\3\17\3z\3\32\20\2\4"+
		"\6\b\n\f\16\20\22\24\26\30\32\34\2\6\4\2\30\30\34\34\3\2!&\3\2\31\32\3"+
		"\2\33\34\2\u00b7\2\37\3\2\2\2\4#\3\2\2\2\6-\3\2\2\2\b\65\3\2\2\2\n9\3"+
		"\2\2\2\f;\3\2\2\2\16A\3\2\2\2\20E\3\2\2\2\22S\3\2\2\2\24Z\3\2\2\2\26b"+
		"\3\2\2\2\30h\3\2\2\2\32\177\3\2\2\2\34\u00a9\3\2\2\2\36 \5\4\3\2\37\36"+
		"\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\3\3\2\2\2#$\7\t\2\2$%\7$\2"+
		"\2%&\7\3\2\2&\'\5\6\4\2\'(\7\4\2\2(\5\3\2\2\2)*\5\b\5\2*+\7\5\2\2+.\3"+
		"\2\2\2,.\5\n\6\2-)\3\2\2\2-,\3\2\2\2.\60\3\2\2\2/\61\5\6\4\2\60/\3\2\2"+
		"\2\60\61\3\2\2\2\61\7\3\2\2\2\62\66\5\f\7\2\63\66\5\22\n\2\64\66\5\20"+
		"\t\2\65\62\3\2\2\2\65\63\3\2\2\2\65\64\3\2\2\2\66\t\3\2\2\2\67:\5\24\13"+
		"\28:\5\26\f\29\67\3\2\2\298\3\2\2\2:\13\3\2\2\2;<\7\16\2\2<=\5\16\b\2"+
		"=>\7\3\2\2>?\7,\2\2?@\7\4\2\2@\r\3\2\2\2AB\7(\2\2BC\7*\2\2CD\7+\2\2D\17"+
		"\3\2\2\2EF\7\r\2\2FQ\7%\2\2GH\7\3\2\2HM\7%\2\2IJ\7\5\2\2JL\7%\2\2KI\3"+
		"\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2OM\3\2\2\2PR\7\4\2\2QG\3"+
		"\2\2\2QR\3\2\2\2R\21\3\2\2\2ST\7\n\2\2TU\7$\2\2UV\7\35\2\2VX\5\32\16\2"+
		"WY\7\23\2\2XW\3\2\2\2XY\3\2\2\2Y\23\3\2\2\2Z[\7\13\2\2[\\\5\32\16\2\\"+
		"]\7\3\2\2]^\5\6\4\2^`\7\4\2\2_a\5\30\r\2`_\3\2\2\2`a\3\2\2\2a\25\3\2\2"+
		"\2bc\7\f\2\2cd\5\32\16\2de\7\3\2\2ef\5\6\4\2fg\7\4\2\2g\27\3\2\2\2hi\7"+
		"\25\2\2ij\7\3\2\2jk\5\6\4\2kl\7\4\2\2l\31\3\2\2\2mn\b\16\1\2no\t\2\2\2"+
		"o\u0080\5\32\16\rpq\7\20\2\2qr\5\32\16\2rs\7\21\2\2s\u0080\3\2\2\2tu\7"+
		"\6\2\2uz\7%\2\2vw\7\b\2\2wy\7%\2\2xv\3\2\2\2y|\3\2\2\2z{\3\2\2\2zx\3\2"+
		"\2\2{}\3\2\2\2|z\3\2\2\2}\u0080\7\7\2\2~\u0080\t\3\2\2\177m\3\2\2\2\177"+
		"p\3\2\2\2\177t\3\2\2\2\177~\3\2\2\2\u0080\u00a6\3\2\2\2\u0081\u0082\f"+
		"\f\2\2\u0082\u0083\t\4\2\2\u0083\u00a5\5\32\16\r\u0084\u0085\f\13\2\2"+
		"\u0085\u0086\t\5\2\2\u0086\u00a5\5\32\16\f\u0087\u0088\f\n\2\2\u0088\u008a"+
		"\7 \2\2\u0089\u008b\7\30\2\2\u008a\u0089\3\2\2\2\u008a\u008b\3\2\2\2\u008b"+
		"\u008d\3\2\2\2\u008c\u008e\7\35\2\2\u008d\u008c\3\2\2\2\u008d\u008e\3"+
		"\2\2\2\u008e\u008f\3\2\2\2\u008f\u00a5\5\32\16\13\u0090\u0091\f\t\2\2"+
		"\u0091\u0092\7 \2\2\u0092\u0094\7\36\2\2\u0093\u0095\5\34\17\2\u0094\u0093"+
		"\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u00a5\5\32\16\n"+
		"\u0097\u0098\f\b\2\2\u0098\u0099\7 \2\2\u0099\u009b\7\37\2\2\u009a\u009c"+
		"\5\34\17\2\u009b\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2"+
		"\u009d\u00a5\5\32\16\t\u009e\u009f\f\7\2\2\u009f\u00a0\7\26\2\2\u00a0"+
		"\u00a5\5\32\16\b\u00a1\u00a2\f\6\2\2\u00a2\u00a3\7\27\2\2\u00a3\u00a5"+
		"\5\32\16\7\u00a4\u0081\3\2\2\2\u00a4\u0084\3\2\2\2\u00a4\u0087\3\2\2\2"+
		"\u00a4\u0090\3\2\2\2\u00a4\u0097\3\2\2\2\u00a4\u009e\3\2\2\2\u00a4\u00a1"+
		"\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7"+
		"\33\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00aa\7\27\2\2\u00aa\u00ab\7\35"+
		"\2\2\u00ab\35\3\2\2\2\23!-\60\659MQX`z\177\u008a\u008d\u0094\u009b\u00a4"+
		"\u00a6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}