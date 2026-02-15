class Board:
    def __init__(self):
        self.grid = [["." for _ in range(3)] for _ in range(3)]

    def is_empty(self, r, c):
        return self.grid[r][c] == "."

    def place(self, r, c, symbol):
        self.grid[r][c] = symbol



    def move(self, r1, c1, r2, c2):
        self.grid[r2][c2] = self.grid[r1][c1]
        self.grid[r1][c1] = "."


    def get_positions(self, symbol):
        return [(r, c) for r in range(3) for c in range(3) if self.grid[r][c] == symbol]

    def empty_squares(self):
        return [(r, c) for r in range(3) for c in range(3) if self.grid[r][c] == "."]


    def check_win(self, symbol):
        lines = [
            [(0,0),(0,1),(0,2)],
            [(1,0),(1,1),(1,2)],
            [(2,0),(2,1),(2,2)],
            [(0,0),(1,0),(2,0)],
            [(0,1),(1,1),(2,1)],
            [(0,2),(1,2),(2,2)],
            [(0,0),(1,1),(2,2)],
            [(0,2),(1,1),(2,0)]
        ]
        return any(all(self.grid[r][c] == symbol for r, c in line) for line in lines)

    @staticmethod
    def adjacent(a, b):
        return max(abs(a[0]-b[0]), abs(a[1]-b[1])) == 1
