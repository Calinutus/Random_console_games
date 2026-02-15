from Checkers.ConstantsForTable import white, red
from Checkers.Logic.Pieces import Piece

class BoardLogic:
    def __init__(self):
        self.pieces = []
        self.setup_pieces()
        self.selected_piece = None
        self.valid_moves = {}
        self.capture_pieces = []



    def check_win_condition(self, turn_manager):
        """
        After each turn checks whether the player has won or not.
        :param turn_manager:checks who won the match/it is used to end the game
        :return: The state of the match and which of the players won
        """
        red_pieces = [p for p in self.pieces if p.color == red]
        white_pieces = [p for p in self.pieces if p.color == white]

        if not red_pieces:
            turn_manager.winner = "white"
            return True

        if not white_pieces:
            turn_manager.winner = "black"
            return True

        red_has_moves = False
        for p in red_pieces:
            if len(self.get_valid_moves(p)) > 0:
                red_has_moves = True
                break

        white_has_moves = False
        for p in white_pieces:
            if len(self.get_valid_moves(p)) > 0:
                white_has_moves = True
                break

        if not red_has_moves:
            turn_manager.winner = "white"
            return True

        if not white_has_moves:
            turn_manager.winner = "black"
            return True

        return False

    def setup_pieces(self):
        """
        It sets up the start-up board and the pieces on it
        :return: The pieces set
        """
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.pieces.append(Piece(white, row, col))
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.pieces.append(Piece(red, row, col))

    def get_piece_at_pos(self, row, col):
        """
        Gets the piece at position (row, col)
        :param row:The row of the piece
        :param col: The column of the piece
        :return: The piece at position (row, col)
        """
        for p in self.pieces:
            if p.row == row and p.column == col:
                return p
        return None

    def get_capture_paths(self, piece, row, col, visited=None):
        """
        It gets the paths to where the piece can capture other pieces
        :param piece: The piece that you press on
        :param row: The row of the piece path
        :param col: The column of the piece path
        :param visited: Checks if the piece moved on that path ,or it stayed on the designated path
        :return: The possible paths
        """
        if visited is None:
            visited = set()

        capture_moves = []
        is_king = piece.king or (piece.color == red and row == 0) or (piece.color == white and row == 7)
        directions = [-1, 1] if is_king else ([-1] if piece.color == red else [1])

        for dr in directions:
            for dc in (-1, 1):
                mid_r = row + dr
                mid_c = col + dc
                end_r = row + dr * 2
                end_c = col + dc * 2

                if 0 <= end_r < 8 and 0 <= end_c < 8:
                    enemy = self.get_piece_at_pos(mid_r, mid_c)
                    landing = self.get_piece_at_pos(end_r, end_c)

                    if enemy and enemy.color != piece.color and not landing and (mid_r, mid_c) not in visited:
                        new_visited = visited.copy()
                        new_visited.add((mid_r, mid_c))

                        deeper = self.get_capture_paths(piece, end_r, end_c, new_visited)

                        capture_moves.append((end_r, end_c))
                        if deeper:
                            capture_moves.extend(deeper)

        return capture_moves

    def clone(self):
        from copy import deepcopy
        return deepcopy(self)

    def get_valid_moves(self, piece):
        """
        Checks the piece valid moves without captures
        :param piece: The piece that you press on
        :return: The valid moves to where the piece can move
        """
        moves = {}
        is_king = piece.king or (piece.color == red and piece.row == 0) or (piece.color == white and piece.row == 7)
        directions = [-1, 1] if is_king else ([-1] if piece.color == red else [1])

        for dr in directions:
            for dc in (-1, 1):
                nr = piece.row + dr
                nc = piece.column + dc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    if not self.get_piece_at_pos(nr, nc):
                        moves[(nr, nc)] = "move"

        for landing in self.get_capture_paths(piece, piece.row, piece.column):
            moves[landing] = "capture"

        return moves

    def get_capture_path_for_move(self, piece, start_row, start_col, dest_row, dest_col):
        """
        Gets the capture path for a move
        :param piece: The piece that you press on
        :param start_row: The row of the start position
        :param start_col: The column of the start position
        :param dest_row: The row of the destination position to where the piece can capture, and it's path
        :param dest_col: The column of the destination position to where the piece can capture, and it's path
        :return: The capture path
        """
        path = []
        dr = 1 if dest_row > start_row else -1
        dc = 1 if dest_col > start_col else -1
        r, c = start_row + dr, start_col + dc
        while r != dest_row and c != dest_col:
            enemy = self.get_piece_at_pos(r, c)
            if enemy and enemy.color != piece.color:
                path.append((r, c))
            r += dr
            c += dc
        return path

    def handle_clicks(self, row, col, turn_manager):
        """
        Handles clicks on the piece
        :param row: The row of that piece
        :param col: The column of that piece
        :param turn_manager: Checks which turn it is (black, white)
        :return: The state of the piece when it has been clicked
        """
        piece = self.get_piece_at_pos(row, col)

        if self.selected_piece and (row, col) in self.valid_moves:
            move_type = self.valid_moves[(row, col)]
            if move_type == "capture":
                start_row, start_col = self.selected_piece.row, self.selected_piece.column
                self._capture_piece_recursive(self.selected_piece, start_row, start_col, row, col)

                if self.check_win_condition(turn_manager):
                    return


            else:
                self.selected_piece.move_piece(row, col)
                if self.selected_piece.color == red and row == 0:
                    self.selected_piece.king = True
                if self.selected_piece.color == white and row == 7:
                    self.selected_piece.king = True

            self.selected_piece = None
            self.valid_moves = {}
            turn_manager.switch_turn()
            return

        if piece:
            if turn_manager.turn == "red" and piece.color != red:
                return
            if turn_manager.turn == "white" and piece.color != white:
                return
            self.selected_piece = piece
            self.valid_moves = self.get_valid_moves(piece)
            return

        self.selected_piece = None
        self.valid_moves = {}

    def _perform_capture(self, piece, dest_row, dest_col):
        """
        Performs the capture move on one or multiple pieces
        :param piece: The piece that you press on, and it is going to capture
        :param dest_row: Which row it lands on
        :param dest_col: Which column it lands on
        :return: Capture the pieces in the way and moves the clicked piece on the space
        """
        while True:
            path = self.get_capture_path_for_move(piece, piece.row, piece.column, dest_row, dest_col)
            for r, c in path:
                enemy = self.get_piece_at_pos(r, c)
                if enemy and enemy.color != piece.color:
                    self.pieces.remove(enemy)
                    self.capture_pieces.append(enemy)

            piece.move_piece(dest_row, dest_col)

            if piece.color == red and dest_row == 0:
                piece.king = True
            if piece.color == white and dest_row == 7:
                piece.king = True

            moves = self.get_valid_moves(piece)
            capture_moves = {pos: t for pos, t in moves.items() if t == "capture"}
            if not capture_moves:
                break
            dest_row, dest_col = list(capture_moves.keys())[0]

    def _capture_piece_recursive(self, piece, start_row, start_col, final_row=None, final_col=None, visited=None):
        """
        Captures all the pieces on the clicked piece way
        :param piece: The piece that you press on
        :param start_row: Starting row of the piece you press on
        :param start_col: Starting column of the piece you press on
        :param final_row: The final row of the piece you press on
        :param final_col: The final column of the piece you press on
        :param visited: Checks if the place was visited or not
        :return: The capture path
        """
        if visited is None:
            visited = set()

        captures = self.get_capture_paths(piece, start_row, start_col, visited)
        if not captures:
            return

        for dest_row, dest_col in captures:
            dr_total = dest_row - start_row
            dc_total = dest_col - start_col

            if dr_total == 0 or dc_total == 0:
                continue
            if abs(dr_total) != abs(dc_total):
                continue

            dr = dr_total // abs(dr_total)
            dc = dc_total // abs(dc_total)

            r, c = start_row + dr, start_col + dc
            removed = []

            while r != dest_row and c != dest_col:
                enemy = self.get_piece_at_pos(r, c)
                if enemy and enemy.color != piece.color and (r, c) not in visited:
                    self.pieces.remove(enemy)
                    removed.append(enemy)
                    visited.add((r, c))
                r += dr
                c += dc

            piece.move_piece(dest_row, dest_col)

            if piece.color == red and dest_row == 0:
                piece.king = True
            if piece.color == white and dest_row == 7:
                piece.king = True

            if final_row is not None and final_col is not None:
                if dest_row == final_row and dest_col == final_col:
                    return

            self._capture_piece_recursive(piece, dest_row, dest_col, final_row, final_col, visited)
            return


