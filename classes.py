class NoArvoreVariaveis(object):
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


    def setValor(self, valor, posicao = 0):
        if(self.eVetor == False): #analisando lista de variaveis
            self.valor.insert(0, valor)
        else:
            if posicao < self.tamanhoVetor and posicao >=0 :
                self.valor.insert(posicao, valor)
        
    
class NoArvoreFuncaoAssinatura(object):
    #lista parametros e uma lista de objetos NoArvoreVariaveis
    def __init__(self, tipoRetornoFuncao = None, nomeFuncao = None,  listaParametros = None):
        #self.nome = nome
        self.tipoRetornoFuncao = tipoRetornoFuncao 
        self.nomeFuncao = nomeFuncao
        self.listaParametros = listaParametros
    
    #parametro e um objeto do tipo NoArvoreVariaveis
    def setParametros(self, parametro):
        self.listaParametros.append(parametro)
    
    #pegar um parametro especifico da funcao
    def getParametro(self, posicaoParametro):
        return self.listaParametros[posicaoParametro]


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
