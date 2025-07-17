import random

print("Bienvenido a Apuestas Deportivas \nDonde el dinero fluye y los goles no paran")

monto_apuesta = int(input("Por favor ingrese su apuesta: $"))
prediccion_a = int(input("Cuántos goles predices que anotará el equipo A (0-9): "))
prediccion_b = int(input("Cuántos goles predices que anotará el equipo B (0-9): "))

goles_a = random.randint(0, 9)
goles_b = random.randint(0, 9)

print(f"\nResultados del partido\nGoles del equipo A: {goles_a}\nGoles del equipo B: {goles_b}")

if goles_a == prediccion_a and goles_b == prediccion_b:
    print("Predicción exacta: Has acertado al número de goles de ambos equipos")
    print("¡Felicidades, ganaste el premio mayor!")
    print(f"Premio obtenido: ${monto_apuesta * 20}")
elif goles_a > goles_b and prediccion_a > prediccion_b:
    print("Predicción correcta: Pudiste predecir la victoria del equipo A")
    print("¡Felicidades, ganaste el premio menor!")
    print(f"Premio obtenido: ${monto_apuesta * 10}")
elif goles_b > goles_a and prediccion_b > prediccion_a:
    print("Predicción correcta: Pudiste predecir la victoria del equipo B")
    print("¡Felicidades, ganaste el premio menor!")
    print(f"Premio obtenido: ${monto_apuesta * 10}")
elif goles_a == goles_b and prediccion_a == prediccion_b:
    print("Predicción correcta: Pudiste predecir el empate de ambos equipos")
    print("¡Felicidades, ganaste el premio menor!")
    print(f"Premio obtenido: ${monto_apuesta * 10}")
else:
    print("Perdiste, tu predicción del partido fue errónea")
    print("No obtuviste ningún premio")