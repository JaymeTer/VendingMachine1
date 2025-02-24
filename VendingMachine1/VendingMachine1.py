import time

def log_vending_activity(item):
    """Logs vending machine activity with a timestamp."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("vending_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - Vended: {item}\n")

def display_menu(items):
    """Displays the vending machine menu."""
    print("Welcome to the Vending Machine!")
    for i, item in enumerate(items):
        print(f"{i+1}. {item}")

def get_user_selection(num_items):
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

def vend_item(selection, items):
    """Simulates vending the selected item and logs it."""
    item = items[selection - 1]
    print(f"Vending {item}... Enjoy!")
    log_vending_activity(item)

def main():
    """Main function to run the vending machine simulation."""
    items = ["Cola", "Chips", "Candy", "Water", "Beer", "Gummies", "Pistol", "Grenade"]
    display_menu(items)
    selection = get_user_selection(len(items))
    vend_item(selection, items)

if __name__ == "__main__":
    main()
