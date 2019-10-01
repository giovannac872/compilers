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
    'escreve': 'ESCREVE',
    'novalinha': 'NOVALINHA',
    'se': 'SE',
    'entao': 'ENTAO',
    'senao': 'SENAO',
    'enquanto': 'ENQUANTO',
    'execute': 'EXECUTE',
    'e': 'E',
    'ou': 'OU'
}

tokens = ['PONTOEVIRGULA', 'ABRECOLCHETE', 'FECHACOLCHETE', 'ABREPARENTESES', 'FECHAPARENTESES', 'ABRECHAVES',
         'FECHACHAVES', 'ATRIBUICAO', 'OPERADORTERNARIO', 'DOISPONTOS', 'COMPARADORIGUAL', 'COMPARADORDIFERENTE',
         'COMPARADORMENOR', 'COMPARADORMAIOR', 'COMPARADORMAIOROUIGUAL', 'COMPARADORMENOROUIGUAL', 'OPERADORMAIS',
         'OPERADORMENOS', 'OPERADORVEZES', 'OPERADORDIVISAO', 'OPERADORRESTODIVISAO', 'OPERADORNEGACAO',
         'OPERADORLOGICOOU', 'OPERADORLOGICOE', 'DEFID'] + list(reservadas.items)

'''
tokens e simbolos
; [] , () {} = ? : == != < > >= <= + - * / %  ! ou e
programa car int leia escreve novalinha se entao senao enquanto execute
'''

t_PONTOEVIRGULA = r'\;'
t_ABRECOLCHETE = r'\]'
t_FECHACOLCHETE = r'\['
t_ABREPARENTESES = r'\('
t_FECHAPARENTESES = r'\)'
t_ABRECHAVES = r'\{'
t_FECHACHAVES = r'\}'

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
t_OPERADORRESTODIVISAO = r'%'
t_OPERADORNEGACAO = r'\!'

t_OPERADORLOGICOOOU = r'ou'
t_OPERADORLOGICOE = r'e'

t_PROGRAMA = r'programa'
t_CAR = r'car'
t_INTEIRO = r'int'
t_LEIA = r'leia'
t_ESCREVE = r'escreve'
t_NOVALINHA = r'novalinha'
t_SE = r'se'
t_ENTAO = r'entao'
t_SENAO = r'senao'
t_ENQUANTO = r'enquanto'
t_EXECUTE = r'execute'


def t_DEFID(t):
    r'[a-zA-z][a-zA-z_0-9]*'
    if t.value in reservadas:
        t.type = reservadas[t.value]
    return t

