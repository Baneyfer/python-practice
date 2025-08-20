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

# Functions 
def print_menu():
        print("Menu")
        for item_no, details in menu.items():
            print(f"{item_no}. {details['name']} - ${details['price']}")

def add_order():
        if item_choice in menu:
            item_name = menu[item_choice]['name']
        
        if item_name in order:
          order[item_name] += item_qty  
        else:
            order[item_name] = item_qty

def order_more():
    continue_order = input("Would you like to continue ordering? y/n: ").lower()
    if continue_order != "y":
        return False
    else: 
        return True

# Print welcome statement
print("Welcome to Python Burger!")

# Initiate WHILE loop 
while True:

# Display menu items 
    print_menu()

# Prompt menu selection (user input)
    item_choice = int(input('Choose item number: '))

# Prompt qty 
    item_qty = int(input('Enter quantity: '))
    
# Add order
    add_order()
    
# Add order more
    if order_more() == False:
        break
    
# Print order so far        
    print(order)
    
# Continue order break loop or stay in
    # continue_order = input("Would you like to continue ordering? y/n: ").lower()
    
    # if continue_order != "y":
    #     break
    
name_price = {d["name"]: d["price"] for d in menu.values()}

#Calculate total
print("Order Summary:")

#use a for loop to go over orders dictionary
    #multiply item_qty and item price 
    #item_qty from orders dictionary
    #set item_price variable -get from menu dictionary
    #item_total = item_price * item_qty
    #print item_name, item_qty, item_total
    #add item_total to order_total 
#print order_total 
order_total = 0.0
for name, quantity in order.items():
    price = name_price[name]
    item_total = price * quantity
    order_total += item_total
    print(f"{name} * {quantity} = ${item_total:.2f}")
    
#Display final summary
print(f"Your total for today is: ${order_total:.2f}")

# Generate receipt
    # open receipt.txt file in write mode
    # write pythonburger's receipt 
    # write each item_name and quantity and total
    # write "Your total for today" order total
    # close receipt.txt file
f = open('receipt.txt', 'a')
f.write(f'Your total for today is: ${order_total:.2f}' + '\n')
f.close