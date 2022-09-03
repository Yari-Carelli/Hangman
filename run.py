import random
from words import word_list
from hangman_visual import display_hangman
import time
import os


# function to clear the terminal: it uses
# the 'cls' statement if on Windows, otherwise (Linux or Mac)
# it uses the 'clear' statement
def clear():
    os.system('cls||clear')

# hangman logo
def logo():
    print("Welcome to\n")
    print(
    """
                 _
                | |
                | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
                | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  \\
                | | | | (_| | | | | (_| | | | | | | (_| | | | |
                |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                    __/ |
                                   |___/
    by Yari Carelli
    """
    )


def game_menu():
    """
    Give player 3 different options to choose from: play, rules,
    exit
    """
    print("\n")
    print("Press 1 - 3 to choose from below options:")
    print("1. Play \n2. Hangman Rules \n3. Exit")

    while True:
        game_choice = input("What would you like to do? \n")
        print("\n")

        if game_choice == "1":
            clear()
            break
        elif game_choice == "2":
            print("""
            To play hangman is very simple. The aim of the hangman game 
            is for a player to guess all the letter in a randomly selected 
            hidden word in as few guesses as possible to stop the hangman 
            from being hanged. When a player starts a new game, the word is 
            displayed to the player as a series of underscores to represent 
            the hidden letters of the word. The player selects letters they 
            think are in the word. When they select a letter that is in the word, 
            all instances of that letter are displayed in place of the underscores.
            When the player selects a letter that is not in the word, it brings 
            the hangman closer to his end, as shown in the hangman image.
            If the player completes the word by selecting all its letters before 
            the hangman is hanged, then the player has succeeded.
            However if the hangman dies before the player completes the word, then 
            the player has failed. \n
            """) 
            game_menu()
        elif game_choice == "3":
            clear()
            print("Sorry to see you go. Come back soon!")
            exit()
        else:
            clear()
            print("Invalid input, please choose between 1 - 3")
            print("1. Play \n2. Hangman Rules \n3. Exit")

# initial steps to invite in the game
logo()
game_menu()

def get_player_name():
    """
    Get player to enter their chosen name.
    """
    while True:
        print("Great!\n")
        time.sleep(1)
        name = input("Enter your name: ")
        print(f"Hello {name}, the game is about to start!\n")
        time.sleep(2)
        print("Let's play Hangman! Best of Luck!")
        time.sleep(2)
        clear()
        break
    


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
                clear()
                print("You already guessed the letter", guess)
            elif guess not in word:
                clear()
                print(guess, "is not in the word.")
                # decrements the number of tries by 1 when guess is incorrect
                tries -= 1
                guessed_letters.append(guess)
            else:
                clear()
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
                clear()
                print("You already guessed the word", guess)
            elif guess != word:
                clear()
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        # end of while loop

# checks whether the user guessed the word correctly or ran out of tries
        else:
            clear()
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        clear()
        print("Congrats, you guessed the word! You win!")
    else:
        clear()
        print("Sorry, you ran out of tries. The word was " + word + ".")
        print("Maybe next time!")


# code to run the game once
def main():
    get_player_name()
    word = get_word()
    play(word)
# loop to re-executes the game when the first round ends
    play_again = input("Do You want to play again? y = yes, n = no \n")
    while play_again not in ["y", "n"]:
        play_again = input("Do You want to play again? y = yes, n = no \n")
    if play_again == "y":
        clear()
        word = get_word()
        play(word)
    elif play_again == "n":
        clear()
        print("Thanks For Playing! We expect you back again!")
        exit()


if __name__ == "__main__":
    main()
