import random
from words import word_list
from hangman_visual import display_hangman
import time


def logo():
    """
    Hangman logo
    """
    print("""
                 _
                | |
                | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
                | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  \\
                | | | | (_| | | | | (_| | | | | | | (_| | | | |
                |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                    __/ |
                                   |___/
                   """)


# initial steps to invite in the game
print("\nWelcome to Hangman game by Yari Carelli\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(2)


def get_word():
    # this function returns a random string from the passed list of strings
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []  # list that'll hold the letters that the user guessed
    guessed_words = []  # list that'll hold the words that the user guessed
    tries = 6
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    # getting user input
    while not guessed and tries > 0:  # conditions for the while loop
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                # decrements the number of tries by 1 when guess is incorrect
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [
                    i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        # end of while loop

# checks whether the user guessed the word correctly or ran out of tries
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ".")
        print("Maybe next time!")


# code to run the game once
def main():
    word = get_word()
    play(word)
# loop to re-executes the game when the first round ends
    play_again = input("Do You want to play again? y = yes, n = no \n")
    while play_again not in ["y", "n"]:
        play_again = input("Do You want to play again? y = yes, n = no \n")
    if play_again == "y":
        main()
    elif play_again == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()


if __name__ == "__main__":
    main()
