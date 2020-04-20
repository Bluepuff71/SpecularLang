// Define a grammar called Hello
grammar SpecLang;

tokens { INDENT, DEDENT }

@lexer::header{
from DenterHelper import DenterHelper
from SpecLangParser import SpecLangParser
}
@lexer::members {
class SpecDenter(DenterHelper):
    def __init__(self, lexer, nlToken, indentToken, dedentToken, ignoreEOF):
        super().__init__(nlToken, indentToken, dedentToken, ignoreEOF)
        self.lexer: SpecLangLexer = lexer

    def pullToken(self):
        return super(SpecLangLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.SpecDenter(self, self.NEWLINE, SpecLangParser.INDENT, SpecLangParser.DEDENT, False)
    return self.denter.nextToken()

}

/*
* Parser Rules
*/

block : INDENT (statement (NEWLINE)?)+? DEDENT;

statement : IF condition ';' block #ifStatement
          | SCENE STRING ';' block #sceneStatement
          | '@' term ':' term #dialog //Needs to be updated with emotion support
          | <assoc=right>  (GLOBAL)? ID '=' expression #assignment;

expression : '&' STRING (':' STRING)*? #choice
           | expression ('*' | '/') expression #mult
           | expression ('+' | '-') expression #add
           | '(' expression ')' #paren
           | term #expr_term;

condition : NOT condition
          | condition ('==' | '!=') condition
          | condition AND condition
          | condition OR condition
          | '(' condition ')'
          | expression;

term : 'None'
     | 'True'
     | 'False'
     | ID
     | STRING
     | NUMBER;


/*
* Lexer Rules
*/

IF : 'if';
SCENE : 'scene';
GLOBAL : 'global';
AND : 'and';
OR : 'or';
NOT : 'not';

STRING : '"' ( '\\"' | . )*? '"' ;
//EMOTION : '(' [a-zA-Z] ')';
ID : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ;

NEWLINE : ('\r'? '\n' '\t'*); // note the ' '*
WS: [ ]+? -> skip;