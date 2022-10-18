from words import WORD_LIST
import random
from hangman_visual import display_hangman
import time
import os

"""
This is a simple command-line game.
It allows for user input and it also outputs a visual of the current hangman
alongside the word that is being guessed at every turn.
This python file contains all of the code to run the program.

I have previously created a file containing a list of several hundreds
words, so I am just going to import that list into this file.

Then, I want to randomly choose a word from this list, so let's also
import the random library.

The 'clear()' function is to clear the terminal: it uses
the 'cls' statement if on Windows, otherwise (Linux or Mac)
it uses the 'clear' statement.

The 'logo()' function prints the Hangman logo for the game.

The 'game_menu()' function gives the player 3 different options to choose from: play, rules,
exit.

The 'get_player_name()' functions allows the player to enter their chosen name.

I need to define a function which will return a word for our game.
For the 'get_word()' function, I can either create a list of words or I can import
a list of words for the program to choose from.
This function returns a random string from the passed list of strings.

The 'play(word)' function is defined for the actual interactive gameplay.
In this function, I have created several variables that I will be updating
during each turn the user takes. First, we want to display the word during each
turn.

Let's represent unguessed letters as underscores and then show the letters
as correct guesses are made. The string of the 'word_completion' variable will
be the same length as the chosen word. It will initially contain only underscores.
The variable 'tries' variable represents the number of tries; this corresponds to the
number of body parts left to be drawn on the hangman before the user loses
(counting the head, body, arms and both legs this will be 6).
After initializing all the variables, let's print some initial output to
help guide the user when the game starts.

The main chunk of our code will be encompassed in a while loop, which will
run until either the word is guessed or the user runs out of tries.
Since each iteration of the loop corresponds to a turn by the user, I will
first prompt the user for a guess and store the guess in a variable, called 'guess'.
I will also make sure to cast this to uppercase.
I will beconverting all user input to uppercase to make our comparison logic
simpler, so the word is printed in all uppercase for the user to read.

Inside the loop I will have three possible conditional branches, each
based on different user input (guessing a letter, guessing a word, or
typing something other than a single letter or word of the correct length)
by creating an if/else block. Guessing a letter would mean that 'guess' has a
length of 1 and contains only characters from the alphabet.
Guessing a word would mean that the length of 'guess' equals the length
of the actual word and contains only letters.

Let's start with guessing a letter: we are going to need another
conditional block inside this if statement checking if the letter
has already been guessed, is not in the word, or is in the word.

Here I will also decrement the number of tries by 1 since the
user made an incorrect guess. The only remaining possibility is that the user
made a correct letter guess, so I will create an else block.
            
Next, I have to update our variable 'word_completion' to reveal to the user
all occurrences of guess. For this, I will first convert 'word_completion'
from a string to a list so I am able to index into it, and I will store this
in a new variable called 'word_as_list'.

Now, I need to find all the indices where 'guess' occurs in a
word, so let's use a list comprehension. Here I am calling the
enumerate method on 'word' to get both the index i and letter
at the index for each iteration.

Now, let's use a simple for loop over 'indices' to replace each
underscore at index with 'guess'.
        
It is also a possibility that 'guess' now completes the word, so
let's include an if statement to check this.

Now, let's move on to the conditional for guessing a word.
Similarly to guessing a letter, I need another conditional block inside
of the if statement checking if the word has already been guessed,
is correct, or is incorrect (lines 249 - 259).

Then we will have an else statement that will catch everything else (line 262).

After each guess is handled, I will print the current state of the
hangman and the word. I will also print a newline to space out each
term (lines 267 - 272).

After the while loop, let's check whether the user guessed the word correctly
or ran out of tries (lines 275 - 287).

The 'game_win()' function prints the Well Done logo once all letters are
guessed (lines 293 -301).
The 'game_over()' function prints the Game over logo once user loses
all their lives (lines 306 - 313).

Finishing up, I first need a 'main()' function to put everything together
(lines 324 -329).

Let's add some code to give the user the option to play again. I do this by
creating a while loop asking the user for input prompting (lines 332 - 345).

Lastly, I will just add a code fragment so that our program will
run by running our script on the command line (lines 351 -352).
"""


class style:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


def clear():
    os.system('cls||clear')


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
                style.YELLOW + """
                +--HOW TO PLAY----------------------------------------------------+
                | To play hangman is very simple. The aim of the hangman game is  |
                | for a player to guess all the letter in a randomly selected     |
                | hidden word in as few guesses as possible to stop the hangman   |
                | from being hanged. When a player starts a new game, the word is |
                | displayed to the player as a series of underscores to represent |
                | the hidden letters of the word. The player selects letters they |
                | think are in the word. When they select a letter that is in the |
                | word, all instances of that letter are displayed in place of    |
                | the underscores. When the player selects a letter that is not   |
                | in the word, it brings the hangman closer to his end, as shown  |
                | in the hangman image. If the player completes the word by       |
                | selecting all its letters before the hangman is hanged, then    |
                | the player has succeeded. However if the hangman dies before    |
                | the player completes the word, then the player has failed.      |
                +-----------------------------------------------------------------+
                """ + style.END
                )
            while True:
                return_key = input("Press R to return to the main menu:\n").upper()
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
    word = random.choice(WORD_LIST)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False  # this variable is initialized to 'false'
    guessed_letters = []  # list that will hold letters the user has guessed
    guessed_words = []  # list that will hold words the user has guessed
    tries = 6
    print(display_hangman(tries))  # prints the initial state of hangman
    print(word_completion)  # prints the initial state of the word with all (_)
    print("\n")  # new line

# getting user input
while not guessed and tries > 0:  # conditions for the while loop
    guess = input("Please guess a letter or word: ").upper()
# checks whether the user guessed the word correctly or ran out of tries
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            clear()
            print("You have already guessed the letter", guess)
        elif guess not in word:
            clear()
            print(guess, "is not in the word.")
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
    else:
        clear()
        print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
# end of while loop

if guessed:
    clear()
    print("Congrats, you guessed the word! You win!".center(60))
    time.sleep(1)
    game_win()
else:
    clear()
    print("Sorry, you ran out of tries.".center(60))
    time.sleep(1)
    print("The word was " + word + ".".center(60))
    time.sleep(1)
    print("Maybe next time!".center(60))
    game_over()


def game_win():
    print(style.GREEN +
          """
__        __   _ _   ____                   _
\ \      / /__| | | |  _ \  ___  _ __   ___| |
 \ \ /\ / / _ \ | | | | | |/ _ \| '_ \ / _ \ |
  \ V  V /  __/ | | | |_| | (_) | | | |  __/_|
   \_/\_/ \___|_|_| |____/ \___/|_| |_|\___(_)
        """ + style.END)


def game_over():
    print(style.RED + """
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

# loop to re-execute the game when the first round ends
play_again = input("Do you want to play again? y = yes, n = no \n".center(60))
while play_again not in ["y", "n"]:
    play_again = input("Play again? y = yes, n = no \n".center(60))
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
