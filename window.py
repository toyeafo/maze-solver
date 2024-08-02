from tkinter import Tk, BOTH, Canvas, Toplevel

class Window:
    def __init__(self, width, height) -> None:
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", width=width, height=height)
        self.canvas.pack()
        self.window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x_coordinate = x
        self.y_coordinate = y


class Line:
    def __init__(self, point_1, point_2) -> None:
        self.point_1 = point_1
        self.point_2 = point_2

    def  draw(self, canvas, fill_color):
        canvas.create_line(self.point_1.x_coordinate, self.point_1.y_coordinate, self.point_2.x_coordinate, self.point_2.y_coordinate, fill=fill_color, width=2)
