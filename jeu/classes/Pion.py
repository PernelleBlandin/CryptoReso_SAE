from classes import Piece

class Pion(Piece):
    nom: str
    deplacements: list[int]
    position: tuple
    est_noir: bool
    mouvements_effectues: int
    stringRep: str

    def __init__(self, est_noir: bool, position: tuple, mouvements_effectues: int) -> None:
        
        super().__init__('Pion', est_noir, position, [(0, 1), (0, 2)] if mouvements_effectues == 0 else [(0, 1)], mouvements_effectues = 0)
        self.stringRep = '▲' if not self.est_noir else '▼'

    def __str__(self) -> str:
        cote = 'Noir' if self.estN else 'Blanc'
        return 'Type : Pion' \
               ' - Position : ' + str(self.position) + \
               ' - Côte : ' + cote + \
               ' -- Value : ' + str(self.value) + \
               ' -- Mouvements effectués : ' + str(self.mouvements_effectues)