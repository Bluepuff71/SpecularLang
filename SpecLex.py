import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'scene': 'SCENE',
    'global': 'GLOBAL',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'None': 'NONE',
    'is': 'IS',
    'True': 'TRUE',
    'False': 'FALSE'
}

operators = [
    'EQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'GREATER',
    'LESS',
    'GREATEREQ',
    'LESSEQ',
    'EQUALTO',
]

# List of token names.   This is always required
tokens = [
             'ID',
             'DIALOG',
             'SEMI',
             'OPSEP',
             'NUMBER',
             'STRING',
             'LPAREN',
             'RPAREN',
             'LSBRACKET',
             'RSBRACKET',
         ] + list(reserved.values()) + operators

# Regular expression rules for simple tokens
t_EQUAL = r'='
t_STRING = r'".*"'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSBRACKET = r'\{'
t_RSBRACKET = r'\}'
t_DIALOG = r'\$'
t_OPSEP = r':'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# A regular expression rule with some action code
def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_BLOCKSEP(t):
    r'\n'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

