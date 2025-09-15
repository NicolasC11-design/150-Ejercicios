tupla = (10, 20, 30, 40, 50)
lista = list(tupla)
lista[2] = 99
tupla = tuple(lista)
print(tupla)