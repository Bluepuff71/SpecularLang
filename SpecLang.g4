// Define a grammar called Hello
grammar SpecLang;

tokens { INDENT, DEDENT }

@lexer::header{
from DenterHelper import DenterHelper
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
* Parser Rules
*/
block : (simple_statement NEWLINE | complex_statement) (block)? ;

simple_statement : '@' (ID | STRING) ':' STRING #dialog //Needs to be updated with emotion support
                 | <assoc=right>  (GLOBAL)? ID '=' expression #assignment;

complex_statement : IF expression ';' INDENT block DEDENT #ifStatement
                  | SCENE STRING ';' INDENT block DEDENT #sceneStatement;

expression : (NOT | SUB) expression #unary
           | '&' STRING (':' STRING)*? #choice
           | expression (MUL | DIV) expression #mult
           | expression (ADD | SUB) expression #add
           | expression ('==' | '!=') expression #equal
           | expression AND expression #and
           | expression OR expression #or
           | '(' expression ')' #paren
           |  (NONE | TRUE | FALSE | ID | STRING | NUMBER) #term;

/*
* Lexer Rules
*/

IF : 'if';
SCENE : 'scene';
GLOBAL : 'global';
AND : 'and';
OR : 'or';
NOT : 'not';
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
STRING : '"' ( '\\"' | . )*? '"' ;
TRUE: 'True';
FALSE: 'False';
NONE: 'None';
//EMOTION : '(' [a-zA-Z] ')';
ID : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ;

NEWLINE : ('\r'? '\n' ('\t'* | ' '*)); // note the ' '*
WS: [ ]+? -> skip;