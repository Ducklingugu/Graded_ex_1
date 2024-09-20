# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),        
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))
    print("Sorted Products:")
    for index, (name, price) in enumerate(sorted_products, start=1):
        print(f"{index}) {name}: ${price:.2f}")

def display_products(products_list):
    print("Available Products:")
    for index, (name, price) in enumerate(products_list, start=1):
        print(f"{index}) {name}: ${price:.2f}")


def display_categories():
  print("Categories:")
  for index, category in enumerate(products.keys(), start=1):
     print(f"{index}. {category}")


def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    print("Your Cart:")
    if not cart:
        print("Your cart is empty.")
        return
    for product_name, price, quantity in cart:
        print(f"{product_name} (x{quantity}) - ${price:.2f} each")



def generate_receipt(name, email, cart, total_cost, address):
    print("Receipt")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Products Purchased:")
    for product_name, price, quantity in cart:
        print(f"{product_name} (x{quantity}) - ${price:.2f} each")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")



def validate_name(name):
    parts = name.split()
    if len(parts) != 2 or not all(part.isalpha() for part in parts):
        return False
    return True

def validate_email(email):
    if "@" in email and "." in email.split("@")[-1]:
        return True
    return False


def main():
    cart = []
    total_cost = 0
    
    # Example usage
    print("Welcome to the Online Store!")
    
    # Display products
    for category, items in products.items():
        print(f"\n{category}:")
        display_products(items)
    
    # Sort and display products
    sort_order = input("Enter sort order (asc/desc): ")
    sorted_products = display_sorted_products(products["IT Products"], sort_order)
    print("\nSorted Products:")
    display_products(sorted_products)
    
    # Add to cart example
    product_choice = int(input("Select a product number to add to cart: ")) - 1
    quantity = int(input("Enter quantity: "))
    selected_product = products["IT Products"][product_choice]
    add_to_cart(cart, selected_product, quantity)
    
    # Calculate total cost
    total_cost += selected_product[1] * quantity
    
    # Generate receipt
    name = input("Enter your name (first and last): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name.")
        name = input("Enter your name (first and last): ")
    
    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email.")
        email = input("Enter your email: ")

    address = input("Enter your delivery address: ")
    generate_receipt(name, email, cart, total_cost, address)
    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
