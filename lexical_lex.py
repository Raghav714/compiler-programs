import ply.lex as lex
f = open('sum.c','r')
i = f.read()
# List of token names.   This is always required
tokens = ('NUMBER','PLUS','MINUS','TIMES','DIVIDE','LPAREN','RPAREN','EQUAL','EQUALEQUAL'
,'LBRAC','RBRAC','COLON','GREATER','LESSER','COMMA','ID','FUNCTION'
,'LIBRARY')
reserved = {'if' : 'IF','then' : 'THEN','else' : 'ELSE','while' :'WHILE','do' :'DO','break':'BREAK','int':'INT',
'double':'DOUBLE','float':'FLOAT','return':'RETURN','char':"CHAR",'void'
:'VOID','#include':'INCLUDE'}
function = {"printf(":'PRINTF', "scanf(":'SCANF', "gets(":'GETS', "puts(":'PUTS', "strcpy(":'STRCPY', "strlen(":'STRLEN', "strcmp(":'STRCMP', "isdigit(":'ISDIGIT', "strcat(":'STRCAT', "isupper(":'ISUPPER', "strstr(":'STRSTR', "islower(":'ISLOWER',}
tokens = list(tokens) +list(function.values()) + list(reserved.values())
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUAL = r'\='
t_EQUALEQUAL = r'\=='
t_LBRAC = r'\{'
t_RBRAC = r'\}'
t_COLON = r'\;'
t_GREATER = r'\>'
t_LESSER = r'\<'
t_COMMA = r'\,'

def t_COMMENT(t):
    r'(?s)/\*(.*?).?(\*/)'
    pass
def t_String(t):
	r'(?s)(\"(.*?).?(\"))'
	pass
def t_FUNCTION(t):
    r'[a-zA-Z_]*[a-zA-Z]\('
    t.type = function.get(t.value,'FUNCTION')
    return t
def t_ID(t):
	r'[#a-zA-Z0-9_]+'
	t.type = reserved.get(t.value,'ID')
	return t
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
# Test it out
#data = "if(3 + 4 * 10+ -20 *2 == 43 ){} else"

# Give the lexer some input
lexer.input(i)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
f.close()

