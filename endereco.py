#
# autor: Michel Silva
#
# data: 20/09/2023

class Endereco:
  def __init__(self, rua, cidade):
    self.rua = str(rua)
    self.cidade = str(cidade)
  
  def mostrar(self):
    print(self.rua)
    print(self.cidade)