#################################################################
# FILE : car.py
# WRITER : Itay Tal , itay.tal2 , 207257023
# EXERCISE : intro2cs ex1 2025
# DESCRIPTION: A simple program that makes the car class.
#################################################################

from typing import Tuple, List, Dict

Coordinates = Tuple[int, int]
VERTICAL = 0
HORIZONTAL = 1

class Car:
    """
        this class is in charge of the car object. it gets the coordinated of the location
        of the car, as well as checks the coordination for every move i want to make.
        and finally it moves the car to the place we want on the board.
    """

    def __init__(self, name: str, length: int, location: Coordinates, 
                 orientation: int) -> None:
        """
        A constructor for a Car object.
        :param name: A string representing the car's name.
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head location (row,col).
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL).
        """
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation
        

    def car_coordinates(self) -> List[Coordinates]:
        """
        :return: A list of coordinates the car is in.
        """
        car_locations = []
        row, col = self.location
        
        if self.orientation == VERTICAL: # adds the locations vertically by running a loop on its length
            for i in range(self.length):
                car_locations.append((row + i, col))
        
        elif self.orientation == HORIZONTAL: # adds the locations horizontally by running a loop on its length
            for j in range(self.length):
                car_locations.append((row, col + j))

        return car_locations

    def possible_moves(self) -> Dict[str, str]:
        """
        :return: A dictionary of strings describing possible movements 
                 permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.

        if self.orientation == VERTICAL:
            return {
                'u': "cause the car to move up on the board",
                'd': "cause the car to move down on the board"
            }
        if self.orientation == HORIZONTAL:
            return {
                'r': "cause the car to move right on the board",
                'l': "cause the car to move left on the board"
            }
        

    def movement_requirements(self, move_key: str) -> List[Coordinates]:
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for 
                 this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        car_locations = self.car_coordinates()
        start_location_row, start_location_col = car_locations[0]
        edge_location_row, edge_location_col = car_locations[-1]

        if move_key == 'd':
            return [(edge_location_row + 1, edge_location_col)]
        if move_key == 'u':
            return [(start_location_row - 1, start_location_col)]
        if move_key == 'r':
            return [(edge_location_row, edge_location_col + 1)]
        if move_key == 'l':
            return [(start_location_row, start_location_col - 1)]

    def move(self, move_key: str) -> bool:
        """ 
        This function moves the car.
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if move_key in self.possible_moves(): # checks if the move is even possible and moves the car accordingly
            if move_key == 'u':
                self.__move_up()
            if move_key == 'd':
                self.__move_down()
            if move_key == 'r':
                self.__move_right()
            if move_key == 'l':
                self.__move_left()
            return True
        else:
            return False
    # function for moving the car up
    def __move_up(self):
        row, col = self.location
        self.location = (row - 1, col)

    # function for moving the car down
    def __move_down(self):
        row, col = self.location
        self.location = (row + 1, col)

    # function for moving the car right
    def __move_right(self):
        row, col = self.location
        self.location = (row, col + 1)

    # function for moving the car left
    def __move_left(self):
        row, col = self.location
        self.location = (row, col - 1)
    
    def get_name(self) -> str:
        """
        :return: The name of this car.
        """
        return self.name
