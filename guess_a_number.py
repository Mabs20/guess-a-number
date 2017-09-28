import random

# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    pass
    
def get_guess(current_low, current_high):
    print("I'm thinking of...")
    guess = (current_high + current_low)//2
    return guess

def pick_number():
    print("Think of number from " + str(low) + " and " + str(high) + ".")
    print("Press 'Enter' when you've thought of a number")
    useless_1 = input ()

def check_guess(guess):
    print(guess)
    test = input("Tell me if my number was too low, too high, or correct. " )
    if test in ["low", "lower"]:
        check = 1
    if test in ["high", "higher"]:
        check = -1
    if test in ["correct", "right", "yes"]:
        check = 0
    return check
    
def show_result(guess):
    print()
    print("I'll never lose to you")
    

def play_again():
    while True:
        print()
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            print("Alright, Goodluck.")
            print()
            return True
        elif decision == 'n' or decision == 'no':
            print("Okay. Bye.")
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            current_high = guess
        elif check == 1:
            current_low = guess


    show_result(guess)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
