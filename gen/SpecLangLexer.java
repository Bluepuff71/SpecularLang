// Generated from C:/Users/Emery/PycharmProjects/SpecularLang/SpecularLang\SpecLangLexer.g4 by ANTLR 4.8

from antlr_denter.DenterHelper import DenterHelper
from SpecLangParser import SpecLangParser

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SpecLangLexer extends Lexer {
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
		CODE_MODE=1, DIALOG_START_MODE=2, EMOTION_MODE=3, DIALOG_TEXT_MODE=4;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE", "CODE_MODE", "DIALOG_START_MODE", "EMOTION_MODE", "DIALOG_TEXT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LEFT_BRACKET", "RIGHT_BRACKET", "COMMA", "LEFT_PARAN", "RIGHT_PARAN", 
			"FR_NEWLINE", "WHITESPACE", "START", "SET", "IF", "WHILE", "DO_Upper", 
			"ACTOR_NAME", "WS", "OPEN_PARAN", "CLOSE_PARAN", "SAYS", "GLOBALLY", 
			"DO_Lower", "OTHERWISE", "AND", "OR", "NOT", "MUL", "DIV", "ADD", "SUB", 
			"EQUAL_TO", "GREATER_THAN", "LESS_THAN", "IS", "TRUE", "FALSE", "NONE", 
			"ID", "STRING", "NUMBER", "C_NEWLINE", "C_WS", "EMOTION_START", "DS_WS", 
			"EMOTION", "EMOTION_END", "ANYCHAR", "DT_NEWLINE"
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


	class SpecDenter(DenterHelper):
	    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
	        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
	        self.lexer: SpecLangLexer = lexer

	    def pull_token(self):
	        return super(SpecLangLexer, self.lexer).nextToken()

	denter = None

	def nextToken(self):
	    if not self.denter:
	        self.denter = self.SpecDenter(self, self.NEWLINE, SpecLangParser.INDENT, SpecLangParser.DEDENT, False)
	    return self.denter.next_token()



	public SpecLangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "SpecLangLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,\u0155\b\1\b\1\b"+
		"\1\b\1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t"+
		"\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4"+
		"\21\t\21\4\22\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4"+
		"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4"+
		"\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)"+
		"\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6"+
		"\3\6\3\7\5\7m\n\7\3\7\3\7\7\7q\n\7\f\7\16\7t\13\7\3\7\7\7w\n\7\f\7\16"+
		"\7z\13\7\5\7|\n\7\3\b\6\b\177\n\b\r\b\16\b\u0080\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\6\16\u00a4\n\16\r\16\16"+
		"\16\u00a5\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21"+
		"\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26"+
		"\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32"+
		"\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36"+
		"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37"+
		"\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3\"\3"+
		"\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\7$\u0117\n$\f$\16$\u011a\13$\3"+
		"%\3%\3%\3%\7%\u0120\n%\f%\16%\u0123\13%\3%\3%\3&\6&\u0128\n&\r&\16&\u0129"+
		"\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3+\6+\u013e\n"+
		"+\r+\16+\u013f\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3"+
		".\3.\4\u0080\u0121\2/\7\6\t\7\13\b\r\2\17\2\21\2\23\2\25\t\27\n\31\13"+
		"\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67"+
		"\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\2S\'U(W)Y*[+],_\2\7\2\3\4\5\6"+
		"\b\3\2\"\"\t\2\"\"))..\60\60\62;C\\aa\5\2\62;C\\aa\5\2C\\aac|\6\2\62;"+
		"C\\aac|\3\2\62;\2\u0157\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\25\3\2"+
		"\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2"+
		"\2!\3\2\2\2\3#\3\2\2\2\3%\3\2\2\2\3\'\3\2\2\2\3)\3\2\2\2\3+\3\2\2\2\3"+
		"-\3\2\2\2\3/\3\2\2\2\3\61\3\2\2\2\3\63\3\2\2\2\3\65\3\2\2\2\3\67\3\2\2"+
		"\2\39\3\2\2\2\3;\3\2\2\2\3=\3\2\2\2\3?\3\2\2\2\3A\3\2\2\2\3C\3\2\2\2\3"+
		"E\3\2\2\2\3G\3\2\2\2\3I\3\2\2\2\3K\3\2\2\2\3M\3\2\2\2\3O\3\2\2\2\3Q\3"+
		"\2\2\2\3S\3\2\2\2\4U\3\2\2\2\4W\3\2\2\2\5Y\3\2\2\2\5[\3\2\2\2\6]\3\2\2"+
		"\2\6_\3\2\2\2\7a\3\2\2\2\tc\3\2\2\2\13e\3\2\2\2\rg\3\2\2\2\17i\3\2\2\2"+
		"\21l\3\2\2\2\23~\3\2\2\2\25\u0082\3\2\2\2\27\u008a\3\2\2\2\31\u0090\3"+
		"\2\2\2\33\u0095\3\2\2\2\35\u009d\3\2\2\2\37\u00a3\3\2\2\2!\u00ab\3\2\2"+
		"\2#\u00af\3\2\2\2%\u00b1\3\2\2\2\'\u00b3\3\2\2\2)\u00b8\3\2\2\2+\u00c1"+
		"\3\2\2\2-\u00c4\3\2\2\2/\u00ce\3\2\2\2\61\u00d2\3\2\2\2\63\u00d5\3\2\2"+
		"\2\65\u00d9\3\2\2\2\67\u00db\3\2\2\29\u00dd\3\2\2\2;\u00df\3\2\2\2=\u00e1"+
		"\3\2\2\2?\u00ea\3\2\2\2A\u00f7\3\2\2\2C\u0101\3\2\2\2E\u0104\3\2\2\2G"+
		"\u0109\3\2\2\2I\u010f\3\2\2\2K\u0114\3\2\2\2M\u011b\3\2\2\2O\u0127\3\2"+
		"\2\2Q\u012b\3\2\2\2S\u0130\3\2\2\2U\u0134\3\2\2\2W\u0138\3\2\2\2Y\u013d"+
		"\3\2\2\2[\u0141\3\2\2\2]\u0145\3\2\2\2_\u0151\3\2\2\2ab\7}\2\2b\b\3\2"+
		"\2\2cd\7\177\2\2d\n\3\2\2\2ef\7.\2\2f\f\3\2\2\2gh\7*\2\2h\16\3\2\2\2i"+
		"j\7+\2\2j\20\3\2\2\2km\7\17\2\2lk\3\2\2\2lm\3\2\2\2mn\3\2\2\2n{\7\f\2"+
		"\2oq\7\13\2\2po\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2s|\3\2\2\2tr\3\2"+
		"\2\2uw\7\"\2\2vu\3\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2y|\3\2\2\2zx\3\2"+
		"\2\2{r\3\2\2\2{x\3\2\2\2|\22\3\2\2\2}\177\t\2\2\2~}\3\2\2\2\177\u0080"+
		"\3\2\2\2\u0080\u0081\3\2\2\2\u0080~\3\2\2\2\u0081\24\3\2\2\2\u0082\u0083"+
		"\7U\2\2\u0083\u0084\7v\2\2\u0084\u0085\7c\2\2\u0085\u0086\7t\2\2\u0086"+
		"\u0087\7v\2\2\u0087\u0088\3\2\2\2\u0088\u0089\b\t\2\2\u0089\26\3\2\2\2"+
		"\u008a\u008b\7U\2\2\u008b\u008c\7g\2\2\u008c\u008d\7v\2\2\u008d\u008e"+
		"\3\2\2\2\u008e\u008f\b\n\2\2\u008f\30\3\2\2\2\u0090\u0091\7K\2\2\u0091"+
		"\u0092\7h\2\2\u0092\u0093\3\2\2\2\u0093\u0094\b\13\2\2\u0094\32\3\2\2"+
		"\2\u0095\u0096\7Y\2\2\u0096\u0097\7j\2\2\u0097\u0098\7k\2\2\u0098\u0099"+
		"\7n\2\2\u0099\u009a\7g\2\2\u009a\u009b\3\2\2\2\u009b\u009c\b\f\2\2\u009c"+
		"\34\3\2\2\2\u009d\u009e\7F\2\2\u009e\u009f\7q\2\2\u009f\u00a0\3\2\2\2"+
		"\u00a0\u00a1\b\r\2\2\u00a1\36\3\2\2\2\u00a2\u00a4\t\3\2\2\u00a3\u00a2"+
		"\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6"+
		"\u00a7\3\2\2\2\u00a7\u00a8\t\4\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\b\16"+
		"\3\2\u00aa \3\2\2\2\u00ab\u00ac\5\23\b\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae"+
		"\b\17\4\2\u00ae\"\3\2\2\2\u00af\u00b0\5\r\5\2\u00b0$\3\2\2\2\u00b1\u00b2"+
		"\5\17\6\2\u00b2&\3\2\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6"+
		"\7{\2\2\u00b6\u00b7\7u\2\2\u00b7(\3\2\2\2\u00b8\u00b9\7i\2\2\u00b9\u00ba"+
		"\7n\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc\7d\2\2\u00bc\u00bd\7c\2\2\u00bd"+
		"\u00be\7n\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0\7{\2\2\u00c0*\3\2\2\2\u00c1"+
		"\u00c2\7f\2\2\u00c2\u00c3\7q\2\2\u00c3,\3\2\2\2\u00c4\u00c5\7Q\2\2\u00c5"+
		"\u00c6\7v\2\2\u00c6\u00c7\7j\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7t\2\2"+
		"\u00c9\u00ca\7y\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd"+
		"\7g\2\2\u00cd.\3\2\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1"+
		"\7f\2\2\u00d1\60\3\2\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7t\2\2\u00d4\62"+
		"\3\2\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7v\2\2\u00d8"+
		"\64\3\2\2\2\u00d9\u00da\7,\2\2\u00da\66\3\2\2\2\u00db\u00dc\7\61\2\2\u00dc"+
		"8\3\2\2\2\u00dd\u00de\7-\2\2\u00de:\3\2\2\2\u00df\u00e0\7/\2\2\u00e0<"+
		"\3\2\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3\7s\2\2\u00e3\u00e4\7w\2\2\u00e4"+
		"\u00e5\7c\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7\7\"\2\2\u00e7\u00e8\7v\2"+
		"\2\u00e8\u00e9\7q\2\2\u00e9>\3\2\2\2\u00ea\u00eb\7i\2\2\u00eb\u00ec\7"+
		"t\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0"+
		"\7g\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7\"\2\2\u00f2\u00f3\7v\2\2\u00f3"+
		"\u00f4\7j\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7p\2\2\u00f6@\3\2\2\2\u00f7"+
		"\u00f8\7n\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa\7u\2\2\u00fa\u00fb\7u\2\2"+
		"\u00fb\u00fc\7\"\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe\7j\2\2\u00fe\u00ff"+
		"\7c\2\2\u00ff\u0100\7p\2\2\u0100B\3\2\2\2\u0101\u0102\7k\2\2\u0102\u0103"+
		"\7u\2\2\u0103D\3\2\2\2\u0104\u0105\7v\2\2\u0105\u0106\7t\2\2\u0106\u0107"+
		"\7w\2\2\u0107\u0108\7g\2\2\u0108F\3\2\2\2\u0109\u010a\7h\2\2\u010a\u010b"+
		"\7c\2\2\u010b\u010c\7n\2\2\u010c\u010d\7u\2\2\u010d\u010e\7g\2\2\u010e"+
		"H\3\2\2\2\u010f\u0110\7p\2\2\u0110\u0111\7q\2\2\u0111\u0112\7p\2\2\u0112"+
		"\u0113\7g\2\2\u0113J\3\2\2\2\u0114\u0118\t\5\2\2\u0115\u0117\t\6\2\2\u0116"+
		"\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2"+
		"\2\2\u0119L\3\2\2\2\u011a\u0118\3\2\2\2\u011b\u0121\7$\2\2\u011c\u011d"+
		"\7^\2\2\u011d\u0120\7$\2\2\u011e\u0120\13\2\2\2\u011f\u011c\3\2\2\2\u011f"+
		"\u011e\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u0122\3\2\2\2\u0121\u011f\3\2"+
		"\2\2\u0122\u0124\3\2\2\2\u0123\u0121\3\2\2\2\u0124\u0125\7$\2\2\u0125"+
		"N\3\2\2\2\u0126\u0128\t\7\2\2\u0127\u0126\3\2\2\2\u0128\u0129\3\2\2\2"+
		"\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012aP\3\2\2\2\u012b\u012c\5"+
		"\21\7\2\u012c\u012d\3\2\2\2\u012d\u012e\b\'\5\2\u012e\u012f\b\'\6\2\u012f"+
		"R\3\2\2\2\u0130\u0131\5\23\b\2\u0131\u0132\3\2\2\2\u0132\u0133\b(\4\2"+
		"\u0133T\3\2\2\2\u0134\u0135\5\r\5\2\u0135\u0136\3\2\2\2\u0136\u0137\b"+
		")\7\2\u0137V\3\2\2\2\u0138\u0139\5\23\b\2\u0139\u013a\3\2\2\2\u013a\u013b"+
		"\b*\4\2\u013bX\3\2\2\2\u013c\u013e\t\6\2\2\u013d\u013c\3\2\2\2\u013e\u013f"+
		"\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140Z\3\2\2\2\u0141"+
		"\u0142\5\17\6\2\u0142\u0143\3\2\2\2\u0143\u0144\b,\b\2\u0144\\\3\2\2\2"+
		"\u0145\u0146\7J\2\2\u0146\u0147\7g\2\2\u0147\u0148\7n\2\2\u0148\u0149"+
		"\7n\2\2\u0149\u014a\7q\2\2\u014a\u014b\7\"\2\2\u014b\u014c\7Y\2\2\u014c"+
		"\u014d\7q\2\2\u014d\u014e\7t\2\2\u014e\u014f\7n\2\2\u014f\u0150\7f\2\2"+
		"\u0150^\3\2\2\2\u0151\u0152\5\21\7\2\u0152\u0153\3\2\2\2\u0153\u0154\b"+
		".\6\2\u0154`\3\2\2\2\22\2\3\4\5\6lrx{\u0080\u00a5\u0118\u011f\u0121\u0129"+
		"\u013f\t\7\3\2\4\4\2\b\2\2\6\2\2\t\5\2\4\5\2\4\6\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}