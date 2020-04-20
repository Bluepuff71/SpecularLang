import csv

from SpecLex import tokens
import ply.yacc as yacc

rows = []
row_num = 0
precedence = (
    ('right', 'EQUAL'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQUALTO'),
    ('nonassoc', 'GREATER', 'GREATEREQ', 'LESS', 'LESSEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'NOT'),
)

def p_program_block(p):
    """program : block"""
    p[0] = p[1]

def p_program_assignment(p):
    """program : assignment"""
    p[0] = p[1]

def p_block_scene(p):
    """block : SCENE STRING SEMI"""

def p_block_if(p):
    """block : IF condition SEMI """

def p_condition(p):
    """condition : condition EQUALS condition
                | """
    rows.append(createRow("if", tags=[p[2], p[1], p[3]]))

def p_statement(p):
    """statement : assignment"""
    p[0] = p[1]


def p_assignment_string(p):
    """assignment : ID EQUAL STRING"""
    rows.append(createRow("assignString", dialogueText=p[3], tags=[p[1]]))

def p_assignment_int(p):
    """assignment : ID EQUAL NUMBER"""
    rows.append(createRow("assignInt", effect=p[3], tags=[p[1]]))


#Not worrying about this yet
# def p_expr_plus(p):
#     """expr : expr PLUS expr"""
#     #createRow("addTemp", tags=[p[1], p[2]])
#
# def p_expr_minus(p):
#     """expr : expr MINUS expr"""
#     #createRow("addTemp", tags=[p[1], -p[2]])
#
# def p_expr_times(p):
#     """expr : expr TIMES expr"""
#     #createRow("timesTemp", tags=[p[1], p[2]])
#
# def p_expr_divide(p):
#     """expr : expr DIVIDE expr"""
#     #createRow("divideTemp", tags=[p[1], p[2]])
#
# def p_expr_term(p):
#     """expr : term"""
#     p[0] = p[1]
#
# def p_expr_number(p):
#     """expr : NUMBER"""
#     p[0] = p[1]
#
# # EVERYTHING THE PARSER WILL HANDLE
# def p_expr_num_plus(p):
#     """expr : NUMBER PLUS NUMBER"""
#     p[0] = p[1] + p[3]
#
# def p_expr_num_minus(p):
#     """expr : NUMBER MINUS NUMBER"""
#     p[0] = p[1] - p[3]
#
# def p_expr_num_times(p):
#     """expr : NUMBER TIMES NUMBER"""
#     p[0] = p[1] * p[3]
#
# def p_expr_num_divide(p):
#     """expr : NUMBER DIVIDE NUMBER"""
#     p[0] = p[1] / p[3]
#
# def p_expr_num_mod(p):
#     """expr : NUMBER MOD NUMBER"""
#     p[0] = p[1] % p[3]
#
#
#


def createRow(actionType, dialogueText = '', speakerEmotion = 'Neutral', effect = '', label = '', tags = None, keepPreviousTarget = False, waitTime = '', characterName = 'None', conditions=None):
    global row_num
    if tags is None:
        tags = []
    row = [['NewRow_{}'.format(row_num),actionType,dialogueText,speakerEmotion,effect,label,tags,keepPreviousTarget,waitTime,characterName]]
    row_num += 1
    return row

def writeRowBuffer(fileName):
    csv_file = open(fileName, 'w', newline='')
    csv_writer = csv.writer(csv_file, quotechar='"', delimiter=',',
                     quoting=csv.QUOTE_ALL, skipinitialspace=True)
    csv_writer.writerow(['---','actionType','dialogueText','speakerEmotion','effect','label','tags','keepPreviousTarget','waitTime','targetActorProperties'])
    for row in rows:
        csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], createTags(row[6]), row[7], row[8], createActorProperties(row[9])])
    csv_file.close()
    rows.clear()

data = '''togami = 0'''


def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('Calc >')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s, debug=True)
    print(result)
