#
# autor: Michel Silva
#
# data: 20/09/2023

from agenda import Agenda as A
#

a1 = A()

a1.add("Michel", "email", "rua das casas", "CZ")
a1.add("João", "email", "rua", "cidade")
a1.add("Maria", "email", "rua", "cidade")

a1.buscar("Michel")
a1.buscar("José")