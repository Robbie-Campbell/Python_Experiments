from question import Question


def go_home():
    returner = input("would you like to return to the directory (y/n)?: ")
    if returner == "y":
        choices()
    else:
        return


def guess():
    secret_word = "python"
    guess_count = 1
    guess_limit = 4
    guesses = input("Can you guess my secret word?: ")

    while guesses != secret_word and guess_count < guess_limit:
        guesses = input("Keep Guessing The Secret word!: ")
        guess_count += 1

    if guess_count < guess_limit:
        if guess_count == 1:
            value = " time"
        else:
            value = " times"
        print("You won the game!")
        print("you guessed " + str(guess_count) + value)
    else:
        print("You lost the game, you took too many guesses")
    go_home()


def translation():
    def translate(phrase):
        translated = ""
        for letter in phrase:
            if letter.lower() in "aeiou":
                if letter.isupper():
                    translated = translated + "G"
                else:
                    translated = translated + "g"
            else:
                translated = translated + letter
        return translated
    print("G language is able to convert any vowels in a word or phrase into the letter g (case sensitive)")
    print(translate(input("What word would you like to translate into G language?: ")))
    go_home()


def calc():
    def calculator():
        try:
            num1 = float(input("Enter a number: "))
            op = input("Enter an operation type: ")
            num2 = float(input("Enter a second number: "))
        except ValueError as err:
            print(err)
            return err
        if op == "+":
            print("The total amount is: ")
            print(num1 + num2)
        elif op == "-":
            print("The total amount is: ")
            print(num1 - num2)
        elif op == "*":
            print("The total amount is: ")
            print(num1 * num2)
        elif op == "/":
            print("The total amount is: ")
            print(num1 / num2)
        else:
            print("Please enter a number value")

    calculator()

    def redo():
        go_again = input("would you like to do another calculation?: ")
        if go_again == "yes" or go_again == "y":
            calculator()
            redo()
        else:
            return
    redo()
    go_home()


def test():
    question_prompts = [
        "What color are apples?\n(a) RED/GREEN\n(b) POLKA DOTS\n(c) PINK\n\n",
        "What color are grapes?\n(a) RED/GREEN\n(b) POLKA DOTS\n(c) PURPLE\n\n",
        "What color are trees\n(a) RED/GREEN\n(b) BROWN/GREEN\n(c) PINK\n\n"
    ]
    questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "c"),
        Question(question_prompts[2], "b")
    ]

    def run_test(queries):
        score = 0
        for query in queries:
            answer = input(query.prompt)
            if answer == query.answer:
                score += 1
            print("You got " + str(score) + "/" + str(len(queries)) + " correct")
    run_test(questions)
    go_home()


def choices():
    which_function = input("which function do you want to use - stop, test, calculator, guess or translator?: ")
    if which_function == "guess":
        guess()
    elif which_function == "calculator":
        calc()
    elif which_function == "translator":
        translation()
    elif which_function == "test":
        test()
    elif which_function == "stop":
        return
    else:
        print("Please enter one of the applicable options")
        choices()


