import random

COLOURS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        colour = random.choice(COLOURS)
        code.append(colour)

    return code

def guess_code(attempts):
    while True:
        guess = input(f"Guess #{attempts}: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colours.")
            continue

        for colour in guess:
            if colour not in COLOURS:
                print(f"Invalid Colour: {colour}. Try again.")
                break
        else:
            break

    return guess


def check_code(guess, real_code):
    colour_counts_real = {}
    colour_counts_guess = {}
    correct_pos = 0
    incorrect_pos = 0

    for guess_colour, real_colour in zip(guess, real_code):
        if guess_colour == real_colour:
            correct_pos += 1
        else:
            if real_colour not in colour_counts_real:
                colour_counts_real[real_colour] = 0
            colour_counts_real[real_colour] += 1

            if guess_colour not in colour_counts_guess:
                colour_counts_guess[guess_colour] = 0
            colour_counts_guess[guess_colour] += 1

    for guess_colour, count in colour_counts_guess.items():
        if guess_colour in colour_counts_real:
            incorrect_pos += min(count, colour_counts_real[guess_colour])

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {TRIES} attempts to guess the code...")
    print(f"The valid colours are", *COLOURS)
    while True:
        difficulty = input("Would you like a challenge? (Y or N)").upper()
        if difficulty == "Y":
            break
        elif difficulty == "N":
            break
        elif difficulty == "D":
            break
        else:
            continue

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code(attempts)
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        if difficulty == "N":
            print(f"Correct Positions: {correct_pos} | Incorrect Position: {incorrect_pos}")
        elif difficulty == "Y":
            print(f"Correct Positions: {correct_pos}")
        else:
            print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos} | Actual Code: ", *code)

    else:
        print("You ran out of tries, the code was:", *code)

if __name__ == "__main__":
    game()


