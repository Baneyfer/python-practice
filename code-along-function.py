# #define functions with def, my_input will be the variable used inside the function
# def get_fizzbuzz(my_input):
#     my_fizzbuzz_result = ''
#     if my_input % 3 == 0 and my_input % 5 == 0: # No curly braces
#         my_fizzbuzz_result = 'Fizzbuzz'
#     elif my_input % 3 == 0 and not (my_input % 5 == 0):
#         my_fizzbuzz_result = 'Fizz'
#     elif not (my_input % 3 == 0) and my_input % 5 == 0:
#         my_fizzbuzz_result = 'Buzz'
#     else:
#         my_fizzbuzz_result = 'Try Again!'
#     print(my_fizzbuzz_result)

# #this is the function
# get_fizzbuzz(34)
# get_fizzbuzz(28)
# get_fizzbuzz(42)

# def calc_exp(num, power = 1):
#     return num ** power

# print(calc_exp(3)) 

# print(calc_exp(3,3))


nbr1 = 5 # <---- global scope version of variable

def print_nbr1():
    nbr1 = 10 #<---- locally scoped version of variable, only equals this inside the function
    print(nbr1)

print(nbr1 * nbr1)

print_nbr1()

