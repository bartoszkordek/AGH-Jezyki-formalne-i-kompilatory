from ply import lex

# List of token names.
tokens = (
    'DOCUMENTCLASS',
    'BEGIN_DOCUMENT',
    'END_DOCUMENT',
    'TEXT',
    'ITEM',
    'BEGIN_ULIST',
    'END_ULIST',
    'BEGIN_OLIST',
    'END_OLIST',
    'ITALIC',
    'BOLD',
    'LBRACE',
    'RBRACE',
)

# Regular expression rules for simple tokens
t_DOCUMENTCLASS = r'\\documentclass.*'
t_BEGIN_DOCUMENT = r'\\begin\{document\}'
t_END_DOCUMENT = r'\\end\{document\}'
t_TEXT = r'\S+'
t_ITEM = r'\\item'
t_BEGIN_ULIST = r'\\begin\{itemize\}'
t_END_ULIST = r'\\end\{itemize\}'
t_BEGIN_OLIST = r'\\begin\{enumerate\}'
t_END_OLIST = r'\\end\{enumerate\}'
t_ITALIC=r'\\textit'
t_BOLD=r'\\textbf'
t_LBRACE=r'\{'
t_RBRACE=r'\}'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_COMMENT(t):
    r'%+.*\n'
    pass

# def t_NUMBER(t):
#      r'\d+'
#      t.value = int(t.value)    
#      return t

# def t_lbrace(t):
#     r'\{'
#     t.type = '{'
#     return t


# def t_rbrace(t):
#     r'\}'
#     t.type = '}'
#     return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' '


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Build the lexer
lexer = lex.lex()
