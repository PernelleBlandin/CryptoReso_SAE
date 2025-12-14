from .Piece import Piece


class Pion(Piece):
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
            "Pion",
            est_noir,
            position,
            [], # Les déplacements du pion sont gérés dynamiquement dans la classe Echiquier avec le nombre de mouvements effectués
            mouvements_effectues,
        )
        self.stringRep = "♙" if self.est_noir else "♟"

    def __str__(self) -> str:
        cote = "Noir" if self.est_noir else "Blanc"
        return (
            "Type : Pion"
            f" - Position : {self.position}"
            f" - Côte : {cote}"
            f" -- Mouvements effectués : {self.mouvements_effectues}"
        )
