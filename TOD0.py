tasks = []

def display_tasks():
    if len(tasks) == 0:
        print("No tasks in the to-do list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully.")

def delete_task():
    display_tasks()
    task_number = int(input("Enter task number to delete: "))
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task number.")

def update_task():
    display_tasks()
    task_number = int(input("Enter task number to update: "))
    if 1 <= task_number <= len(tasks):
        new_task = input("Enter new task: ")
        tasks[task_number - 1] = new_task
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Update task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
