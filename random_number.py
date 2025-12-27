#python number guessing game
import random

lowest_num = 1
highest_num = 50
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print ("-----------PYTHON NUMBER GUESSING GAME-------------\n")
print(f"select an number between {lowest_num} and {highest_num}: ")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print ("That number is out of range")
            print(f"select an number between {lowest_num} and {highest_num}: ")
        elif guess < answer:
            print ("TOO Low Try Again!")
        elif guess > answer:
            print("TOO High Try Again!")
        else:
            print (f"CORRECT! The answer was {answer}")
            print (f"Number of guesses: {guesses}")
            is_running = False

    else:
        print ("invalid guess")
        print(f"please select a number between {lowest_num} and {highest_num}: ")
