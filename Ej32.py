import re  # Regular expressions para patrones avanzados

def analizar_estructura(texto):
    """Analiza la estructura básica del texto"""
    estadisticas = {
        'caracteres_total': len(texto),
        'caracteres_sin_espacios': len(texto.replace(' ', '')),
        'palabras': len(texto.split()),
        'oraciones': len([s for s in texto.split('.') if s.strip()]),
        'párrafos': len([p for p in texto.split('\n\n') if p.strip()])
    }
    return estadisticas


def encontrar_patrones_email(texto):
    """Encuentra direcciones de email en el texto"""
    patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(patron_email, texto)
    return emails


def encontrar_patrones_telefono(texto):
    """Encuentra números de teléfono en diferentes formatos"""
    patrones = [
        r'\b\d{3}-\d{3}-\d{4}\b',           # 123-456-7890
        r'\b\(\d{3}\)\s?\d{3}-\d{4}\b',     # (123) 456-7890
        r'\b\d{10}\b'                       # 1234567890
    ]
    telefonos = []
    for patron in patrones:
        telefonos.extend(re.findall(patron, texto))
    return telefonos


def analizar_sentimiento_basico(texto):
    """Análisis básico de sentimiento basado en palabras clave"""
    palabras_positivas = [
        'excelente', 'genial', 'fantástico', 'increíble', 'perfecto',
        'bueno', 'feliz', 'contento', 'alegre', 'maravilloso'
    ]
    palabras_negativas = [
        'terrible', 'malo', 'horrible', 'triste', 'enojado',
        'molesto', 'frustrado', 'decepcionado', 'pesimo'
    ]
    texto_lower = texto.lower()
    puntuacion_positiva = sum(1 for palabra in palabras_positivas if palabra in texto_lower)
    puntuacion_negativa = sum(1 for palabra in palabras_negativas if palabra in texto_lower)

    if puntuacion_positiva > puntuacion_negativa:
        sentimiento = "Positivo"
    elif puntuacion_negativa > puntuacion_positiva:
        sentimiento = "Negativo"
    else:
        sentimiento = "Neutral"

    return {
        'positivo': puntuacion_positiva,
        'negativo': puntuacion_negativa,
        'resultado': sentimiento
    }
