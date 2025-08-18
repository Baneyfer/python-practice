our_number = 42
guess = None
quit = False

#main while loop
while quit == False:
    #while loop for guessing number 
    while guess != our_number:

        guess = int(input('Enter an integer: '))
        # the == allows you to compare the two elements
        guess == our_number

        if guess == our_number:
            print('Yay!')
        elif guess > our_number:
            print('Too high nerd!')
        elif guess < our_number:
            print('Too low dipshit!')
    #if statement this is outside of the above loop because the indentation, still inside main while loop   
    play_again = input("Do you want to play again? Y/N")

    if play_again == "Y" or play_again == "y":
        print("Let's play again!")
        guess = None
    elif play_again != "Y": # != means "does not equal"
        quit = True    
        print("Thank you for playing, see you next time!")
        # naming convention activity-pseudocode-baney