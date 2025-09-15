lista = [12, 3, 5, 8, 10, 7]
pares = sum([x for x in lista if x % 2 == 0])
impares = sum([x for x in lista if x % 2 != 0])
print('Suma pares:', pares, 'Suma impares:', impares)