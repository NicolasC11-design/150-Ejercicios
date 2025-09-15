import math
puntos = ((0, 0), (2, 3), (5, 7))
x1, y1 = puntos[0]
x2, y2 = puntos[2]
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distancia:", distancia)