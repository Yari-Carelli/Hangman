"""
This is a simple command-line game.
It allows for user input and it also outputs a visual of the current hangman
alongside the word that is being guessed at every turn.
This python file contains all of the code to run the program. 
"""

"""
I have previously created a file containing a list of several hundreds
words, so I am just going to import that list into this file. 
"""
from words import WORD_LIST
"""
Then, I want to randomly choose a word from this list, so let's also
import the random library.
"""
import random
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


"""
This function is to clear the terminal: it uses
the 'cls' statement if on Windows, otherwise (Linux or Mac)
it uses the 'clear' statement.
"""
def clear():
    os.system('cls||clear')

"""
This function prints the Hangman logo for the game.
"""
def logo():    
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
    

"""
This function gives the player 3 different options to choose from: play, rules,
exit.
"""
def game_menu():    
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
                    print("\n")
                    print("Press 1 - 3 to choose from below options:\n".center(60))
                    print("1. Play".center(60))
                    print("2. How To Play".center(60))
                    print("3. Exit".center(60))
                    print("\n")
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
    
"""
I need to define a function which will return a word for our game. 
For this function, I can either create a list of words or I can import
a list of words for the program to choose from.
"""
def get_word():
    """
    this function returns a random string from the passed list of strings
    """
    word = random.choice(WORD_LIST)
    return word.upper()

"""
This function is defined for the actual interactive gameplay.
In this function, I have created several variables that I will be updating during
each turn the user takes. First, we want to display the word during each turn. 
"""
def play(word):
    """
    Let's represent unguessed letters as underscores and then show the letters as correct
    guesses are made. The following string will be the same length as the chosen word. It
    will initially contain only underscores.
    """
    word_completion = "_" * len(word)
    guessed = False  # this variable is initialized to 'false'
    guessed_letters = []  # this list willl hold the letters that the user has guessed
    guessed_words = []  # this list that will hold the words that the user has guessed
    """
    This last variable represents the number of tries; this corresponds to the number of
    body parts left to be drawn on the hangman before the user loses (counting the head, body,
    arms and both legs this will be 6).
    """
    tries = 6
    """
    After initializing the above variables, let's print some initial output to help guide the
    user when the game starts.
    """
    print(display_hangman(tries))  # this statement prints the initial state of hangman
    print(word_completion)  # this statement prints the initial state of the word with all underscores
    print("\n")  # new line

"""
The main chunk of our code will be encompassed in a while loop, a this will run until either the
word is guessed or the user runs out of tries.
"""
    # getting user input
    while not guessed and tries > 0:  # conditions for the while loop
        """
        Since each iteration of the loop corresponds to a turn by the user, I will first prompt
        the user for a guess and store the guess in a variable. I will also make sure to cast this
        to uppercase. I will be converting all user input to uppercase to make our comparison logic
        simpler, so the word is printed in all uppercase for the user to read.
        """
        guess = input("Please guess a letter or word: ").upper()
        """
        Inside the loop I will have three possible conditional branches, each based on different
        user input (guessing a letter, guessing a word, or typing something other than a single
        letter or word of the correct length) by creating an if/else block.
        Guessing a letter would mean that 'guess' has a length of 1 and contains only characters
        from the alphabet.
        Guessing a word would mean that the length of 'guess' equals the length of the actual word
        and contains only letters.
        """
        # checks whether the user guessed the word correctly or ran out of tries
        if len(guess) == 1 and guess.isalpha():
            """
            Let's start with guessing a letter: we are going to need another conditional block
            inside this if statement checking if the letter has already been guessed, is not in
            the word, or is in the word.
            """
            if guess in guessed_letters:
                clear()
                print("You have already guessed the letter", guess)
            elif guess not in word:
                clear()
                print(guess, "is not in the word.")
                """
                Here I will also decrement the number of tries by 1 since the user made an incorrect
                guess.
                """
                tries -= 1
                guessed_letters.append(guess)
                """
                The only remaining possibility is that the user made a correct letter guess, so I will
                make the following else block.
                """
            else:
                clear()
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                """
                Next, I have to update our variable 'word_completion' to reveal to the user all occurrences
                of guess. For this, I will first convert word_completion from a string to a list so I am able
                to index into it, and I will store this in a new variable called 'word_as_list'.
                """
                word_as_list = list(word_completion)
                """
                Now, I need to find all the indices where guess occurs in a word, so let's use a list
                comprehension. Here I am calling the enumerate method on word to get both the index i and letter
                at the index for each iteration.
                """
                indices = [
                    i for i, letter in enumerate(word) if letter == guess]
                """
                Now, let's use a simple for loop over indices to replace each underscore at index with guess.
                """
                for index in indices:
                    word_as_list[index] = guess
                """
                By calling the following statement I will update 'word_completion' with the new changes and
                convert it bact to a string.
                """
                word_completion = "".join(word_as_list)
                """
                It is also a possibility that guess now completes the word, so let's include an if statement
                to check this. 
                """
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            """
            Now, let's move on to the conditional for guessing a word. Similarly to guessing a letter, I need
            another conditional block inside of the if statement checking if the word has already been guessed,
            is correct, or is incorrect.
            """
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
"""
Then we will have an else statement that will catch everything else.
"""
        else:
            clear()
            print("Not a valid guess.")
    """
    After each guess is handled, I will print the current state of the hangman
    and the word. I will also print a newline to space out each term.
    """
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    """
    After the while loop, let's check whether the user guessed the word correctly or ran
    out of tries.
    """
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


"""
Finishing up, I first need a main function to put everything together.
"""
# code to run the game once
def main():
    logo()
    game_menu()
    get_player_name()
    word = get_word()
    play(word)

"""
Let's add some code to give the user the option to play again. I do this by creating a while
loop asking the user for input prompting
"""
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

"""
Lastly, I will just add the following code fragment so that our program will run by running our
script on the command line.
"""
if __name__ == "__main__":
    main()
