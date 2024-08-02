from window import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)

    cell = Cell(10, 10, 30, 30, win)
    cell.draw()

    cell2 = Cell(30, 30, 50, 50, win)
    cell2.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()