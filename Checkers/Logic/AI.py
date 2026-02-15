import math
from Checkers.ConstantsForTable import red, white
from Checkers.Logic.RoundManagement import RoundManagement

class MinimaxAI:
    """
    AI player using the minimax algorithm for Checkers.
    """

    def __init__(self, color, depth=4):
        """
        Initializes the AI.

        :param color: Color of the AI pieces (red or white)
        :param depth: Depth of the minimax search
        """
        self.color = color
        self.depth = depth

    def evaluate(self, board):
        """
        Evaluates the board from the perspective of the AI.

        :param board: BoardLogic instance
        :return: Integer score (positive if favorable to AI, negative if favorable to opponent)
        """
        score = 0
        for p in board.pieces:
            val = 3 + (2 if p.king else 0)  # King pieces are more valuable
            score += val if p.color == self.color else -val
        return score

    def get_all_moves(self, board, color):
        """
        Returns all valid moves for a given color.

        :param board: BoardLogic instance
        :param color: Color of the pieces to generate moves for
        :return: List of moves in the form (start_row, start_col, dest_row, dest_col)
        """
        moves = []
        for p in board.pieces:
            if p.color == color:
                for (r, c), _ in board.get_valid_moves(p).items():
                    moves.append((p.row, p.column, r, c))
        return moves

    def simulate(self, board, sr, sc, dr, dc):
        """
        Simulates a move on the board.

        :param board: BoardLogic instance
        :param sr: Start row
        :param sc: Start column
        :param dr: Destination row
        :param dc: Destination column
        """
        tm = RoundManagement()
        piece = board.get_piece_at_pos(sr, sc)
        tm.turn = piece.color
        board.selected_piece = piece
        board.valid_moves = board.get_valid_moves(piece)
        board.handle_clicks(dr, dc, tm)

    def minimax(self, board, depth, maximizing):
        """
        Performs minimax search to determine the best move.

        :param board: BoardLogic instance
        :param depth: Remaining depth to search
        :param maximizing: Boolean, True if maximizing player (AI), False if minimizing
        :return: Tuple (score, best_move) where best_move = (sr, sc, dr, dc)
        """
        if depth == 0:
            return self.evaluate(board), None

        color = self.color if maximizing else (red if self.color == white else white)
        best = -math.inf if maximizing else math.inf
        best_move = None

        for sr, sc, dr, dc in self.get_all_moves(board, color):
            new_board = board.clone()
            self.simulate(new_board, sr, sc, dr, dc)
            score, _ = self.minimax(new_board, depth - 1, not maximizing)

            if maximizing and score > best:
                best = score
                best_move = (sr, sc, dr, dc)
            if not maximizing and score < best:
                best = score
                best_move = (sr, sc, dr, dc)

        return best, best_move

    def make_move(self, board, turn_manager):
        """
        Makes the AI move on the actual board using minimax.

        :param board: BoardLogic instance
        :param turn_manager: TurnManager instance
        """
        _, move = self.minimax(board, self.depth, True)
        if move:
            sr, sc, dr, dc = move
            piece = board.get_piece_at_pos(sr, sc)
            board.selected_piece = piece
            board.valid_moves = board.get_valid_moves(piece)
            board.handle_clicks(dr, dc, turn_manager)
