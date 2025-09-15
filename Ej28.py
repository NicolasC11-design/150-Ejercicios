def contar_frecuencias(lista):
    """Cuenta la frecuencia de cada elemento en la lista. Retorna un diccionario con elemento: frecuencia."""
    frecuencias = {}  
    print(f"\nAnalizando lista: {lista}")
    print("\nProceso de conteo:")

    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
            print(f" {elemento}: incrementado a {frecuencias[elemento]}")
        else:
            frecuencias[elemento] = 1
            print(f" {elemento}: primera aparición")
    
    return frecuencias


def encontrar_mas_frecuente(frecuencias):
    """Encuentra el elemento que más se repite"""
    if not frecuencias:
        return None, 0
    elemento_max = max(frecuencias, key=frecuencias.get)
    frecuencia_max = frecuencias[elemento_max]
    return elemento_max, frecuencia_max


def mostrar_estadisticas(frecuencias):
    """Muestra estadísticas detalladas"""
    print("\n" + "=" * 40)
    print("ESTADÍSTICAS DE FRECUENCIA")
    print("=" * 40)

    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    total_elementos = sum(frecuencias.values())
    elementos_unicos = len(frecuencias)

    print(f"Total de elementos: {total_elementos}")
    print(f"Elementos únicos: {elementos_unicos}")

    print("\nFrecuencias (ordenadas por cantidad):")
    for elemento, frecuencia in frecuencias_ordenadas:
        porcentaje = (frecuencia / total_elementos) * 100
        barra = "█" * frecuencia  # Gráfico de barras simple con bloques
        print(f" {elemento:>3}: {frecuencia:>2} veces ({porcentaje:4.1f}%) {barra}")

    mas_frecuente, max_freq = encontrar_mas_frecuente(frecuencias)
    print(f"\nElemento más frecuente: {mas_frecuente} ({max_freq} veces)")

print("\n" + "=" * 30)
print("CONTADOR DE FRECUENCIAS")
print("=" * 30)

# Ejemplo 1: Lista de números diferentes
numeros = [7, 3, 7, 2, 5, 3, 7, 9, 5, 3, 2, 7, 5]
frecuencias_num = contar_frecuencias(numeros)
mostrar_estadisticas(frecuencias_num)

# Ejemplo 2: Texto diferente
print("\n" + "=" * 50)
texto = "inteligenciaartificial"
letras = list(texto)  # Convierte el texto en lista de caracteres
print(f"\nAnalizando la palabra: '{texto}'")
frecuencias_letras = contar_frecuencias(letras)
mostrar_estadisticas(frecuencias_letras)
