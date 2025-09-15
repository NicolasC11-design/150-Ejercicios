Nota = int(input("Ingrese su Calificacion: "))

if Nota >= 5.0:
    Calificacion = "Excelente"
    Mensaje = "¡Felicidades! Sigue asi"
elif Nota >= 3.0:
    Calificacion = "Necesita Mejorar"
    Mensaje = "Buen Trabajo, Debes Mejorar"
else:
    Calificacion = "Mal"
    Mensaje = "Necesitas estudiar mas"

print("Tu Nota es: ", Nota)
print("Calificacion", Calificacion) 
print("Comentario", Mensaje)         