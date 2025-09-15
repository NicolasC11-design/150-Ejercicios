Numero_Secreto = int(input("Ingrese el numero secreto: "))
Adivinanza = int(input("Ingrese un numero del 1-100: "))

print("El Numero secreto es: ", Numero_Secreto)
print("Tu adivinanza es: ", Adivinanza)

if Adivinanza == Numero_Secreto:
    print("¡FELICIDADES! Adivinaste el numero")
elif Adivinanza < Numero_Secreto: 
    print("Tu Numero es menor, Intenta de nuevo con uno mas grande")
else:
    print("Tu Numero es menor, Intenta de nuevo con uno mas pequeño")