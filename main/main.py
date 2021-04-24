# -----------------------------------------------------------------------------
# A simple PLY Latex to HTML parser schema.
# -----------------------------------------------------------------------------

tokens = (
    'TEXT','BEGIN', 'END', 'DOCUMENTCLASS', 'BOLD'
    )

# Tokens

t_BEGIN         = r'\\begin\{[a-zA-Z0-9_ ]*\}'
t_END           = r'\\end\{[a-zA-Z0-9_ ]*\}'
t_DOCUMENTCLASS = r'\\documentclass\[.*\]\{[a-zA-Z0-9_ ]*\}'
t_BOLD          = r'\\textbf\{[a-zA-Z0-9_ ]*\}'
#t_TEXT          = r'[a-zA-Z0-9_! ]*[a-zA-Z0-9_!]'

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

def p_expression_bold(p):
    'expression : BOLD'
    try:
        input_label = p[1]
        open_bracket = input_label.index('{')
        close_bracket = input_label.index('}')
        extracted_bolded_text = input_label[open_bracket+1 : close_bracket]
        p[0] = extracted_bolded_text
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0

def p_expression_schema(p):
    '''expression : BEGIN expression
                  | expression END'''
    p[0] = '<html>' + '<head>' + '</head>' + p[1] + p[2]  + '</html>'

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