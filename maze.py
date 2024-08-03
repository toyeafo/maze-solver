from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, I, J):
        if self._win is None:
            return
        # current_x1 = self._x1
        # current_x2 = self._cell_size_x
        # current_y1 = self._y1
        # current_y2 = self._cell_size_y

        # if I != 0:
        #     current_y1 = current_y2
        #     current_y2 = current_y1 * I
            
        # if J != 0:
        #     current_x1 = current_x2
        #     current_x2 = current_x1 * J

        current_x1 = self._x1 + I * self._cell_size_x
        current_y1 = self._y1 + J * self._cell_size_y
        current_x2 = current_x1 + self._cell_size_x
        current_y2 = current_y1 + self._cell_size_y

        self._cells[I][J].draw(current_x1, current_y1, current_x2, current_y2)
        self._animate()

    def _animate(self):
        # self._win.redraw()
        self._win.root.after(1000, self._win.redraw())