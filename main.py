import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)

def guess_the_number(number_of_attempts):
  while number_of_attempts > 0:
    print(f"You have {number_of_attempts} remaining to guess the number. ")
    guess = int(input("Make a guess: "))
    if guess < number:
      print("Too low.\nGuess again.")
      number_of_attempts -= 1
    elif guess > number:
      print("Too high.\nGuess again.")
      number_of_attempts -= 1
    elif guess == number:
      print(f"You got it. The answer was {number}.")
      number_of_attempts = 0

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  guess_the_number(10)  
else:
  guess_the_number(5)


