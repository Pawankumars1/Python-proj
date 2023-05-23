import mysql.connector

# Function to establish a connection to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bill123$",
            database="task_manager"
        )
        print("Connected to MySQL database!")
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None

# Function to create the tasks table if it doesn't exist
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description VARCHAR(255) NOT NULL,
                completed ENUM('Yes', 'No') NOT NULL
            )
        """)
        print("Tasks table created successfully!")
    except mysql.connector.Error as error:
        print("Error creating tasks table:", error)

# Function to display all tasks
def view_tasks(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        if tasks:
            print("--- Tasks ---")
            print("ID  |  Name         | Description                   | Completed")
            print("--------------------------------------------------------------")
            for task in tasks:
                print(f"{task[0]:<4}|  {task[1]:<12}| {task[2]:<30}| {task[3]}")
        else:
            print("No tasks found.")
    except mysql.connector.Error as error:
        print("Error viewing tasks:", error)

# Function to add a new task
def add_task(connection):
    try:
        name = input("Task Name: ")
        description = input("Task Description: ")
        completed = input("Completion Status (Yes/No): ")

        cursor = connection.cursor()
        query = "INSERT INTO tasks (name, description, completed) VALUES (%s, %s, %s)"
        values = (name, description, completed)
        cursor.execute(query, values)
        connection.commit()
        print("Task added successfully!")
    except mysql.connector.Error as error:
        print("Error adding task:", error)

# Function to delete a task
def delete_task(connection):
    try:
        task_id = int(input("Enter the ID of the task you want to delete: "))

        cursor = connection.cursor()
        query = "DELETE FROM tasks WHERE id = %s"
        values = (task_id,)
        cursor.execute(query, values)
        connection.commit()
        print("Task deleted successfully!")
    except mysql.connector.Error as error:
        print("Error deleting task:", error)

# Main function to run the task manager
def run_task_manager():
    connection = create_connection()

    if connection:
        create_table(connection)

        while True:
            print("\nWelcome to the Task Manager!\n")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Delete Task")
            print("4. Quit\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                view_tasks(connection)
            elif choice == "2":
                add_task(connection)
            elif choice == "3":
                delete_task(connection)
            elif choice == "4":
                print("\n--- Quitting Task Manager ---")
                break
            else:
                print("Invalid choice. Please try again.")

        connection.close()
        print("MySQL connection closed.")

# Run the task manager
run_task_manager()
