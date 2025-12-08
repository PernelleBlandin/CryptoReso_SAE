from classes import Echiquier

class Piece:
    nom: str
    deplacements: list[int]
    position: tuple
    estNoir: bool
    echiquier: Echiquier
    mouvementsEffectues: int


    def __init__(self,nom: str, echiquier: Echiquier, estNoir: bool, position: tuple, deplacements: list[int], mouvementsEffectues: int = 0) -> None:
        self.nom = nom
        self.echiquier = echiquier
        self.estNoir = estNoir
        self.position = position
        self.deplacements = []
        self.mouvementsEffectues = 0

    def __str__(self) -> str:
        cote = 'Noir' if self.estN else 'Blanc'
        return 'Type : Piece' \
               ' - Position : ' + str(self.position) + \
               ' - Côte : ' + cote + \
               ' -- Value : ' + str(self.value) + \
               ' -- Mouvements effectués : ' + str(self.mouvementsEffectues)

    def estMouvementValide(self, position:tuple) -> bool:
        """Retourne vrai si la pièce peut effectuer le mouvement

        Args:
            position (tuple): la position d'arrivée

        Returns:
            bool: true si le déplacement est possible, false sinon
        """
        pass

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Piece):
            return NotImplemented
        if (
                self.board == other.board and self.side == other.side
                and self.position == other.position
                and self.__class__ == other.__class__
        ):
            return True
        return False

    def getMouvementsPossibles(self) -> List[int]:  # type: ignore[empty-body]
        """Retourne la liste des mouvements possibles de la pièce

        Returns:
            List[int]: la liste de tuples de mouvements possibles
        """
        return self.deplacements