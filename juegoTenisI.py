# TDD partido de tenis
def  test1 (x):
    """
    prueba 1: verificar que no se ha anotado ningun tanto
    >>> test1(1)
    0
    """
    ju1=[]
    ju2=[]
    ju1.append(0)
    ju2.append(0)
    return ju1[-1] if x==1 else ju2[-1]


class score(object):
    scores = [0, 15, 30, 40]
    
    def __init__(self, valor):
        self.valor = valor
    
    def getvalor(self):
        return self.scores[self.valor]

    def sumarpto(self): 
        self.valor+=1     


def juego(x):
    juego1 = score(0)
    juego1.sumarpto()
    juego1.sumarpto()
    #juego1.sumarpto()
    return juego1.getvalor()

def test2(x):
    """"
    prueba2: verifica que se acumule el punto de un jugador
    >>> test2(1)
    30
    """
    return juego(x)
  

