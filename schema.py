# -----------------------------------------------------------------------------
# A simple PLY Latex to HTML parser schema.
# -----------------------------------------------------------------------------

tokens = (
    'TEXT','BEGIN', 'END', 'DOCUMENTCLASS'
    )

# Tokens

t_BEGIN         = r'\\begin\{[a-zA-Z0-9_ ]*\}'
t_END           = r'\\end\{[a-zA-Z0-9_ ]*\}'
t_DOCUMENTCLASS = r'\\documentclass\[.*\]\{[a-zA-Z0-9_ ]*\}'
t_TEXT          = r'[a-zA-Z0-9_! ]*[a-zA-Z0-9_!]'

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()


# dictionary of names (for storing variables)
names = { }

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_begin(p):
    'expression : BEGIN'
    try:
        p[0] = '<body>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0
		
def p_expression_end(p):
    'expression : END'
    try:
        p[0] = '</body>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0
		
def p_expression_TEXT(p):
    'expression : TEXT'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0

def p_expression_schema(p):
    '''expression : expression BEGIN expression
                  | expression TEXT expression
                  | expression END expression
                  | expression DOCUMENTCLASS expression'''
    p[0] = '<html>' + '<head>' + '</head>' + p[1] + p[2] + p[3] + '</html>'

def p_error(p):
    print(f"Syntax error at {p.value!r}")

import ply.yacc as yacc
yacc.yacc()

#read from file
#f = open("sample.tex", "r")
#yacc.parse(f.read())

while True:
    try:
        s = input('result > ')
    except EOFError:
        break
    yacc.parse(s)
