shopping_list = []
def add_item(item):
    """Add an item to the shopping list."""
    shopping_list.append(item)
def remove_item(item):
    """Remove an item from the shopping list if it exists."""
    if item in shopping_list:
        shopping_list.remove(item)
def view_list():
    """Return the current shopping list."""
    return shopping_list

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
            print(f'"{item}" has been added to the shopping list.')
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item)   
            print(f'"{item}" has been removed from the shopping list.')
            # Prompt for and remove an item
        elif choice == '3':
            print("Current Shopping List:")
            print(view_list())
            # Display the shopping list
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()