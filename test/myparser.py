import ply.yacc as yacc

# Get the token map from the lexer.
from mylexer import tokens

# grammar rules


def p_statement_preamble(p):
    'statement : DOCUMENTCLASS head body'
    p[0] = '<!DOCTYPE html>'+'\n<html lang="en">' + p[2] + p[3]+'\n</html>'


def p_header(p):
    '''head : USE_PACKAGE head
            | USE_PACKAGE'''
    p[0] = '\n<head>' + '\n</head>'


def p_body(p):
    'body : BEGIN_DOCUMENT expression END_DOCUMENT'
    p[0] = '\n<body>\n' + p[2] + '\n</body>'

def p_break(p):
    '''expression : BREAK expression
            | BREAK'''
    if len(p) == 3:
        p[0] = '</br>' + p[2]
    else:
        p[0] = '</br>'

def p_expression_text(p):
    '''expression : TEXT expression
                  | TEXT'''
    if len(p) == 3:
        p[0] = p[1] + " " + p[2]
    else:
        p[0] = p[1]

def p_expression_caption(p):
    '''expression : CAPTION LBRACE expression RBRACE expression
                  | CAPTION LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '<caption>' + p[3] + '</caption>' + p[5]
    else:
        p[0] = '<caption>' + p[3] + '</caption>'


def p_expression_table(p):
    '''expression : BEGIN_TABULAR LBRACE expression RBRACE expression END_TABULAR expression
                  | BEGIN_TABULAR LBRACE expression RBRACE expression END_TABULAR'''
    if len(p) == 8:
        p[0] = '<table>' + p[5] + '</table>' + p[7]
    else:
        p[0] = '<table>' + p[5] + '</table>'


def p_expression_paragraph(p):
    '''expression : PARAGRAPH LBRACE expression RBRACE expression
                  | PARAGRAPH LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '<p>' + p[3] + '</p>' + p[5]
    else:
        p[0] = '<p>' + p[3] + '</p>'


def p_expression_bold(p):
    '''expression : BOLD LBRACE expression RBRACE expression
                  | BOLD LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '<strong>' + p[3] + '</strong>' + p[5]
    else:
        p[0] = '<strong>' + p[3] + '</strong>'


def p_expression_italic(p):
    '''expression : ITALIC LBRACE expression RBRACE expression
                  | ITALIC LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '<em>' + p[3] + '</em>' + p[5]
    else:
        p[0] = '<em>' + p[3] + '</em>'


def p_expression_underline(p):
    '''expression : UNDERLINE LBRACE expression RBRACE expression
                  | UNDERLINE LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '<u>' + p[3] + '</u>' + p[5]
    else:
        p[0] = '<u>' + p[3] + '</u>'


def p_expression_url(p):
    '''expression : URL LBRACE expression RBRACE expression
                  | URL LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '<a href=' + p[3] + '>' + p[3] + '</a>' + p[5]
    else:
        p[0] = '<a href=' + p[3] + '>' + p[3] + '</a>'


def p_expression_graphicspath(p):
    '''expression : GRAPHICS_PATH LBRACE expression RBRACE expression
                  | GRAPHICS_PATH LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '''<img src="''' + p[3] + '''">''' + p[5]
    else:
        p[0] = '''<img src="''' + p[3] + '''">'''


def p_expression_includegraphics(p):
    '''expression : INCLUDE_GRAPHICS TEXT LBRACE expression RBRACE expression
                  | INCLUDE_GRAPHICS LBRACE expression RBRACE expression
                  | INCLUDE_GRAPHICS LBRACE expression RBRACE'''
    if len(p) == 7:
        attributes = p[2][1:-1]
        p[0] = '''<img src="''' + p[4] + '''"''' + attributes + '''>''' + p[6]
    elif len(p) == 6:
        p[0] = '''<img src="''' + p[3] + '''">''' + p[5]
    else:
        p[0] = '''<img src="''' + p[3] + '''">'''


def p_expression_chapter(p):
    '''expression : CHAPTER LBRACE expression RBRACE expression
                  | CHAPTER LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '<h1>' + p[3] + '</h1>' + p[5]
    else:
        p[0] = '<h1>' + p[3] + '</h1>'


def p_expression_section(p):
    '''expression : SECTION LBRACE expression RBRACE expression
                  | SECTION LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '<h2>' + p[3] + '</h2>' + p[5]
    else:
        p[0] = '<h2>' + p[3] + '</h2>'


def p_expression_subsection(p):
    '''expression : SUBSECTION LBRACE expression RBRACE expression
                  | SUBSECTION LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '<h3>' + p[3] + '</h3>' + p[5]
    else:
        p[0] = '<h3>' + p[3] + '</h3>'


def p_expression_subsubsection(p):
    '''expression : SUBSUBSECTION LBRACE expression RBRACE expression
                  | SUBSUBSECTION LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '<h4>' + p[3] + '</h4>' + p[5]
    else:
        p[0] = '<h4>' + p[3] + '</h4>'


def p_title(p):
    'expression : TITLE LBRACE TEXT RBRACE'
    p[0] = '<i>' + p[3] + '</i>'


def p_expression_unordered_list(p):
    '''expression : BEGIN_ULIST listitems END_ULIST expression
                  | BEGIN_ULIST listitems END_ULIST'''
    if len(p) == 5:
        p[0] = '\n<ul>' + p[2] + '\n</ul>' + p[4]
    else:
        p[0] = '\n<ul>' + p[2] + '\n</ul>'


def p_expression_ordered_list(p):
    '''expression : BEGIN_OLIST listitems END_OLIST expression
                  | BEGIN_OLIST listitems END_OLIST'''
    if len(p) == 5:
        p[0] = '\n<ol>' + p[2] + '\n</ol>' + p[4]
    else:
        p[0] = '\n<ol>' + p[2] + '\n</ol>'


def p_listitems(p):
    '''listitems : ITEM expression listitems
                 | ITEM expression'''
    if len(p) == 4:
        p[0] = '\n<li>' + p[2] + '</li>' + p[3]
    else:
        p[0] = '\n<li>' + p[2] + '</li>'


# def p_expression_newline(p):
#     '''expression : NEWLINE expression
#                   | NEWLINE'''
#     if len(p) == 3:
#         p[0] = '<br/>' + p[2]
#     else:
#         p[0] = p[1]


# def p_expression_newline_2(p):
#     '''expression : TEXT NEWLINE_2'''
#     p[0] = p[1] + '<br/>'

# Error rule for syntax errors


def p_error(p):
    print(p)
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()