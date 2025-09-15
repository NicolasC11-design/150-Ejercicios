from collections import Counter
import heapq

class NodoHuffman:
    """Nodo para el árbol de codificación Huffman"""

    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def comprimir_repeticion_simple(texto):
    """
    Compresión simple: reemplaza secuencias repetidas
    Ejemplo: "aaaa" -> "4a"
    """
    if not texto:
        return ""

    resultado = []
    contador = 1
    char_actual = texto[0]

    for i in range(1, len(texto)):
        if texto[i] == char_actual:
            contador += 1
        else:
            # Guardar secuencia comprimida
            if contador > 1:
                resultado.append(f"{contador}{char_actual}")
            else:
                resultado.append(char_actual)
            char_actual = texto[i]
            contador = 1

    # Último grupo
    if contador > 1:
        resultado.append(f"{contador}{char_actual}")
    else:
        resultado.append(char_actual)

    return "".join(resultado)


# --- Ejemplo de uso ---
if __name__ == "__main__":
    texto = "aaabbcdddddaa"
    comprimido = comprimir_repeticion_simple(texto)
    print("Texto original:", texto)
    print("Texto comprimido:", comprimido)
