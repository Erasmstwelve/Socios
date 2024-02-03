# Definir el tamaño del cine (filas y columnas de asientos)
filas = 5
columnas = 10

cine = [['O' for _ in range(columnas)] for _ in range(filas)]

def mostrar_disponibilidad():
    print("Disponibilidad de asientos:")
    for i in range(filas):
        for j in range(columnas):
            print(cine[i][j], end=' ')
        print()

def reservar_asientos(fila, columna):
    if cine[fila - 1][columna - 1] == 'O':
        cine[fila - 1][columna - 1] = 'X'
        print(f"Asiento {fila}-{columna} reservado exitosamente.")
        return True
    else:
        print(f"Lo siento, el asiento {fila}-{columna} ya está ocupado. Por favor, elige otro.")
        return False

def main():
    while True:
        print("\n1. Mostrar disponibilidad de asientos")
        print("2. Reservar asientos")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == '1':
            mostrar_disponibilidad()
        elif opcion == '2':
            fila = int(input("Ingresa el número de fila: "))
            columna = int(input("Ingresa el número de columna: "))
            reservar_asientos(fila, columna)
        elif opcion == '3':
            print("Gracias por usar el Sistema de Reservas de Cine. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
