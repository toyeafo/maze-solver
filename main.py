from window import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(10, 10, 3, 3, 60, 60, win)

    # cell = Cell(win)
    # cell.draw(50, 50, 100, 100)

    # cell2 = Cell(win)
    # cell2.draw(100, 50, 150, 100)

    # cell.draw_move(cell2, undo=True)

    # cell3 = Cell(win)
    # cell3.has_top_wall = False
    # cell3.has_right_wall = False
    # cell3.draw(100, 100, 150, 150)

    # cell2.draw_move(cell3)

    # cell4 = Cell(win)
    # cell4.has_left_wall = False
    # cell4.draw(150, 100, 200, 150)

    # cell3.draw_move(cell4, True)

    win.wait_for_close()

if __name__ == "__main__":
    main()