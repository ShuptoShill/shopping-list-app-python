# Shopping List App
shopping_list = []

def show_menu():
    print("\n===== Shopping List Menu =====")
    print("1. View Shopping List")
    print("2. Add Item to Shopping List")
    print("3. Remove Item from Shopping List")
    print("4. Clear Shopping List")
    print("5. Exit")
    print("==============================")

def view_list():
    if shopping_list:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("\nYour shopping list is empty.")

def add_item():
    item = input("\nEnter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")
    else:
        print("Item cannot be empty!")

def remove_item():
    view_list()
    if shopping_list:
        try:
            index = int(input("\nEnter the number of the item to remove: "))
            if 1 <= index <= len(shopping_list):
                removed_item = shopping_list.pop(index - 1)
                print(f"'{removed_item}' has been removed from the list.")
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def clear_list():
    confirm = input("\nAre you sure you want to clear the entire shopping list? (yes/no): ").strip().lower()
    if confirm == "yes":
        shopping_list.clear()
        print("Shopping list cleared!")
    else:
        print("Operation canceled.")

# Main program loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ").strip()
    if choice == "1":
        view_list()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        clear_list()
    elif choice == "5":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
