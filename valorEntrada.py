import ply.lex as lex

palavrasReservadas = {
        'programa' : 'PROGRAMA',
        
}


tokens = [
    'INTEIRO',
    'OPERADORSOMA',
    'OPERADORSUBTRACAO',
    'OPERADORVEZES',
    'OPERADORDIVISAO',
    'ABREPARENTESES',
    'FECHAPARENTESES',
    'ATRIBUICAO',
    'IDENTIFICADOR',
    'newline',
    'error',
    'CADEIACARACTERE',
    'CARACTERE',
    'EMPTYSPACE',
    'PONTOEVIRGULA',
    'ABRECOLCHETE',
    'FECHACOLCHETE'
] + list(palavrasReservadas.values())



t_OPERADORSOMA = r'\+'
t_OPERADORSUBTRACAO = r'\-'
t_OPERADORVEZES = r'\*'
t_OPERADORDIVISAO = r'/'
t_ABREPARENTESES = r'\('
t_FECHAPARENTESES = r'\)'
t_ATRIBUICAO = r'\='
t_PONTOEVIRGULA = r';'
t_ABRECOLCHETE = r'\['
t_FECHACOLCHETE = r'\]'


def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#t_ignore = r' \t'

t_PROGRAMA = r'programa'

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in palavrasReservadas:# teste de palavras reservadas
        t.type = palavrasReservadas[str(t.value)]
#	print(t)
    return t


def t_CADEIACARACTERE(t):
    r'\".*\"'
    return t

def t_CARACTERE(t):
    r"\'.\'"
    return t
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_EMPTYSPACE(t):
    r'\s'
    return t



lexer = lex.lex()

lexer.input("()")
#arquivo.close()
#print(palavrasReservadas['programa'])
teste = "programa"
#print(palavrasReservadas[teste])
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
