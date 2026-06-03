#################################################################
# FILE : board.py
# WRITER : Itay Tal , itay.tal2 , 207257023
# EXERCISE : intro2cs ex1 2025
# DESCRIPTION: A simple program that makes the board class.
#################################################################

from typing import Tuple, List, Optional
from car import Car

Coordinates = Tuple[int, int]
VERTICAL = 0
HORIZONTAL = 1
class Board:
    """
    this class handles the board state.
    it initiates the board with an empty one, adds cars and move cars as wished.
    """

    def __init__(self) -> None:
        """
        A constructor for a Board object.
        """
        self.__board: List[List[str]] = self.__init_board()
        self.__cars: List[Car] = []


    def __init_board(self):
        """this function is for initializing the board.
            it adds '_' in all the places except the exit point."""
        rows = 7
        cols = 7
        init_board = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append('_')
            if i == rows // 2:
                row.append(None)
            init_board.append(row)

        return init_board

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string representing the current status of the board.
        """
        rows = len(self.__board)
        cols = len(self.__board[0]) + 1
        board_str:str = ""
        for i in range(rows):
            for j in range(cols):
                # prints '*' on the right edge except the middle row where it prints 'E' for the exit point
                if j == cols - 1:
                    if i == rows // 2:
                        board_str += 'E'
                    else:
                        board_str += '*'
                else:
                    board_str += self.__board[i][j] + ' ' # prints the element in the board list.
            board_str += '\n'
        return board_str
              
        
        

    def cell_list(self) -> List[Coordinates]:
        """
        This function returns the coordinates of cells in this board.
        :return: list of coordinates.
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        rows, cols = len(self.__board), len(self.__board[0])
        cells_board:List[Coordinates] = []

        for i in range(rows):
            for j in range(cols):
                cells_board.append((i,j))
            # adds the target cell (3,7) to the list
            if i == rows // 2:
                cells_board.append((i, cols))

        return cells_board

    def possible_moves(self) -> List[Tuple[str, str, str]]:
        """ 
        This function returns the legal moves of all cars in this board.
        :return: list of tuples of the form (name, move_key, description)
                 representing legal moves. The description should briefly
                 explain what is the movement represented by move_key.
        """
        cars_moves: List[Tuple[str, str, str]] = []
        # runs a loop on the cars already in the board and checks depends on the orientation if a certain move is possible
        # and adds it to the list of tuples.
        for car in self.__cars:
            if car.orientation == VERTICAL:
                if self.__try_move('d', car):
                    cars_moves.append((car.name, 'd', 'the car can move down'))
                if self.__try_move('u', car):
                    cars_moves.append((car.name, 'u', 'the car can move up'))
            if car.orientation == 1:
                if self.__try_move('r', car):
                    cars_moves.append((car.name, 'r', 'the car can move right'))
                if self.__try_move('l', car):
                    cars_moves.append((car.name, 'l', 'the car can move left'))
        return cars_moves

    def __try_move(self, move_key: str, car: Car) -> bool:
        """this function checks if the move wanted to perform on a car is possible by checking the movement requirements
            from the car class and checking if they are inside the bounds of the board and if the cell it wish to move is not
            empty.
            :param move_key: The key of the move to check.
            :param car: The car to check.
            :return: True if the move is possible, False otherwise."""
        movement_requirement = car.movement_requirements(move_key)
        row, col = movement_requirement[0]
        # True if its inbounds and empty, False otherwise
        return self.__is_in_bounds((row, col)) and self.__is_cell_empty((row, col))

    def __is_cell_empty(self, coordinates: Coordinates) -> bool:
        """checks if a cell is empty
        :param coordinates: The coordinates of the cell to check.
        :return: True if the cell is empty, False otherwise."""
        row,col = coordinates
        return self.__board[row][col] == "_" or self.__board[row][col] is None

    def __is_in_bounds(self, coordinates: Coordinates) -> bool:
        """checks if a cell is inside the bounds of the board.
        :param coordinates: The coordinates of the cell to check.
        :return: True if the cell is inside the bounds of the board, False otherwise."""
        row, col = coordinates
        if self.__board[row][col] is None:
            return True
    
        return 0 <= row < len(self.__board) and 0 <= col < len(self.__board[0])


    def target_location(self) -> Coordinates:
        """
        This function returns the coordinates of the location that should be 
        filled for victory.
        :return: (row, col) of the goal location.
        """
        # In this board, returns (3,7)
        rows = len(self.__board)
        cols = len(self.__board[0])
        return rows // 2, cols

    def cell_content(self, coordinates: Coordinates) -> Optional[str]:
        """
        Checks if the given coordinates are empty.
        :param coordinates: tuple of (row, col) of the coordinates to check.
        :return: The name of the car in "coordinates", None if it's empty.
        """
        if self.__is_cell_empty(coordinates):
            return None
        else:
            return self.__board[coordinates[0]][coordinates[1]]

    def add_car(self, car: Car) -> bool:
        """
        Adds a car to the game.
        :param car: car object to add.
        :return: True upon success, False if failed.
        """
        # return false if the name in already taken or if the name is not uppercased

        if self.__is_name_taken(car.name) or not car.name.isupper():
            return False
        # returns false if the length of the car is within the bounds of the board.
        if not self.__check_length(car):
            return False
        # adds the car vertically
        if car.orientation == VERTICAL:

            return self.__add_vertical_car(car)
        # adds the car horizontally
        elif car.orientation == HORIZONTAL:
            return self.__add_horizontal_car(car)

    def __check_length(self, car: Car) -> bool:
        """this function checks if the given car length is within bounds of the board.
        :param car: car object to check.
        :return: True if the car length is within bounds of the board, False otherwise."""
        rows, cols = len(self.__board), len(self.__board[0])
        row, col = car.location
        if car.orientation == VERTICAL:
            return 0 <= row + car.length <= rows # checks if its location row + length is within bounds
        if car.orientation == HORIZONTAL:
            if row == len(self.__board) // 2:
                return 0 <= col + car.length <= cols + 1
            return 0 <= col + car.length <= cols # checks if its location col + length is within bounds

    def __add_vertical_car(self, car:Car) -> bool:
        """this function adds a car vertically to the board.
        :param car: car object to add.
        :return: True after the car was added. False otherwise."""
        row, col = car.location
        # runs a loop on the car length. if each cell is not empty and within bounds it adds the car.
        for i in range(car.length):
            if not self.__is_cell_empty((row + i, col)) or not self.__is_in_bounds((row + i, col)):
                return False
        self.__add_vertical_car_to_board(car)
        self.__cars.append(car)
        return True

    def __add_horizontal_car(self, car:Car) -> bool:
        """this function adds a car horizontally to the board.
        :param car: car object to add.
        :return: True after the car was added. False otherwise."""
        row,col = car.location
        # runs a loop on the car length. if each cell is not empty and within bounds it adds the car.
        for i in range(car.length):
            if not self.__is_cell_empty((row, col + i)) or not self.__is_in_bounds((row, col + i)):
                return False
        self.__add_horizontal_car_to_board(car)
        self.__cars.append(car)
        return True

    def __add_vertical_car_to_board(self, car:Car):
        """
        this function adds the vertical car to the board.
        :param car: car object to add.
        """
        row, col = car.location
        for i in range(car.length):
            self.__board[row + i][col] = car.name
    
    def __add_horizontal_car_to_board(self, car:Car):
        """
        this function adds the horizontal car to the board.
        :param car: car object to add.
        """
        row, col = car.location
        for i in range(car.length):
            self.__board[row][col + i] = car.name
    
    def __is_name_taken(self, name) -> bool:
        """this function checks if the given name is taken.
        :param name: name of the car to check.
        :return: True if is taken, False otherwise
        """
        for car in self.__cars:
            if car.name == name:
                return True
        return False

    def move_car(self, name: str, move_key: str) -> bool:
        """
        Moves car one step in a given direction.
        :param name: name of the car to move.
        :param move_key: the key of the required move.
        :return: True upon success, False otherwise.
        """
        # runs the loop until reached the desired car.
        for i in range(len(self.__cars)):
            if self.__cars[i].name == name:
                current_car = self.__cars[i]
                # if the coordinates it wants to move to are legal proceed
                if self.__try_move(move_key, current_car):
                    is_moved = current_car.move(move_key) # moves the car
                    # this block of code updates the car location on the board and on the cars list.
                    if is_moved:
                        self.__cars.remove(current_car)
                        self.__remove_car_from_board(name)
                        self.add_car(current_car)
                        return True
                    # if the coordinates it wants to move to are illegal return False.
                    else:
                        return False
        #if the loop is not stopped, it means there's no such car and return False
        return False

    def __remove_car_from_board(self, name):
        """this function removes a car from the board.
        :param name: name of the car to remove."""
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                if self.__board[i][j] == name:
                    self.__board[i][j] = '_'
