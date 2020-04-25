// Define a grammar called Hello
grammar SpecLang;

tokens { INDENT, DEDENT }

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
* Parser Rules
*/
program : (assignment NEWLINE)* (scene_statement)+;

block : (simple_statement NEWLINE | complex_statement) (block)? ;

simple_statement : dialog
                 | assignment
                 | '(' stage_direction ')';

stage_direction : ENTER (ID | STRING)
                | (ID | STRING) EXITS
                | MOVE (ID | STRING) TO (ID | STRING);

assignment: <assoc=right>  (GLOBAL)? ID '=' expression;

dialog: '@' (ID | STRING) ':' STRING NEXT?; //Needs to be updated with emotion support

complex_statement : ifstatement
                  | whileLoop;
                  //| DO ';' INDENT block DEDENT WHILE expression ';' #doWhileLoop

ifstatement: IF expression ';' INDENT block DEDENT (else_if_statement)*? else_statement?;

else_if_statement : ELIF  expression ';' INDENT block DEDENT;

else_statement : ELSE ';' INDENT block DEDENT;

whileLoop: WHILE expression ';' INDENT block DEDENT;

scene_statement : SCENE STRING ';' INDENT block DEDENT ;

expression : (NOT | SUB) expression #unary
           | expression (MUL | DIV) expression #mult
           | expression (ADD | SUB) expression #add
           | expression ('==' | '!=') expression #equal
           | expression AND expression #and
           | expression OR expression #or
           | '(' expression ')' #paren
           | '[' STRING (',' STRING)*? ']' #choice
           | (NONE | TRUE | FALSE | ID | STRING | NUMBER) #term;

/*
* Lexer Rules
*/
NEXT: '->';
WHILE : 'while';
ENTER: 'enter';
EXITS: 'exits';
MOVE: 'move';
TO: 'to';
DO : 'do';
IF : 'if';
ELIF: 'elif';
ELSE: 'else';
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