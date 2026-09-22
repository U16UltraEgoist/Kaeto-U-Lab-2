import random

game_number = random.randint(1, 10)

while True:
    guess_count = 0

    while True:
        guess = int(input("Enter a number between 1 and 10: "))
        guess_count += 1

        if guess > game_number:
            print("Too high")
        elif guess < game_number:
            print("Too low")
        else:
            print(f"You got it in {guess_count} guesses!")

            if guess_count > 5:
                print("You took more than 5 guesses.")
            elif guess_count < 5:
                print("Nice! You got it in less than 5 guesses.")
                print("Reward: Free pizza and a gold star!")
            else:
                print("Exactly 5 guesses. Solid effort.")

            # Generate a new number different from the previous one
            old_number = game_number
            while game_number == old_number:
                game_number = random.randint(1, 10)

            print("A new number has been selected!")
            break