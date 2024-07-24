import os
from art import logo4

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo4)
print("Welcome to the secret auction program.")

auction = {}
end = False
sale_price = 0
winner = ""

while not end:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction[name] = bid
    dir = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if dir == "no":
        end = True
    else:
        clear_console()

for i in auction:
    if auction[i]>sale_price:
        sale_price = auction[i]
        winner = i

print(f"The winner is {winner} with a bid of ${sale_price}")
