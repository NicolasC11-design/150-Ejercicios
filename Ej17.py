compras = ["pan", "leche", "huevos"]
print("Lista inicial:")
print(compras)

compras.append("queso") 
compras.append("yogur")
print("\nDespués de agregar queso y yogur:")
print(compras)

compras.insert(1, "mantequilla") 
print("\nDespués de insertar mantequilla en posición 1:")
print(compras)

compras.remove("huevos") 
print("\nDespués de eliminar huevos:")
print(compras)

elemento_eliminado = compras.pop(0) 
print("\nEliminamos el primer elemento:", elemento_eliminado)
print("Lista final:", compras)