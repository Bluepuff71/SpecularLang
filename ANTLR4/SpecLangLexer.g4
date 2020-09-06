lexer grammar SpecLangLexer;

tokens { INDENT, DEDENT, NEWLINE, STRING, SEPARATOR, OPEN, CLOSE }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from SpecLangParser import SpecLangParser
}
@lexer::members {
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

}

/*
* Lexer 2.0 Rules
*/
fragment LEFT_PARAN : '(' ;
fragment RIGHT_PARAN : ')';
fragment LEFT_SQUARE_BRACKET : '[';
fragment RIGHT_SQUARE_BRACKET : ']';
fragment FR_CLEAN_WORD : [a-zA-Z_0-9]+;
fragment FR_NEWLINE : ('\r'? '\n' ('\t'* | ' '*));
fragment FR_STRING : '"' ( '\\"' | . )*? '"';
fragment FR_COMMA : ',';
fragment WHITESPACE : [ ]+?;

START : 'Start' -> pushMode(CODE_MODE);
SET : 'Set' -> pushMode(CODE_MODE);
IF : 'If' -> pushMode(CODE_MODE);
WHILE : 'While' -> pushMode(CODE_MODE);
DO_Upper : 'Do' -> pushMode(CUSTOM_ACTION_MODE);
ACTOR_NAME : [A-Z_0-9 .,']+[A-Z_0-9] -> mode(DIALOG_START_MODE);
WS : WHITESPACE -> skip;

mode CODE_MODE;
OPEN_PARAN : LEFT_PARAN -> type(OPEN);
CLOSE_PARAN : RIGHT_PARAN -> type(CLOSE);
SAYS : 'says';
GLOBALLY : 'globally';
DO_Lower : 'do';
OTHERWISE : 'Otherwise';
AND : 'and';
OR : 'or';
NOT : 'not';
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
EQUAL_TO : 'equal to';
GREATER_THAN : 'greater than';
LESS_THAN : 'less than';
IS : 'is';
TRUE: 'true';
FALSE: 'false';
NONE: 'none';
ID : [a-zA-Z_][a-zA-Z_0-9]*;
C_STRING : FR_STRING -> type(STRING);
NUMBER : [0-9]+;
C_NEWLINE : FR_NEWLINE -> popMode, type(NEWLINE);
C_WS: WHITESPACE -> skip;
PL_START : LEFT_SQUARE_BRACKET -> pushMode(PARAM_LIST_MODE);

mode CUSTOM_ACTION_MODE;
CA_CLEAN_WORD : FR_CLEAN_WORD;
CA_COMMA : FR_COMMA -> type(SEPARATOR);
COLON : ':';
CA_STRING : FR_STRING -> type(STRING);
CA_NEWLINE : FR_NEWLINE -> type(NEWLINE), popMode, pushMode(CODE_MODE);
CA_WS: WHITESPACE -> skip;


mode PARAM_LIST_MODE;
PL_STRING : FR_STRING -> type(STRING);
PL_COMMA : FR_COMMA -> type(SEPARATOR);
PL_END : RIGHT_SQUARE_BRACKET -> popMode;
PL_NEWLINE : FR_NEWLINE -> skip;
PL_WS : WHITESPACE ->  skip;

mode DIALOG_START_MODE;
EMOTION_START : LEFT_PARAN -> mode(EMOTION_MODE);
DS_NEWLINE : FR_NEWLINE -> mode(DIALOG_TEXT_MODE), type(NEWLINE);
DS_WS : WHITESPACE ->  skip;

mode EMOTION_MODE;
EMOTION : FR_CLEAN_WORD;
EMOTION_END : RIGHT_PARAN;
E_NEWLINE : FR_NEWLINE -> mode(DIALOG_TEXT_MODE), type(NEWLINE);

mode DIALOG_TEXT_MODE;
DT_NEWLINE : FR_NEWLINE -> mode(DEFAULT_MODE), type(NEWLINE);
DT_STRING : FR_STRING -> type(STRING);
ANYCHAR : ~('\r' | '\n' | '\t')+;
