def convertir_longitud(valor, unidad_origen, unidad_destino):
    unidades = {
        "metros": 1,
        "kilometros": 0.001,
        "millas": 0.000621371,
        "pulgadas": 39.3701,
        "centimetros": 100
    }
    resultado = valor * unidades[unidad_origen] / unidades[unidad_destino]
    return resultado

def convertir_masa(valor, unidad_origen, unidad_destino):
    unidades = {
        "kilogramos": 1,
        "gramos": 1000,
        "libras": 2.20462,
        "onzas": 35.274
    }
    resultado = valor * unidades[unidad_origen] / unidades[unidad_destino]
    return resultado

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == unidad_destino:
        return valor
    
    if unidad_origen == "celsius" and unidad_destino == "fahrenheit":
        return (valor * 9/5) + 32
    elif unidad_origen == "fahrenheit" and unidad_destino == "celsius":
        return (valor - 32) * 5/9
    else:
        print("No se puede realizar la conversión de temperatura deseada.")

def main():
    print("Conversor de Unidades:")
    
    while True:
        print("\nMenú:")
        print("1. Longitud")
        print("2. Masa")
        print("3. Temperatura")
        print("4. Salir")

        choice = input("Seleccione una opción (1-4): ")

        if choice == "1":
            valor = float(input("Ingrese el valor a convertir: "))
            unidad_origen = input("Ingrese la unidad de origen (metros, kilometros, millas, pulgadas, centimetros): ")
            unidad_destino = input("Ingrese la unidad de destino (metros, kilometros, millas, pulgadas, centimetros): ")
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
            print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}")

        elif choice == "2":
            valor = float(input("Ingrese el valor a convertir: "))
            unidad_origen = input("Ingrese la unidad de origen (kilogramos, gramos, libras, onzas): ")
            unidad_destino = input("Ingrese la unidad de destino (kilogramos, gramos, libras, onzas): ")
            resultado = convertir_masa(valor, unidad_origen, unidad_destino)
            print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}")

        elif choice == "3":
            valor = float(input("Ingrese el valor a convertir: "))
            unidad_origen = input("Ingrese la unidad de origen (celsius, fahrenheit): ")
            unidad_destino = input("Ingrese la unidad de destino (celsius, fahrenheit): ")
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
            print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}")

        elif choice == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()
