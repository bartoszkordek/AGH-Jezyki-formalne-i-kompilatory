from ply import lex

# List of token names.
tokens = (
    'DOCUMENTCLASS',
    'BEGIN_DOCUMENT',
    'END_DOCUMENT',
    'TEXT',

#    'NUMBER',
#    'PLUS',
#    'MINUS',
#    'TIMES',
#    'DIVIDE',
#    'LPAREN',
#    'RPAREN',
)

# Regular expression rules for simple tokens
t_DOCUMENTCLASS = r'\\documentclass'
t_BEGIN_DOCUMENT=r'\\begin\{document\}'
t_END_DOCUMENT=r'\\end\{document\}'
t_TEXT=r'[a-zA-Z0-9][a-zA-Z0-9 ]*'

# t_PLUS    = r'\+'
# t_MINUS   = r'-'
# t_TIMES   = r'\*'
# t_DIVIDE  = r'/'
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'

# # A regular expression rule with some action code
# def t_NUMBER(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t


def t_newline(t):
    r'\n+'
    # t.lexer.lineno += len(t.value)
    t.lexer.lineno += t.value.count("\n")

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
