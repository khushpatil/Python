import random
import hangmanwords
import hangman_art
print(hangman_art.logo)
chosen_word = random.choice(hangmanwords.word_list)
print("Welcome to the hangman game!\nThe word has already been chosen for you\nHere are the blanks")
ans_list = []
lives = 6
for i in range(len(chosen_word)):
    ans_list.append(" ")
print(ans_list)
print("You know the rules, start guessing!")
end_game = False
while not end_game:
    guess = input("Enter your guess: ")
    for i in range(len(chosen_word)):
        if(guess == chosen_word[i]):
            if(guess in ans_list):
                print("You've already guessed this before, nigga")
            ans_list[i] = guess
    print(ans_list)
    if guess not in chosen_word:
        print(hangman_art.stages[lives])
        print(f"You've guessed {guess} which is wrong")
        lives -= 1
    if(" " not in ans_list or lives < 0):
        end_game = True
    if " " not in ans_list:
        print("You win")
    elif lives<0:print("You lose") and print(f"\nThe word was {chosen_word} ya noob")

