def convertir_moneda(monto, tasa_cambio):
    return monto * tasa_cambio

def main():
    print("Bienvenido al Conversor de Monedas.")

    while True:
        print("\nMenú:")
        print("1. Utilizar tasas de cambio predefinidas")
        print("2. Ingresar tasas de cambio personalizadas")
        print("3. Salir")

        choice = input("Seleccione una opción (1-3): ")

        if choice == "1":
            tasas_cambio = {"USD a EUR": 0.85, "USD a GBP": 0.73, "USD a JPY": 113.14}
            for i, (moneda, tasa) in enumerate(tasas_cambio.items(), 1):
                print(f"{i}. {moneda} - Tasa de Cambio: {tasa}")

            seleccion = int(input("Seleccione una tasa de cambio (1-3): "))
            if 1 <= seleccion <= 3:
                moneda_origen = "USD"
                moneda_destino = list(tasas_cambio.keys())[seleccion - 1].split(" a ")[1]
                monto = float(input(f"Ingrese el monto en {moneda_origen}: "))
                tasa_seleccionada = tasas_cambio[list(tasas_cambio.keys())[seleccion - 1]]
                resultado = convertir_moneda(monto, tasa_seleccionada)
                print(f"{monto} {moneda_origen} son {resultado} {moneda_destino}")

        elif choice == "2":
            moneda_origen = input("Ingrese la moneda de origen: ")
            moneda_destino = input("Ingrese la moneda de destino: ")
            tasa_cambio_personalizada = float(input(f"Ingrese la tasa de cambio de {moneda_origen} a {moneda_destino}: "))
            monto = float(input(f"Ingrese el monto en {moneda_origen}: "))
            resultado = convertir_moneda(monto, tasa_cambio_personalizada)
            print(f"{monto} {moneda_origen} son {resultado} {moneda_destino}")

        elif choice == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

if __name__ == "__main__":
    main()
