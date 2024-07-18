import random
from hangman_words import word_list
from hangman_art import logo, stages
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(logo)
end_of_game = False
lives = 6

display = []
for i in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    else:
        for i in range(word_length):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = guess
                print(f"You guessed correctly. {guess} is in the word.")
    
    if guess not in chosen_word:
        if lives>0:
            print("You did not guess correctly. You lose a life")
            lives -= 1
            print(stages[lives])
        else:
            end_of_game = True
            print("You lose.")
            print(f"The original word is {chosen_word}")
    
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("You win!")
        end_of_game = True
