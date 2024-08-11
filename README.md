# Maze Solver

## Overview

The **Maze Solver** is a Python application that generates and solves mazes using a recursive backtracking algorithm. The program visually displays the maze and its solution using a graphical user interface (GUI) built with the Tkinter library.

## Features

- **Maze Generation**: Dynamically creates a maze with a specified number of rows and columns.
- **Maze Solving**: Implements a backtracking algorithm to solve the maze, finding a path from the entrance to the exit.
- **Graphical Display**: Visualizes the maze and its solution in a GUI window.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone the repository or download the ZIP file and extract it.

    ```bash
    git clone https://github.com/yourusername/maze-solver.git
    ```

2. Navigate to the project directory.

    ```bash
    cd maze-solver
    ```

3. Ensure you have Python installed and ready to use.

## Usage

To run the Maze Solver, execute the `main.py` script:

```bash
python main.py
```

This will open a window displaying the generated maze. The program will then automatically solve the maze, and you can watch the process in real-time.

## Customization

- **Maze Size**: You can adjust the number of rows and columns in the maze by modifying the variables `num_rows` and `num_cols` in `main.py`.
- **Window Size**: The size of the display window can be customized by altering `screen_size_x` and `screen_size_y` in `main.py`.

## Project Structure

- **`main.py`**: The main script to run the maze solver.
- **`maze.py`**: Contains the `Maze` class that handles maze generation and solving.
- **`cell.py`**: Defines the `Cell` class representing each cell in the maze.
- **`window.py`**: Implements the Tkinter-based GUI for displaying the maze.
- **`tests.py`**: Contains test cases for the program (if any).
- **`__pycache__/`**: Directory containing compiled Python files to improve performance.
- **`.gitignore`**: Specifies files and directories that should be ignored by Git.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## Acknowledgements

This project was inspired by classic maze generation and solving algorithms.
