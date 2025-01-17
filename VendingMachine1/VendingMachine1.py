
def display_menu():
    """Displays the vending machine menu."""
    print("Welcome to the Vending Machine!")
    print("Please select an item by entering the corresponding number:")
    print("1. Cola")
    print("2. Chips")
    print("3. Candy")
    print("4. Water")

def get_user_selection():
    """Prompts the user to make a selection and returns the selection."""
    while True:
        try:
            selection = int(input("Enter your selection: "))
            if selection < 1 or selection > 4:
                print("Invalid selection. Please enter a number between 1 and 4.")
            else:
                return selection
        except ValueError:
            print("Invalid input. Please enter a number.")

def vend_item(selection):
    """Simulates vending the selected item."""
    items = ["Cola", "Chips", "Candy", "Water"]
    print(f"Vending {items[selection - 1]}... Enjoy your {items[selection - 1]}!")

def main():
    """Main function to run the vending machine simulation."""
    display_menu()
    selection = get_user_selection()
    vend_item(selection)

if __name__ == "__main__":
    main()