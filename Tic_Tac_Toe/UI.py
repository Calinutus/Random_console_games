from Tic_Tac_Toe.Domain import Board

class ConsoleUI:
    def safe_int(self, command):
        while True:
            value = input(command)
            if not value.strip().isdigit():
                print("Try again")
                continue
            return int(value)

    def show_board(self, board):
        print("\n  0 1 2")
        for i, row in enumerate(board.grid):
            print(i, " ".join(row))
        print()

    def get_placement_input(self, board):
        print("Place piece")
        while True:
            r = self.safe_int("Row (0–2): ")
            c = self.safe_int("Column (0–2): ")

            if r not in range(3) or c not in range(3):
                print("Outside the board")
                continue

            if not board.is_empty(r, c):
                print("Square taken")
                continue

            return r, c

    def get_move_input(self, board, symbol):
        print("Choose a piece to move")
        while True:
            r1 = self.safe_int("Piece row: ")
            c1 = self.safe_int("Piece col: ")

            if (r1 not in range(3)) or (c1 not in range(3)):
                print("Not on board")
                continue

            if board.grid[r1][c1] != symbol:
                print("Not your piece")
                continue


            r2 = self.safe_int("Move to row: ")
            c2 = self.safe_int("Move to col: ")


            if (r2 not in range(3)) or (c2 not in range(3)):
                print("Outside board")
                continue

            if not board.is_empty(r2, c2):
                print("Occupied")
                continue

            if not Board.adjacent((r1, c1), (r2, c2)):
                print("Must move to adjacent square")
                continue

            return (r1, c1), (r2, c2)
