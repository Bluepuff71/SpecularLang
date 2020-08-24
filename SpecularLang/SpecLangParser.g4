parser grammar SpecLangParser;

options { tokenVocab=SpecLangLexer; }


/*
* Parser 2.0 Rules
*/
program : (scene_statement)+;

scene_statement : START ID INDENT block DEDENT;

block :  (simple_statement NEWLINE | complex_statement) (block)?;

simple_statement : dialog
                 | assignment
                 | custom_statement;


complex_statement : ifstatement
                  | whileLoop;


dialog : ACTOR_NAME emotion INDENT ANYCHAR DEDENT;

emotion : EMOTION_START EMOTION EMOTION_END;

custom_statement : DO_Upper STRING (INDENT STRING (NEWLINE STRING)* DEDENT)?;

assignment: <assoc=right>  SET ID EQUAL_TO expression (GLOBALLY)?;

ifstatement: IF expression INDENT block DEDENT else_statement?;

whileLoop: WHILE expression INDENT block DEDENT;

else_statement : OTHERWISE INDENT block DEDENT;

expression : (NOT | SUB) expression #unary
           | expression (MUL | DIV) expression #mult
           | expression (ADD | SUB) expression #add
           | expression IS (NOT)? (EQUAL_TO)? expression #equals
           | expression IS GREATER_THAN (or_equal_to_modifier)? expression #greater_than
           | expression IS LESS_THAN (or_equal_to_modifier)? expression #less_than
           | expression AND expression #and
           | expression OR expression #or
           | OPEN_PARAN expression CLOSE_PARAN #paren
           | LEFT_BRACKET STRING (COMMA STRING)*? RIGHT_BRACKET #choice
           | (NONE | TRUE | FALSE | ID | STRING | NUMBER) #term;

or_equal_to_modifier : OR EQUAL_TO;

