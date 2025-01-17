def display_menu(items):  # More flexible with a list of items
    """Displays the vending machine menu."""
    print("Welcome to the Vending Machine!")
    for i, item in enumerate(items):
        print(f"{i+1}. {item}")

def get_user_selection(num_items):  # Validates based on number of items
    """Prompts the user to make a selection and returns the selection."""
    while True:
        try:
            selection = int(input("Enter your selection: "))
            if 1 <= selection <= num_items:
                return selection
            else:
                print(f"Invalid selection. Please enter a number between 1 and {num_items}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def vend_item(selection, items):  # Uses the item list
    """Simulates vending the selected item."""
    print(f"Vending {items[selection - 1]}... Enjoy!")

def main():
    """Main function to run the vending machine simulation."""
    items = ["Cola", "Chips", "Candy", "Water"]  # Now you can easily add more!
    display_menu(items)
    selection = get_user_selection(len(items))
    vend_item(selection, items)

if __name__ == "__main__":
    main()