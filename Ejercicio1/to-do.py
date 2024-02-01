from datetime import datetime, timedelta

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, description, due_date, priority):
        task = {"description": description, "due_date": due_date, "priority": priority}
        self.tasks[len(self.tasks) + 1] = task
        print("Tarea agregada con éxito!")

    def edit_task(self, task_id, description=None, due_date=None, priority=None):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            if description:
                task["description"] = description
            if due_date:
                task["due_date"] = due_date
            if priority:
                task["priority"] = priority
            print("Tarea editada con éxito!")
        else:
            print("No se encontró la tarea con ese ID.")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print("Tarea eliminada con éxito!")
        else:
            print("No se encontró la tarea con ese ID.")

    def show_tasks(self):
        print("Lista de Tareas:")
        for task_id, task in self.tasks.items():
            print(f"{task_id}. Descripción: {task['description']}, Fecha de Vencimiento: {task['due_date']}, Prioridad: {task['priority']}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenú:")
        print("1. Agregar tarea")
        print("2. Editar tarea")
        print("3. Eliminar tarea")
        print("4. Mostrar tareas")
        print("5. Salir")

        choice = input("Seleccione una opción (1-5): ")

        if choice == "1":
            description = input("Ingrese la descripción de la tarea: ")
            due_date = input("Ingrese la fecha de vencimiento (DD-MM-YYYY): ")
            priority = input("Ingrese la prioridad de la tarea: ")
            todo_list.add_task(description, due_date, priority)

        elif choice == "2":
            task_id = int(input("Ingrese el ID de la tarea que desea editar: "))
            description = input("Nueva descripción (Deje en blanco si no desea cambiar): ")
            due_date = input("Nueva fecha de vencimiento (Deje en blanco si no desea cambiar): ")
            priority = input("Nueva prioridad (Deje en blanco si no desea cambiar): ")
            todo_list.edit_task(task_id, description, due_date, priority)

        elif choice == "3":
            task_id = int(input("Ingrese el ID de la tarea que desea eliminar: "))
            todo_list.delete_task(task_id)

        elif choice == "4":
            todo_list.show_tasks()

        elif choice == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
