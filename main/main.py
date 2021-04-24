# -----------------------------------------------------------------------------
# A simple PLY Latex to HTML parser schema.
# -----------------------------------------------------------------------------

tokens = (
    'TEXT','BEGIN', 'END', 'DOCUMENTCLASS', 'BOLD', 'ITALIC'
    )

# Tokens

t_BEGIN         = r'\\begin\{[a-zA-Z0-9_ ]*\}'
t_END           = r'\\end\{[a-zA-Z0-9_ ]*\}'
t_DOCUMENTCLASS = r'\\documentclass\[.*\]\{[a-zA-Z0-9_ ]*\}'
t_BOLD          = r'\\textbf\{[a-zA-Z0-9_ ]*\}'
t_ITALIC        = r'\\textit\{[a-zA-Z0-9_ ]*\}'
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


def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_begin_end(p):
    'expression : BEGIN expression END'
    try:
        p[0] = '<html>' + '<head>' + '</head>' + '<body>' + p[2] + '</body>' + '</html>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0

def p_expression_sample(p):
    'expression : TEXT expression BOLD BOLD expression'
    try:
        p[0] = 'TEST: ' + p[1] + p[2] + p[3] + p[4] + p[5]
    except LookupError:
        print(f"Undefined name {p[1]!r} or {p[2]!r} ")
        p[0] = 0


def p_expression_bold(p):
    'expression : BOLD'
    try:
        input_label = p[1]
        open_bracket = input_label.index('{')
        close_bracket = input_label.index('}')
        extracted_bolded_text = input_label[open_bracket+1 : close_bracket]
        p[0] =  '<b>' + extracted_bolded_text + '<b>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0


def p_expression_italic(p):
    'expression : ITALIC'
    try:
        input_label = p[1]
        open_bracket = input_label.index('{')
        close_bracket = input_label.index('}')
        extracted_italic_text = input_label[open_bracket+1 : close_bracket]
        p[0] =  '<i>' + extracted_italic_text + '<i>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0


def p_expression_text(p):
    'expression : TEXT'
    try:
        p[0] = p[1]
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0

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