# Begin restaraunt ordering system
order = {
    }

# Define variables  
menu = {
    1 : {"name":"Burger","price":5.99},
    2 : {"name":"Pizza","price":8.49},
    3 : {"name":"Salad","price":4.99},
    4 : {"name":"Drink","price":1.99},
}

# Print welcome statement
print("Welcome to Python Burger!")

# Initiate WHILE loop 
while True:

# Display menu items 
    print("Menu")
    for item_no, details in menu.items():
        print(f"{item_no}. {details['name']} - ${details['price']}")

# Prompt menu selection (user input)
    item_choice = int(input('Choose item number: '))

# Prompt qty 
    item_qty = int(input('Enter quantity: '))
    
# Add order
    if item_choice in menu:
        item_name = menu[item_choice]['name']
        
        if item_name in order:
          order[item_name] += item_qty  
        else:
            order[item_name] = item_qty
    
    else:
        print("That is not a valid menu item.")
            
    print(order)
    
# Continue order break loop or stay in
    continue_order = input("Would you like to continue ordering? y/n: ").lower()
    
    if continue_order != "y":
        break