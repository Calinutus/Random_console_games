import pygame.draw

from Checkers.ConstantsForTable import *


class DrawCube:
    def __init__(self , cube):
        self.cube = cube

    def draw_cube(self):
        """
        Draws the spaces on the board
        :return: The spaces on the board
        """
        self.cube.fill(black)
        for row in range(ROWS):
            for col in range(row % 2 , COLS , 2):
                pygame.draw.rect(self.cube , white , (row*SQUARE_SIZE , col*SQUARE_SIZE , SQUARE_SIZE, SQUARE_SIZE))




