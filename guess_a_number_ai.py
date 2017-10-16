import random

# config
default_low = 1
default_high = 100


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    print(" This game was created by Marc. ")
    print(" It was created on Oct. 1, 2017 ")

def get_guess(current_low, current_high):
    guess = (current_high + current_low)//2
    print("Is the number...")
    return guess

def decide_number(default_low,default_high):
    print()
    decide_1 = input("Hey " + str(name) + ", would you like to pick the numbers for your game? ")
    decide_1 = decide_1.lower()
    if decide_1 in ["yes", "y"]:
        print()
        
        low = input(name + ", what would you like your low value to be? ")
        low = int(low)
        print()
        
        high = input("What about your highest value? ")
        high = int(high)

    else:
        print("The default numbers will be used for this game")
        low = default_low
        high = default_high

    return low,high
    

def pick_number(current_low, current_high):
    print()
    print("Okay, " + name + " think of number from " + str(current_low) + " and " + str(current_high) + ".")
    print("Press 'Enter' when you've thought of a number")
    useless_1 = input ()

def check_guess(guess, tries, limit):
    print(guess)
    print(str(guess) + "?")
    test = input("Tell me if my number was too low, too high, or correct. " )
    test = test.lower()
    print()

    if test in ["low", "higher", "h", "H"]:
        check = 1
        return check
    if test in ["high", "lower", "l" ,"L"]:
        check = -1
        return check
    if test in ["correct", "right", "yes", "y", "Y", "c", "C"]:
        check = 0
        return check
    else:
        print("Enter a valid response, please.")
        print()
    
def show_result(guess):
    print()
    print("Did you actually think I was gonna lose?")
    print("I'll never lose to you!")
    

def play_again(name):
    while True:
        print()
        decision = input("Would you like to play again, " + name + "?(y/n) " )

        if decision == 'y' or decision == 'yes':
            print("Alright, Goodluck.")
            print()
            return True
        elif decision == 'n' or decision == 'no':
            print("Bye.")
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play(name):
    current_low, current_high = decide_number(default_low, default_high)
    check = -1
    
    pick_number(current_low, current_high)
    
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
    name = input("Welcome to my game. What is your name? " )
    play(name)
    playing = play_again(name)

show_credits()
