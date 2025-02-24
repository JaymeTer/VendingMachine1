import time

def log_vending_activity(item):
    """Logs vending machine activity with a timestamp."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("vending_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - Vended: {item}\n")

def display_menu(items, prices):  
    """Displays the vending machine menu."""
    print("Welcome to the Vending Machine!")
    for i, (item, price) in enumerate(zip(items, prices)):
        print(f"{i+1}. {item} - ${price:.2f}")

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

def take_payment(price):  
    """Takes payment from the user and returns the amount given and the change."""
    while True:
        try:
            payment = float(input(f"Please insert ${price:.2f} to purchase this item: $"))
            if payment < price:
                print("Insufficient payment. Please provide enough money.")
            else:
                change = payment - price
                return payment, change
        except ValueError:
            print("Invalid input. Please enter a valid amount of money.")

def vend_item(selection, items, prices):  
    """Simulates vending the selected item."""
    item = items[selection - 1]
    print(f"Vending {item}... Enjoy!")
    log_vending_activity(item)

def main():  
    """Main function to run the vending machine simulation."""
    items = ["Cola", "Chips", "Candy", "Water", "Beer", "Gummies", "Pistol", "Grenade"]
    prices = [1.50, 1.00, 0.75, 1.25, 2.50, 1.00, 5.00, 7.50]  # Prices for each item
    
    display_menu(items, prices)
    
    selection = get_user_selection(len(items))
    selected_price = prices[selection - 1]
    
    payment, change = take_payment(selected_price)
    
    if change > 0:
        print(f"Change to return: ${change:.2f}")
    
    vend_item(selection, items, prices)

if __name__ == "__main__":  
    main()
