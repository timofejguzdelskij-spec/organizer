tasks = []  # список задач

def show_menu():
    print("\n1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Отметить выполненной")
    print("4. Выйти")

def add_task(tasks):
    task = input("Введи задачу: ")
    tasks.append(task)

def show_tasks(tasks):
    for i, t in enumerate(tasks):
        print(f"{i + 1}. {t}")
    print("\n\n\n")  # ← 3 пустые строки (3 пробела-перевода) между задачами и меню

while True:
    show_menu()
    choice = input("Выбери действие: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        print("Функция в разработке")
    elif choice == "4":
        break
    else:
        print("Неверный ввод!")

