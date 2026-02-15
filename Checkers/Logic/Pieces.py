from Checkers.ConstantsForTable import *
import pygame

black_piece_img = pygame.image.load("../PiecesImages/BlackPiece.png")
white_piece_img = pygame.image.load("../PiecesImages/WhitePiece.png")
black_piece_king_img = pygame.image.load("../PiecesImages/BlackPieceKing.png")
white_piece_king_img = pygame.image.load("../PiecesImages/WhitePieceKing.png")
black_piece_img = pygame.transform.scale(black_piece_img, (SQUARE_SIZE - 10, SQUARE_SIZE - 10))
white_piece_img = pygame.transform.scale(white_piece_img, (SQUARE_SIZE - 10, SQUARE_SIZE - 10))
black_piece_king_img = pygame.transform.scale(black_piece_king_img, (SQUARE_SIZE - 10, SQUARE_SIZE - 10))
white_piece_king_img = pygame.transform.scale(white_piece_king_img, (SQUARE_SIZE - 10, SQUARE_SIZE - 10))


class Piece:
    def  __init__(self , color , row , column):
        self.direction = None
        self.color = color
        self.row = row
        self.column = column
        self.king = False
        self.x = 0
        self.y = 0

    def draw(self, surface):
        """
        Gets the set images from the set and updates the surface.
        :param surface: The surface to draw on.
        :return: The updated surface with the images of the pieces drawn
        """
        self.calculate_position()

        if self.king:
            if self.color == red:
                surface.blit(black_piece_king_img, (self.x + 2, self.y + 2))
            else:
                surface.blit(white_piece_king_img, (self.x + 2, self.y + 2))
        else:
            if self.color == red:
                surface.blit(black_piece_img, (self.x + 2, self.y + 2))
            else:
                surface.blit(white_piece_img,  (self.x + 2, self.y + 2))

    def set_direction(self):
        """
        Sets the direction of the piece.
        :return: The current direction of the piece.
        """
        if self.color == red:
            self.direction = -1
        else:
            self.direction = 1


    def calculate_position(self):
        """
        Calculates the current position of the piece.
        :return: Current position of the piece.
        """
        self.x = SQUARE_SIZE * self.column
        self.y = SQUARE_SIZE * self.row

    def make_king(self):
        """
        Makes the king.
        :return: The piece becomes king.
        """
        self.king = True

    def move_piece(self , row , col):
        """
        Moves the piece.
        :param row:The row of the piece.
        :param col: The column of the piece.
        :return: Changes the position of the piece
        """
        self.row = row
        self.column = col

        if self.color == red and row == 0:
            self.make_king()
        if self.color == white and row == 7:
            self.make_king()

