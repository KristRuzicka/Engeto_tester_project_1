"""
main.py: Task Manager
author: Kristýna Růžičková
email: krist.ruzickova@gmail.com
"""
tasks = []
separator = 30*"="

# Prints Main Menu with options.
def main_menu():
    print("\nTask manager - Main menu\n" 
    "1. Add new task\n"
    "2. View all tasks\n" 
    "3. Remove task\n"
    "4. End program\n"
    )

# Takes input from user. Adds task to the list of tasks.
def add_task():
    task_name = input("Enter task name:" )
    task_description = input("Enter task description:" )
    while not task_name or not task_description:
        print("\nThis is an empty entry. Please enter valid value.")
        task_name = input("Enter task name:" )
        task_description = input("Enter task description:" )
    print(f"\nTask {task_name} has been added.")
    print(separator)
    tasks.append({"name": task_name,
         "description": task_description})
    return tasks
    
# Prints a list of tasks with sequential number.
def view_tasks():
        if len(tasks) == 0:
            print("\nNo tasks have been added yet.")
        else:
            print("Added tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task["name"]} - {task["description"]}")
        print(separator)

# Removes selected task from the list of tasks.
def remove_task():
    if len(tasks) == 0:
        print("\nNo tasks have been added yet.")
    else:
        view_tasks()
        try:
            task_number = int(input("Enter number of task which should be removed: "))

            if task_number not in range(1, len(tasks)+1):
                print(f"\nThis task number is not listed.")
            else: 
                print(f"Task number {task_number} has been removed.")
                tasks.pop(task_number-1)
        except ValueError:
            print("Please enter a valid number.")

    print(separator)

# Main loop
while True:
    main_menu()
    choice = input("Choose option (1-4):" )
 
    if not choice.isdigit():
        print("Choose valid option (1-4).")
        continue
    print(separator)

    choice = int(choice)
    
    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        remove_task()
    elif choice == 4:
        print("\nEnding program.")
        break
    else: 
        print("\nChoose valid option (1-4).")