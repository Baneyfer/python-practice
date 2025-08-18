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

menu = {
    "Burger" : 5.99,
    "Pizza" : 8.49,
    "Salad" : 4.99, 
    "Drink" : 1.99
}

item_number = 1
for item, price in menu.items():
    print(f'{item_number}, {item}, ${price}')
    item_number += 1