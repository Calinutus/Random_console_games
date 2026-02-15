import pygame
from Checkers.ConstantsForTable import *

class DrawBoard:
    def __init__(self, board_logic):
        self.board_logic = board_logic

    def draw(self, surface):
        """
        Draw the board on the surface
        :param surface: The surface to draw on
        :return: The board surface
        """
        self.draw_squares(surface)
        self.draw_pieces(surface)
        self.draw_valid_moves(surface)

    def draw_squares(self, surface):
        """
        Draw the squares on the surface
        :param surface: The surface to draw on
        :return: The board surface with the squares drawn
        """
        surface.fill(black)
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(surface, white,
                                     (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                      SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self, surface):
        """
        Draw the pieces on the surface
        :param surface: Draw on the surface
        :return: Draws the board with the squares drawn and with pieces
        """
        for piece in self.board_logic.pieces:
            piece.draw(surface)

    def draw_valid_moves(self, surface):
        """
        Creates small colored circles on the surface
        :param surface: The board to draw on
        :return: The valid positions on the surface
        """
        for (row, col), move_type in self.board_logic.valid_moves.items():
            center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2

            color = blue if move_type == "move" else red
            pygame.draw.circle(surface, color, (center_x, center_y), 15)
