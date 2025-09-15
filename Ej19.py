animales = ["perro", "gato", "pájaro", "pez", "hamster", "conejo", "gato", "tiburon"]
print("Lista de animales:", animales)

animal_buscado = "gato"

if animal_buscado in animales: 
    print(f"\n{animal_buscado} está en la lista")

    posicion = animales.index(animal_buscado) 
    print(f"Primera aparición en posición: {posicion}")

    cantidad = animales.count(animal_buscado) 
    print(f"Aparece {cantidad} veces en total")
else:
    print(f"\n{animal_buscado} no está en la lista")


buscados = ["gato", "serpiente", "pájaro"]
print(f"\nBuscando: {buscados}")

for animal in buscados:
    if animal in animales:
        posicion = animales.index(animal)
        print(f"{animal} encontrado en posición {posicion}")
    else:
        print(f"{animal} no encontrado")