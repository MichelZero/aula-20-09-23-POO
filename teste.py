#
# autor: Michel Silva
#
# data: 20/09/2023

class Pessoa:
  pass

class Endereco:
  pass

class Contato(Pessoa, Endereco):
  pass

class Agenda:
  def somar(self, a, b):
    return a + b
  #pass


a1 = Agenda()
print(a1.somar(1, 2))