# Exercise 20: Define a secret number. User guesses until correct. Show hints and attempts.

secret_number = 42
attempts = 0

while True:
    guess = int(input("Guess the secret number: "))
    attempts += 1
    
    if guess == secret_number:
        print("Congratulations! You guessed it right!")
        print("Total attempts:", attempts)
        break
    elif guess > secret_number:
        print("The secret number is smaller than your guess.")
    else:
        print("The secret number is larger than your guess.")