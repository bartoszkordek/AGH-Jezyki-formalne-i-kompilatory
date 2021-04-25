import ply.yacc as yacc

# Get the token map from the lexer.
from mylexer import tokens

# grammar rules


def p_statement_preamble(p):
    'statement : DOCUMENTCLASS expression'
    p[0] = '<!DOCTYPE html>' + p[2]

def p_expression_x(p):
    'expression : USE_PACKAGE expression'
    p[0] = '\n<header>' + '\n</header>' + p[2]

def p_expression_page(p):
    'expression : BEGIN_DOCUMENT expression END_DOCUMENT'
    p[0] = '\n<html lang="en">' + '\n<body>' + \
        p[2] + '\n</body>' + '\n</html>'


def p_expression_text(p):
    'expression : TEXT'
    p[0] = '\n'+p[1]


def p_expression_unordered_list(p):
    'expression : BEGIN_ULIST expression END_ULIST'
    p[0] = '\n<ul>' + p[2] + '\n</ul>'


def p_expression_ordered_list(p):
    'expression : BEGIN_OLIST expression END_OLIST'
    p[0] = '\n<ol>' + p[2] + '\n</ol>'


def p_expression_listitem(p):
    '''expression : ITEM expression expression 
                  | ITEM expression '''
    if len(p) == 4:
        p[0] = '\n<li>' + p[2] + '</li>' + p[3]
    else:
        p[0] = '\n<li>' + p[2] + '</li>'


# Error rule for syntax errors


def p_error(p):
    print(p)
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
