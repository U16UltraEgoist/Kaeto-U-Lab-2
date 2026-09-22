import random

game_number = random.randint(1,10)
print(game_number)

guess = int(input ("Enter a number between 1 and 10: "))

if guess > game_number:
    print("Too high")
elif guess < game_number:
    print("Too low")
else:
    print ("NO DAGESTAN U SAFE")