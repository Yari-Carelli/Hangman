# Hangman

Hangman is a word-guessing game, that runs in a terminal. The objective of the game is to find the word by guessing letters.

The live version of the website can be found by clicking [here](https://pyth-hangman.herokuapp.com/).

##  __How to play__

This game is modelled on the classic paper and pencil game of the same name. After inputting their name and choosing the difficulty, players will be presented with a series of underscores, and told how many letters are in the word. They then have 10 lives, and must successfuly find all of the letters in the word before they run out.

##  __Features__

The game features a welcome message before the name input:


![Welcome message and name input:](assets/readme/welcome_screen.png)

Upon entering a name, it presents the user wih a choice of difficulty:


![Choose difficulty input:](assets/readme/choose_difficulty.png)

Finally, the word is printed and its length is declared:


![Game start screenshot:](assets/readme/game_start.png)

### Features to implement

* There are several ways that the game could be improved, and more functionalities could be added. For example, by importing the Python time module, it would be possible to have a countdown timer to guess the correct word, or to calculate the overall time and compare it against other players. On that subject, at the moment, the game is a single-player experience, and no scores are recorded. It could be possible to store the scores in a document, that could then be accessed by different players.

* Another possibility would be to add a visual element to the game, using symbols to build a 'hangman'. Thus, rather than merely displaying the number of lives remaining, this could be accompanied by a drawing of hangman, which becomes more detailed with incorrect answers.

##  __Input validation__

### Username input

* The user must enter a valid username, which is composed uniquely of alphabetical characters:

![Screenshot of name input with valid name](assets/readme/input_validation/name_input.png)

* If this is the case, then a greeting is printed with the name:

![Screenshot of the valid name passing through with a greeting printed:](assets/readme/input_validation/name_input_succeeded.png)

* However, if the input is invalid, using a non-alphabetical character such as a number or a symbol, the following message is printed:

![Screenshot of message printed upon invalid name entry:](assets/readme/input_validation/invalid_name_message.png)


### Choose difficulty input

* When users have input their name successfully, they will then be faced with a choice of difficulties:

![Screenshot of difficulty choice:](assets/readme/input_validation/cd_open.png)

* If they do not input the correct character, either 1, 2, or 3, then the following happens:

![Screenshot of invalid input](assets/readme/input_validation/cd_invalid_input.png)

* If they enter the correct input, such as below...:

![Screenshot of correct input](assets/readme/input_validation/cd_correct_input.png)

* They will then pass to the game stage, with confirmation of their chouce printed at the top of the terminal.

![Screenshot of confirmation of correct choice](assets/readme/input_validation/cd_confirmation.png)


### Guess letter input

* If a user enters a letter, and that letter has not already been guessed, and the letter appears in the word, then they receive the following messages:

![Screenshot showing successful guess:](assets/readme/input_validation/letter_input_correct.png)

* If a user enters a letter that has already been guessed, they will see the following messages printed:

![Screenshot showing letter already guessed:](assets/readme/input_validation/letter_already_guessed.png)

* If a user enters a letter, and this does not appear in the word, then they will see the following messages:

![Screenshot showing an incorrect guess:](assets/readme/input_validation/incorrect_answer.png)

* If a user enters an invalid guess, i.e a number or a symbol, then they will receive the following message:

![Screenshot showing an invalid guess:](assets/readme/input_validation/invalid_guess.png)


### End game input

* Upon finishing a game, either winning or losing, the user will have the choice as to whether or not to play again:

![Screenshot of end game options:](assets/readme/input_validation/end_game_options.png)

* If the user inputs y, as in the screenshot below:

![Screenshot of input of y on end game function:](assets/readme/input_validation/end_game_y.png)

* They will be re-directed to the choose difficulty function, and can start a new game:

![Screenshot showing the result of an input of y:](assets/readme/input_validation/restart_game_choose_difficulty.png)

* If the user enters invalid input, they will see the following message:

![Screenshot showing invalid put for the end game function:](assets/readme/input_validation/end_game_invalid_command.png)

* If the user enters n, then the game ends and they will see this message:

![Screenshot showing message on exiting the game:](assets/readme/input_validation/end_game_n.png)


## __Flowchart__


* This flowchart was created with lucidchart.com, in order to demonstrate how the program would function.

![Picture of flowchart](assets/readme/flowchart/hangman_flowchart.png)


## __Technologies Used__
  * Python is the language that the game was coded in.
  * The application is deployed on Heroku.
  * The repository is hosted on GitHub.
  * Gitpod was the workspace used to code, and build the content of the website, which would then be committed to GitHub.
  * Git was used for version control.


## __Testing__

* The code has passed through the pep8 online check, without any issues:

![Screenshot of code successfuly passing through the pep8 validator](assets/readme/pep8_validation.png)

## __Bugs__

* During the course of the development of this application, I encountered several bugs. The most complex one for me to solve can be seen below:

* This code was causing an error message:

![Screenshot of code which was throwing the error](assets/readme/errors/string_object_error_code.png)

* This was the error message:

![Screenshot of error message](assets/readme/errors/string_object_error.png)

* This bug took me a long time to solve, which involved a lot of research. I understood that in Python, strings are immutable, but I thought that the code that I had used would convert the string into a list, allowing it to be modified, and then converted back into a string. After many hours of trial and error, and looking at examples of working code, I was able to find a working solution. 

### Unfixed bugs

* To the best of my knowledge, no bugs exist in the website in its current state.

## __Credits__

* When researching this project, I did a lot of research on the best way to structure the code, e.g, should everything be within one function or not, which features should come in which order. I found [this Youtube Video](https://www.youtube.com/watch?v=m4nEnsavl6w&ab_channel=Kite) which proved very helpful. A link to the github repository used for the code in the video can be found by clicking [here](https://github.com/kiteco/python-youtube-code/tree/master/build-hangman-in-python).
* I also used [this](https://inventwithpython.com/invent4thed/chapter8.html) website in order to gather ideas for the structure of the code.
* The most complicated part of the code for me to code was on lines 186-189 on run.py. By studying both [this](https://stackoverflow.com/questions/41747017/python-hangman-removing-blanks-from-the-answer-pool-and-refining-what-can-be-in) answer and [this](https://stackoverflow.com/questions/26937153/python-hangman-replacing-letters) one on stack overflow, I was able to understand exactly what problems I was having. 

##  __Deployment__

* This application has been deployed to Heroku. I will describe the process I used below:

* Log in to your Heroku account, and when you are on the dashboard, click on the new button in the top right-hand corner, and then click 'create new app'

![](assets/readme/deployment/1heroku_dashboard.png)

* You must now choose a name for your app, which must be unique, and the appropriate region.

![](assets/readme/deployment/2name_region.png)

* On the next page, you will see the Github logo. As my repository is stored there, I connected it to my github account.

![](assets/readme/deployment/3connect_github.png)

* You must then type in the name of your repository in order for it to be connected.

![](assets/readme/deployment/4connect_repository.png)

* Once that is done, click on the settings tab at the top.

![](assets/readme/deployment/5click_settings.png)

* Scroll down until you reach config vars, and click on the button, 'Reveal Config Vars'.

![](assets/readme/deployment/6reveal_config_vars.png)

* In the key section, type 'PORT' (it MUST be in capital letters) and in the value section, 8000.

![](assets/readme/deployment/7add_port.png)

* Next, select buildpacks, and add python, and nodejs.

![](assets/readme/deployment/8add_buildpack.png)

* When they have been successfully added, they should look as follows:

![](assets/readme/deployment/9added_buildpacks.png)

* Now, go back to the deploy tab, and scroll down until you see this button. Click 'Deploy Branch'.

![](assets/readme/deployment/10deploy_branch.png)

* You should see the terminal working while it deploys, as below:

![](assets/readme/deployment/11building_app.png)

* If everything has been successful, then you should see the following message printed:

![](assets/readme/deployment/12successfully_deployed.png)

* By clicking 'View', you will be able to see the app running in a new tab, as below:

![](assets/readme/deployment/13app_working.png)

### Local Deployment

If you would like to make a clone of this repository, you can type the following command in your IDE terminal:

- `git clone https://github.com/Robn88/hangman`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Robn88/hangman)

### Acknowledgements

* I would like to acknowledge the help provided to me by various people and websites, who have rendered the task of making this website easier, and in some cases, possible. In no particular order, I would like to thank:
   * w3schools.com, whose tutorials on Python were a frequent reference for all matter of questions both large and small;
   * stackoverflow.com, whose forums provided me with many helpful answers to problems I was experiencing when writing my code, and offered good examples for me to compare my code against;
   * The Slack community of Code Institute, a consistent source of warmth and encouragement, especially when I felt I was hitting my head against a wall;
   * The Code Institute tutor system, who were able to gently push me into the right direction when I felt like I had expended my last reserves of patience on some issues;
   * My mentor Tim, who was as wonderful as ever in setting me straight;
* And lastly, all of my friends and family who play-tested the application in its various iterations.