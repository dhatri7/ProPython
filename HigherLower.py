from game_data import data
from art import logo7, vs
from random import choice
score = 0
print(logo7)
over = False
def arrange(data):
    A = choice(data)
    B = choice(data)
    return A,B

def compare(A,B):
    if A['follower_count']>B['follower_count']:
        return "A"
    else:
        return "B"

while not over:
    A,B = arrange(data)
    ans = compare(A,B)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    c = input("Who has more followers? Type 'A' or 'B': ")
    if c==ans:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        over = True
