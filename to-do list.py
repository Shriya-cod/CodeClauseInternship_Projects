tasks =[]


while True:
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete tasks")
    print("4. Mark as completed")
    print("5. Edit tasks")
    print("6. Save & exit")

    n = int(input("Enter a number from (1-6):"))


    if n==1:
        task = input("Enter a new task:")
        tasks.append({"task": task})
        print(f"Task added: {task}")

    elif n==2:
        if not tasks:
            print("No tasks to display")
        else:
            for i, task in enumerate(tasks , 1):
                status = "completed" if task.get('completed') else "not completed"
                print(f"{i}. {task['task']} - {status}")


    elif n==3:
        if not tasks:
            print("No tasks to be deleted")
        else:
            task_num = int(input("Enter the task number to be deleted:"))
            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num - 1)
                print(f"Task deleted: {deleted_task['task']}")
            else:
                print("Invalid task number")

    elif n==4:
        if not tasks:
            print("No task to be marked as completed")
        else:
            task_num = int(input("Enter the task number to be marked as completed:"))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print(f"Task{task_num} marked as completed")
            else:
                print("Invalid task number")


    elif n==5:
        if not tasks:
            print("No tasks to be edited")
        else:
            task_num = int(input("Enter the task number to be edited:"))
            if 1 <=task_num <=len(tasks):
                new_task = input("Enter the new task:")
                task[task_num - 1]["task"] = new_task
                print(f"Task{task_num} updated")
            else:
                print("Invalid task number")

    elif n==6:
        print("Saving tasks & exiting....")
        break

    else:
        print("Invalid option. Please select a number between 1 and 6")








