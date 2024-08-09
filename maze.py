from cell import Cell
from random import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            self.seed = random.seed(seed)

    def _create_cells(self):
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, I, J):
        if self._win is None:
            return

        current_x1 = self._x1 + I * self._cell_size_x
        current_y1 = self._y1 + J * self._cell_size_y
        current_x2 = current_x1 + self._cell_size_x
        current_y2 = current_y1 + self._cell_size_y

        self._cells[I][J].draw(current_x1, current_y1, current_x2, current_y2)
        self._animate()

    def _animate(self):
        self._win.root.after(200, self._win.redraw())

    def _break_entrance_and_exit(self):
        first_index_end = self._cells.index(self._cells[-1])
        second_index_end = self._cells[-1].index(self._cells[-1][-1])

        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].bottom_wall = False
        self._draw_cell(first_index_end, second_index_end)

    def _break_walls_r(self, I, J):
        self._cells[I][J].visited = True
        while self._cells[I][J] is not None:
            to_visit = []
            
            adjacent_1 = self._cells[I+1][J]
            adjacent_2 = self._cells[I][J+1]

            if adjacent_1.visited == False:
                to_visit.append(adjacent_1)
            if adjacent_2.visited == False:
                to_visit.append(adjacent_2)

            if len(to_visit) is None:
                self._draw_cell(I, J)
                return
            else:
                chosen_cell = to_visit[random(len(to_visit))]
                