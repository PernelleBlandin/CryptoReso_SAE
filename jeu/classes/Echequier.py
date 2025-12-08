from classes import *

from classes.Pion import Pion

PIECE= []

class Echiquier():

    def __init__(self):
        for x in range(8):
            PIECE.append(Pion(self))#TODO REVOIR INITIALISATION
        pass
    
    def initialiser_piece(self):
        PIECE = []

    def ajouter_piece(self, piece:Piece, pos: tuple):
        PIECE.append((piece, pos))
    
    def deplacer(self, piece:Piece, pos: tuple):
        pass

    def get_piece(self, pos: tuple):
        for p in PIECE:
            if p[1] == pos:
                return p[0]
            
    def est_vide(self, pos: tuple):
        pass

    def pos_valide(self, pos: tuple):
        p
    
    def jouer(self):
        pass

        


        