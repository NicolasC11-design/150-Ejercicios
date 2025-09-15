def saludar(nombre): 

    mensaje = f"¡Hola {nombre}! ¿Cómo estás?"
    return mensaje 

saludo1 = saludar("Mateo") 
saludo2 = saludar("Nicolas")
saludo3 = saludar("Michelle") 
print("Usando mi función de saludo:")
print(saludo1)
print(saludo2)
print(saludo3)

print("\nUsando directamente:")
print(saludar("Sebastian"))
print(saludar("Diego"))