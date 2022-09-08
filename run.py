import random
from words import WORD_LIST
from hangman_visual import display_hangman
import time
import os


class style:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


# function to clear the terminal: it uses
# the 'cls' statement if on Windows, otherwise (Linux or Mac)
# it uses the 'clear' statement
def clear():
    os.system('cls||clear')


def logo():
    """
    Prints the Hangman logo for the game
    """
    
    print(
        style.BLUE + 
        """
    Welcome to\n
                                                            +---+
.-. .-.  .--.  .-. .-. .---. .-.   .-.  .--.  .-. .-.       |   |
| {_} | / {} \ |  `| |/   __}|  `.'  | / {} \ |  `| |       O   |
| { } |/  /\  \| |\  |\  {_ }| |\ /| |/  /\  \| |\  |      /|\  |
`-' `-'`-'  `-'`-' `-' `---' `-' ` `-'`-'  `-'`-' `-'      / \  |
                                                                |  
                                                         =========                                   
    by Yari Carelli
    """ + style.END)
    


def game_menu():
    """
    Give player 3 different options to choose from: play, rules,
    exit
    """
    print("\n")
    print("Press 1 - 3 to choose from below options:\n".center(60))
    print("1. Play".center(60))
    print("2. How To Play".center(60))
    print("3. Exit".center(60))
    print("\n")
    while True:
        game_choice = input("What would you like to do?\n".center(60))
        print("\n")
        if game_choice == "1":
            clear()
            break
        elif game_choice == "2":
            clear()
            print(
                style.YELLOW +
                """
              +--HOW TO PLAY-------------------------------------------------------------+
              |  To play hangman is very simple. The aim of the hangman game             |
              |  is for a player to guess all the letter in a randomly selected          | 
              |  hidden word in as few guesses as possible to stop the hangman           |
              |  from being hanged. When a player starts a new game, the word is         |
              |  displayed to the player as a series of underscores to represent         |
              |  the hidden letters of the word. The player selects letters they         |
              |  think are in the word. When they select a letter that is in the word,   |
              |  all instances of that letter are displayed in place of the underscores. |
              |  When the player selects a letter that is not in the word, it brings     |
              |  the hangman closer to his end, as shown in the hangman image.           |
              |  If the player completes the word by selecting all its letters before    |
              |  the hangman is hanged, then the player has succeeded.                   |
              |  However if the hangman dies before the player completes the word, then  |
              |  the player has failed.                                                  |
              +--------------------------------------------------------------------------+
              
              """ + style.END
              )
            while True:
                return_key = input("Press R to return to the main menu: \n").upper()
                if return_key == "R":
                    clear()
                    logo()
                    break
                else:
                    print(style.RED + "Invalid input" + style.END)
        elif game_choice == "3":
            clear()
            print("Sorry to see you go.".center(60))
            time.sleep(1)
            print("Come back soon!".center(60))
            exit()
        else:
            clear()
            print(style.RED + "Invalid input" + style.END)
            print("Please choose between 1 - 3.\n".center(60))
            print("1. Play".center(60))
            print("2. How To Play".center(60))
            print("3. Exit".center(60))
            print("\n")


def get_player_name():
    """
    Get player to enter their chosen name.
    """
    while True:
        print("Great!\n".center(60))
        time.sleep(1)
        print("Before we start, choose a name.".center(60))
        time.sleep(1)
        name = input("Enter your name:\n".center(60))
        print(f"Hello {name}, the game is about to start!\n".center(60))
        time.sleep(2)
        print("Let's play Hangman! Best of Luck!".center(60))
        time.sleep(2)
        clear()
        break
    

def get_word():
    # this function returns a random string from the passed list of strings
    word = random.choice(WORD_LIST)
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
                print("You have already guessed the letter", guess)
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
                print("You have already guessed the word", guess)
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
        print("Congrats, you guessed the word! You win!".center(60))
        time.sleep(1)
        game_win()
    else:
        clear()
        print("Sorry, you ran out of tries. The word was " + word + ".".center(60))
        print("Maybe next time!".center(60))
        game_over()
        time.sleep(1)


def game_win():
    """
    Prints the Well Done logo once all letters are guessed
    """
    print(style.GREEN +
          """
 __        __   _ _   ____                   _ 
 \ \      / /__| | | |  _ \  ___  _ __   ___| |
  \ \ /\ / / _ \ | | | | | |/ _ \| '_ \ / _ \ |
   \ V  V /  __/ | | | |_| | (_) | | | |  __/_|
    \_/\_/ \___|_|_| |____/ \___/|_| |_|\___(_)
                                                                                             
        """ + style.END)



def game_over():
    """
    Game over logo shown once user loses all their lives
    """
    print(style.RED +
          """
   ____                         ___                 _ 
  / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __| |
 | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |
 | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  |_|
  \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)
                                                      
        """ + style.END)

# code to run the game once
def main():
    logo()
    game_menu()
    get_player_name()
    word = get_word()
    play(word)

# loop to re-executes the game when the first round ends
    play_again = input("Do you want to play again? y = yes, n = no \n".center(60))
    while play_again not in ["y", "n"]:
        play_again = input("Do you want to play again? y = yes, n = no \n".center(60))
    if play_again == "y":
        clear()
        word = get_word()
        play(word)
    elif play_again == "n":
        clear()
        print("Thanks For Playing!".center(60))
        time.sleep(1)
        print("We expect you back again!".center(60))
        exit()


if __name__ == "__main__":
    main()
