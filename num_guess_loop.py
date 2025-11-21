#!/usr/bin/env python3
# Created By: Abdul
# Date: 11/20/2025
# Program to ask the user for an integer and check if it matches a randomly generated number between 0 and 9


import random


def main():

    # generate random number between 0 and 9
    correct_guess = random.randint(0, 9)

    while True:

        # get user input and handle exceptions
        user_num = input("Please enter a random number 0-9: ")

        try:
            # convert user input to integer and check if it's within the valid range
            user_num = int(user_num)

            # check if the user input is a positive integer between 0 and 9
            if user_num < 0 or user_num > 9:
                print("Please enter a positive integer.")
            else:
                # check if the user guess is correct
                if user_num == correct_guess:
                    print("Congratulations! You guessed the correct number.")
                    break
                else:
                    print("Sorry, that's not the correct number. Try again!")

        except ValueError:
            print(user_num, "is not an integer.")

        # display ending message to user no matter the outcome
        finally:
            print("Thanks for playing!")


if __name__ == "__main__":
    main()
