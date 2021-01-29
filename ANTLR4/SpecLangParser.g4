parser grammar SpecLangParser;

options { tokenVocab=SpecLangLexer; }


/*
* Parser 2.0 Rules
*/
program : (scene_statement)+;

scene_statement : START ID INDENT block DEDENT;

block :  (simple_statement NEWLINE | complex_statement) (block)?;

simple_statement : assignment
                 | play_scene;


complex_statement : dialog
                  | ifstatement
                  | whileLoop
                  | custom_statement;

play_scene : PLAY ID;


dialog : ACTOR_NAME emotion? INDENT dialog_block NEWLINE DEDENT;

dialog_block : (ANYCHAR | STRING);

emotion : EMOTION_START EMOTION EMOTION_END;

custom_statement : DO_Upper CA_CLEAN_WORD (custom_param_name_list? custom_params_list? | NEWLINE);

custom_param_name_list : COLON CA_CLEAN_WORD (SEPARATOR CA_CLEAN_WORD)*;

custom_params_list : INDENT ( STRING | param_list ) NEWLINE DEDENT;

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
           | OPEN expression CLOSE #paren
           | param_list #choice
           | (NONE | TRUE | FALSE | ID | STRING | NUMBER) #term;

param_list : PL_START STRING (SEPARATOR STRING)*? PL_END;

or_equal_to_modifier : OR EQUAL_TO;

