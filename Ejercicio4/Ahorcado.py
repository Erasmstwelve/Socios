import random

def seleccionar_palabra():
    palabras = ["jack", "perla", "ahorcado", "garfield", "luna", "kiara","mesopotamia"]
    return random.choice(palabras)

def mostrar_palabra_oculta(palabra, letras_correctas):
    resultado = ""
    for letra in palabra:
        if letra in letras_correctas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def jugar_ahorcado():
    intentos_maximos = 6
    palabra_oculta = seleccionar_palabra()
    letras_correctas = set()
    letras_incorrectas = set()

    while True:
        palabra_mostrada = mostrar_palabra_oculta(palabra_oculta, letras_correctas)
        print(f"\nPalabra actual: {palabra_mostrada}")
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
        
        letra = input("Ingrese una letra: ").lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in letras_correctas or letra in letras_incorrectas:
                print("Ya has intentado con esa letra. ¡Intenta con otra!")
            elif letra in palabra_oculta:
                letras_correctas.add(letra)
                print("¡Letra correcta!")
            else:
                letras_incorrectas.add(letra)
                print("Letra incorrecta. ¡Pierdes un intento!")
                intentos_maximos -= 1
        else:
            print("Por favor, ingresa una letra válida.")

        if intentos_maximos == 0:
            print("¡Perdiste! La palabra correcta era:", palabra_oculta)
            break

        if set(palabra_oculta) == letras_correctas:
            print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
            break

def main():
    print("Bienvenido al Juego del Ahorcado.")
    print("Trata de adivinar la palabra oculta. Tienes 6 intentos.")

    while True:
        jugar_ahorcado()

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_nuevamente != 's':
            print("¡Gracias por jugar! Hasta luego.")
            break

if __name__ == "__main__":
    main()
