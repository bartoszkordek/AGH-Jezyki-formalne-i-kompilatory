# -----------------------------------------------------------------------------
# A simple PLY Latex to HTML parser schema.
# -----------------------------------------------------------------------------

tokens = (
    'NAME','BEGIN', 'END'
    )

# Tokens

t_BEGIN   = r'\\begin'
t_END     = r'\\end'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

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
names = { 'Hello'}

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_begin(p):
    'expression : BEGIN'
    try:
        p[0] = '<html>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0
		
def p_expression_end(p):
    'expression : END'
    try:
        p[0] = '<\html>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0
		
def p_expression_name(p):
    'expression : NAME'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0

def p_expression_schema(p):
    '''expression : expression BEGIN expression
                  | expression NAME expression
                  | expression END expression'''
    p[0] = '<html>' + p[2] + '</html>'
	
def p_error(p):
    print(f"Syntax error at {p.value!r}")

import ply.yacc as yacc
yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    yacc.parse(s)