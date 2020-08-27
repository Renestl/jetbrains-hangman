# Write your code here
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
replaced = list(len(word) * '-')
already_tried_letters = set()

tries = 8


def get_guess():
    print()
    print("".join(replaced))

    user_input = input("Input a letter: ")
    return user_input


def check_guess(letter):
    global tries

    if len(letter) != 1:
        print("You should input a single letter")
        return False
    elif not letter.islower():
        print("It is not an ASCII lowercase letter")
        return False
    elif letter in already_tried_letters:
        print("You already typed this letter")
        return False
    elif letter not in word:
        already_tried_letters.add(letter)
        print("No such letter in the word")
        tries -= 1
    return True


def game():
    while tries > 0:
        dash_count = replaced.count("-")

        if dash_count != 0:
            guess = get_guess()

            if check_guess(guess):
                if guess in word:
                    guess_idx = [index for index, value in enumerate(word) if value == guess]

                    for idx in guess_idx:
                        replaced[idx] = guess

                    already_tried_letters.add(guess)
                else:
                    if tries == 0:
                        print("You are hanged!")
                        break
        else:
            if tries > 0:
                print("You survived!")
                break


print("H A N G M A N")
play = input('Type "play" to play the game, "exit" to quit:')

if play == "play":
    game()
elif play == "exit":
    pass
else:
    play = input('Type "play" to play the game, "exit" to quit:')
