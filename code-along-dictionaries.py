# empty_dict = {}
# print(type(empty_dict))

# product_prices = {
#     'creamer' : 3.79,
#     'apples' : 3.99,
#     'pears' : 11.99,
#     'salmon' : 14.99
# }

# product_keys = product_prices.keys()
# print(product_keys)

# product_values = product_prices.values()
# print(product_values)

# product_items = product_prices.items()
# print(product_items)

# 1 Burger $5.99
# 2 Pizza $8.49
# 3 Salad $4.99
# 4 Drink $1.99

# menu = {
#     "Burger" : 5.99,
#     "Pizza" : 8.49,
#     "Salad" : 4.99, 
#     "Drink" : 1.99
# }

# item_number = 1
# for item, price in menu.items():
#     print(f'{item_number}, {item}, ${price}')
#     item_number += 1
order = {
    }

menu = {
    1 : {"name":"Burger","price":5.99},
    2 : {"name":"Pizza","price":8.49},
    3 : {"name":"Salad","price":4.99},
    4 : {"name":"Drink","price":1.99},
}

# order_total = 0

# Print welcome statement
print("Welcome to Python Burger!")

# Initiate WHILE loop 
while True:

#  Display menu items - (print statement) - for loop initiate menu_items
    print("Menu")
    for item_no, details in menu.items():
        print(f"{item_no}. {details['name']} - ${details['price']}")

# Prompt menu selection (user input)
    item_choice = (int(input('Choose item number: ')))

# Prompt qty 
    item_qty = (int(input('Enter quantity: ')))
#add order
    
    if item_choice in menu:
        item_name = menu[item_choice]['name']
        
        if item_name in order:
          order[item_name] += item_qty  
        else:
            order[item_name] = item_qty
    
    else:
        print("That is not a valid menu item.")
            
    print(order)

# Yes/No break loop or stay in
    continue_order = input("Would you like to continue ordering? y/n: ")
    continue_order[0].lower()
    
    if continue_order != "y":
        break
    
name_price = {d["name"]: d["price"] for d in menu.values()}

#Calculate total
print("Order Summary")
order_total = 0.0
#use a for loop to go over orders dictionary
    #multiply item_qty and item price 
    #item_qty from orders dictionary
    #set item_price variable -get from menu dictionary
    #item_total = item_price * item_qty
    #print item_name, item_qty, item_total
    #add item_total to order_total 
#print order_total 
for name, quantity in order.items():
    price = name_price[name]
    item_total = price * quantity
    order_total += item_total
    print(f"{name} * {quantity} = ${item_total:.2f}")
    
#Display final summary
print(f"Your total for today is: ${order_total:.2f}")