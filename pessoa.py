#
# autor: Michel Silva
#
# data: 20/09/2023

#
class Pessoa:
  def __init__(self, nome, email):
    self.nome = nome
    self.email = str(email)
  
  def mostrar(self):
    print(f"{self.nome}, {self.email}")
