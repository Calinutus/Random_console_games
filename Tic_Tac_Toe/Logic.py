import random
from Tic_Tac_Toe.Domain import Board

class GameEngine:
    def __init__(self, repo, human_symbol):
        self.repo = repo
        self.board = repo.get_board()
        self.human = human_symbol
        self.computer_player = "O" if human_symbol == "X" else "X"
        self.turn = "X"
        self.human_pieces = 0
        self.computer_pieces = 0


    def computer_place(self):
        """
        Places exactly one computer piece on the board during the placement phase

        :return:exactly one empty square becomes filled with the computer's symbol
        """
        for r, c in self.board.empty_squares():
            self.board.place(r, c, self.computer_player)
            if self.board.check_win(self.computer_player):
                return
            self.board.place(r, c, ".")

        for r, c in self.board.empty_squares():
            self.board.place(r, c, self.human)
            if self.board.check_win(self.human):
                self.board.place(r, c, self.computer_player)
                return
            self.board.place(r, c, ".")

        r, c = random.choice(self.board.empty_squares())
        self.board.place(r, c, self.computer_player)

    def computer_move(self):
        """
        Moves exactly one computer piece during the movement phase
        :return:one computer piece that  is moved to a legal adjacent empty square after checking for  each logic rule
        """
        pieces = self.board.get_positions(self.computer_player)
        random.shuffle(pieces)

        for r, c in pieces:
            moves = [(nr, nc) for nr in range(3) for nc in range(3) if self.board.is_empty(nr, nc) and Board.adjacent((r, c), (nr, nc))]

            if moves:
                nr, nc = random.choice(moves)
                self.board.move(r, c, nr, nc)
                return

    def switch_turn(self):
        self.turn = self.computer_player if self.turn == self.human else self.human
