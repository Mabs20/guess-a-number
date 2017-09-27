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
    guess = (current_high + current_low)//2
    return guess

def pick_number():
    print("Think of number from " + str(low) + " and " + str(high) + ".")
    useless_1 = input ()

def check_guess(guess):
    print(guess)
    test = input("Tell me if my number was too low, too high, or correct.")
    if "low" in test:
        check = 1
    if "high" in test:
        check = -1
    if "correct" in test:
        check = 0
    return check
    
def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
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
