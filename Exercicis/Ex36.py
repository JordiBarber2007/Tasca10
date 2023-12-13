import random

def generate_code():
    return random.sample(range(10), 4)

def check_code(guess, code):
    count = [0, 0]
    for g, c in zip(guess, code):
        if g == c:
            count[0] += 1
        elif g in code:
            count[1] += 1
    return count

def play_game():
    code = generate_code()
    attempts = 0

    while True:
        guess = list(map(int, input("Introdueix el teu codi (4 xifres): ").strip()))
        while len(guess) != 4 or any(x < 0 or x > 9 for x in guess):
            print("Error: El codi ha de tenir 4 xifres entre 0 i 9.")
            guess = list(map(int, input("Introdueix el teu codi (4 xifres): ").strip()))

        count = check_code(guess, code)
        attempts += 1

        if count[0] == 4:
            print("Felicitats! Ho has encertat. El nombre d'intents va ser:", attempts)
            break
        else:
            print("Estats:", count[0], "en la posició correcta,", count[1], "coincidències.")

play_game()