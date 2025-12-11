from .Piece import Piece
from constantes import DEPLACEMENT_ROI

class Roi(Piece):
    nom: str
    deplacements: list[int]
    position: tuple
    est_noir: bool
    mouvements_effectues: int
    stringRep: str

    def __init__(
        self, est_noir: bool, position: tuple, mouvements_effectues: int
    ) -> None:
        super().__init__(
            "Roi",
            est_noir,
            position,
            DEPLACEMENT_ROI,
            mouvements_effectues=0,
        )
        self.stringRep = "♔" if not self.est_noir else "♚"

    def __str__(self) -> str:
        cote = "Noir" if self.est_noir else "Blanc"
        return "Type : Roi" " - Position : " + str(
            self.position
        ) + " - Côte : " + cote + " -- Mouvements effectués : " + str(
            self.mouvements_effectues
        )
