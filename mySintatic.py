import ply.lex as lex
import ply.yacc as sintatic
from myLexer import tokens, lexer


def p_programa(p):
    """
    programa : declfuncvar declprog
    """

def p_declfuncvar(p):
    """
    declfuncvar : tipo IDENTIFICADOR declvar PONTOEVIRGULA declfuncvar
    declfuncvar : tipo IDENTIFICADOR ABRECOLCHETE  INTEIROCONSTANTE FECHACOLCHETE declvar PONTOEVIRGULA declfuncvar
    declfuncvar : tipo IDENTIFICADOR declfunc declfuncvar
    declfuncvar : 
    """

def p_declprog(p):
    """
    declprog : PROGRAMA bloco
    """

def p_declvar(p):
    """
    declvar : VIRGULA IDENTIFICADOR declvar
    declvar : VIRGULA IDENTIFICADOR ABRECOLCHETE INTEIROCONSTANTE FECHACOLCHETE declvar
    declvar : 
    """

def p_declfunc(p):
    """
    declfunc : ABREPARENTESES listaparametros FECHAPARENTESES bloco
    """

def p_listaparametros(p):
    """
    listaparametros : 
    listaparametros : listaparametroscont
    """   

def p_listaparametroscont(p):
    """
    listaparametroscont : tipo IDENTIFICADOR
    listaparametroscont : tipo IDENTIFICADOR ABRECOLCHETE FECHACOLCHETE
    listaparametroscont : tipo IDENTIFICADOR VIRGULA listaparametroscont
    listaparametroscont : tipo IDENTIFICADOR ABRECOLCHETE FECHACOLCHETE VIRGULA listaparametroscont
    """

def p_bloco(p):
    """
    bloco : ABRECHAVES listadeclvar listacomando FECHACHAVES
    bloco : ABRECHAVES listadeclvar FECHACHAVES
    """

def p_listadeclvar(p):
    """
    listadeclvar : 
    listadeclvar : tipo IDENTIFICADOR declvar PONTOEVIRGULA listadeclvar
    listadeclvar : tipo IDENTIFICADOR ABRECOLCHETE INTEIROCONSTANTE FECHACOLCHETE declvar PONTOEVIRGULA listadeclvar
    """

def p_tipo(p):
    """
    tipo : INTEIRO
    tipo : CARACTERE
    """

def p_listacomando(p):
    """
    listacomando : comando
    listacomando : comando listacomando
    """
def p_comando(p):
    """
    comando : PONTOEVIRGULA
    comando : expr PONTOEVIRGULA
    comando : RETORNE expr PONTOEVIRGULA
    comando : LEIA lvalueexpr PONTOEVIRGULA
    comando : ESCREVA  expr PONTOEVIRGULA
    comando : ESCREVA CADEIACARACTERE PONTOEVIRGULA
    comando : NOVALINHA PONTOEVIRGULA
    comando : SE ABREPARENTESES expr FECHAPARENTESES ENTAO comando
    comando : SE ABREPARENTESES expr FECHAPARENTESES ENTAO comando SENAO comando
    comando : ENQUANTO ABREPARENTESES expr FECHAPARENTESES EXECUTE comando
    comando : bloco
    """

def p_expr(p):
    """
    expr : assignexpr
    """

def p_assignexpr(p):
    """
    assignexpr : condexpr
    assignexpr : lvalueexpr ATRIBUICAO assignexpr
    """

def p_condexpr(p):
    """
    condexpr : orexpr
    condexpr : orexpr OPERADORTERNARIO expr DOISPONTOS condexpr
    """

def p_orexpr(p):
    """
    orexpr : orexpr OPERADORLOGICOOU andexpr
    orexpr : andexpr
    """

def p_andexpr(p):
    """
    andexpr : andexpr OPERADORLOGICOE eqexpr
    andexpr : eqexpr
    """

def p_eqexpr(p):
    """
    eqexpr : eqexpr COMPARACAOIGUAL desigexpr
    eqexpr : eqexpr COMPARACAODIFERENTE desigexpr
    eqexpr : desigexpr
    """

def p_desigexpr(p):
    """
    desigexpr : desigexpr COMPARACAOMENOR addexpr
    desigexpr : desigexpr COMPARACAOMAIOR addexpr
    desigexpr : desigexpr COMPARACAOMAIOROUIGUAL addexpr
    desigexpr : desigexpr COMPARACAOMENOROUIGUAL addexpr
    desigexpr : addexpr
    """

def p_addexpr(p):
    """
    addexpr : addexpr OPERADORSOMA mulexpr
    addexpr : addexpr OPERADORSUBTRACAO mulexpr
    addexpr : mulexpr
    """

def p_mulexpr(p):
    """
    mulexpr : mulexpr OPERADORVEZES unexpr
    mulexpr : mulexpr OPERADORDIVISAO unexpr
    mulexpr : mulexpr OPERADORRESTODIVISAO unexpr
    mulexpr : unexpr
    """

def p_unexpr(p):
    """
    unexpr : OPERADORSUBTRACAO primexpr
    unexpr : OPERADORNEGACAO primexpr
    unexpr : primexpr
    """

def p_lvalueexpr(p):
    """
    lvalueexpr : IDENTIFICADOR ABRECOLCHETE expr FECHACOLCHETE
    lvalueexpr : IDENTIFICADOR
    """
def p_primexpr(p):
    """
    primexpr : IDENTIFICADOR ABREPARENTESES listexpr FECHAPARENTESES
    primexpr : IDENTIFICADOR ABREPARENTESES FECHAPARENTESES
    primexpr : IDENTIFICADOR ABRECOLCHETE expr FECHACOLCHETE
    primexpr : IDENTIFICADOR
    primexpr : CARACTERECONSTANTE
    primexpr : INTEIROCONSTANTE
    primexpr :  ABREPARENTESES expr FECHAPARENTESES
    """

def p_listexpr(p):
    """
    listexpr : assignexpr
    listexpr : listexpr VIRGULA assignexpr
   """

def p_error(p):
    print("ERRO sintatico")
    exit()
'''
def p_SOMA(p):
    """
    SOMA : tipo OPERADORSOMA tipo
    """
    p[0] = p[1] + p[3]

def p_tipo(p):
    """
    tipo : INTEIRO 
    """
    p[0] = p[1]
'''


valor = sintatic.yacc()
arquivo = open("entrada.txt","r").read()
print(valor.parse(arquivo))
#print(valor.parse("2 + 2"))

