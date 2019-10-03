#!/usr/bin/python

from ply import *


''''
palavras reservadas cafezinho 
programa, car, int, retorne, leia, escreve, novalinha, se, entao, senao, enquanto, execute

'''

reservadas = {
    'programa' : 'PROGRAMA',
    'car': 'CAR',
    'int': 'INT',
    'leia': 'LEIA',
    'escreva': 'ESCREVA',
    'novalinha': 'NOVALINHA',
    'se': 'SE',
    'entao': 'ENTAO',
    'senao': 'SENAO',
    'enquanto': 'ENQUANTO',
    'execute': 'EXECUTE',
    'e': 'E',
    'ou': 'OU',
    'retorne': 'RETORNE'
}

tokens = ('PONTOEVIRGULA', 'VIRGULA', 'ABRECOLCHETE', 'FECHACOLCHETE', 'ABREPARENTESES', 'FECHAPARENTESES', 'ABRECHAVES',
         'FECHACHAVES', 'ASPAS', 'ATRIBUICAO', 'OPERADORTERNARIO', 'DOISPONTOS', 'COMPARADORIGUAL', 'COMPARADORDIFERENTE',
         'COMPARADORMENOR', 'COMPARADORMAIOR', 'COMPARADORMAIOROUIGUAL', 'COMPARADORMENOROUIGUAL', 'OPERADORMAIS',
         'OPERADORMENOS', 'OPERADORVEZES', 'OPERADORDIVISAO', 'OPERADORRESTODIVISAO', 'OPERADORNEGACAO',
         'OPERADORLOGICOOU', 'OPERADORLOGICOE', 'DEFID', 'DEFINTEIRO', 'DEFCADEIACARACTERES',
         'DEFCARACTERE') #+ list(reservadas.items)

'''
tokens e simbolos cafezinho
; [] , () {} = ? : == != < > >= <= + - * / %  ! ou e " 
programa car int leia escreve novalinha se entao senao enquanto execute
'''

t_PONTOEVIRGULA = r'\;'
t_VIRGULA = r'\,'
t_ABRECOLCHETE = r'\]'
t_FECHACOLCHETE = r'\['
t_ABREPARENTESES = r'\('
t_FECHAPARENTESES = r'\)'
t_ABRECHAVES = r'\{'
t_FECHACHAVES = r'\}'
t_ASPAS = r'\"'


t_ATRIBUICAO = r'='
t_OPERADORTERNARIO = r'\?'
t_DOISPONTOS = r':'

t_COMPARADORIGUAL = r'=='
t_COMPARADORDIFERENTE = r'!='
t_COMPARADORMENOR = r'<'
t_COMPARADORMAIOR = r'>'
t_COMPARADORMAIOROUIGUAL = r'>='
t_COMPARADORMENOROUIGUAL = r'<='

t_OPERADORMAIS = r'\+'
t_OPERADORMENOS = r'\-'
t_OPERADORVEZES = r'\*'
t_OPERADORDIVISAO = r'\/'
t_OPERADORRESTODIVISAO = r'\%'
t_OPERADORNEGACAO = r'\!'

t_OPERADORLOGICOOOU = r'ou'
t_OPERADORLOGICOE = r'e'

'''
t_PROGRAMA = r'programa'
t_CAR = r'car'
t_INTEIRO = r'int'
t_LEIA = r'leia'
t_ESCREVA = r'escreva'
t_NOVALINHA = r'novalinha'
t_SE = r'se'
t_ENTAO = r'entao'
t_SENAO = r'senao'
t_ENQUANTO = r'enquanto'
t_EXECUTE = r'execute'
t_RETORNE = r'retorne'
'''
def t_DEFID(t):
    r'[a-zA-z][a-zA-z_0-9]*'
    if t.value in reservadas:
        t.type = reservadas[t.value]
    return t

#\d+ 1 digito ou mais
def t_DEFINTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_DEFCADEIACARACTERES(t):
    r'\"([^\\\n]|(\\.))*\"'
    return t

def t_DEFCARACTERE(t):
    r'\'([^\\\n]|(\\.))\''
    return t


if __name__ == '__main__':
    lexer = lex.lex()
    lexer.input("3 + 4")
    lexer.token()


