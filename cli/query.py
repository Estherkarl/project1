
"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""


from data import warehouse1, warehouse2
user_name = input("What is your user name? ")

# Greet the user
print(f"\nHello, {user_name}!")

# Display menu options
print("What would you like to do?")
print("1. List items by warehouse")
print("2. Search an item and place an order")
print("3. Quit")

# Prompt user for operation choice
operation = input("Type the number of the operation: ")

# Perform the selected operation
if operation == "1":
    # List items by warehouse
    print("\nItems in warehouse 1:")
    for item in warehouse1:
        print(f"- {item}")
    
    print("\nItems in warehouse 2:")
    for item in warehouse2:
        print(f"- {item}")

elif operation == "2":
    # Search an item and place an order
    item_name = input("\nWhat is the name of the item? ")
    
    # Search for the item in the warehouses
    count_warehouse1 = warehouse1.count(item_name)
    count_warehouse2 = warehouse2.count(item_name)
    
    # Determine the location and availability of the item
    if count_warehouse1 == 0 and count_warehouse2 == 0:
        location = "Not in stock"
    elif count_warehouse1 > 0 and count_warehouse2 == 0:
        location = "Warehouse 1"
    elif count_warehouse1 == 0 and count_warehouse2 > 0:
        location = "Warehouse 2"
    else:
        location = "Both warehouses"
        
    print(f"\nAmount available: {count_warehouse1 + count_warehouse2}")
    print(f"Location: {location}")
    
    # Determine the warehouse with the highest amount
    if location == "Both warehouses":
        if count_warehouse1 >= count_warehouse2:
            max_location = "Warehouse 1"
            max_amount = count_warehouse1
        else:
            max_location = "Warehouse 2"
            max_amount = count_warehouse2
        print(f"Maximum availability: {max_amount} in {max_location}")
    
    # Ask user if they want to place an order
    order = input("\nWould you like to order this item? (y/n) ")
    if order.lower() == "y":
        desired_amount = int(input("How many would you like? "))
        
        # Check if desired amount is available
        total_available = count_warehouse1 + count_warehouse2
        if desired_amount <= total_available:
            print(f"\n{desired_amount} {item_name} have been ordered.")
        else:
            print("\n******************")
            print("There are not this many available. The maximum amount that can be ordered is", total_available)
            order_max = input("Would you like to order the maximum available? (y/n) ")
            if order_max.lower() == "y":
                print(f"{total_available} {item_name} have been ordered.")
    
elif operation == "3":
    # Quit the program
   print()
    
else:
    # Invalid operation
    print("\nError: Invalid operation entered.")

# Display final message
print(f"\nThank you for your visit, {user_name}!")