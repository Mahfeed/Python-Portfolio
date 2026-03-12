tasks = []
while True:
    print("-------------Tasks Manager-------------") 
    print("1.Add 2.Remove 3.View 4.Sort 5.Exit")
    choice = input("Enter the choice: ").lower()
    
    if choice == "1" or choice == "add":
        new_task = input("Enter the new task:")
        tasks.append(new_task)
        print("Task Added")
    elif choice == "2" or choice == "remove":
        if len(tasks) > 0:
            print(f"your tasks : {tasks}")
            remove_task = input("Enter the task to remove : ")
            if remove_task in tasks:
                tasks.remove(remove_task)
                print("task removed!")
            else:
                print("not found")
        else:
            print('nothing to remove')
    elif choice == "3" or choice == "view":
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}.{task}")
    elif choice == "4" or choice == "sort":
        tasks.sort()
        print("Tasks sorted!")
    elif choice == "5" or choice == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")