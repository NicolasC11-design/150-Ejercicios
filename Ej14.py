numero = 1 
limite = 50
pares_encontrados = 0
print("Buscando números pares entre 1 y", limite, ":")
while numero <= limite:
    if numero % 2 == 0: 
        print(numero, "es par")
        pares_encontrados = pares_encontrados + 1
    numero = numero + 1
print("\nResumen:")
print("Se encontraron", pares_encontrados, "números pares")