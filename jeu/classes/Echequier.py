from .Piece import Piece
from .Pion import Pion
from .Cavalier import Cavalier
from .Fou import Fou
from .Tour import Tour
from .Reine import Reine
from .Roi import Roi

class Echiquier:
    pieces: list[Piece]

    def __init__(self):
        self.pieces = []
        self.initialiser_piece()

    def initialiser_piece(self):
        # Pions blancs
        for i in range(8):
            self.ajouter_piece(Pion(est_noir=False, position=(i, 1), mouvements_effectues=0))

        # Pions noirs
        for i in range(8):
            self.ajouter_piece(Pion(est_noir=True, position=(i, 6), mouvements_effectues=0))

        # Cavalier blancs
        self.ajouter_piece(Cavalier(est_noir=False, position=(1, 0), mouvements_effectues=0))
        self.ajouter_piece(Cavalier(est_noir=False, position=(6, 0), mouvements_effectues=0))

        # Cavalier noirs
        self.ajouter_piece(Cavalier(est_noir=True, position=(1, 7), mouvements_effectues=0))
        self.ajouter_piece(Cavalier(est_noir=True, position=(6, 7), mouvements_effectues=0))

        # Fou blancs
        self.ajouter_piece(Fou(est_noir=False, position=(2, 0), mouvements_effectues=0))
        self.ajouter_piece(Fou(est_noir=False, position=(5, 0), mouvements_effectues=0))

        # Fou noirs
        self.ajouter_piece(Fou(est_noir=True, position=(2, 7), mouvements_effectues=0))
        self.ajouter_piece(Fou(est_noir=True, position=(5, 7), mouvements_effectues=0))

        # Tour noirs
        self.ajouter_piece(Tour(est_noir=True, position=(0, 7), mouvements_effectues=0))
        self.ajouter_piece(Tour(est_noir=True, position=(7, 7), mouvements_effectues=0))

        # Tour blancs
        self.ajouter_piece(Tour(est_noir=False, position=(0, 0), mouvements_effectues=0))
        self.ajouter_piece(Tour(est_noir=False, position=(7, 0), mouvements_effectues=0))

        # Reine blanche
        self.ajouter_piece(Reine(est_noir=False, position=(3, 0), mouvements_effectues=0))

        # Reine noire
        self.ajouter_piece(Reine(est_noir=True, position=(3, 7), mouvements_effectues=0))

        # Roi blanc
        self.ajouter_piece(Roi(est_noir=False, position=(4, 0), mouvements_effectues=0))

        # Roi noir
        self.ajouter_piece(Roi(est_noir=True, position=(4, 7), mouvements_effectues=0))

    def ajouter_piece(self, piece: Piece, pos: tuple):
        self.pieces.append((piece, pos))

    def ajouter_piece(self, piece: Piece):
        self.pieces.append(piece)

    def deplacer(self, piece: Piece, pos: tuple):
        pass

    def get_piece(self, position: tuple[int, int]) -> Piece | None:
        """Retourne la pièce à une position donnée ou None si aucune pièce n'est présente
        Args:
            position (tuple[int, int]): la position à vérifier
        Returns:
            Piece | None: la pièce à la position donnée ou None si aucune pièce n'est présente
        """
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def est_vide(self, pos: tuple):
        pass

    def pos_valide(self, pos: tuple):
        pass

    def __str__(self) -> str:
        """Affiche l'échiquier dans la console
        Returns:
            str: la représentation textuelle de l'échiquier
        """
        board_str = ""
        for y in range(7, -1, -1):
            board_str += f"{y+1} "
            for x in range(8):
                piece = self.get_piece((x, y))
                if piece:
                    board_str += f" {piece.stringRep} "
                else:
                    board_str += " ☐ "
            board_str += "\n"
        board_str += "   a  b  c  d  e  f  g  h \n"
        return board_str

    def jouer(self):
        pass
