# Restaurant pseudo code
# # define variables  
#Item number name of item price
# 1 Burger $5.99
# 2 Pizza $8.49
# 3 Salad $4.99
# 4 Drink $1.99

# # display welcome
# PRINT statement - WELCOME TO RESTAURANT
print("Welcome to Python Burger!")
# Initiate WHILE loop 
#   WHILE order is still open display menu
order_total = 0
while True:
# # display menu items
#  Display menu items - (print statement) - for loop initiate menu_items
    menu = {
        "Burger" : 5.99,
        "Pizza" : 8.49,
        "Salad" : 4.99, 
        "Drink" : 1.99
    }
    # print("Item | Name | Price")
    # print("#1 | Burger | $5.99")
    # print("#2 | Pizza | $8.49")
    # print("#3 | Salad | $4.99")
    # print("#4 | Drink | $1.99")
# # prompt menu selection
# Prompt menu selection (user input)
    item_choice = (input("Choose item: "))

# # prompt qty
# Prompt qty 
    item_quantity = (int(input("Enter quantity: ")))

# STOP HERE
#print, input, int only things we should use right now