inventory = {"phone": 5, "laptop": 2}

while True:
    print("--- SHOP INVENTORY ---")
    print("1. Add/Update  2. Check Stock  3. View All  4. Exit")
    
    choice = input("Select an option: ")

    if choice == '1':
        item = input("Enter item name: ").lower()
        quantity = int(input(f"Enter quantity for {item}: "))
        inventory[item] = quantity
        print(f"Updated {item}. Total stock: {inventory[item]}")

    elif choice == '2':
        item = input("Search for item: ").lower()
        if item in inventory:
            count = inventory[item]
            if count == 0:
                print(f"ALERT: {item.capitalize()} is Out of Stock!")
            else:
                print(f"{item.capitalize()} stock: {count}")
        else:
            print("Item not found in inventory.")

    elif choice == '3':
        print("\nCurrent Inventory List:")
        for item, count in inventory.items():
            status = "OUT OF STOCK" if count == 0 else count
            print(f"- {item.capitalize()}: {status}")

    elif choice == '4':
        print("Closing tracker...")
        break
    
    else:
        print("Invalid choice.")