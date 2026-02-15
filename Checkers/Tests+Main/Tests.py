import unittest
from unittest.mock import patch, MagicMock

with patch("pygame.image.load") as mock_load, patch("pygame.transform.scale") as mock_scale:
    mock_surface = MagicMock()
    mock_load.return_value = mock_surface
    mock_scale.return_value = mock_surface

    from ConstantsForTable import white, red
    from Checkers.Logic.Pieces import Piece
    from Checkers.Board.BoardLogic import BoardLogic

    class ControlTurnManager:
        def __init__(self):
            self.turn = "red"
            self.winner = None
            self.switch = False

        def switch_turn(self):
            self.switch = True
            self.turn = "white" if self.turn == "red" else "red"

    class TestBoardLogic(unittest.TestCase):
        def setUp(self):
            self.board = BoardLogic()
            self.turn_manager = ControlTurnManager()

        def test_check_win_condition(self):
            self.board.pieces = [p for p in self.board.pieces if p.color == white]
            result = self.board.check_win_condition(self.turn_manager)
            self.assertTrue(result)
            self.assertEqual(self.turn_manager.winner , "white")
            self.assertEqual(self.turn_manager.switch, False)
            self.assertNotEqual(self.turn_manager.winner, "red")

            self.board.setup_pieces()
            self.board.pieces = [p for p in self.board.pieces if p.color == red]
            result - self.board.check_win_condition(self.turn_manager)
            self.assertTrue(result)
            self.assertEqual(self.turn_manager.winner, "black")



        def test_setup_pieces(self):
            self.assertEqual(len(self.board.pieces), 24)
            red_pieces = [p for p in self.board.pieces if p.color == red]
            self.assertEqual(len(red_pieces), 12)
            white_pieces =[p for p in self.board.pieces if p.color == white]
            self.assertEqual(len(white_pieces), 12)

        def test_get_piece_at_pos(self):
            piece = self.board.get_piece_at_pos(3 , 3)

            self.assertIsNone(piece)
            self.assertIsNone(self.board.get_piece_at_pos(1, 1))

            piece = self.board.get_piece_at_pos(1, 2)
            self.assertEqual(piece.color , white)

        def test_get_capture_paths(self):
            #Test capture
            red_piece = Piece(red , 5 , 0)
            white_piece = Piece(white , 4 , 1)
            self.board.pieces = [red_piece, white_piece]
            moves = self.board.get_valid_moves(red_piece)

            self.assertIn((3 , 2) , moves)
            self.assertEqual(moves[(3 , 2)] , 'capture')



        def test_get_valid_moves(self):
            # Test move
            red_piece = Piece(red, 5, 0)
            self.board.pieces = [red_piece]
            moves = self.board.get_valid_moves(red_piece)
            for pos, move_type in moves.items():
                self.assertEqual(move_type, "move")

        def test_get_capture_path_for_move(self):
            red_piece = Piece(red, 5, 0)
            white_piece = Piece (white , 4 , 1)
            self.board.pieces = [red_piece, white_piece]
            moves = self.board.get_valid_moves(red_piece)

            self.assertIn((3 , 2) , moves)
            self.assertEqual(moves[(3 , 2)] , 'capture')

        def handle_clicks(self):
            piece = self.board.get_piece_at_pos(5 , 0)
            self.board.selected_piece = piece
            self.board.valid_moves = self.board.get_valid_moves(piece)
            dest_row , dest_col = list(self.board.valid_moves.keys())[0]
            self.board.handle_clicks(dest_row, dest_col, self.turn_manager)

            self.assertEqual(piece.row , dest_row)
            self.assertEqual(piece.col , dest_col)
            self.assertTrue(self.turn_manager.switch)

        def test_capture_piece_recursive(self):
            red_piece = Piece(red , 5 , 0)
            white_piece1 = Piece(white , 4 , 1)
            white_piece2 = Piece(white , 2, 3)
            self.board.pieces = [red_piece , white_piece1, white_piece2]
            self.board._capture_piece_recursive(red_piece , 5 , 0 , final_row= 1 , final_col= 1)

            self.assertEqual((red_piece.row , red_piece.column) , (1 , 4))
            self.assertNotIn(white_piece1 , self.board.pieces)
            self.assertNotIn(white_piece2, self.board.pieces)
            self.assertIn(red_piece , self.board.pieces)




if __name__ == "__main__":
    unittest.main()
