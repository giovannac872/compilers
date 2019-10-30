import ply.lex as lex
import ply.yacc as sintatic
from myLexer import tokens, lexer
import classes as Classes


def p_programa(p):
    """
    programa : declfuncvar declprog
    """
    

def p_declfuncvar(p):
    """
    declfuncvar : tipo IDENTIFICADOR declvar  PONTOEVIRGULA declfuncvar
    declfuncvar : tipo IDENTIFICADOR ABRECOLCHETE INTEIROCONSTANTE FECHACOLCHETE declvar PONTOEVIRGULA declfuncvar
    declfuncvar : tipo IDENTIFICADOR declfunc declfuncvar
    declfuncvar : 
    """

    if len(p) > 5:
        aux = None
        flagRepetido = False
        dicionarioVariaveisEscopo = {}
        #dicionarioVariaveisFuncao = {}
        # e uma variavel
        if p[3] != "[":
            aux = Classes.NoArvoreVariaveis()
            #pegando recursao do p[3] que e declvar
            if p[3] != None:
                dicionarioAux = p[3]
                for valor in dicionarioAux:
                    dicionarioAux[valor].setTipo(str(p[1]))
                    if valor in dicionarioVariaveisEscopo:
                        flagRepetido = True
                        break
                dicionarioVariaveisEscopo.update(dicionarioAux)
            #pegando recursao do p[5] que e declfuncvar
            if p[5] != None:
                dicionarioVariaveisEscopo = p[5]
        # e um vetor
        elif p[3] == "[":
            aux = Classes.NoArvoreVariaveis(vetor=True, tamanhoVetor=int(p[4]))
            #pegando recursao do p[6] que e declvar
            if p[6] != None:
                dicionarioAux = p[6] 
                for valor in dicionarioAux:
                   dicionarioAux[valor].setTipo(str(p[1]))
                   if valor in dicionarioVariaveisEscopo:
                       flagRepetido = True
                       break 
                    
            #pegando recursao do p
                dicionarioVariaveisEscopo.update(dicionarioAux) 
            if p[8] != None:
                dicionarioVariaveisEscopo = p[8]
        if p[1] in dicionarioVariaveisEscopo or flagRepetido == True:
            print("Erro na linha:" + str(p.lineno(2)) + " variavel: " + str(p[2]) + " ja declarada")
            exit()
        else:
            dicionarioVariaveisEscopo[str(p[2])] = aux
        p[0] = dicionarioVariaveisEscopo
    
    elif len(p) <= 5 and len(p) > 1 and p[3] != None:
        aux = Classes.NoArvoreFuncaoAssinatura(tipoRetornoFuncao= str(p[1]), nomeFuncao= str(p[2]), listaParametros= p[3])
        #print("O tamanho e" +str(len(p)))
        #print(p[3])
        if p[4] != None:
            dicionarioVariaveisEscopo = p[4]
        
            variavelAux = p[4]
            variavelAux = list(variavelAux)
        
            for incremento in variavelAux:
                #pegar o caso de uma variavel global ter sido declarada antes e depois da definicao de uma funcao
                if incremento in dicionarioVariaveisEscopo:
                    print("Erro na linha:" + str(p.lineno(2)) + " variavel: " + incremento + " ja declarada")
                exit()
        '''
        if p[1] in dicionarioVariaveisEscopo:
            print("Erro na linha:" + str(p.lineno(2)) + " variavel: " + str(p[2]) + " ja declarada")
            exit()
        '''      
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
    dicionarioVariaveisEscopo = {}
    
    #nao gera vazio em declvar
    if len(p) > 1:
        aux = None
        #aqui e variavel e nao vetor
        if p[3] != "[":
            aux = Classes.NoArvoreVariaveis()
            #pegando recursao
            if p[3] != None:
                dicionarioVariaveisEscopo = p[3]
        #aqui e vetor 
        elif p[3] == "[":
            aux = Classes.NoArvoreVariaveis(vetor= True, tamanhoVetor= int(p[4]))
            #pegando recursao           
            if p[6] != None: 
                dicionarioVariaveisEscopo = p[6]

        if p[2] in dicionarioVariaveisEscopo:
            print("Erro na linha:" + str(p.lineno(2)) + "variavel: " + str(p[2]) + "ja declarada")
            exit()
        else:
            dicionarioVariaveisEscopo[str(p[2])] = aux

        #subindo na arvore os valores pelo ply
        p[0] = dicionarioVariaveisEscopo

def p_declfunc(p):
    """
    declfunc : ABREPARENTESES listaparametros FECHAPARENTESES bloco
    """
    if len(p) > 1:
        dicionarioVariaiveisFuncaoAssinatura = {}
        dicionarioVariaveisEscopo = {}
        if p[2] != None:
            dicionarioVariaiveisFuncaoAssinatura = p[2]
            if p[4] != None:
                dicionarioVariaveisEscopo = p[4]
                for valor in dicionarioVariaveisEscopo:
                    if valor.getTipo() in dicionarioVariaiveisFuncaoAssinatura:
                        print("Erro: variavel " + str(valor) +  " nao pode ser declarada pois ja esta presente no parametro da funcao")
                        exit()


    

def p_listaparametros(p):
    """
    listaparametros : 
    listaparametros : listaparametroscont
    """

    if len(p) > 1:
        p[0] = p[1]
    else:
        p[0] = None

def p_listaparametroscont(p):
    """
    listaparametroscont : tipo IDENTIFICADOR
    listaparametroscont : tipo IDENTIFICADOR ABRECOLCHETE FECHACOLCHETE
    listaparametroscont : tipo IDENTIFICADOR VIRGULA listaparametroscont
    listaparametroscont : tipo IDENTIFICADOR ABRECOLCHETE FECHACOLCHETE VIRGULA listaparametroscont
    """
    aux = None
    dicionarioVariaveisEscopo = {}
    print(len(p))
    if len(p) > 1:
        flagRepetido = False
        #variavel comum sem recursao
        #print(p[3])
        if  len(p) <= 3:
            aux = Classes.NoArvoreVariaveis()
        #vetor comum sem recursao
        elif len(p) <= 5 and p[3] == "[":
            aux = Classes.NoArvoreVariaveis(vetor=True)
        #variavel comum com recursao
        elif len(p) <= 5 and p[3] == ",":
            aux = Classes.NoArvoreVariaveis()
            #pegando recursao de listaparametroscont
            if p[4] != None:
                #dicionarioVariaveisEscopo = p[4]
                dicionarioAux = p[4]
                for valor in dicionarioAux:
                    dicionarioAux[valor].setTipo(str(p[1]))
                    if valor in  dicionarioVariaveisEscopo:
                        flagRepetido = True
                        break 
                dicionarioVariaveisEscopo.update(dicionarioAux)           
        #vetor com recursao
        elif len(p) > 5 and p[3] == "[":        
            aux = Classes.NoArvoreVariaveis(vetor= True)
            #pegando recursao de listaparametroscont
            if p[6] != None:
                dicionarioAux = p[6]
                for valor in dicionarioAux:
                    #print(p[1])
                    #print(dicionarioAux)
                    dicionarioAux[valor].setTipo(p[1])
                    if valor in dicionarioVariaveisEscopo:
                        flagRepetido = True
                        break
                dicionarioVariaveisEscopo.update(dicionarioAux)                

        if p[2] in dicionarioVariaveisEscopo or flagRepetido == True:
           print("Erro na linha:" + str(p.lineno(2)) + "variavel: " + str(p[2]) + " ja declarada")
           exit()     
        else:
            dicionarioVariaveisEscopo[str(p[2])] = aux
        p[0] = dicionarioVariaveisEscopo
    

def p_bloco(p):
    """
    bloco : ABRECHAVES listadeclvar listacomando FECHACHAVES
    bloco : ABRECHAVES listadeclvar FECHACHAVES
    """

    if len(p) > 4:
        print("")
    elif len(p) <= 4:
        p[0] = p[2]
    else:
        p[0] = None

def p_listadeclvar(p):
    """
    listadeclvar : 
    listadeclvar : tipo IDENTIFICADOR declvar PONTOEVIRGULA listadeclvar
    listadeclvar : tipo IDENTIFICADOR ABRECOLCHETE INTEIROCONSTANTE FECHACOLCHETE declvar PONTOEVIRGULA listadeclvar
    """

    if len(p) > 1:
        aux = None
        dicionarioVariaveisEscopo = {}
        flagRepetido = False
        #variavel comum com recursao
        if len(p) <= 6:
            aux = Classes.NoArvoreVariaveis()
            if p[3] != None:
                dicionarioAux = p[3]
                for valor in dicionarioAux:
                    dicionarioAux.setTipo(str(p[1]))
                    if valor in dicionarioAux:
                        print("Erro na linha:" + str(p.lineno(2)) + " variavel: " + valor + " ja declarada")
                        flagRepetido = True
                        break
                dicionarioVariaveisEscopo.update(dicionarioAux)
            if p[5] != None:
                dicionarioVariaveisEscopo  = p[5]
        #variavel vetor
        elif len(p) > 6:
            aux = Classes.NoArvoreVariaveis(vetor=True, tamanhoVetor=p[4])
            if p[6] != None:
                dicionarioAux = p[6]
                for valor in dicionarioAux:
                    dicionarioAux.setTipo(str(p[1]))
                    if valor in dicionarioAux:
                        print("Erro na linha:" + str(p.lineno(2)) + " variavel: " + valor + " ja declarada")
                        flagRepetido = True
                        break
                dicionarioVariaveisEscopo.update(dicionarioAux)
            if p[8] != None:
                dicionarioVariaveisEscopo = p[8]
        
        if p[1] in dicionarioVariaveisEscopo or flagRepetido == True:
            print("Erro na linha:" + str(p.lineno(2)) + " variavel: " + str(p[1]) + " ja declarada")
            exit()
        else:
            dicionarioVariaveisEscopo[str(p[2])] = aux
        p[0]= dicionarioVariaveisEscopo
    else:
        p[0]= None


def p_tipo(p):
    """
    tipo : INTEIRO
    tipo : CARACTERE
    """
    p[0] = p[1]

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
    comando : ESCREVA expr PONTOEVIRGULA
    comando : ESCREVA CADEIACARACTERE PONTOEVIRGULA
    comando : NOVALINHA PONTOEVIRGULA
    comando : SE ABREPARENTESES expr FECHAPARENTESES ENTAO comando
    comando : SE ABREPARENTESES expr FECHAPARENTESES ENTAO comando SENAO comando
    comando : ENQUANTO ABREPARENTESES expr FECHAPARENTESES EXECUTE  comando
    comando : bloco
    """

    if len(p) > 1:
        aux = Classes.Comando()
        if p[1] == ";":
            aux.adicionaElementoLadoDireito(";")
        
        




def p_expr(p):
    """
    expr : assignexpr
    """

    if len(p) > 1:
        p[0] = p[1]

def p_assignexpr(p):
    """
    assignexpr : condexpr
    assignexpr : lvalueexpr ATRIBUICAO assignexpr
    """

    if len(p) > 1:
        if len(p) <= 2:
            p[0] = p[1]

def p_condexpr(p):
    """
    condexpr : orexpr
    condexpr : orexpr OPERADORTERNARIO expr DOISPONTOS condexpr
    """

    if len(p) > 1:
        if len(p) <= 2:
            p[0] = p[1]


def p_orexpr(p):
    """
    orexpr : orexpr OPERADORLOGICOOU andexpr
    orexpr : andexpr
    """

    if len(p) > 1:
        if len(p) <= 2:
            p[0] = p[1]



def p_andexpr(p):
    """
    andexpr : andexpr OPERADORLOGICOE eqexpr
    andexpr : eqexpr
    """
    if len(p) > 1:
        if len(p) <= 2:
            p[0] = p[1]


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
    primexpr : CARACTERE
    primexpr : INTEIROCONSTANTE
    primexpr : ABREPARENTESES expr FECHAPARENTESES
    """

def p_listexpr(p):
    """
    listexpr : assignexpr
    listexpr : listexpr VIRGULA assignexpr
    """


valor = sintatic.yacc()
arquivo = open("entrada.txt", "r").read()
print(valor.parse(arquivo))