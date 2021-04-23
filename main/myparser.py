from ply import yacc
import main.mylexer as mylexer

tokens = mylexer.tokens

# grammar rules


def p_assign(p):
    '''assign : NAME EQUALS expr'''
    vars[p[1]] = p[3]


def p_expr_plus(p):
    '''expr : expr PLUS term'''
    p[0] = p[1]+p[3]


# def p_expr(p):
#     '''expr : expr PLUS term
#             | expr MINUS term
#             | term '''
#     p[0]

def p_term_mul(p):
    '''term : term TIMES factor'''
    p[0] = p[1]*p[3]


# def p_term(p):
#     '''term : term TIMES factor
#             | term DIVIDE factor
#             | factor'''


# def p_factor(p):
#     '''term : NUMBER'''

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]


def p_factor(p):
    '''factor : NUMBER'''
    p[0] = p[1]


# Build the parser
yacc.yacc()

data = "x=3*4+5*6"
yacc.parse(data)
