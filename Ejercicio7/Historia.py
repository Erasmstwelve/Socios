import random

personajes = ["Luisa", "Miguel", "Andres", "Ana", "Elena"]
lugares = ["en la ciudad", "en censa", "en las montañas", "en un pueblo", "en Jupiter"]
eventos = ["descubrió un tesoro", "encontró un portal mágico", "se embarcó en una aventura", "conoció a un extraterrestre", "resolvió un misterio"]

def generar_historia():
    personaje = random.choice(personajes)
    lugar = random.choice(lugares)
    evento = random.choice(eventos)

    historia = f"{personaje} {evento} {lugar}."
    return historia

def main():
    print("¡Bienvenido al Generador de Historias Aleatorias!")

    while True:
        print("\n1. Generar historia aleatoria")
        print("2. Salir")

        opcion = input("Selecciona una opción (1/2): ")

        if opcion == '1':
            historia_generada = generar_historia()
            print("\nHistoria generada:")
            print(historia_generada)
        elif opcion == '2':
            print("Gracias por usar el Generador de Historias Aleatorias. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
