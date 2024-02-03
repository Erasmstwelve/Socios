import random
preguntas_respuestas = {
    "Ciencia": [
        {"pregunta": "¿Cuál es el planeta más grande del sistema solar?", "respuesta": "Júpiter"},
        {"pregunta": "¿Cuál es el elemento químico con el símbolo 'O'?", "respuesta": "Oxígeno"},
        {"pregunta": "¿Cuál es la velocidad de la luz?", "respuesta": "299,792 kilómetros por segundo"},
    ],
    "Historia": [
        {"pregunta": "¿En qué año comenzó la Primera Guerra Mundial?", "respuesta": "1914"},
        {"pregunta": "¿Quién fue el primer presidente de Estados Unidos?", "respuesta": "George Washington"},
        {"pregunta": "¿Cuándo cayó el Muro de Berlín?", "respuesta": "1989"},
    ],
    "Geografía": [
        {"pregunta": "¿Cuál es la capital de Francia?", "respuesta": "París"},
        {"pregunta": "¿En qué continente se encuentra Australia?", "respuesta": "Oceanía"},
        {"pregunta": "¿Cuál es el río más largo del mundo?", "respuesta": "El río Amazonas"},
    ],
}

def jugar():
    categoria = random.choice(list(preguntas_respuestas.keys()))
    print(f"Categoría seleccionada: {categoria}")
    
    pregunta = random.choice(preguntas_respuestas[categoria])
    print(f"Pregunta: {pregunta['pregunta']}")

    respuesta_usuario = input("Tu respuesta: ").strip().capitalize()

    if respuesta_usuario == pregunta["respuesta"]:
        print("¡Correcto! Has acertado.")
    else:
        print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}.")

def main():
    print("¡Bienvenido al Juego de Preguntas y Respuestas!")

    while True:
        print("\n1. Jugar")
        print("2. Salir")

        opcion = input("Selecciona una opción (1/2): ")

        if opcion == '1':
            jugar()
        elif opcion == '2':
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
