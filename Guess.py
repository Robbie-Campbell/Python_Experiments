from random import randint
# guess my number


first_guess = input("Enter whatever number you think i have! (between 1 and 10): ")


def guess_properly():
    global first_guess
    sure = input("Please enter a y or an n!: ")
    while sure != "y" or "n":
        if sure == "y":
            computer(first_guess)
        elif sure == "n":
            first_guess = input("Try again: ")
            guess()
            computer(first_guess)

        else:
            guess_properly()


def guess():
    global first_guess
    sure = input("so you think that " + str(first_guess) + " is my number?! Are you sure?(y/n): ")
    if sure == "y":
        computer(first_guess)
    elif sure == "n":
        first_guess = input("Try again: ")
        guess()
    else:
        guess_properly()


def computer(x):
    actual_number = randint(1, 10)
    actual_number = actual_number
    random_range = randint(2, 4)
    try:
        if int(first_guess) == actual_number:
            again = input("Congratulations! You Got it right! Would you like to play again (y/n): ")
            if again == "y":
                first_guess
                guess()
            else:
                return
        elif first_guess != actual_number:
            second_guess = input("Close! Here's a little clue; The number is between " + str(actual_number+random_range)
                                 + " and " + str(actual_number-random_range) + ": ")
            if int(second_guess) == actual_number:
                again = input("Congratulations! You Got it right! Would you like to play again (y/n): ")
                if again == "y":
                    first_guess
                    guess()
                else:
                    return
            elif second_guess != actual_number:
                print("Bad luck! My actual number was " + str(actual_number))
                again = input("Have another go? (y/n): ")
                if again == "y":
                    first_guess
                    guess()
                else:
                    return
    except ValueError:
        print("you needed to input a number!")
        guess()


guess()
