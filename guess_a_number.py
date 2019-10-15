import random

highest_number = int(input("please choose a number to guess between 0 and "))

random_number_to_guess = random.randint(0, highest_number)
number_guessed = 0
count = 1

while number_guessed != random_number_to_guess:
    number_guessed = int(input("guess a number between your limits: "))
    if 0 < number_guessed <= highest_number:
        if number_guessed > random_number_to_guess:
            print("your guess is to high")
        elif number_guessed < random_number_to_guess:
            print("Your guess is to low")
        elif number_guessed == random_number_to_guess:
            print("congrates you got it on attempt number {0}".format(count))
        count += 1
    else:
        print("please guess a number between the limits")
