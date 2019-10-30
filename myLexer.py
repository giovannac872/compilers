# -*- coding: utf-8 -*-
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
    'CADEIACARACTERE',
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
    'COMENTARIOMAISUMALINHA',
    'INTEIROCONSTANTE',
    'CARACTERECONSTANTE',
    'OPERADORRESTODIVISAO'
] + list(palavrasReservadas.values())


t_OPERADORRESTODIVISAO = r'%'
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
t_COMPARACAOIGUAL = r'\=\='
t_COMPARACAODIFERENTE = r'!='
t_COMPARACAOMAIOR = r'>'
t_COMPARACAOMENOR = r'<'
t_COMPARACAOMAIOROUIGUAL = r'>='
t_COMPARACAOMENOROUIGUAL = r'<='

'''
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
'''

def t_INTEIROCONSTANTE(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NOVALINHA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t\r'


def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in palavrasReservadas:# teste de palavras reservadas
        t.type = palavrasReservadas[str(t.value)]
#	print(t)
    return t


def t_CADEIACARACTERE(t):
    r'\"[^\"]*\"'
    
    t.value = t.value[1:-1]
    if t.value.find("\n") != -1:
        print("Erro:Cadeia de caractere ocupa mais de uma linha, linha:%d" % t.lexer.lineno)
        exit()
    
    return t

def t_CARACTERECONSTANTE(t):
    r"\'.\'"
    t.value = t.value[1:-1]
    return t

def t_COMENTARIOUMALINHA(t):
    r'//.*'
    t.lexer.lineno += 1
    pass 

def t_COMENTARIOMAISUMALINHA(t):
    r'(/\*[^(\*/)]*(\*/)?)'
    #print(t)
    if t.value[len(t.value)-1] != '/' and t.value[len(t.value)-2] != '*':
        print("Erro:Comentario nao termina, linha: %d" % t.lexer.lineno)
        exit()
    t.lexer.lineno += t.value.count('\n')
    pass

def t_error(t):
    print("Erro:Caractere invalido " +  "'" + t.value[0] + "'" + "linha " + str(t.lexer.lineno))
    exit() 

'''
def t_EMPTYSPACE(t):
    r'\s'
    return t

'''

lexer = lex.lex()
'''
arquivo = open("entrada.txt","r").read()
'''

#lexer.input("a = 2 + 2;")
#arquivo.close()

#print(palavrasReservadas['programa'])
#teste = "programa"
#print(palavrasReservadas[teste])
lexer.input(open("entrada.txt","r").read())
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
