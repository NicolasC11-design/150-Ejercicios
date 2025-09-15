numeros = [23, 47, 58, 62, 74, 39, 85, 91, 16, 44, 68]

print("Lista original:", numeros)
print("Cantidad de elementos:", len(numeros))

numeros_ascendente = numeros.copy() 
numeros_descendente = numeros.copy()

numeros_ascendente.sort() 
print("\nOrdenada ascendente:", numeros_ascendente)

numeros_descendente.sort(reverse=True) 
print("Ordenada descendente:", numeros_descendente)

import random 
numeros_mezclados = numeros.copy()
random.shuffle(numeros_mezclados) 
print("Lista mezclada:", numeros_mezclados)

numeros_invertidos = numeros.copy()
numeros_invertidos.reverse()
print("Orden invertido:", numeros_invertidos)
print("\nLista original (sin cambios):", numeros)