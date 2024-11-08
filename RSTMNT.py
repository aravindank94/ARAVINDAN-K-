# Restaurant Management System with User Input for Menu and Bill

def get_menu():
    menu = {}
    print("Enter the menu items and their prices (type 'done' when finished):")
    while True:
        item = input("Enter item name (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        try:
            price = float(input(f"Enter price for {item}: "))
            menu[item] = price
        except ValueError:
            print("Invalid price. Please enter a number.")
    return menu

def display_menu(menu):
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    print()

def take_order(menu):
    order = []
    while True:
        item = input("Enter the item you want to order (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        if item in menu:
            try:
                quantity = int(input(f"How many {item}s would you like? "))
                order.append((item, quantity))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Sorry, we don't have that item. Please choose from the menu.")
    return order

def calculate_bill(menu, order):
    total = 0
    print("\nYour order:")
    for item, quantity in order:
        price = menu[item]
        cost = price * quantity
        print(f"{item} x{quantity} @ ${price:.2f} each: ${cost:.2f}")
        total += cost
    print(f"Total bill: ${total:.2f}")
    return total

def process_payment(total):
    while True:
        try:
            payment = float(input(f"Enter the amount to pay (Total bill: ${total:.2f}): "))
            if payment < total:
                print("Insufficient amount. Please enter an amount equal to or greater than the total bill.")
            else:
                change = payment - total
                print(f"Payment received: ${payment:.2f}")
                if change > 0:
                    print(f"Change to be returned: ${change:.2f}")
                break
        except ValueError:
            print("Invalid amount. Please enter a number.")

def main():
    print("Welcome to the Restaurant Management System")
    menu = get_menu()
    if not menu:
        print("No items in the menu. Exiting.")
        return
    while True:
        display_menu(menu)
        order = take_order(menu)
        if order:
            total = calculate_bill(menu, order)
            process_payment(total)
        another_order = input("\nWould you like to place another order? (yes/no): ")
        if another_order.lower() != 'yes':
            print("Thank you for visiting! Have a great day!")
            break

if __name__ == "__main__":
    main()
