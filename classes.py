

class ArvoreEscopo(object):
    Escopo = {}
    pai = None
    filho = []

    def __init__(self, escopo, pai, filho):
        self.Escopo = escopo
        self.pai = pai
        #self.filho = filho

    def adicionaFilho(self, filho):
        self.filho.append(filho)
    
    def adicionaPai(self, pai):
        self.pai = pai
    
    def getPai(self):
        return self.pai
    
    def getEscopo(self):
        return self.Escopo
    
    def setEscopo(self, escopo):
        self.Escopo = escopo
    
    def getFilho(self):
        return self.filho

    


class NoArvoreVetores(object):
    
    def __init__(self, valor = None, tipo= None):
        self.valor = valor
        self.tipo = tipo
    
    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor
    
    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo



class NoArvoreVariaveis(object):
    #lista de objetos dos demais vetores
    valor = []
    tamanhoVetor = None
    def __init__(self, tipo = None, vetor = False,  tamanhoVetor = 1):
        #self.nome = nome
        self.tipo = tipo 
        self.eVetor = vetor
        self.tamanhoVetor = tamanhoVetor

    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo
    
    def getTamanhoVetor(self):
        return self.tamanhoVetor

    
    def getElementoVetor(self, posicao):
        if posicao < self.tamanhoVetor and posicao >= 0:
            return self.valor[posicao]
    
    #def setElementoVetor(self, posicao):
    #   if 




    def iniciaVetor(self):
        if self.eVetor == True:
            for iterador in range(self.tamanhoVetor):
                self.valor.insert(iterador, NoArvoreVetores(self.tipo))

    def getValor(self, posicao = None):
        if self.eVetor == False:
            return self.valor[0]
        elif self.eVetor == True and posicao < self.tamanhoVetor and posicao >= 0:
            return self.valor[posicao].getValor()

    def setValor(self, valor = None, posicao = None):
        if self.eVetor == False:
            self.valor[0] = valor
        elif self.eVetor == True and posicao < self.tamanhoVetor and posicao >= 0:
            self.valor[posicao].setValor(valor)
            


    '''
    def getValor(self, posicao=None):
        #atributo e um vetor
        if self.eVetor == True and posicao < self.tamanhoVetor and posicao >= 0:
            return self.valor[posicao]
        #atributo e uma  variavel
        elif self.eVetor == False and posicao == None:
            return self.valor[0]


    def setValor(self, valor, posicao = 0):
        if(self.eVetor == False): #variaveis
            self.valor.insert(0, valor)
        else: #vetores
            if posicao < self.tamanhoVetor and posicao >=0 :
                self.valor.insert(posicao, valor)
    '''


    
class NoArvoreFuncaoAssinatura(object):
    #lista parametros e uma lista de objetos NoArvoreVariaveis
    def __init__(self, tipoRetornoFuncao = None, listaParametros = None):
        #self.nome = nome
        self.tipoRetornoFuncao = tipoRetornoFuncao 
        #self.nomeFuncao = nomeFuncao
        self.listaParametros = listaParametros
    
    #parametro e um objeto do tipo NoArvoreVariaveis
    def setParametros(self, parametro):
        self.listaParametros.append(parametro)
    
    #pegar um parametro especifico da funcao
    def getParametro(self, posicaoParametro):
        return self.listaParametros[posicaoParametro]


class Escopo(object):
    
    def __init__(self, nomeEscopo = None, variaveisEscopo = None):
        self.nomeEscopo = nomeEscopo
        self.variaveisEscopo = variaveisEscopo
    

    '''
    Escopo = {}

    def __init__(self, escopo = None):
        self.Escopo = escopo
        
    def criaEscopo(self, nomeEscopo, variaveisEscopo):
        self.Escopo[str(nomeEscopo)] = variaveisEscopo

    def removeEscopo(self, nomeEscopo):
    '''
        

'''
class Comando(object):
    ladoEsquerdoComando = []
    ladoDireitoComando = []
    def __init__(self, ladoEsquerdoComando = None, ladoDireitoComando = None):
        self.ladoEsquerdoComando = ladoEsquerdoComando
        self.ladoDireitoComando = ladoDireitoComando

    def adicionaElementoLadoEsquerdo(self, elemento):
        self.ladoEsquerdoComando.append(elemento)

    def adicionaElementoLadoDireito(self, elemento):
        self.ladoDireitoComando.append(elemento)
'''