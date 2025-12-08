from classes import Piece

class Pion(Piece):
    nom: str
    deplacements: list[int]
    position: tuple
    estNoir: bool
    mouvementsEffectues: int
    stringRep: str

    def __init__(self, estNoir: bool, position: tuple, mouvementsEffectues: int) -> None:
        
        super().__init__('Pion', estNoir, position, [(0, 1), (0, 2), (-1,1), (1,1)] if mouvementsEffectues == 0 else [(0, 1)], mouvementsEffectues = 0)
        self.stringRep = '♙' if not self.estNoir else '♟'