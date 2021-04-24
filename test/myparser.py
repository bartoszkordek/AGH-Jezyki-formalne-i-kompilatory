import ply.yacc as yacc

# Get the token map from the lexer.
from mylexer import tokens

# grammar rules


def p_expression_text(p):
    'expression : BEGIN_DOCUMENT expression END_DOCUMENT'
    p[0] = '<html lang="en">\n' + p[2] + '\n</html>'


def p_expression_text(p):
    'expression : BEGIN_DOCUMENT body END_DOCUMENT'
    p[0] = '<body>' + p[2] + '<body>'


def p_expression_body(p):
    'body : TEXT'
    p[0] = p[1]


# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]


# def p_term_times(p):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]


# def p_term_div(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]


# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]


# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]


# def p_factor_expr(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
