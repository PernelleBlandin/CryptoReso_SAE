from .Piece import Piece
from constantes import DEPLACEMENT_REINE


class Reine(Piece):
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
            "Reine",
            est_noir,
            position,
            DEPLACEMENT_REINE,
            mouvements_effectues,
        )
        self.stringRep = "♕" if self.est_noir else "♛"

    def __str__(self) -> str:
        cote = "Noir" if self.est_noir else "Blanc"
        return (
            "Type : Reine"
            f" - Position : {self.position}"
            f" - Côte : {cote}"
            f" -- Mouvements effectués : {self.mouvements_effectues}"
        )
