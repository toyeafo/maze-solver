from window import Window, Point, Line
from cell import Cell
from maze import Maze

def main():

    margin = 10
    screen_size_x = 800
    screen_size_y = 600
    num_cols = 4
    num_rows = 4

    cell_size_x = (screen_size_x - 2 * margin) / num_cols
    cell_size_y = (screen_size_y - 2 * margin) / num_rows

    win = Window(screen_size_x, screen_size_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()