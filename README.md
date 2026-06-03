# Rush Hour - OOP Terminal Game

This repository features a Python implementation of the classic logic puzzle game "Rush Hour". The project is built entirely from scratch using strictly Object-Oriented Programming (OOP) principles, demonstrating strong encapsulation, separation of concerns, and robust error handling.

## 🎯 Gameplay Overview

The objective of the game is to maneuver a specific car out of a congested 7x7 parking grid through a designated exit point. Vehicles can only move along their fixed axes (vertically or horizontally) and cannot bypass other vehicles. 

## 🏗️ Object-Oriented Architecture

The system is highly modular, split into distinct classes with clear responsibilities:

*   **`Car` Class:** Encapsulates the state of individual vehicles, including their name, length, coordinates, and orientation (Vertical or Horizontal). It calculates the necessary spatial requirements for any requested move (`u`, `d`, `l`, `r`).
*   **`Board` Class:** Manages the overall 7x7 grid state and tracks all active vehicles. It strictly enforces game physics by validating if a target cell is empty and within the board's bounds before allowing any movement.
*   **`Game` Class:** Acts as the main engine driving the game loop. It parses user input, validates correct formatting (`<name>,<direction>`), and continually checks the board for the target victory condition.

## 💻 Technical Highlights

*   **Encapsulation:** Extensive use of private variables and methods (e.g., `__try_move`, `__add_vertical_car`) to prevent external interference with the game state.
*   **Input Validation:** The game engine includes a robust `try-except` mechanism to catch and handle invalid user inputs gracefully without crashing the application.
*   **Dynamic Loading:** Game states and vehicle layouts are initialized dynamically by parsing a JSON configuration file.

## 🚀 How to Run

1. Ensure you have Python installed on your system.
2. Prepare a JSON configuration file containing the initial car layout.
3. Run the application from your terminal by passing the JSON file path as a command-line argument:
```bash
python rush-hour.py <path_to_json_file>
```

4. Follow the on-screen prompts to input your moves (format: Name,Direction) until you reach the exit!
