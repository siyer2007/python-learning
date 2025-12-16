import random
secret_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

guesses = 0

if guess == secret_number:
    guesses += 1
    print("You guessed it right!")
elif guess > secret_number:
    guesses += 1
    print("The secret number is lower")
elif guess < secret_number:
    guesses += 1
    print("The secret number is higher")

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == secret_number:
        guesses += 1
        print("You guessed it right!")
    elif guess > secret_number:
        guesses += 1
        print("The secret number is lower")
    elif guess < secret_number:
        guesses += 1
        print("The secret number is higher")
if guess == secret_number:
    print("You took", guesses, "guesses to guess the secret number")