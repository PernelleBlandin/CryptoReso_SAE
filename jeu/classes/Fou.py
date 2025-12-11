from .Piece import Piece

class Fou(Piece):
    nom: str
    deplacements: list[int]
    position: tuple
    est_noir: bool
    mouvementsEffectues: int
    stringRep: str

    def __init__(self, est_noir: bool, position: tuple, mouvements_effectues: int) -> None:
        super().__init__('Fou', est_noir, position,
                         [(1, 1), (-1, 1), (1, -1), (-1, -1)],
                         mouvements_effectues)
        self.stringRep = '♗' if not self.est_noir else '♝'

    def __str__(self) -> str:
        cote = 'Noir' if self.est_noir else 'Blanc'
        return 'Type : Fou' \
                f' - Position : {self.position}' \
                f' - Côte : {cote}' \
                f' -- Mouvements effectués : {self.mouvements_effectues}'