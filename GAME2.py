import random

def secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    secret_num = digits[:3]
    return secret_num


def is_three_digit_number(guess):
    return len(guess) == 3 and all(str(num).isdigit() for num in guess)


def guess():
    while True:
        guess_str = input('Enter your guess: ')
        if not is_three_digit_number(guess_str):
            print("Invalid guess. Please enter a three-digit number.")
        else:
            return list(map(int, guess_str))


def these_clues(guess, secret_num, clues=None):
    if clues is None:
        clues = []
    for i in range(3):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")
    if len(clues) == 0:
        clues.append("Bangles")

    return clues


def playing():

    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues: ")
    clue_names = ["Clue", "Meaning"]
    clue_meanings = ["Pico\t One digit is correct but in the wrong position.",
                     "Fermi\t One digit is correct and in the right position.",
                     "Bagels\t No digit is correct."]

    print("Clue\tMeaning")

    for clue in clue_meanings:
        print(clue)
    print("I have thought up a number. "
          "You have 5 guesses to get it.")

    secret_num = secret_number()

    for _ in range(5): #iterates 5 times
        guess = list(input("Enter your guess (a three-digit number): "))
        if not is_three_digit_number(guess):
            print("Invalid guess. Please enter a three-digit number.")
            continue

        guess = list(map(int, guess))
        clues = these_clues(guess, secret_num)

        print("Clues:", ", ".join(clues))

        if guess == secret_num and "Fermi, Fermi, Fermi" in ", ".join(clues):
            print("Congratulations! You guessed the secret number:", "".join(map(str, secret_num)))
            return
    print("Game over. You couldn't guess the secret number. It was:", "".join(map(str, secret_num)))
playing()