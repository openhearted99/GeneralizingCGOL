# Copyright 2018 Theodore Pena
# Licensed under the MIT License
from __future__ import division, print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib import animation
# This is a (hopefully) short program to make a and seed a 2D grid,
# in which a N-by-M game of life will be played.


# We start with our classes. This class is the Grid object, which handles the
# rules and board of the Game.
class Grid(object):
    def __init__(self, len_x, len_y):
        self.grid = np.zeros((len_x, len_y), dtype=int)

    def get_shape(self):
        if self.grid.ndim == 2:
            return np.shape(self.grid)
        elif self.grid.ndim == 0:
            print("Somehow, you've defined a zero dimensional array.")
            print("This is a problem.\n")
            return 0
        else:
            sys.exit("N-D variant to come.\n")

    def neighbors(self, x, y):
        top_left = self.grid[x - 1, y - 1]
        top = self.grid[x - 1, y]
        top_right = self.grid[x - 1, y + 1]
        right = self.grid[x, y + 1]
        bottom_right = self.grid[x + 1, y + 1]
        bottom = self.grid[x + 1, y]
        bottom_left = self.grid[x + 1, y - 1]
        left = self.grid[x, y - 1]
        return top_left + top + top_right + right + bottom_right + bottom \
            + bottom_left + left

    def evolve(self, iterations):
        for i in np.arange(iterations):
            _temp_grid = np.zeros((usr_inputs[0], usr_inputs[1]), dtype=int)
            # First, let's set the boundaries of the grid to zero. We'll start
            # by setting the upper-most and lower-most rows to be zero.
            self.grid[0, :] = 0
            self.grid[usr_inputs[0] - 1, :] = 0
            # Now we'll do the left-most and right-most columns.
            self.grid[:, 0] = 0
            self.grid[:, usr_inputs[1] - 1] = 0
            # And *here* is where we implement the rules of the Game.
            for i in np.arange(usr_inputs[0]):
                # The following four if statements make sure that the perimiter
                # wall doesn't interact with the game.
                if i == 0:
                    continue
                if i == (usr_inputs[0] - 1):
                    continue
                for t in np.arange(usr_inputs[1]):
                    if t == 0:
                        continue
                    if t == (usr_inputs[1] - 1):
                        continue
                    # Here are the rules of death and life.
                    if self.neighbors(i, t) < 2:
                        _temp_grid[i, t] = 0
                    elif self.neighbors(i, t) == 2 and \
                            self.grid[i, t] == 1:
                            _temp_grid[i, t] = 1
                    elif self.neighbors(i, t) == 2 and \
                            self.grid[i, t] == 0:
                        _temp_grid[i, t] = 0
                    elif self.neighbors(i, t) == 3:
                        _temp_grid[i, t] = 1
                    elif self.neighbors(i, t) > 3:
                        _temp_grid[i, t] = 0
        # Now we set the temp grid to be the actual grid.
        # We do this so the entire grid is updated at once.
        self.grid = _temp_grid

    def play_game_on_term(self, num_iterations):
        for num in np.arange(0, int(num_iterations)):
            self.show_on_term()
            self.evolve(1)

    def seed(self, *args):
        for xy_pair in args:
            self.grid[xy_pair[0], xy_pair[1]] = 1

    def show_on_term(self):
        print(self.grid)

    def animate_game(self, num_iterations):

        def update(i):
            self.evolve(1)
            life_grid = plt.matshow(self.grid, 0)
            return [life_grid]

        fig, ax = plt.subplots()
        fig.set_tight_layout(True)
        global life_grid
        life_grid = plt.matshow(self.grid, 0)
        anime = animation.FuncAnimation(fig, update,
                                        frames=num_iterations,
                                        interval=200, blit=True)
        mywriter = animation.FFMpegWriter(fps=7, extra_args=['-vcodec',
                                                             'libx264'])
        anime.save('simulation ' + time.asctime + '.mp4',
                   writer=mywriter)
        print()
        print("All done! Check your root directory, " +
              "or wherever this program is.")


# Now for our functions...

# This function handles the terminal-based UI.
def two_d_ui():
    usr_input_list = [-1, -1, -1, -1, -1]
    print(welcome)
    print(main_menu)
    input = raw_input("Please input an option:\n")
    try:
        usr_input = int(input)
    except ValueError:
        usr_input = -1

    while usr_input != 1 and usr_input != 2:
        input = raw_input("\nSorry, please input an integer representing "
                          "your choice.\n")
        try:
            usr_input = int(input)
        except ValueError:
            usr_input = -1

    if usr_input == 1:
        print(instructions_size)
        input = raw_input("Please input two ints:\n")
        try:
            usr_input_list[0], usr_input_list[1] = map(int, input.split())
        except ValueError:
            usr_input_list[0] = -1
            usr_input_list[1] = -1
        while usr_input_list[0] <= 0 or usr_input_list[1] <= 0:
            input = raw_input("\nPlease input two integers:\n")
            try:
                usr_input_list[0], usr_input_list[1] = map(int, input.split())
            except ValueError:
                usr_input_list[0] = -1
                usr_input_list[1] = -1

        mistake_check(usr_input_list)

        print(instructions_ticks)
        usr_input = raw_input("Please input an int:\n")
        try:
            usr_input_list[2] = int(usr_input)
        except ValueError:
            usr_input_list[2] = -1
        while not(isinstance((usr_input_list[2]), int)):
            usr_input = raw_input("\nPlease input an integer:\n")
            try:
                usr_input_list[2] = int(usr_input)
            except ValueError:
                usr_input_list[2] = -1

        print(menu_anime)
        usr_input = raw_input("Please enter an option:\n")
        try:
            usr_input_list[3] = int(usr_input)
        except ValueError:
            usr_input_list[3] = -1
        while int(usr_input_list[3]) != 1 and int(usr_input_list[3]) != 2:
            usr_input = raw_input("\nPlease input an option:\n")
            try:
                usr_input_list[3] = int(usr_input)
            except ValueError:
                usr_input_list[3] = -1

        print("Okay, here we go!\n")
        return usr_input_list

    elif int(usr_input) == 2:
        sys.exit("\nThanks for stopping by!")


# The function checks if the user made a mistake inputing their grid.
def mistake_check(usr_inputs):
    print("So, you want to run a {0}x{1} grid?\n".format(usr_inputs[0],
                                                         usr_inputs[1]))

    IsUserSure = raw_input("(Y/N)\n")
    # Now, we'll check if the user intended for the grid to be run with the
    # dimensions they specified.
    while True:
        if IsUserSure in ["Yes", "yes", "Y", "y", "wwssadadba", "Yep", "yep"]:
            break
        elif IsUserSure in ["No", "nope", "N", "n", "Nope", "nope"]:
            sys.exit("Oh, okay. Well, since you didn't want to run "
                     + "a {0}x{1} grid,\n".format(usr_inputs[0], usr_inputs[1])
                     + 'remember that you can set the dimensions of the grid '
                     + 'with command-line arguments.\nAs an example,'
                     + ' "python 2DScript.py  3 8" woudld create'
                     + ' a 3x8 grid.\n')
        IsUserSure = raw_input("(Y/N)\n")


welcome = ("=================2D GAME OF LIFE=================\n"
           "Welcome the 2D implenetation of the Game of Life!\n"
           "Menu is below.\n")

main_menu = ("1: Play the game.\n" "2: Exit the program.\n")

menu_anime = ("Now, pick how you want your Game visualized:\n"
              "1: Create a .mp4 movie in the local directory.\n"
              "2: Display the array here on the terminal.\n")

menu_seed = ("Finally, pick your seed.\n"
             "1. ")

instructions_size = ("Alright. Let's start by determining the size of your"
                     "\ngrid. You must enter two integers.\n"
                     "The first will be the height of your grid (number of "
                     "rows).\nThe second will be the width of "
                     "your grid (number of colunms).\n")


instructions_ticks = ("\nGreat. How many iterations (or ticks)\n"
                      "of the Game do you want to play?\n")


instructions_seed = ("\nCool. Next, pick your starting seed.\n")


seed_option1 = ("1. Single glider -- nothing special here.\n")
seed_option2 = ("\n2. Diehard, a seed which will dissapear after 130 ticks.")
seed_option3 = ("")

error_message_value = (
                 '\nError!! All command-line arguments must be integers!!\n'
                 'Remember, you set the dimensions of the grid with '
                 'command-line arguments.\nAs an example, '
                 '"python 2DScript.py 3 8" woudld create a 3x8 grid.')


error_message_index = (
                 '\nError!! There should be four command-line arguments!!\n'
                 'Remember, you set the dimensions of the grid with '
                 'command-line arguments.\nAs an example, '
                 '"python 2DScript.py 3 8" woudld create a 3x8 grid.')
#
"""EXPLAIN THAT usr_input = [grid_rows, grid_columns, ticks, anime, seed]"""
#


# And then we have the actual program:


if __name__ == "__main__":

    # First, we'll check if the user used the command line for input.
    if len(sys.argv) == 6:
        try:
            usr_inputs = np.array([-1, -1, -1, -1, -1])
            for i in np.arange(1, 5, 1):
                usr_inputs[i - 1] = int(sys.argv[i])
        except ValueError:
                sys.exit(error_message_value)
        except IndexError:
                sys.exit(error_message_index)
    else:
        usr_inputs = two_d_ui()

    # Now we can get into the simulaton itself.

    # First we establish the Grid.
    gol_grid = Grid(int(usr_inputs[0]), int(usr_inputs[1]))

    # Next, we seed the grid.
    try:
        gol_grid.seed([4, 4], [6, 3], [6, 4], [6, 5], [5, 5])
    except IndexError:
        sys.exit('Whoops! You just tried to plot something outside the'
                 + ' matrix. Try again!')

    # Now we evolve. (In CGoL terms, we tick.) At this point, the user must
    # choose between having the program print the results to the terminal
    # or having the results animated.
    if int(usr_inputs[3]) == 2:
        try:
            gol_grid.play_game_on_term(usr_inputs[2])
        except ValueError:
            sys.exit("Uh oh, something went wrong.")

    # Here we define a function for the animation capabilites.
    # This function is required for animate_game(). It tells matplotlib
    # what changes each frame of the animation.
    elif int(usr_inputs[3]) == 1:
        gol_grid.animate_game(usr_inputs[2])

    sys.exit("\n... And that's all for now folks!")
