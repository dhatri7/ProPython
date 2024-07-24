from random import randint
from art import logo6
print(logo6)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
n = randint(1,100)

def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def game():
  guess = 0
  if level=="easy":
    turn = 10
  else:
    turn = 5
  while guess != n:
    print(f"You have {turn} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turn = check_answer(guess, n, turn)
    if turn == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != n:
      print("Guess again.")

game()
