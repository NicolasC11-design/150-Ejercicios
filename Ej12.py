Numero = 5 
Multiplicador = 1
 
print("Tabla de multiplicar del", Numero, ":")
print("=" * 25) 

while Multiplicador <= 10:
    resultado = Numero * Multiplicador
    print(Numero, "x", Multiplicador, "=", resultado)
    Multiplicador = Multiplicador + 1
    print("=" * 25)
    print("¡Tabla completa!")