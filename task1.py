

tasks = []  

while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    
    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    
    elif choice == "3":
        task_no = int(input("Enter task number to mark completed: "))
        if task_no <= len(tasks):
            tasks[task_no - 1] = tasks[task_no - 1] + " ✔"
            print("Task marked as completed!")
        else:
            print("Invalid task number")

    
    elif choice == "4":
        task_no = int(input("Enter task number to delete: "))
        if task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number")

    elif choice == "5":
        print("Thank you for using To-Do List App!")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")
