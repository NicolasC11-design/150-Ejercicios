Contraseña = "MiClave123" 
longitud_minima = 8 

print("Contraseña a validar:", Contraseña)
print("Longitud de la contraseña:", len(Contraseña))

if len(Contraseña) >= longitud_minima:
    print("La contraseña tiene la longitud correcta")
if Contraseña.islower():
    print("La Contraseña no tiene la minima longitud") 
    