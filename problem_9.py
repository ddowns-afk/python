import random
import sys

while True:
    random_number = random.randint(1, 9)
    user_input = input('Guess a number between 1 and 9! Enter "exit" to exit.')
    count = 1

    if user_input == str("exit"):
        break
    else:
        user_input_int = int(user_input)
        while user_input_int != random_number:
            if user_input_int > random_number:
                print("Your number is too high!")
                count += 1
                user_input_int = int(input("Guess again!"))
            elif user_input_int < random_number:
                print("Your number is too low!")
                count += 1
                user_input_int = int(input("Guess again!"))
        print("You guessed exactly right! The amount of tries it took you was " + str(count))