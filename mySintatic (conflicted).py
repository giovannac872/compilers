import ply.lex as lex
import ply.yacc as sintatic
from myLexer import tokens, lexer
import classes as Classes


Escopo = {}
dicionarioNomeFuncao = {}

def insereEscopo(nomeEscopo, variaveisEscopo):
    global Escopo

    Escopo[str(nomeEscopo)] = variaveisEscopo

def removeEscopo(nomeEscopo):
    global Escopo

    if nomeEscopo in Escopo:
        del(Escopo[nomeEscopo])
    else:
        print("Nao existe esse escopo")




def p_programa(p):
    """
    programa : declfuncvar declprog
    """
    
    insereEscopo('global', p[1])

dicionarioVariaveisEscopo = {}
#aqui só há variáveis no escopo global e no escopo de funcoes
def p_declfuncvar(p):
    """
    declfuncvar : tipo IDENTIFICADOR declvar  PONTOEVIRGULA declfuncvar
    declfuncvar : tipo IDENTIFICADOR ABRECOLCHETE INTEIROCONSTANTE FECHACOLCHETE declvar PONTOEVIRGULA declfuncvar
    declfuncvar : tipo IDENTIFICADOR declfunc declfuncvar
    declfuncvar : 
    """
    global Escopo
    global dicionarioNomeFuncao
    #print(len(p))
    #print(p[0])
    #print("Tamanho p\n")
    
    aux = None
    flagRepetido = False
    global dicionarioVariaveisEscopo 
    if len(p) > 5:    
        
        #dicionarioVariaveisFuncao = {}
        # e uma variavel
        if p[3] != "[":
            aux = Classes.NoArvoreVariaveis(tipo = p[1])
            #print("Valor aux")
            #print(aux)
            #aux = Classes.NoArvoreVariaveis()
            #pegando recursao do p[3] que e declvar e nao ha mais p[5] 
            #print(p[5])
            if p[3] != None and p[5] == None:
                dicionarioAux = p[3]
                for valor in dicionarioAux:
                    dicionarioAux[valor].setTipo(str(p[1]))
                    if valor in dicionarioVariaveisEscopo:
                        flagRepetido = True
                        break
                dicionarioVariaveisEscopo.update(dicionarioAux)
                #print(aux)
                dicionarioVariaveisEscopo.update(aux)
            #pegando recursao do p[5] que e declfuncvar
            if p[3] == None and p[5] != None:
                #print(p[5])
                dicionarioVariaveisEscopo.update(p[5])
                #print("valor p[5]\n")
                #print(p[5])
                #dicionarioVariaveisEscopo.update(aux)
            #pegando recursao em p[3] e p[5]
            if p[3] != None and p[5] != None:
                dicionarioAux = p[3]
                for valor in dicionarioAux:
                    dicionarioAux[valor].setTipo(str(p[1]))
                    if valor in dicionarioVariaveisEscopo:
                        flagRepetido = True
                        break
                dicionarioVariaveisEscopo.update(dicionarioAux)
                dicionarioVariaveisEscopo.update(p[5])
                #dicionarioVariaveisEscopo.update(aux)

            #for valor in dicionarioVariaveisEscopo         
        
        # e um vetor
        elif p[3] == "[":
            aux = Classes.NoArvoreVariaveis(vetor=True, tamanhoVetor=int(p[4]), tipo= p[1])
            aux.iniciaVetor()
            #pegando recursao do p[6] que e declvar e nao ha p[8]
            if p[6] != None and p[8] == None:
                dicionarioAux = p[6] 
                for valor in dicionarioAux:
                   dicionarioAux[valor].setTipo(str(p[1]))
                   if valor in dicionarioVariaveisEscopo:
                       flagRepetido = True
                       break 
                dicionarioVariaveisEscopo.update(dicionarioAux)
            #pegando recursao do p[8]
            elif p[6] == None and p[8] != None:
                dicionarioVariaveisEscopo.update(p[8])

            elif p[6] != None and p[8] != None:
                dicionarioAux = p[6] 
                for valor in dicionarioAux:
                   dicionarioAux[valor].setTipo(str(p[1]))
                   if valor in dicionarioVariaveisEscopo:
                       flagRepetido = True
                       break 
                dicionarioVariaveisEscopo.update(dicionarioAux)
                dicionarioVariaveisEscopo.update(p[8])

        #print(str(p[2]))
        if str(p[2]) in dicionarioVariaveisEscopo or flagRepetido == True:
            print("Erro na linha:" + str(p.lineno(2)) + " variavel: " + str(p[2]) + " ja declarada")
            exit()
        else:
            dicionarioVariaveisEscopo[str(p[2])] = aux
        #print("Valor fim dicionario\n")
        #print(dicionarioVariaveisEscopo)
        p[0] = dicionarioVariaveisEscopo
        
        #insereEscopo(nomeEscopo = 'global', variaveisEscopo = dicionarioVariaveisEscopo)

        #print(dicionarioVariaveisEscopo.values())

    #possui funcao 
    elif len(p) <= 5 and len(p) > 1:
        aux = Classes.NoArvoreFuncaoAssinatura(tipoRetornoFuncao= str(p[1]), listaParametros= p[3])
        #print("O tamanho e" +str(len(p)))
        #print(p[3])
        #ha variaveis globais ou outras funcoes depois da funcao 
        #print("valor p[4]")
        #print(p[4])
        if p[4] != None:
            #dicionarioVariaveisEscopo.update(p[4])
        
            variavelAux = p[4]
            variavelAux = list(variavelAux)
            #print("ValorvariavelAux")
            #print(variavelAux)
            #print(dicionarioVariaveisEscopo)
            for incremento in variavelAux:
                #print(incremento)
                #pegar o caso de uma variavel global ter sido declarada antes e depois da definicao de uma funcao
                if incremento in dicionarioVariaveisEscopo:
                    print("Erro na linha:" + str(p.lineno(2)) + " variavel: " + incremento + " ja declarada")
                exit()
        
            dicionarioVariaveisEscopo.update(p[4])
        
        #nao e permitido funcao com o mesmo nome 
        if p[2] in dicionarioNomeFuncao:
            print("Erro na linha:" + str(p.lineno(2)) + " funcao: " + str(p[2]) + " ja existente")
            exit()
        else:
            dicionarioNomeFuncao[str(p[2])] = aux
        
        p[0] = dicionarioVariaveisEscopo
    
    else:
        p[0] = None    

    
        
        
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
                dicionarioVariaveisEscopo.update(p[3])
        #aqui e vetor 
        elif p[3] == "[":
            aux = Classes.NoArvoreVariaveis(vetor= True, tamanhoVetor= int(p[4]))
            aux.iniciaVetor()
            #pegando recursao           
            if p[6] != None: 
                dicionarioVariaveisEscopo.update(p[6])

        if p[2] in dicionarioVariaveisEscopo:
            print("Erro na linha:" + str(p.lineno(2)) + "variavel: " + str(p[2]) + "ja declarada")
            exit()
        else:
            dicionarioVariaveisEscopo[str(p[2])] = aux

        #subindo na arvore os valores pelo ply
        p[0] = dicionarioVariaveisEscopo
    
    else:
        p[0] = None

def p_declfunc(p):
    """
    declfunc : ABREPARENTESES listaparametros FECHAPARENTESES bloco
    """
    if len(p) > 1:
        dicionarioVariaiveisFuncaoAssinatura = {}
        dicionariVariaveisoEscopoFuncao = {}
        


    

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
    dicionarioVariaveisAssinaturaFuncao = {}
    #print(len(p))
    if len(p) > 1:
        flagRepetido = False
        #variavel comum sem recursao
        if  len(p) <= 3:
            aux = Classes.NoArvoreVariaveis(tipo=p[1])
        #vetor comum sem recursao
        elif len(p) <= 5 and p[3] == "[":
            aux = Classes.NoArvoreVariaveis(vetor=True, tipo=p[1])
        #variavel comum com recursao
        elif len(p) <= 5 and p[3] == ",":
            aux = Classes.NoArvoreVariaveis(tipo=p[1])
            #pegando recursao de listaparametroscont
            if p[4] != None:
                #dicionarioVariaveisAssinaturaFuncao = p[4]
                '''
                dicionarioAux = p[4]
                for valor in dicionarioAux:
                    dicionarioAux[valor].setTipo(str(p[1]))
                    if valor in  dicionarioVariaveisAssinaturaFuncao:
                        flagRepetido = True
                        break 
                '''
                dicionarioVariaveisAssinaturaFuncao.update(p[4])           
        #vetor com recursao
        elif len(p) > 5 and p[3] == "[":        
            aux = Classes.NoArvoreVariaveis(vetor= True, tipo=p[1])
            #pegando recursao de listaparametroscont
            if p[6] != None:
                '''
                dicionarioAux = p[6]
                for valor in dicionarioAux:
                    #print(p[1])
                    #print(dicionarioAux)
                    dicionarioAux[valor].setTipo(p[1])
                    if valor in dicionarioVariaveisAssinaturaFuncao:
                        flagRepetido = True
                        break
                '''
                dicionarioVariaveisAssinaturaFuncao.update(p[6])                

        if p[2] in dicionarioVariaveisAssinaturaFuncao or flagRepetido == True:
           print("Erro na linha:" + str(p.lineno(2)) + "variavel: " + str(p[2]) + " ja declarada na assinatura de funcao")
           exit()     
        else:
            dicionarioVariaveisAssinaturaFuncao[str(p[2])] = aux
        
        p[0] = dicionarioVariaveisAssinaturaFuncao
    

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
    if len(p) > 1:
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
        aux = p[1]
        aux2 = p[3]
        if len(p) <= 2:
            p[0] = p[1]
        elif p[2] == "=":
            if type(aux2) == bool:
                print("Erro: Nao e possivel realizar a atribuicao, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()
            
            elif type(aux2) == int and aux.getTipo() == 'int':
                #atribuicao para uma variavel simples
                if type(aux) == Classes.NoArvoreVariaveis:
                    aux.setValor(aux2)
                #atribuicao para um elemento do vetor
                elif type(aux) == Classes.NoArvoreVetores:
                   aux.setValor(aux2)
                p[1] = aux
            
            elif type(aux2) == str and aux.getTipo() == 'car':
                #atribuicao para uma variavel simples
                if type(aux) == Classes.NoArvoreVariaveis:
                    aux.setValor(aux2)
                #atribuicao para um elemento do vetor
                elif type(aux) == Classes.NoArvoreVetores:
                   aux.setValor(aux2)
                p[1] = aux
            
            else:
                print("Erro: Nao e possivel realizar a atribuicao, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()


                

def p_condexpr(p):
    """
    condexpr : orexpr
    condexpr : orexpr OPERADORTERNARIO expr DOISPONTOS condexpr
    """
    # p[0] = p[3] if p[1] else p[5]
    if len(p) > 1:
        if len(p) <= 2:
            p[0] = p[1]
        elif len(p) > 2:
            if type(p[1]) == int and type(p[3]) == int and type(p[5]) == int:
                if p[1] == 0 and p[3] == 0 and p[5] == 0:
                    p[0] = False if False else False

                elif p[1] != 0 and p[3] == 0 and p[5] == 0:
                    p[0] = False if True else False

                elif p[1] == 0 and p[3] != 0 and p[5] == 0:
                    p[0] = True if False else False
                
                elif p[1] == 0 and p[3] == 0 and p[5] != 0:
                    p[0] = False if False else True

                elif p[1] == 0 and p[3] != 0 and p[5] != 0:
                    p[0] = True if False else True

                elif p[1] != 0 and p[3] != 0 and p[5] == 0:
                    p[0] = True if True else False
                
                elif p[1] != 0 and p[3] == 0 and p[5] != 0:
                    p[0] = False if True else True

                elif p[1] != 0 and p[3] != 0 and p[5] != 0:
                    p[0] = True if True else True


            elif type(p[1]) == int and type(p[3]) == int and type(p[5]) == bool:
                
                if p[1] == 0 and p[3] == 0:
                    p[0] = False if False else p[5]

                elif p[1] != 0 and p[3] == 0:
                    p[0] = False if True else p[5]

                elif p[1] != 0 and p[3] != 0:
                    p[0] = True if True else p[5]

                elif  p[1] == 0 and p[3] != 0:
                    p[0] = True if False else p[5]
                

            elif type(p[1]) == int and type(p[3]) == bool and type(p[5]) == int:
                if p[1] == 0 and p[5] == 0:
                    p[0] = p[3] if False else False

                elif p[1] != 0 and p[5] == 0:
                    p[0] = p[3] if True else False

                elif p[1] != 0 and p[5] != 0:
                    p[0] = p[3] if True else True

                elif  p[1] == 0 and p[5] != 0:
                    p[0] = p[3] if False else True
            
            elif type(p[1]) == bool and type(p[3]) == int and type(p[5]) == int:
                if p[3] == 0 and p[5] == 0:
                    p[0] = False if p[1] else False

                elif p[3] != 0 and p[5] == 0:
                    p[0] = True if p[1] else False

                elif p[3] != 0 and p[5] != 0:
                    p[0] = True if p[1] else True

                elif  p[3] == 0 and p[5] != 0:
                    p[0] = False if p[1] else True

            
            elif type(p[1]) == int and type(p[3]) == bool and type(p[5]) == bool:
                if p[1] == 0:
                    p[0] = p[3] if False else p[5]
                
                else:
                    p[0] = p[3] if True else p[5]

            elif type(p[1]) == bool and type(p[3]) == bool and type(p[5]) == int:
                if p[5] == 0:
                    p[0] = p[3] if p[1] else False
                
                else:
                    p[0] = p[3] if [1] else True

            elif type(p[1]) == bool and type(p[3]) == int and type(p[5]) == bool:
                if p[3] == 0:
                    p[0] = False if p[1] else p[5]
                
                else:
                    p[0] = True if p[1] else p[5]
            
            elif type(p[1]) == bool and type(p[3]) == bool and type(p[5]) == bool:
                p[0] = p[3] if p[1] else p[5]

            else:
                print("Erro: Operacao nao e possivel de ser realizada, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()


            #p[0] = p[3] if p[1] else p[5]        
    
def p_orexpr(p):
    """
    orexpr : orexpr OPERADORLOGICOOU andexpr
    orexpr : andexpr
    """

    if len(p) > 1:

        #retorno de expressao logica    
        if p[2] == 'ou':
            if type(p[1]) == int and type(p[3]) == bool:
                if p[1] == 0:
                    p[0] = False or p[3]
                else:
                    p[0] = True or p[3]
            
            elif type(p[1]) == bool and type(p[3]) == int:
                if p[3] == 0:
                    p[0] = p[1] or False
                else:
                    p[0] = p[1] or True
            
            elif type(p[1]) == int and type(p[3]) == int:
                if p[1] == 0 and p[3] == 0:
                    p[0] = False or False

                elif p[1] != 0 and p[3] == 0:
                    p[0] = True or False

                elif p[1] != 0 and p[3] != 0:
                    p[0] = True or True

                elif  p[1] == 0 and p[3] != 0:
                    p[0] = False or p[3]

            elif type(p[1]) == bool and type(p[3]) == bool:
                p[0] = p[1] or p[3]

            else:
                print("Erro: Operacao nao e possivel de ser realizada, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()

        #expressao simples
        else:
            p[0] = p[1]     



def p_andexpr(p):
    """
    andexpr : andexpr OPERADORLOGICOE eqexpr
    andexpr : eqexpr
    """
    #global Escopo
    if len(p) > 1:
        #operacao logica e
        if p[2] == 'e':
            #lado esquero e inteiro e direito bool
            if type(p[1]) == int and type(p[3]) == bool:
                #valor int diferente 0 e true
                if p[1] != 0:
                    p[0] = True and p[3]
                #valor int igual O e false
                else:
                    p[0] = False and p[3]
            
            elif type(p[1]) == bool and type(p[3]) == int:
                if p[3] != 0:
                    p[0] = p[1] and True
                #valor int igual O e false
                else:
                    p[0] = p[1] and False
            
            elif type(p[1]) == int and type(p[3]) == int:
                if p[1] == 0 and p[3] == 0:
                    p[0] = False and False
                
                elif p[1] != 0 and p[3] == 0:
                    p[0] = True and False
                
                elif p[1] != 0 and p[3] != 0:
                    p[0] = True and True

                else:
                    p[0] = False and True   
            
            elif type(p[1]) == bool and type(p[3]) == bool:
                p[0] = p[1] and p[3]

            else:
                print("Erro: Operacao nao e possivel de ser realizada, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()
        else:
            p[0] = p[1]


def p_eqexpr(p):
    """
    eqexpr : eqexpr COMPARACAOIGUAL desigexpr
    eqexpr : eqexpr COMPARACAODIFERENTE desigexpr
    eqexpr : desigexpr
    """

    if len(p) > 1:
        #comparacao de igualdade
        if p[2] == "==":
            #fnc para os tipos aceitos na comparacao dois int, dois bool ou dois caractere
            if (type(p[1]) == int and type(p[3]) == int) or (type(p[1]) == bool and type(p[2]) == bool) or (type(p[1]) == str and type(p[2]) == str):
                p[0] = p[1] == p[2]
            else:
                print("Erro: Operacao nao e possivel de ser realizada, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()
        #comparacao de diferenca
        elif p[2] == "!=":
            #fnc para os tipos aceitos na comparacao dois int, dois bool ou dois caractere
            if (type(p[1]) == int and type(p[3]) == int) or (type(p[1]) == bool and type(p[2]) == bool) or (type(p[1]) == str and type(p[2]) == str):
                p[0] = p[1] != p[2]
            else:
                print("Erro: Operacao nao e possivel de ser realizada, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()
        #elemento unitario
        else:
            p[0] = p[1]



def p_desigexpr(p):
    """
    desigexpr : desigexpr COMPARACAOMENOR addexpr
    desigexpr : desigexpr COMPARACAOMAIOR addexpr
    desigexpr : desigexpr COMPARACAOMAIOROUIGUAL addexpr
    desigexpr : desigexpr COMPARACAOMENOROUIGUAL addexpr
    desigexpr : addexpr
    """
    if len(p) > 1:
        if p[2] == "<":
            if type(p[1]) == int and type(p[3]) == int:
                p[0] = p[1] < p[3] 
            else:
                print("Erro: Operacao nao e possivel de ser realizada, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()

        elif p[2] == ">":
            if type(p[1]) == int and type(p[3]) == int:
                p[0] = p[1] > p[3]
            else:
                print("Erro: Operacao nao e possivel de ser realizada, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()

        elif p[2] == ">=":
            if type(p[1]) == int and type(p[3]) == int:
                p[0] = p[1] >= p[3]
            else:
                print("Erro: Operacao nao e possivel de ser realizada, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()

        elif p[2] == "<=":
            if type(p[1]) == int and type(p[2]) == int:
                p[0] = p[1] <= p[3]
        else:
            p[0] = p[1]


def p_addexpr(p):
    """
    addexpr : addexpr OPERADORSOMA mulexpr
    addexpr : addexpr OPERADORSUBTRACAO mulexpr
    addexpr : mulexpr
    """

    if len(p) > 1:
        if p[2] == "+":
            if type(p[1]) == int  and type(p[3]) == int:
                p[0] = int(p[1] + p[3])
            ##elif p[1] == r"\'.\'" and p[3] == r"\'.\'":
            ##    p[0] = p[1] + p[3]
            else:
                print("Erro: Operacao nao e possivel de ser realizada, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()
        elif p[2] == "-":
            if type(p[1]) == int and type(p[3]) == int:
                p[0] = int(p[1] - p[3])
            else:
                print("Erro: Operacao nao e possivel de ser realizada, tipos nao compativeis, linha: " + str(p.lineno(p[1])))
                exit()
        else:
            p[0] = p[1]
def p_mulexpr(p):
    """
    mulexpr : mulexpr OPERADORVEZES unexpr
    mulexpr : mulexpr OPERADORDIVISAO unexpr
    mulexpr : mulexpr OPERADORRESTODIVISAO unexpr
    mulexpr : unexpr
    """

    if len(p) > 1:
        #se a operacao for um produto
        if p[2] == "*":
            if type(p[1]) == int and type(p[3]) == int:
                p[0] = int(p[1] * p[3])
            else:
                print("Erro: nao e possivel realizar o produto, ha divergencias de tipo, linha: " + p.lineno(1))
                exit()
        #se a operacao for uma divisao
        elif p[2] == "/":
            if type(p[1]) == int and type(p[3]) == int:
                if p[3] != 0:
                    p[0] = int(p[0] / p[3])
                else:
                    print("Erro: nao e possivel realizar a divisao por zero, linha: " + p.lineno(3))
                    exit()
            else:
                print("Erro: nao e possivel realizar a divisao, ha divergencias de tipo, linha: " + p.lineno(1))
                exit()
        #se a operacao for um resto de divisao
        elif p[2] == "%":
            if type(p[1]) == int and type(p[2]) == int:
                if p[3] != 0:
                    p[0] = int(p[1] % p[3])
                else:
                    print("Erro: nao e possivel realizar a divisao por zero, linha: " + p.lineno(3))
                    exit()
            else:
                print("Erro: nao e possivel realizar o resto da divisao, ha divergencias de tipo, linha: " + p.lineno(1))
                exit()
        #a expressao recebe apenas um elemento
        else:
            p[0] = [1]

def p_unexpr(p):
    """
    unexpr : OPERADORSUBTRACAO primexpr
    unexpr : OPERADORNEGACAO primexpr
    unexpr : primexpr
    """

    if len(p) > 1:
        if p[1] == "-":
            if p[2] != True and p[2] != False:
                p[0] =  - p[2]
            else:
                print("Erro: Nao e possivel realizar subtracao de uma expressao logica, linha: " + str(p.lineno(2)))
                exit()
        elif p[1] == "!":
            if p[2] == True or p[2] == False:
                p[0] = not p[2]
            else:
                print("Erro: Nao e possivel realizar a negacao de uma expressao numerica, linha " + str(p.lineno(2)))
                exit()
        else:
            p[0] = p[1]  

def p_lvalueexpr(p):
    """
    lvalueexpr : IDENTIFICADOR ABRECOLCHETE expr FECHACOLCHETE
    lvalueexpr : IDENTIFICADOR
    """
    global Escopo
    if len(p) > 1:
        
        flagnaoEstaEscopo = False
        #aux = None
        #a atribuicao e para uma variavel simples
        if len(p) <= 2:
            for valor in Escopo:
                if p[1] not in valor:
                    #print("Operacao invalida, na linha: " +  str(p.lineno(1)) + ", variavel: " + str(p[1]) + " nao declarada")
                    #exit()
                    flagnaoEstaEscopo = True
                else:
                    flagnaoEstaEscopo = False
                    #aux= valor  

            if flagnaoEstaEscopo == True:
                print("Operacao invalida, na linha: " +  str(p.lineno(1)) + ", variavel: " + str(p[1]) + " nao declarada")
                exit()
            
            p[0] = p[1]
        #a atribuicao e para um elemento do vetor
        elif len(p) > 2:
            for valor in Escopo:
                if p[1] not in valor:
                    #print("Operacao invalida, na linha: " +  str(p.lineno(1)) + ", variavel: " + str(p[1]) + " nao declarada")
                    #exit()
                    flagnaoEstaEscopo = True
                else:
                    flagnaoEstaEscopo = False
                    #aux= valor  

            if flagnaoEstaEscopo == True:
                print("Operacao invalida, na linha: " +  str(p.lineno(1)) + ", variavel: " + str(p[1]) + " nao declarada")
                exit()
            
            if p[3]!= None:
                aux = p[3]
                if aux != True and aux != False and aux >= 0:
                    if p[1].getTamanhoVetor() <= aux:
                        print("Erro: indice do vetor nao existe, linha: " + str(p.lineno(1)))
                        exit()
                    else:
                        p[0] = p[1].getElementoVetor(aux)
                else:
                    print("Erro: Indice nao valido para o vetor, linha: " + str(p.lineno(1)))
                    exit()
            else:
                print("Erro: Indice nao valido para o vetor, linha: " + str(p.lineno(1)))
                exit()
            



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
    global Escopo

    if len(p) > 1:
        flagnaoEstaEscopo = False
        
        #falta fazer
        #if p[2] == "(" and p[4] == ")":


        #falta fazer
        #elif p[2] == "(" and p[3] == ")":

        #se p[1] e um elemento de um vetor
        if p[2] == "[":
            for valor in Escopo:
                if p[1] not in valor:
                    #print("Operacao invalida, na linha: " +  str(p.lineno(1)) + ", variavel: " + str(p[1]) + " nao declarada")
                    #exit()
                    flagnaoEstaEscopo = True
                else:
                    flagnaoEstaEscopo = False
                    #aux= valor  
            #nao esta em nenhum escopo
            if flagnaoEstaEscopo == True:
                print("Operacao invalida, na linha: " +  str(p.lineno(1)) + ", variavel: " + str(p[1]) + " nao declarada")
                exit()

            if p[3] != None:
                aux = p[3]
                if aux != True and aux != False:
                    if p[1].getTamanhoVetor() <= aux:
                        print("Erro: indice do vetor nao existe, linha: " + str(p.lineno(1)))
                        exit()
                    else:
                        p[0] = p[1].getValor(aux)
                else:
                    print("Erro: Indice nao valido para o vetor, linha: " + str(p.lineno(1)))
                    exit()
            else:
                print("Erro: Indice nao valido para o vetor, linha: " + str(p.lineno(1)))
                exit()
            
        #se p[1] e um identificador simples
        elif p[1]!= str and p[1] != int and  p[2] != "(" and p[2] != "[":
            for valor in Escopo:
                if p[1] not in valor:
                    #print("Operacao invalida, na linha: " +  str(p.lineno(1)) + ", variavel: " + str(p[1]) + " nao declarada")
                    #exit()
                    flagnaoEstaEscopo = True
                else:
                    flagnaoEstaEscopo = False
                    #aux= valor  

            if flagnaoEstaEscopo == True:
                print("Operacao invalida, na linha: " +  str(p.lineno(1)) + ", variavel: " + str(p[1]) + " nao declarada")
                exit()        
            
            p[0] =  p[1].getValor()
        #se p[1] e um caractere
        elif type(p[1]) ==  str:
            #p[1].setTipo('car')
            p[0] = p[1]
        #se p[1] e um inteiro constante
        elif type(p[1]) == int:
            #p[1].setTipo('int')
            p[0] = p[1]
        # p[1] e uma expressao entre parenteses
        elif p[1] == "(":
            p[0] = p[1]

def p_listexpr(p):
    """
    listexpr : assignexpr
    listexpr : listexpr VIRGULA assignexpr
    """

def p_error(p):
    print("ERRO, token " + p.type + " nao esperado na linha " + str(p.lineno))
    #print (p.__dict__.keys())
    exit()

valor = sintatic.yacc()
arquivo = open("entrada.txt", "r").read()
print(valor.parse(arquivo))