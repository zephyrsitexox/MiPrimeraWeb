import random

# 1. La PC piensa el número
numero_secreto = random.randint(1, 100)
intento = 0 # Inicializamos la variable en 0 para que entre al ciclo
intentos_totales = 0

print("🤖: He pensado un número entre 1 y 100. ¿Puedes adivinarlo?")

# 2. El Ciclo: MIENTRAS el intento NO SEA IGUAL (!=) al secreto...
while intento != numero_secreto:
    
    entrada = input("Tu respuesta: ")

    # AQUÍ ESTÁ EL BLINDAJE
    try:
        intento = int(entrada) # Intentamos convertir a número
    except ValueError:
        print("⚠️ ¡Eso no es un número! Escribe un número válido.")
        continue # 'continue' salta al inicio del ciclo otra vez e ignora lo de abajo
    
    # Si todo salió bien arriba, seguimos con la lógica...
    intentos_totales = intentos_totales + 1

    if intento < numero_secreto:
        print("❌ Más ALTO... ↑")
    elif intento > numero_secreto:
        print("❌ Más BAJO... ↓")
    else:
        print(f"🎉 ¡GANASTE! Lo lograste en {intentos_totales} intentos.")