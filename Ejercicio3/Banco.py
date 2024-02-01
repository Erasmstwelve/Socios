class BancoDeDatos:
    def __init__(self):
        self.registros = {}

    def agregar_registro(self, identificador, nombre, edad, saldo):
        if identificador not in self.registros:
            self.registros[identificador] = {"Nombre": nombre, "Edad": edad, "Saldo": saldo}
            print("Registro agregado con éxito!")
        else:
            print("Ya existe un registro con ese identificador. Utilice la opción de actualización para modificarlo.")

    def actualizar_registro(self, identificador, nombre=None, edad=None, saldo=None):
        if identificador in self.registros:
            if nombre:
                self.registros[identificador]["Nombre"] = nombre
            if edad:
                self.registros[identificador]["Edad"] = edad
            if saldo:
                self.registros[identificador]["Saldo"] = saldo
            print("Registro actualizado con éxito!")
        else:
            print("No se encontró un registro con ese identificador. Utilice la opción de agregar para crear uno nuevo.")

    def eliminar_registro(self, identificador):
        if identificador in self.registros:
            del self.registros[identificador]
            print("Registro eliminado con éxito!")
        else:
            print("No se encontró un registro con ese identificador.")

    def buscar_registro(self, identificador):
        if identificador in self.registros:
            print(f"Registro encontrado:\nID: {identificador}\nNombre: {self.registros[identificador]['Nombre']}\nEdad: {self.registros[identificador]['Edad']}\nSaldo: {self.registros[identificador]['Saldo']}")
        else:
            print("No se encontró un registro con ese identificador.")

    def mostrar_registros(self):
        if self.registros:
            print("Registros en la base de datos:")
            for identificador, info in self.registros.items():
                print(f"ID: {identificador}, Nombre: {info['Nombre']}, Edad: {info['Edad']}, Saldo: {info['Saldo']}")
        else:
            print("La base de datos está vacía.")

def main():
    banco_de_datos = BancoDeDatos()

    while True:
        print("\nMenú:")
        print("1. Agregar registro")
        print("2. Actualizar registro")
        print("3. Eliminar registro")
        print("4. Buscar registro")
        print("5. Mostrar todos los registros")
        print("6. Salir")

        choice = input("Seleccione una opción (1-6): ")

        if choice == "1":
            identificador = input("Ingrese el identificador del nuevo registro: ")
            nombre = input("Ingrese el nombre: ")
            edad = input("Ingrese la edad: ")
            saldo = input("Ingrese el saldo: ")
            banco_de_datos.agregar_registro(identificador, nombre, edad, saldo)

        elif choice == "2":
            identificador = input("Ingrese el identificador del registro a actualizar: ")
            nombre = input("Nuevo nombre (Deje en blanco si no desea cambiar): ")
            edad = input("Nueva edad (Deje en blanco si no desea cambiar): ")
            saldo = input("Nuevo saldo (Deje en blanco si no desea cambiar): ")
            banco_de_datos.actualizar_registro(identificador, nombre, edad, saldo)

        elif choice == "3":
            identificador = input("Ingrese el identificador del registro a eliminar: ")
            banco_de_datos.eliminar_registro(identificador)

        elif choice == "4":
            identificador = input("Ingrese el identificador del registro a buscar: ")
            banco_de_datos.buscar_registro(identificador)

        elif choice == "5":
            banco_de_datos.mostrar_registros()

        elif choice == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()
