import random

ancho = 11
alto = 11

laberinto = [["#"] * ancho for _ in range(alto)]

def imprimir_laberinto():
    for fila in laberinto:
        print(" ".join(fila))
    print()

def recursive_backtracking(x, y):
    laberinto[y][x] = " "

    direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(direcciones)

    for dx, dy in direcciones:
        nx, ny = x + 2 * dx, y + 2 * dy

        if 0 <= nx < ancho and 0 <= ny < alto and laberinto[ny][nx] == "#":
            laberinto[y + dy][x + dx] = " "
            recursive_backtracking(nx, ny)

def encontrar_salida(x, y):
    if x < 0 or x >= ancho or y < 0 or y >= alto or laberinto[y][x] != " ":
        return False

    if x == ancho - 1 or y == alto - 1 or x == 0 or y == 0:
        laberinto[y][x] = "E"  
        return True

    laberinto[y][x] = "."  

    direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(direcciones)

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if encontrar_salida(nx, ny):
            return True

    return False

def main():
    print("Generador de Laberintos\n")
    recursive_backtracking(1, 1) 
    imprimir_laberinto()

    inicio_x, inicio_y = 1, 1 
    encontrar_salida(inicio_x, inicio_y) 
    imprimir_laberinto()

    print("Instrucciones:")
    print("#: Pared")
    print(" : Camino")
    print(".: Camino visitado")
    print("E: Salida\n")

    print("Intenta encontrar la salida del laberinto. ¡Buena suerte!")

    while True:
        mov = input("Ingresa tu movimiento (w/a/s/d para arriba/izquierda/abajo/derecha, 'q' para salir): ")
        if mov == 'q':
            print("¡Hasta luego!")
            break

        dx, dy = 0, 0
        if mov == 'w':
            dy = -1
        elif mov == 'a':
            dx = -1
        elif mov == 's':
            dy = 1
        elif mov == 'd':
            dx = 1

        nx, ny = inicio_x + dx, inicio_y + dy
        if 0 <= nx < ancho and 0 <= ny < alto and laberinto[ny][nx] != '#':
            inicio_x, inicio_y = nx, ny
            laberinto[ny][nx] = "P" 
            imprimir_laberinto()

            if laberinto[ny][nx] == "E":
                print("¡Has encontrado la salida! ¡Felicidades!")
                break
        else:
            print("Movimiento no válido. Intenta nuevamente.")

if __name__ == "__main__":
    main()
