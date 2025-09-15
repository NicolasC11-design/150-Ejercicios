def calcular_similitud(usuario1, usuario2):
    """Calcula la similitud entre dos usuarios basada en gustos comunes. Retorna un valor entre 0 (muy diferentes) y 1 (muy similares)."""
    gustos_comunes = 0
    total_comparaciones = 0

    for categoria in usuario1:
        if categoria in usuario2:
            total_comparaciones += 1
            if usuario1[categoria] == usuario2[categoria]:
                gustos_comunes += 1

    if total_comparaciones == 0:
        return 0

    similitud = gustos_comunes / total_comparaciones
    return round(similitud, 2)


def encontrar_usuarios_similares(usuario_objetivo, base_usuarios, umbral=0.5):
    """Encuentra usuarios similares al usuario objetivo."""
    similares = []
    print(f"\nBuscando usuarios similares a '{usuario_objetivo}' (umbral = {umbral})")
    print("-" * 40)

    gustos_objetivo = base_usuarios[usuario_objetivo]
    for nombre_usuario, gustos_usuario in base_usuarios.items():
        if nombre_usuario != usuario_objetivo:
            similitud = calcular_similitud(gustos_objetivo, gustos_usuario)
            print(f"{nombre_usuario}: similitud = {similitud}")
            if similitud >= umbral:
                similares.append((nombre_usuario, similitud))

    similares.sort(key=lambda x: x[1], reverse=True)
    return similares


def recomendar_contenido(usuario_objetivo, usuarios_similares, base_usuarios):
    """Recomienda contenido al usuario objetivo basado en gustos de usuarios similares."""
    gustos_objetivo = base_usuarios[usuario_objetivo]
    recomendaciones = {}

    print(f"\nGenerando recomendaciones para '{usuario_objetivo}':")
    for nombre_similar, similitud in usuarios_similares:
        gustos_similar = base_usuarios[nombre_similar]
        print(f"\nAnalizando gustos de {nombre_similar} (similitud: {similitud}):")

        for categoria, le_gusta in gustos_similar.items():
            if categoria not in gustos_objetivo and le_gusta:
                if categoria not in recomendaciones:
                    recomendaciones[categoria] = []
                recomendaciones[categoria].append((nombre_similar, similitud))
                print(f" → Recomendar '{categoria}' (le gusta a {nombre_similar})")

    return recomendaciones




usuarios = {
    "Julia": {
        "acción": True, "comedia": False, "drama": True,
        "misterio": True, "documental": False
    },
    "David": {
        "acción": True, "comedia": False, "drama": True,
        "misterio": False, "documental": True
    },
    "Lucía": {
        "acción": False, "comedia": True, "drama": False,
        "misterio": True, "documental": False
    },
    "Marco": {
        "acción": True, "comedia": False, "drama": True,
        "misterio": True, "documental": False
    },
    "Elena": {
        "acción": False, "comedia": True, "drama": True,
        "misterio": False, "documental": True
    }
}



print("SISTEMA DE RECOMENDACIÓN DE CONTENIDO")
print("=" * 45)


print("\nBase de usuarios:")
for usuario, gustos in usuarios.items():
    print(f" - {usuario}: {gustos}")

print("\n" + "=" * 50)


usuario_objetivo = "Julia"
usuarios_similares = encontrar_usuarios_similares(usuario_objetivo, usuarios, umbral=0.5)

print(f"\nUsuarios similares a {usuario_objetivo}:")
for nombre, sim in usuarios_similares:
    print(f" - {nombre}: {sim * 100:.0f}% similar")

recomendaciones = recomendar_contenido(usuario_objetivo, usuarios_similares, usuarios)

print("\n" + "=" * 40)
print("RECOMENDACIONES FINALES")
print("=" * 40)
if recomendaciones:
    for categoria, recomendadores in recomendaciones.items():
        nombres = ", ".join(f"{u} ({s:.2f})" for u, s in recomendadores)
        print(f"✔ '{categoria}' recomendado por: {nombres}")
else:
    print("No hay recomendaciones disponibles.")
