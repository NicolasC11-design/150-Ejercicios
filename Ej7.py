Precio_Total = int(input("Ingrese el precio total de su compra: "))
Descuento = 0

if Precio_Total > 100.000:
    Descuento = Precio_Total * 0.10 
    Precio_Final = Precio_Total - Descuento
    print("¡Felicidades! Tienes un descuento del 10%")
    print("Descuento aplicado:$", Descuento)
else:
    Precio_Final = Precio_Total 
    print("No hay descuento disponible")
print("Precio Original: $", Precio_Total)
print("Precio Final: $", Precio_Final)