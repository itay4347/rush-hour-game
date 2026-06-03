#################################################################
# FILE : game.py
# WRITER : Itay Tal , itay.tal2 , 207257023
# EXERCISE : intro2cs ex1 2025
# DESCRIPTION: A simple program that makes the game class.
#################################################################

from board import Board
from typing import Tuple, Optional, Union

from car import Car


class Game:
    """
    this class is in charge of running the game until the user wins or wish to end the game.
    """

    def __init__(self, board: Board) -> None:
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def __single_turn(self):
        """
        this function perform a single turn in the game.
        """
        print(self.board)
        user_input = self.__get_input()
        return user_input

    def __get_input(self) -> Union[Tuple[str, str],str]:
        """
        this function gets the input from the user and raises an exception if the input is not good
        :return: returns the input the user has entered.
        """
        try:
            user_input = input("Please enter the car and the move in the format: '<name>,<direction>': " )
            #if the user enters '!' the game should end.
            if not user_input == '!':
                # if the user entered more than 1 comma, its wrong format
                if user_input.count(',') != 1:
                    raise ValueError("Please enter the car and the move in the format: '<name>,<direction>'.")
                letters = user_input.split(',')
                # if the user entered more than 2 letters it raises value error
                if len(letters) != 2:
                    raise ValueError("Please enter the car and the move in the format: '<name>,<direction>'.")

                name:str = letters[0]
                direction:str = letters[1]
                # if the name is not a single letter and not in uppercase it raises a value error
                if len(name) != 1 or not name.isupper():
                    raise ValueError("The name of the car must be a single uppercase letter.")
                # if the direction is not a single letter and in uppercase it raises a value error
                if len(direction) != 1 or direction.isupper():
                    raise ValueError("The direction should be a singular lowercase letter.")
                # if the direction entered is a letter that is not of the directions possible raise a value error
                if direction not in ['d','l','r','u']:
                    raise ValueError("The direction should be either 'd','l','r','u'.")
                # if the car couldn't be moved for any reason, it raises a value error.
                # note: the care is moved if the value of board.move_car is true.
                if not self.board.move_car(name, direction):
                    raise ValueError("The car cannot be moved, or you entered the wrong direction, or there is no such car on the board.")

                return name, direction
            else:
                # this happens if the user entered '!'
                print("The game has stopped")
                return user_input
        except ValueError as err:
            print(err)
            #keeps calling this function until there is no error raised.
            return self.__get_input()



    def play(self) -> None:
        """
        The main driver of the Game. Manages the game until completion.
        the game is running while there is no car that reached the exit point and while the user didn't enter '!'
        :return: None
        """
        # implement your code and erase the "pass"

        is_running = True
        exit_point = self.board.target_location() # assigns the exit point of the board.
        while is_running: # runs a while loop until is_running is false
            user_input = self.__single_turn() # gets the user_input
            # end the game if the user entered '!'
            if user_input == '!':
                is_running = False
            # if the cell_content of the exit_point in not None which means there's a car inside the user has won and it stops
            #running the game.
            if self.board.cell_content(exit_point) is not None:
                print("You have won!")
                is_running = False

