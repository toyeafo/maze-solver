from cell import Cell
from random import random, randrange

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None) -> None:
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            self.seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        

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

        while True:
            to_visit = []

            # left
            if I > 0 and not self._cells[I - 1][J].visited:
                to_visit.append((I - 1, J))
            # right
            if I < self._num_cols - 1 and not self._cells[I + 1][J].visited:
                to_visit.append((I + 1, J))
            # up
            if J > 0 and not self._cells[I][J - 1].visited:
                to_visit.append((I, J - 1))
            # down
            if J < self._num_rows - 1 and not self._cells[I][J + 1].visited:
                to_visit.append((I, J + 1))

            if len(to_visit) == 0:
                self._draw_cell(I, J)
                return
            
            chosen_neighbor = to_visit[randrange(len(to_visit))]

             # right
            if chosen_neighbor[0] == I + 1:
                self._cells[I][J].right_wall = False
                self._cells[I + 1][J].left_wall = False
            # left
            if chosen_neighbor[0] == I - 1:
                self._cells[I][J].left_wall = False
                self._cells[I - 1][J].right_wall = False
            # down
            if chosen_neighbor[1] == J + 1:
                self._cells[I][J].bottom_wall = False
                self._cells[I][J + 1].top_wall = False
            # up
            if chosen_neighbor[1] == J - 1:
                self._cells[I][J].top_wall = False
                self._cells[I][J - 1].bottom_wall = False
            
            self._break_walls_r(chosen_neighbor[0], chosen_neighbor[1])

    def _reset_cells_visited(self):
        for node in self._cells:
            for val in node:
                val.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, I, J):
        self._animate()
        directions = [(I - 1, J), (I + 1, J), (I, J - 1), (I, J + 1)]

        self._cells[I][J].visited = True
        if self._cells[I][J] == self._cells[-1][-1]:
            return True
        for val_I, val_J in directions:
             # right
            if val_I == I + 1:
                if self._cells[val_I][val_J] and not self._cells[val_I][val_J].visited and not self._cells[I][J].right_wall and not self._cells[val_I][val_J].left_wall:
                    self._cells[I][J].draw_move(self._cells[val_I][val_J])
                if self._solve_r(val_I, val_J):
                    return True
                else:
                    self._cells[I][J].draw_move(self._cells[val_I][val_J], undo=True)
            # left
            if val_I == I - 1:
                if self._cells[val_I][val_J] and not self._cells[val_I][val_J].visited and not self._cells[I][J].left_wall and not self._cells[val_I][val_J].right_wall:
                    self._cells[I][J].draw_move(self._cells[val_I][val_J])
                if self._solve_r(val_I, val_J):
                    return True
                else:
                    self._cells[I][J].draw_move(self._cells[val_I][val_J], undo=True)
            #val_I
            if val_J == J + 1:
                if self._cells[val_I][val_J] and not self._cells[val_I][val_J].visited and not self._cells[I][J].bottom_wall and not self._cells[val_I][val_J].top_wall:
                    self._cells[I][J].draw_move(self._cells[val_I][val_J])
                if self._solve_r(val_I, val_J):
                    return True
                else:
                    self._cells[I][J].draw_move(self._cells[val_I][val_J], undo=True)
            # up
            if val_J == J - 1:
                if self._cells[val_I][val_J] and not self._cells[val_I][val_J].visited and not self._cells[I][J].top_wall and not self._cells[val_I][val_J].bottom_wall:
                    self._cells[I][J].draw_move(self._cells[val_I][val_J])
                if self._solve_r(val_I, val_J):
                    return True
                else:
                    self._cells[I][J].draw_move(self._cells[val_I][val_J], undo=True)

        return False
                