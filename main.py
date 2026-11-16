tasks = []  # список задач

while True:
    print("\n1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Отметить выполненной")
    print("4. Выйти")

    choice = input("Выбери действие: ")

    if choice == "1":
        task = input("Введи задачу: ")
        tasks.append(task)
    elif choice == "2":
        for i, t in enumerate(tasks):
            print(f"{i + 1}. {t}")
    elif choice == "3":
        # отметить выполненной
        pass
    elif choice == "4":
        break
    else:
        print("Неверный ввод!")
 
