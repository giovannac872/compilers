import ply.lex as lex

palavrasReservadas = {
        'programa' : 'PROGRAMA',
        'car': 'CARACTERE',
        'int': 'INTEIRO',
        'retorne': 'RETORNE',
        'leia': 'LEIA',
        'escreva': 'ESCREVA',
        'novalinha': 'NOVALINHA',
        'se': 'SE',
        'entao': 'ENTAO',
        'senao': 'SENAO',
        'enquanto': 'ENQUANTO',
        'execute': 'EXECUTE',
        'e': 'OPERADORLOGICOE',
        'ou': 'OPERADORLOGICOOU'
        
}


tokens = [
    'OPERADORSOMA',
    'OPERADORSUBTRACAO',
    'OPERADORVEZES',
    'OPERADORDIVISAO',
    'ABREPARENTESES',
    'FECHAPARENTESES',
    'ATRIBUICAO',
    'IDENTIFICADOR',
    'error',
    'CADEIACARACTERE',
    'EMPTYSPACE',
    'PONTOEVIRGULA',
    'ABRECOLCHETE',
    'FECHACOLCHETE',
    'VIRGULA',
    'ASPAS',
    'COMPARACAOMAIOR',
    'COMPARACAOMENOR',
    'ABRECHAVES',
    'FECHACHAVES',
    'OPERADORTERNARIO',
    'DOISPONTOS',
    'COMPARACAOIGUAL',
    'COMPARACAODIFERENTE',
    'COMPARACAOMAIOROUIGUAL',
    'COMPARACAOMENOROUIGUAL',
    'OPERADORNEGACAO',
    'COMENTARIOUMALINHA',
    'COMENTARIOMAISUMALINHA'
] + list(palavrasReservadas.values())



t_OPERADORSOMA = r'\+'
t_OPERADORSUBTRACAO = r'\-'
t_OPERADORVEZES = r'\*'
t_OPERADORDIVISAO = r'/'
t_OPERADORTERNARIO = r'\?'
t_OPERADORNEGACAO = r'!'
t_ABREPARENTESES = r'\('
t_FECHAPARENTESES = r'\)'
t_ATRIBUICAO = r'\='
t_PONTOEVIRGULA = r';'
t_ABRECOLCHETE = r'\['
t_FECHACOLCHETE = r'\]'
t_VIRGULA = r','
t_ASPAS = r'"'
t_ABRECHAVES = r'\{'
t_FECHACHAVES = r'\}'
t_DOISPONTOS = r':'
t_COMPARACAOIGUAL = r'=='
t_COMPARACAODIFERENTE = r'!='
t_COMPARACAOMAIOR = r'>'
t_COMPARACAOMENOR = r'<'
t_COMPARACAOMAIOROUIGUAL = r'>='
t_COMPARACAOMENOROUIGUAL = r'<='


t_PROGRAMA = r'programa'
t_RETORNE = r'retorne'
t_LEIA = r'leia'
t_ESCREVA = r'escreva'
t_SE = r'se'
t_ENTAO = r'entao'
t_SENAO = r'senao'
t_ENQUANTO = r'enquanto'
t_EXECUTE = r'execute'
t_OPERADORLOGICOOU = r'ou'
t_OPERADORLOGICOE = r'e'


def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NOVALINHA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#t_ignore = r' \t'


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

def t_COMENTARIOUMALINHA(t):
    r'//.*'
    t.lexer.lineno += 1
    pass 

def t_COMENTARIOMAISUMALINHA(t):
    r'/\*(.|\n)* \*/'
    t.lexer.lineno += len(t.value)
    pass

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_EMPTYSPACE(t):
    r'\s'
    return t



lexer = lex.lex()

lexer.input("/**/")
#arquivo.close()
#print(palavrasReservadas['programa'])
teste = "programa"
#print(palavrasReservadas[teste])
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
