def ordenamiento_burbuja(lista):
    """Implementa el algoritmo de ordenamiento burbuja"""
    n = len(lista)
    lista_copia = lista.copy()  
    comparaciones = 0
    intercambios = 0

    print(f"Lista original: {lista_copia}")
    print("\nProceso paso a paso:")

    for i in range(n):
        print(f"\n--- Pasada {i + 1} ---")
        hubo_intercambio = False

        for j in range(0, n - i - 1):
            comparaciones += 1
            print(f"Comparando {lista_copia[j]} y {lista_copia[j + 1]}")

            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
                intercambios += 1
                hubo_intercambio = True
                print(f"Intercambio realizado: {lista_copia}")
            else:
                print("No hay intercambio")

        print(f"Estado después de pasada {i + 1}: {lista_copia}")

        if not hubo_intercambio:
            print("¡No hubo intercambios! La lista ya está ordenada.")
            break

    print(f"\nResultado final: {lista_copia}")
    print("Estadísticas:")
    print(f" - Total de comparaciones: {comparaciones}")
    print(f" - Total de intercambios: {intercambios}")

    return lista_copia



numeros = [64, 34, 25, 12, 22, 11, 90]
print("ALGORITMO DE ORDENAMIENTO BURBUJA")
print("=" * 45)
resultado = ordenamiento_burbuja(numeros)
