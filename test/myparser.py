import ply.yacc as yacc
from mylexer import Lexer


class Parser(object):
    tokens = Lexer.tokens

    def p_statement_preamble(self, p):
        'statement : DOCUMENTCLASS head body'
        p[0] = '<!DOCTYPE html>'+'\n<html lang="en">' + p[2] + p[3]+'\n</html>'

    def p_header(self, p):
        '''head : USE_PACKAGE head
                | USE_PACKAGE'''
        p[0] = '\n<head>' + '\n</head>'

    def p_body(self, p):
        'body : BEGIN_DOCUMENT expression END_DOCUMENT'
        p[0] = '\n<body>\n' + p[2] + '\n</body>'

    def p_expression_text(self, p):
        '''expression : TEXT expression
                      | TEXT'''
        if len(p) == 3:
            p[0] = p[1] + " " + p[2]
        else:
            p[0] = p[1]

    def p_expression_caption(self, p):
        '''expression : CAPTION LBRACE expression RBRACE expression
                      | CAPTION LBRACE expression RBRACE'''
        if len(p) == 6:
            p[0] = '<caption>' + p[3] + '</caption>' + p[5]
        else:
            p[0] = '<caption>' + p[3] + '</caption>'

    def p_expression_table(self, p):
        '''expression : BEGIN_TABULAR LBRACE expression RBRACE tablerow END_TABULAR expression
                      | BEGIN_TABULAR LBRACE expression RBRACE tablerow END_TABULAR'''
        if len(p) == 8:
            p[0] = '<table style="border: 1px solid black">' + p[5] + '</table>' + p[7]
        else:
            p[0] = '<table style="border: 1px solid black">' + p[5] + '</table>'

    def p_tablerow(self, p):
        '''tablerow : tablecolumn BREAK tablerow
                    | tablecolumn'''
        if len(p) == 4:
            p[0] = '<tr>' + p[1] + '</tr>' + p[3]
        else:
            p[0] = '<tr>' + p[1] + '</tr>'

    def p_tablecolumn(self, p):
        '''tablecolumn : expression COLUMN_DIVIDER tablecolumn
                       | expression'''
        if len(p) == 4:
            p[0] = '<td style="border: 1px solid black">' + p[1] + '</td>' + p[3]
        else:
            p[0] = '<td style="border: 1px solid black">' + p[1] + '</td>'

    def p_expression_paragraph(self, p):
        '''expression : PARAGRAPH LBRACE expression RBRACE expression
                      | PARAGRAPH LBRACE expression RBRACE'''
        if len(p) == 6:
            p[0] = '<p>' + p[3] + '</p>' + p[5]
        else:
            p[0] = '<p>' + p[3] + '</p>'

    def p_expression_bold(self, p):
        '''expression : BOLD LBRACE expression RBRACE expression
                      | BOLD LBRACE expression RBRACE'''
        if len(p) == 6:
            p[0] = '<strong>' + p[3] + '</strong>' + p[5]
        else:
            p[0] = '<strong>' + p[3] + '</strong>'

    def p_expression_italic(self, p):
        '''expression : ITALIC LBRACE expression RBRACE expression
                      | ITALIC LBRACE expression RBRACE'''
        if len(p) == 6:
            p[0] = '<em>' + p[3] + '</em>' + p[5]
        else:
            p[0] = '<em>' + p[3] + '</em>'

    def p_expression_underline(self, p):
        '''expression : UNDERLINE LBRACE expression RBRACE expression
                      | UNDERLINE LBRACE expression RBRACE'''
        if len(p) == 6:
            p[0] = '<u>' + p[3] + '</u>' + p[5]
        else:
            p[0] = '<u>' + p[3] + '</u>'

    def p_expression_url(self, p):
        '''expression : URL LBRACE expression RBRACE expression
                      | URL LBRACE expression RBRACE'''
        if len(p) == 6:
            p[0] = '<a href=' + p[3] + '>' + p[3] + '</a>' + p[5]
        else:
            p[0] = '<a href=' + p[3] + '>' + p[3] + '</a>'

    def p_expression_graphicspath(self, p):
        '''expression : GRAPHICS_PATH LBRACE expression RBRACE expression
                      | GRAPHICS_PATH LBRACE expression RBRACE'''
        if len(p) == 6:
            p[0] = '''<img src="''' + p[3] + '''">''' + p[5]
        else:
            p[0] = '''<img src="''' + p[3] + '''">'''

    def p_expression_includegraphics(self, p):
        '''expression : INCLUDE_GRAPHICS TEXT LBRACE expression RBRACE expression
                      | INCLUDE_GRAPHICS LBRACE expression RBRACE expression
                      | INCLUDE_GRAPHICS LBRACE expression RBRACE'''
        if len(p) == 7:
            attributes = p[2][1:-1]
            p[0] = '''<img src="''' + p[4] + \
                '''"''' + attributes + '''>''' + p[6]
        elif len(p) == 6:
            p[0] = '''<img src="''' + p[3] + '''">''' + p[5]
        else:
            p[0] = '''<img src="''' + p[3] + '''">'''

    def p_expression_chapter(self, p):
        '''expression : CHAPTER LBRACE expression RBRACE expression
                      | CHAPTER LBRACE expression RBRACE'''
        if len(p) == 6:
            p[0] = '<h1>' + p[3] + '</h1>' + p[5]
        else:
            p[0] = '<h1>' + p[3] + '</h1>'

    def p_expression_section(self, p):
        '''expression : SECTION LBRACE expression RBRACE expression
                      | SECTION LBRACE expression RBRACE'''
        if len(p) == 6:
            p[0] = '<h2>' + p[3] + '</h2>' + p[5]
        else:
            p[0] = '<h2>' + p[3] + '</h2>'

    def p_expression_subsection(self, p):
        '''expression : SUBSECTION LBRACE expression RBRACE expression
                      | SUBSECTION LBRACE expression RBRACE'''
        if len(p) == 6:
            p[0] = '<h3>' + p[3] + '</h3>' + p[5]
        else:
            p[0] = '<h3>' + p[3] + '</h3>'

    def p_expression_subsubsection(self, p):
        '''expression : SUBSUBSECTION LBRACE expression RBRACE expression
                      | SUBSUBSECTION LBRACE expression RBRACE'''
        if len(p) == 6:
            p[0] = '<h4>' + p[3] + '</h4>' + p[5]
        else:
            p[0] = '<h4>' + p[3] + '</h4>'

    def p_title(self, p):
        'expression : TITLE LBRACE TEXT RBRACE'
        p[0] = '<i>' + p[3] + '</i>'

    def p_expression_unordered_list(self, p):
        '''expression : BEGIN_ULIST listitems END_ULIST expression
                      | BEGIN_ULIST listitems END_ULIST'''
        if len(p) == 5:
            p[0] = '\n<ul>' + p[2] + '\n</ul>' + p[4]
        else:
            p[0] = '\n<ul>' + p[2] + '\n</ul>'

    def p_expression_ordered_list(self, p):
        '''expression : BEGIN_OLIST listitems END_OLIST expression
                      | BEGIN_OLIST listitems END_OLIST'''
        if len(p) == 5:
            p[0] = '\n<ol>' + p[2] + '\n</ol>' + p[4]
        else:
            p[0] = '\n<ol>' + p[2] + '\n</ol>'

    def p_listitems(self, p):
        '''listitems : ITEM expression listitems
                     | ITEM expression'''
        if len(p) == 4:
            p[0] = '\n<li>' + p[2] + '</li>' + p[3]
        else:
            p[0] = '\n<li>' + p[2] + '</li>'

    # def p_break(self, p):
    #     '''expression : BREAK expression
    #                   | BREAK'''
    #     if len(p) == 3:
    #         p[0] = '</br>' + p[2]
    #     else:
    #         p[0] = '</br>'

    # def p_expression_newline(self, p):
    #     '''expression : NEWLINE expression
    #                   | NEWLINE'''
    #     if len(p) == 3:
    #         p[0] = '<br/>' + p[2]
    #     else:
    #         p[0] = p[1]

    # def p_expression_newline_2(self, p):
    #     '''expression : TEXT NEWLINE_2'''
    #     p[0] = p[1] + '<br/>'

    # Error rule for syntax errors

    def p_error(self, p):
        print(p)
        print("Syntax error in input!")

    def __init__(self):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)

    def parse(self, code):
        return self.parser.parse(code)
