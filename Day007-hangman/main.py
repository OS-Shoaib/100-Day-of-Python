# Day 007

import random
from hangman_words import word_list
from hangman_art import logo, stages


def hangman_process(word):
    end_of_game = False
    lives = 6

    # creat Blanks
    display = []
    for _ in word:
        display.append('_ ')
    # print Blanks
    print("".join(display))

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        print("you guessed: {}, ".format(guess))
        if guess in word:
            index_val = [_ for _, char in enumerate(word) if char == guess]
            for i in index_val:
                display[i] = guess
            out_word = "".join(display)
            print(out_word)
            # check for remaining letters
            x = out_word.find('_ ')
            if x != -1:
                continue
            else:
                print("Game Over")
                end_of_game = True

        else:
            print("out of luck")
            lives -= 1
            print(stages[lives])
            # check for remaining turns
            if lives == 0:
                print("Congrats")
                end_of_game = True
            else:
                continue


if __name__ == '__main__':
    chosen_word = random.choice(word_list)

    print(logo)

    # Testing code
    print(f'Pssst, the solution is {chosen_word}.')

    hangman_process(chosen_word)
