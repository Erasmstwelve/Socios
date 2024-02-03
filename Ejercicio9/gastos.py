registro_gastos = {}

def ingresar_gasto():
    fecha = input("Ingrese la fecha (formato YYYY-MM-DD): ")
    monto = float(input("Ingrese el monto del gasto en pesos: "))
    categoria = input("Ingrese la categoría del gasto: ")

    if fecha not in registro_gastos:
        registro_gastos[fecha] = []

    gasto = {"monto": monto, "categoria": categoria}
    registro_gastos[fecha].append(gasto)
    print(f"Gasto de {monto} pesos en la categoría '{categoria}' registrado el {fecha}.")

def main():
    while True:
        print("\n1. Ingresar un nuevo gasto")
        print("2. Calcular total de gastos en una fecha")
        print("3. Generar informe de gastos por categoría")
        print("4. Establecer presupuesto mensual por categoría")
        print("5. Verificar presupuesto mensual")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            ingresar_gasto()
        elif opcion == '2':
            fecha = input("Ingrese la fecha para calcular el total de gastos (formato YYYY-MM-DD): ")
            calcular_total_gastos(fecha)
        elif opcion == '3':
            generar_informe_categorias()
        elif opcion == '4':
            categoria = input("Ingrese la categoría para establecer el presupuesto mensual: ")
            presupuesto = float(input("Ingrese el presupuesto mensual para la categoría: "))
            establecer_presupuesto_mensual(categoria, presupuesto)
        elif opcion == '5':
            fecha = input("Ingrese la fecha para verificar el presupuesto mensual (formato YYYY-MM-DD): ")
            verificar_presupuesto_mensual(fecha)
        elif opcion == '6':
            print("Gracias por usar el Registro de Gastos. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
