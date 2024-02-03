import random

def generar_datos_simulados():
    temperatura = random.uniform(15.0, 35.0)  
    humedad = random.uniform(30.0, 80.0)  
    estado_tiempo = random.choice(["Despejado", "Nublado", "Lluvia", "Tormenta"])

    return temperatura, humedad, estado_tiempo

def main():
    print("¡Bienvenido al Simulador de Tiempo!")

    while True:
        print("\n1. Obtener información meteorológica")
        print("2. Salir")

        opcion = input("Selecciona una opción (1/2): ")

        if opcion == '1':
            temperatura, humedad, estado_tiempo = generar_datos_simulados()
            print(f"Temperatura: {temperatura:.2f}°C")
            print(f"Humedad: {humedad:.2f}%")
            print(f"Estado del tiempo: {estado_tiempo}")
        elif opcion == '2':
            print("Gracias por usar el Simulador de Tiempo. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
