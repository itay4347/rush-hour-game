#################################################################
# FILE : rush-hour.py
# WRITER : Itay Tal , itay.tal2 , 207257023
# EXERCISE : intro2cs ex1 2025
# DESCRIPTION: A simple program that runs the game rush-hour.
#################################################################

from helper import *
from car import Car
from board import Board
from game import Game
import sys

def load_cars(file_path:str):
    """this function loads the cars that is in the json file.
    :param: file_path
    :return: the board with all the cars"""
    board = Board()
    cars = load_json(file_path)
    # iterates  on the car given and adding each one of them to the board.
    for key, value in cars.items():
        name = key
        length = value[0]
        location = (value[1][0], value[1][1])
        orientation = value[2]
        car = Car(name, length, location, orientation)
        # if one of the car coordinates is the exit point, it returns 'in_exit' and the game ends.
        if board.target_location() in car.car_coordinates():
            return 'in_exit'
        # adds the car.
        board.add_car(car)
    return board

def play_game(board):
    """this function plays the game."""
    #if the board == 'in_exit' it means a car is in the exit point. in that case, just end the game.
    if board == 'in_exit':
        print('You added a car in the exit point. the game is over!')
        return
    # if an actual board was given start the game using the game class.
    else:
        game = Game(board)
        game.play()

def main():
    """this function is in charge of running the main operation."""
    args = sys.argv
    file_path = args[1]
    play_game(load_cars(file_path))


if __name__ == '__main__':
    main()




