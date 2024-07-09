import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

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

