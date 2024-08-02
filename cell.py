from window import Window, Point, Line

class Cell:
    def __init__(self, x1, y1, x2, y2, parent) -> None:
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = parent

    def draw(self):
        if self.left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, fill_color="black")
        if self.right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, fill_color="black")
        if self.top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, fill_color="black")
        if self.bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, fill_color="black")

    def draw_move(self, to_cell, undo=False):
        pass
        