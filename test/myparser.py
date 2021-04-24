import ply.yacc as yacc

# Get the token map from the lexer.
from mylexer import tokens

# grammar rules


def p_statement_preamble(p):
    'statement : DOCUMENTCLASS expression'
    p[0] = '<!DOCTYPE html>\n' + p[2]


def p_expression_page(p):
    'expression : BEGIN_DOCUMENT expression END_DOCUMENT'
    p[0] = '<html lang="en">\n' + '<body>\n\t' + \
        p[2] + '\n</body>' + '\n</html>'


def p_expression_text(p):
    'expression : TEXT'
    p[0] = p[1]


def p_expression_unordered_list(p):
    'expression : BEGIN_ULIST listitem END_ULIST'
    p[0] = '<ul>' + p[2] + '</ul>'


def p_listitems(p):
    '''listitem : ITEM expression listitem 
                 | ITEM expression'''
    if len(p) == 2:
        p[0] ='<li>' + p[2] + '</li>' + p[2]
    else:
        p[0] = '<li>' + p[2] + '</li>'


def p_expression_ordered_list(p):
    'expression : BEGIN_OLIST expression END_OLIST'
    p[0] = '<ol>' + p[2] + '</ol>'



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
