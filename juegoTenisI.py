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

def test2(x):
  """"
  prueba2: verifica que se acumule el punto de un jugador
  >>> test2(1)
  30
  """
  
  def juego():
   juego1=score()
   juego1.sumarpto()
   juego1.sumarpto()
   juego1.sumarpto()
   self.assertNotEqual("40", juego1.getvalor())
   print ("ho")
class score(object):
    scores=[0, 15, 30, 40]
    def __init__(self):
        self.valor=valor
    def getvalor(self):
        return self.scores[self.valor]
    def sumarpto(self): 
        self.valor+=1        
    juego() 


