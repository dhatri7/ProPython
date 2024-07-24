from art import logo2
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Enter your text: ")
shift = int(input("Enter the shift amount: "))
dir = input("Type 'encode' if you wish to encrypt the text message or 'decode' if you want to decrypt a certain text: ").lower()

print(logo2)

def caesar(text, shift, dir):
    res = ""
    if dir == "decode":
        shift *= -1
    for i in text:
        l = alphabet.index(i)
        n = l + shift
        res += alphabet[n]

    print(f"Here's the {dir}d result: {res}")

caesar(text, shift, dir)
