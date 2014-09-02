

"""
cuando se ha iniciado el juego
>>> score().getvalor()
[0, 0]

cuando un jugador anota
>>> score().sumarpto(1).getvalor()
[15, 0]

cuando se ha tirado dos veces
>>> score().sumarpto(2).sumarpto(2).getvalor()
[0, 30]

cuando se ha tirado tres veces
>>> score().sumarpto(2).sumarpto(2).sumarpto(2).getvalor()
[0, 40]

cuando empatan y tienen menos de 40
>>> score().sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).getvalor()
[30, 30]

cuando empatan y tienen 40, 40 (Duce)
>>> score().sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).getvalor()
'Douce'

cuando un jugador lleva ventaja
>>> score().sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).sumarpto(1).getvalor()
['Advantage', 40]

cuando el segundo jugador anota y es un segundo Douce
>>> score().sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).getvalor()
'Douce'

cuando un jugar lleva la ventaja despues del 2 Douce
>>> score().sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).sumarpto(1).getvalor()
['Advantage', 40]

cuando un jugador gana el juego
>>> score().sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(2).sumarpto(1).sumarpto(1).getvalor()
'Win'
"""



class score(object):
    scores = [0, 15, 30, 40, "Advantage", "Win"]
    
    def __init__(self, valor1 = 0, valor2 = 0):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def getvalor(self):
            if (self.scores[self.valor1] == 40 and self.scores[self.valor2] == 40):
                return "Douce"
            elif (self.scores[self.valor1] == "Win" or self.scores[self.valor2] == "Win"): 
                return 'Win'
            else:
                return [self.scores[self.valor1], self.scores[self.valor2]]  

    def gano(self):
        return self.scores ==4

    def sumarpto(self, dos):
        if dos == 1:
            self.valor1 +=1
        else:
            self.valor2 +=1
        
        if self.scores[self.valor1] == 'Advantage' and self.scores[self.valor2] == 'Advantage':
            self.valor1-=1
            self.valor2-=1
            
        if self.getvalor() == "Advantage":
            self.valor1 -=1
            
        return self


    
    

