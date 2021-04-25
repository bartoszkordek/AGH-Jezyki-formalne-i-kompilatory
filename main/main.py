# -----------------------------------------------------------------------------
# A simple PLY Latex to HTML parser schema.
# -----------------------------------------------------------------------------

tokens = (
    'TEXT',
    'BEGIN_DOCUMENT', 
    'END_DOCUMENT', 
    'DOCUMENTCLASS', 
    'BOLD', 
    'ITALIC', 
    'UNDERLINE', 
    'NEWLINE',
    'ITEM',
    'BEGIN_ULIST',
    'END_ULIST',
    'BEGIN_OLIST',
    'END_OLIST'
    )

# Tokens

t_BEGIN_DOCUMENT   = r'\\begin\{document*\}'
t_END_DOCUMENT     = r'\\end\{document*\}'
t_DOCUMENTCLASS    = r'\\documentclass\[.*px\]\{[a-zA-Z0-9_ ]*\}'
t_BOLD             = r'\\textbf\{[a-zA-Z0-9_ ]*\}'
t_ITALIC           = r'\\textit\{[a-zA-Z0-9_ ]*\}'
t_UNDERLINE        = r'\\underline\{[a-zA-Z0-9_ ]*\}'
t_NEWLINE          = r'\\\\'
t_TEXT             = r'[a-zA-Z0-9_!,\. ]*[a-zA-Z0-9_!,\.]'
t_ITEM             = r'\\item'
t_BEGIN_ULIST      = r'\\begin\{itemize\}'
t_END_ULIST        = r'\\end\{itemize\}'
t_BEGIN_OLIST      = r'\\begin\{enumerate\}'
t_END_OLIST        = r'\\end\{enumerate\}'


def extract_moustachioed_bracket_content(input_label):
    open_bracket = input_label.index('{')
    close_bracket = input_label.index('}')
    extracted_text = input_label[open_bracket+1 : close_bracket]
    return extracted_text

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
    '''expression : BEGIN_DOCUMENT multiexpression END_DOCUMENT'''
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
        extracted_text = extract_moustachioed_bracket_content(input_label)
        p[0] =  '<b>' +'\n'+ extracted_text +'\n'+ '</b>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0


def p_expression_italic(p):
    'multiexpression : ITALIC'
    try:
        input_label = p[1]
        extracted_text = extract_moustachioed_bracket_content(input_label)
        p[0] = '<i>' +'\n'+ extracted_text +'\n'+ '</i>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0


def p_expression_underline(p):
    'multiexpression : UNDERLINE'
    try:
        input_label = p[1]
        extracted_text = extract_moustachioed_bracket_content(input_label)
        p[0] = '<u>' +'\n'+ extracted_text +'\n'+ '</u>'
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


def p_expression_newline(p):
    'multiexpression : NEWLINE'
    try:
        p[0] = '</br>'
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0


def p_expression_unordered_list(p):
    'multiexpression : BEGIN_ULIST multiexpression END_ULIST'
    p[0] = '\n<ul>' + p[2] + '\n</ul>'


def p_expression_ordered_list(p):
    'multiexpression : BEGIN_OLIST multiexpression END_OLIST'
    p[0] = '\n<ol>' + p[2] + '\n</ol>'


def p_expression_item(p):
    'multiexpression : ITEM TEXT'
    try:
        p[0] = '\n<li>' + p[2] + '</li>'
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