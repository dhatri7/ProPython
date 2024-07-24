import random
from art import rock, paper, scissors

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
b = int(input())

a = random.randint(0, 2)

c = [rock, paper, scissors]
print(c[b])
print("Computer chose:")
print(c[a])

if b >= 3 or b < 0: 
  print("You typed an invalid number, you lose!") 
elif b == 0 and a == 2:
  print("You win!")
elif a == 0 and b == 2:
  print("You lose")
elif a > b:
  print("You lose")
elif b > a:
  print("You win!")
elif a == b:
  print("It's a draw")

