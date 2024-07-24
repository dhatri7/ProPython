from art import logo3

def add(m,n):
    return m+n
def substract(m,n):
    return m-n
def multiply(m,n):
    return m*n
def divide (m,n):
    return m/n
ops = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
    }
print(logo3)
n1 = int(input("Enter your first number: "))
can = True
while can:
    op = input("Pick your operation from '+,-,*,/': ")
    n2 = int(input("Enter second number: "))
    func = ops[op]
    ans = func(n1,n2)
    print(f"{n1} {op} {n2} = {ans}")
    dir = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to exit: ")
    if dir == "y":
        n1 = ans
    else:
        can = False                
