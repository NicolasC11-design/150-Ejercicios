import random

class Animal:
    def __init__(self, nombre, tipo, energia=80, posicion_x=0, posicion_y=0):
        self.nombre = nombre
        self.tipo = tipo  
        self.energia = energia
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.vivo = True

    def mover(self):
        """Mueve el animal aleatoriamente (costo energético)"""
        if self.vivo:
            dx = random.randint(-2, 2)
            dy = random.randint(-2, 2)
            self.posicion_x += dx
            self.posicion_y += dy
            self.energia -= 7  
            print(f"{self.nombre} se movió a ({self.posicion_x}, {self.posicion_y}) - Energía: {self.energia}")
            if self.energia <= 0:
                self.vivo = False
                print(f"⚠️ {self.nombre} ha muerto por falta de energía.")
        else:
            print(f"{self.nombre} está muerto y no puede moverse.")

    def comer(self):
        """Restaura energía si está vivo"""
        if self.vivo:
            if self.tipo == "herbívoro":
                energia_recuperada = random.randint(10, 20)
            else:  # carnívoro
                energia_recuperada = random.randint(15, 25)
            self.energia += energia_recuperada
            print(f"{self.nombre} comió y recuperó {energia_recuperada} de energía. Total: {self.energia}")
        else:
            print(f"{self.nombre} está muerto y no puede comer.")

    def estado(self):
        """Imprime el estado actual del animal"""
        estado = "vivo" if self.vivo else "muerto"
        print(f"\n🐾 {self.nombre} ({self.tipo})")
        print(f"   Posición: ({self.posicion_x}, {self.posicion_y})")
        print(f"   Energía: {self.energia}")
        print(f"   Estado: {estado}")



animales = [
    Animal("Leo", "carnívoro"),
    Animal("Luna", "herbívoro"),
    Animal("Fang", "carnívoro", energia=60),
    Animal("Bambi", "herbívoro", energia=50)
]

print("🌿 ECOSISTEMA SIMULADO")
print("=" * 30)


for ronda in range(1, 4):
    print(f"\n🔁 RONDA {ronda}")
    for animal in animales:
        animal.mover()
        animal.comer()
        animal.estado()
