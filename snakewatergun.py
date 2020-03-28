# Welcame to Snake Water Gun Game Written in Python.
# By Govind Suroliya
import random  # inport random module for make random things.
SWG = ["g", "w", "s"]
no_chance = 0
chance = 10
user_point = 0
computer_point = 0
print("Welcame to Snake Water or Gun Game.\n")
# we guide the user.
print("####################################\n")
print("If You want to exit this game please press -> Q\n")
print("####################################\n")
print("\nS for Snake\nW for Water\nG for Gun")
while no_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(SWG)
    if _input == "q":
        break

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"Your guess {_input} and Computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(
            f"Computer point is {computer_point} and Your point is {user_point} \n ")

    elif _input == "s" and _random == "w":
        user_point = user_point + 1
        print(f"Your guess {_input} and Computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(
            f"Computer point is {computer_point} and Your point is {user_point} \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"Your guess {_input} and Computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(
            f"Computer point is {computer_point} and Your point is {user_point} \n ")

    elif _input == "w" and _random == "g":
        user_point = user_point + 1
        print(f"Your guess {_input} and Computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(
            f"Computer point is {computer_point} and Your point is {user_point} \n")

    # if user enter g

    elif _input == "g" and _random == "s":
        user_point = user_point + 1
        print(f"Your guess {_input} and Computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(
            f"Computer point is {computer_point} and Your point is {user_point} \n")

    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"Your guess {_input} and Computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(
            f"Computer point is {computer_point} and Your point is {user_point} \n ")

    else:
        print("you have input wrong \n")

    no_chance = no_chance + 1
    print(f"{chance - no_chance} is left out of {chance} \n")

if _input != "q":

    print("Game over")

    if computer_point == user_point:
        print("Tie")

    elif computer_point > user_point:
        print("Computer wins and You loose")

    else:
        print("You win and Computer loose")

    print(f"Your point is {user_point} and Computer point is {computer_point}")
