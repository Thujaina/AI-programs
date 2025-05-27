def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def read_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]
        return tasks
    except FileNotFoundError:
        return []

def write_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks yet!")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter your task: ")
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print("Task added!")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove: "))
        tasks = read_tasks()
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            write_tasks(tasks)
            print(f"Task '{removed}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
