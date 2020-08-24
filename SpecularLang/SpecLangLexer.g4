lexer grammar SpecLangLexer;

tokens { INDENT, DEDENT, NEWLINE }

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
* Lexer 1.0 Rules
*/
LEFT_BRACKET : '{';
RIGHT_BRACKET : '}';
COMMA : ',';

/*
* Lexer 2.0 Rules
*/
fragment LEFT_PARAN : '(';
fragment RIGHT_PARAN : ')';
fragment FR_NEWLINE : ('\r'? '\n' ('\t'* | ' '*));
fragment WHITESPACE : [ ]+?;

//DIALOG_START : '$' -> pushMode(DIALOG_START_MODE);

START : 'Start' -> pushMode(CODE_MODE);
SET : 'Set' -> pushMode(CODE_MODE);
IF : 'If' -> pushMode(CODE_MODE);
WHILE : 'While' -> pushMode(CODE_MODE);
DO_Upper : 'Do' -> pushMode(CODE_MODE);
ACTOR_NAME : [A-Z_0-9 .,']+[A-Z_0-9] -> mode(DIALOG_START_MODE);
WS : WHITESPACE -> skip;

mode CODE_MODE;
OPEN_PARAN : LEFT_PARAN;
CLOSE_PARAN : RIGHT_PARAN;
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
STRING : '"' ( '\\"' | . )*? '"';
NUMBER : [0-9]+;
C_NEWLINE : FR_NEWLINE -> popMode, type(NEWLINE); // note the ' '*
C_WS: WHITESPACE -> skip;

mode DIALOG_START_MODE;
EMOTION_START : LEFT_PARAN -> mode(EMOTION_MODE);
//DS_NEWLINE : FR_NEWLINE -> type(NEWLINE), mode(DIALOG_TEXT_MODE);
DS_WS : WHITESPACE ->  skip;

mode EMOTION_MODE;
EMOTION : [a-zA-Z_0-9]+;
EMOTION_END : RIGHT_PARAN -> mode(DIALOG_TEXT_MODE);

mode DIALOG_TEXT_MODE;
ANYCHAR : [a-zA-Z_0-9]+;
DT_NEWLINE : FR_NEWLINE -> type(NEWLINE);



