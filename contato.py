#
#
# autor: Michel Silva
#
# data: 20/09/2023
from pessoa import Pessoa as P
from endereco import Endereco as E

class Contato(P, E):
  def __init__(self, nome, email, rua, cidade):
    P.__init__(self, nome, email)
    E.__init__(self, rua, cidade)
    

  def mostrar(self):
      P.mostrar(self)
      E.mostrar(self)
      # print()
     
