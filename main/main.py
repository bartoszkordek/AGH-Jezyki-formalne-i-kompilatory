# -----------------------------------------------------------------------------
# A simple PLY Latex to HTML parser schema.
# -----------------------------------------------------------------------------

tokens = (
    'TEXT','BEGIN', 'END', 'DOCUMENTCLASS', 'BOLD', 'ITALIC', 'NEWLINE'
    )

# Tokens

t_BEGIN         = r'\\begin\{[a-zA-Z0-9_ ]*\}'
t_END           = r'\\end\{[a-zA-Z0-9_ ]*\}'
t_DOCUMENTCLASS = r'\\documentclass\[.*px\]\{[a-zA-Z0-9_ ]*\}'
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
    '''expression : BEGIN multiexpression END'''
    try:
        p[0] = '<!DOCTYPE html>' +'\n'+ '<html>' +'\n'+ '<head>' +'\n'+ '</head>' +'\n'+ '<body>' +'\n'+ p[2] +'\n'+ '</body>' +'\n'+ '</html>'
    except LookupError:
        print(f"Undefined name {p[2]!r}")
        p[0] = 0

def p_expression_multi(p):
    'multiexpression : multiexpression multiexpression'
    try:
        p[0] = p[1] +'\n'+ p[2]
    except LookupError:
        print(f"Undefined name {p[1]!r} or {p[2]!r}")
        p[0] = 0

def p_expression_bold(p):
    'multiexpression : BOLD'
    try:
        input_label = p[1]
        open_bracket = input_label.index('{')
        close_bracket = input_label.index('}')
        extracted_bolded_text = input_label[open_bracket+1 : close_bracket]
        p[0] =  '<b>' +'\n'+ extracted_bolded_text +'\n'+ '</b>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0


def p_expression_italic(p):
    'multiexpression : ITALIC'
    try:
        input_label = p[1]
        open_bracket = input_label.index('{')
        close_bracket = input_label.index('}')
        extracted_italic_text = input_label[open_bracket+1 : close_bracket]
        p[0] = '<i>' +'\n'+ extracted_italic_text +'\n'+ '</i>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0


def p_expression_text(p):
    'multiexpression : TEXT'
    try:
        p[0] = p[1]
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0

import ply.yacc as yacc
yacc.yacc()

#read from file
f = open("main/input/sample.tex", "r")
yacc.parse(f.read())

#read from console
# while True:
#     try:
#         s = input('result > ')
#     except EOFError:
#         break
#     yacc.parse(s)