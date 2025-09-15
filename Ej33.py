import random
import time

def crear_tablero(filas, columnas, densidad=0.3):
    """
    Crea un tablero inicial con células vivas y muertas
    densidad: probabilidad de que una célula esté viva inicialmente
    """
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            # Aleatoriamente decidir si la célula está viva (1) o muerta (0)
            esta_viva = 1 if random.random() < densidad else 0
            fila.append(esta_viva)
        tablero.append(fila)
    return tablero


def contar_vecinos_vivos(tablero, fila, columna):
    """
    Cuenta cuántos vecinos vivos tiene una célula
    Considera las 8 células adyacentes (incluidas las diagonales)
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinos_vivos = 0

    # Revisar las 8 direcciones posibles
    direcciones = [
        (-1, -1), (-1, 0), (-1, 1),   # Arriba izquierda, arriba, arriba derecha
        (0, -1),          (0, 1),     # Izquierda, derecha
        (1, -1),  (1, 0), (1, 1)      # Abajo izquierda, abajo, abajo derecha
    ]

    for df, dc in direcciones:
        nueva_fila = fila + df
        nueva_columna = columna + dc
        # Verificar que esté dentro de los límites
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            vecinos_vivos += tablero[nueva_fila][nueva_columna]

    return vecinos_vivos


def aplicar_reglas(tablero):
    """
    Aplica las reglas del Juego de la Vida para generar la siguiente generación
    Reglas:
    1. Célula viva con < 2 vecinos vivos: muere (soledad)
    2. Célula viva con 2-3 vecinos vivos: sobrevive
    3. Célula viva con > 3 vecinos vivos: muere (sobrepoblación)
    4. Célula muerta con exactamente 3 vecinos vivos: nace
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    cambios = []  # Para registrar los cambios

    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos_vivos(tablero, i, j)
            celula_actual = tablero[i][j]
            nueva_celula = celula_actual  # Por defecto, mantiene su estado

            if celula_actual == 1:  # Célula viva
                if vecinos < 2:
                    nueva_celula = 0  # Muere por soledad
                    cambios.append((i, j, "murió por soledad"))
                elif vecinos > 3:
                    nueva_celula = 0  # Muere por sobrepoblación
                    cambios.append((i, j, "murió por sobrepoblación"))
                # Si tiene 2 o 3 vecinos, sobrevive (no hay cambio)

            else:  # Célula muerta
                if vecinos == 3:
                    nueva_celula = 1  # Nace
                    cambios.append((i, j, "nació"))

            nuevo_tablero[i][j] = nueva_celula

    return nuevo_tablero, cambios


def mostrar_tablero(tablero, generacion, mostrar_coordenadas=False):
    """Muestra el tablero en formato visual"""
    print(f"\nGeneración {generacion}")
    print("-" * (len(tablero[0]) * 2))

    for i, fila in enumerate(tablero):
        fila_str = ""
        for j, celula in enumerate(fila):
            if celula == 1:
                fila_str += "■ " if not mostrar_coordenadas else f"({i},{j}) "
            else:
                fila_str += "· "
        print(fila_str)
    print("-" * (len(tablero[0]) * 2))


# --- Ejecución del Juego ---
if __name__ == "__main__":
    filas, columnas = 10, 20
    tablero = crear_tablero(filas, columnas, densidad=0.3)

    generaciones = 10
    for gen in range(1, generaciones + 1):
        mostrar_tablero(tablero, gen)
        tablero, cambios = aplicar_reglas(tablero)
        print(f"Cambios en esta generación: {cambios}")
        time.sleep(0.5)
