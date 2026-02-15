from Tic_Tac_Toe.Domain import Board

class BoardRepository:
    def __init__(self):
        self.board = Board()

    def get_board(self):
        return self.board
