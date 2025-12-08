from classes import Piece

class Reine(Piece):
    nom: str
    deplacements: list[int]
    position: tuple
    est_noir: bool
    mouvementsEffectues: int
    stringRep: str

    def __init__(self, est_noir: bool, position: tuple, mouvementsEffectues: int) -> None:
        
        super().__init__('Reine', est_noir, position, [(0, 1), (-1, 1), (-1, 0),  (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)] if mouvementsEffectues == 0 else [(0, 1)], mouvementsEffectues = 0)
        self.stringRep = '♕' if not self.est_noir else '♛'
        
    def __str__(self) -> str:
        cote = 'Noir' if self.est_noir else 'Blanc'
        return 'Type : Reine' \
               ' - Position : ' + str(self.position) + \
               ' - Côte : ' + cote + \
               ' -- Value : ' + str(self.value) + \
               ' -- Mouvements effectués : ' + str(self.mouvements_effectues)