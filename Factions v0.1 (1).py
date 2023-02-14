"""
Copyright Jerry Cui 2019. All rights reserved. Factions and Factions Premium are all registered trademarks of Jerry
Studios Inc. Do not distribute!

Factions v0.1

---------------

*Note to modders: If you are making a mod, please go to line 229, where it says root.title("Factions v0.1") and change
it to root.title("Factions v0.1 (Modded))

The first version of Factions is now out! Factions v0.1 is now availible for download!
"""

# import modules needed
from tkinter import *
from random import randint, choice
from os import *
from time import sleep


# Game class
class ClassicGame(object):
    def __init__(self):
        global root
        # Keep track of the round
        self.round = 1
        # Possible operators for each question
        self.operators = ["+", "+", "+", "+", "-", "-", "-", "*", "*", "/"]
        # Choose a random operator
        self.operator = choice(self.operators)
        # Starting score for each team
        self.blue_team_points = 10000
        self.red_team_points = 10000
        # Team labels. Show the team_label will show the team with the background of that team's color.
        self.blue_team_label = Label(root, text="BLUE TEAM", bg="blue")
        # Make the font courier and the size 50
        self.blue_team_label.config(font=("courier", 50))
        # Put it on the grid at 0, 0 with 10 columnspan
        self.blue_team_label.grid(row=0, column=0, columnspan=10)
        # Same for red team
        self.red_team_label = Label(root, text="RED TEAM", bg="red")
        self.red_team_label.config(font=("courier", 50))
        # Same, but this time at column 23
        self.red_team_label.grid(row=0, column=23, columnspan=10)
        # Each team has points. Label, POINTS + the amount of points from that team.
        self.blue_team_points_label = Label(root, text="POINTS: " + str(self.blue_team_points))
        # Font as courier, but size 30
        self.blue_team_points_label.config(font=("courier", 30))
        # Grid it on 5, 0 with 10 columnspan
        self.blue_team_points_label.grid(row=5, column=0, columnspan=10)
        # Same for red
        self.red_team_points_label = Label(root, text="POINTS: " + str(self.red_team_points))
        self.red_team_points_label.config(font=("courier", 30))
        # This time at column 23
        self.red_team_points_label.grid(row=5, column=23, columnspan=10)
        # Create a question template for later
        self.question = "(first_numerator / first_denominator) " + self.operator + \
                        "(second_numerator / second_denominator) " \
            # Turn logic. If self.turn is True, then it is blue team's turn. otherwise it is red team's turn
        self.turn = True
        # The label to tell players what round it is
        self.round_label = Label(root, text="ROUND " + str(self.round))
        # Set it to font courier and size 20
        self.round_label.config(font=("courier", 20))
        # Put it on the grid at row 26, column 23 and columnspan 10
        self.round_label.grid(row=26, column=23, columnspan=10)
        # Create a label to show who's turn it is, starting with blue team
        self.turn_label = Label(root, text="BLUE TEAM TURN")
        # Also set it to courier 20
        self.turn_label.config(font=("courier", 20))
        # Put it on the grid at row 26. column 0 and columnspan 10
        self.turn_label.grid(row=26, column=0, columnspan=10)
        # Questions
        # Set a bunch of stuff for later to None for now
        self.first_numerator = None
        self.first_denominator = None
        self.second_numerator = None
        self.second_denominator = None
        # The random operator being chosen
        self.operator = choice(self.operators)
        # More stuff being set to None
        self.row_1_question = None
        self.row_2_question = None
        self.row_3_question = None
        self.question_entry_box = None
        self.question_check_button = None
        self.answer = None
        self.attempted_answer = None
        self.correct_or_incorrect_label = None
        self.is_game_still_playing = True
        self.winner = None
        self.the_answer_was_label = None
        # Start to generate a question
        self.generate_question()

    def generate_question(self):
        """Generate the questions for the game."""
        # The smallest possible number that can be generated
        number_minimum = 1
        # The largest possible number that can be generated, which is the round * 5, so the difficulty increases
        number_maximum = self.round * 5
        # Set numerators and denominators to a random number between those 2 numbers
        self.first_numerator = randint(number_minimum, number_maximum)
        self.first_denominator = randint(number_minimum, number_maximum)
        self.second_numerator = randint(number_minimum, number_maximum)
        self.second_denominator = randint(number_minimum, number_maximum)
        # Pick an operator
        self.operator = choice(self.operators)
        # Display the question and other stuff on the screen
        self.display_question()

    def display_question(self):
        """Display the question onto the screen."""
        # Destroy the labels that show the points and then replace them.
        self.red_team_points_label.destroy()
        self.blue_team_points_label.destroy()
        # Destroy the round label as well to display it.
        self.round_label.destroy()
        # The new round label.
        self.round_label = Label(root, text="ROUND: " + str(self.round))
        self.round_label.config(font=("courier", 20))
        self.round_label.grid(row=26, column=23, columnspan=10)
        # The new labels for points.
        self.red_team_points_label = Label(root, text="POINTS: " + str(self.red_team_points))
        self.red_team_points_label.config(font=("courier", 30))
        self.red_team_points_label.grid(row=5, column=23, columnspan=10)
        self.blue_team_points_label = Label(root, text="POINTS: " + str(self.blue_team_points))
        self.blue_team_points_label.config(font=("courier", 30))
        self.blue_team_points_label.grid(row=5, column=0, columnspan=10)
        # Create the labels for the question. I know the issue of it not being created properly during later rounds.
        self.row_1_question = Label(root, text=str(self.first_numerator) + "   " + str(self.second_numerator))
        self.row_2_question = Label(root, text="- " + self.operator + " - =")
        self.row_3_question = Label(root, text=str(self.first_denominator) + "   " + str(self.second_denominator))
        self.question = "(self.first_numerator / self.first_denominator) " + self.operator + \
                        "(self.second_numerator / self.second_denominator) "
        # Make each one courier size 12
        self.row_1_question.config(font=("courier", 12))
        self.row_2_question.config(font=("courier", 12))
        self.row_3_question.config(font=("courier", 12))
        # grid them
        self.row_1_question.grid(row=25, column=10, columnspan=5)
        self.row_2_question.grid(row=26, column=10, columnspan=5)
        self.row_3_question.grid(row=27, column=10, columnspan=5)
        # The entry box
        self.question_entry_box = Entry(root)
        self.question_entry_box.grid(row=26, pady=12, column=16, columnspan=3)
        # The button to press when you entered your question
        self.question_check_button = Button(root, text="ENTER", command=self.check_answer)
        self.question_check_button.grid(row=26, column=20)
        # Destroy the label that shows whose turn it is.
        self.turn_label.destroy()
        # Make the turn label the corresponding turn.
        if self.turn:
            self.turn_label = Label(root, text="BLUE TEAM TURN")
        else:
            self.turn_label = Label(root, text="RED TEAM TURN")
        # Font size 20, courier
        self.turn_label.config(font=("courier", 20))
        # Grid it
        self.turn_label.grid(row=26, column=0, columnspan=10)

    def check_answer(self):
        """Check to see if the answer is correct and a bunch of other stuff"""
        # The answer will be eval the question.
        self.answer = eval(self.question)
        # Round the answer to 2 decimal digits.
        self.answer = round(self.answer, 2)
        # The attempted answer will be what the user entered as a float
        self.attempted_answer = float(self.question_entry_box.get())
        # Round the attempted answer to 2 decimal digits.
        self.attempted_answer = round(self.attempted_answer, 2)
        # If your answer is correct
        if self.attempted_answer == self.answer:
            # The "award" is the round * 100
            award = self.round * 100
            # The label will be "CORRECT" and the have a green background.
            self.correct_or_incorrect_label = Label(root, text="CORRECT", bg="green")
            # Font courier and 20
            self.correct_or_incorrect_label.config(font=("courier", 20))
            # Grid it on row 0, column 11 with 10 columnspan
            self.correct_or_incorrect_label.grid(row=0, column=11, columnspan=10)
        else:
            # If the question is wrong, the award becomes negative.
            award = self.round * 100 - self.round * 100 * 2
            # Same thing as above, but it says "INCORRECT" and the background is red
            self.correct_or_incorrect_label = Label(root, text="INCORRECT", bg="red")
            self.correct_or_incorrect_label.config(font=("courier", 20))
            self.correct_or_incorrect_label.grid(row=0, column=11, columnspan=10)
        try:
            # Try to destroy the "the answer was" label, because it doesn't exist at the beginning
            self.the_answer_was_label.destroy()
        except AttributeError:
            pass
        # The "the answer was" label being created.
        self.the_answer_was_label = Label(root, text="The ANSWER WAS: " + str(self.answer))
        # Make it font courier and size 20.
        self.the_answer_was_label.config(font=("courier", 20))
        # Grid it at row 35, column 10, columnspan 10
        self.the_answer_was_label.grid(row=35, column=10, columnspan=10)
        # If this is blue team turn, Increase blue team's points by the award and then switch who's turn it is
        if self.turn:
            self.blue_team_points += award
            self.turn = False
        else:
            self.red_team_points += award
            self.turn = True
            # Increase the round.
            self.round += 1
        # Check to see if any team's points are below 0. If so, then they lose, and wait 5 seconds.
        if self.blue_team_points < 1:
            self.winner = "RED TEAM"
            sleep(5)
            sys.exit()
        elif self.red_team_points < 1:
            self.winner = "BLUE TEAM"
            sleep(5)
            sys.exit()
        # If no one has won, then continue the game by generating a question.
        else:
            self.generate_question()


# The class for a Custom Game (With different victory conditions and up to 4 players/teams
class CustomGame(object):
    def __init__(self):
        pass


# Create the window of the game
root = Tk()
root.title("Factions v0.1")

# Create the drop down menu
menu = Menu(root)
root.config(menu=menu)


# "File" sub-menu, which includes "New Game", "Restart Game", "Quit Game| "Open Saved Game", "Open Previous Game Score"


def start_new_game():
    """Start a game, and return a message if a game is already in progress"""
    ClassicGame()


def start_new_custom_game():
    """Start a custom game, and return a message if a game is already in progress"""
    pass


def restart_game():
    """Restart a game, and if a game is not currently in progress, return a message."""
    pass


def quit_game():
    """Quit a game, and if a game is not currently in progress, return a button."""
    pass


def open_saved_game():
    """Open a previously saved game. Ask for the name of a .txt file in the directory of this file. Return a message
    if the file is not a Factions Premium Saved Game file and start a game based on the save data if it is.

    """
    pass


def open_saved_game_score():
    """Open a previously saved game results. Ask for the name of a .txt file in the directory of this file. Return a
    message if the file is not a Factions Premium Saved Game Results file and display it based on the save data if it
    is.

    """
    pass


# The menu for "File"
file_menu = Menu(menu)
# Create a cascade for "File"
menu.add_cascade(label="File", menu=file_menu)
# Create the commands
file_menu.add_command(label="New Classic Game", command=start_new_game)
file_menu.add_command(label="New Custom Game (COMING SOON!)", command=start_new_custom_game)
file_menu.add_cascade(label="Restart Game (COMING SOON!)", command=restart_game)
file_menu.add_command(label="Quit Game (COMING SOON!)", command=quit_game)
# Add a separator
file_menu.add_separator()
# More commands
file_menu.add_command(label="Open Saved Game (COMING SOON!)", command=open_saved_game)
file_menu.add_command(label="Open Saved Game Score (COMING SOON!)", command=open_saved_game_score)


# "Settings" sub-menu, which includes "Soundtrack", "Volume" | "Background Image"


def soundtrack():
    """Settings for what song to play. Ask for input for which .wav file in the directory this file is in. If that
    is a valid file, play that song instead of the current one. If not, return a message.

    """
    pass


def volume():
    """Change the volume of the music."""
    pass


def change_background_image():
    """Change the background image of the main window."""
    pass


# Create a menu for settings
settings_menu = Menu(menu)
# Add a cascade
menu.add_cascade(label="Settings (COMING SOON!)", menu=settings_menu)
# More commands
settings_menu.add_command(label="Soundtrack (COMING SOON!)", command=soundtrack)
settings_menu.add_command(label="Volume (COMING SOON!)", command=volume)
# A separator
settings_menu.add_separator()
# One more command
settings_menu.add_command(label="Background Image (COMING SOON!)", command=change_background_image)

# Mainloop
mainloop()
