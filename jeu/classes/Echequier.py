from .Piece import Piece
from .Pion import Pion

class Echiquier():
    pieces: list[Piece]
    
    def __init__(self):
        self.pieces = []

        # Pions blancs
        for i in range(8):
            self.pieces.append(Pion(est_noir=False, position=(i, 1), mouvements_effectues=0))

        # Pions noirs
        for i in range(8):
            self.pieces.append(Pion(est_noir=True, position=(i, 6), mouvements_effectues=0))

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