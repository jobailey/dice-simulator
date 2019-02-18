import random
import time
#import built-in libraries

#continue game while user wants to keep playing
roll_again = "Y"
prize = "P"

while roll_again == "Y" or roll_again == "y" or roll_again == "yes" or roll_again == "Yes" or roll_again == "YES":
    print("Die rolling...")
    time.sleep(.5)

    #store die variables 
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1,6)

    print("You rolled ", dice1, " on dice 1 and ", dice2, " on dice 2.")

    #user wins prizes for doubles 
    if dice1 == dice2:
        print("You rolled a double! Collect your prize.")
        prize = input("Would you like to roll the dice again (R) or accept a prize (P)? ")

        if prize == "P" or prize == "p":
            print("Select a prize from this list: ")
            #where code would be expanded upon for future work 
        else:
            roll_again()
    else:
        print("Try again!")

    roll_again = input("\nWould you like to roll the dice again? (Y/N) ")

