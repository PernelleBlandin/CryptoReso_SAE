class Piece:
    nom: str
    deplacements: list[int]
    position: tuple
    estNoir: bool
    mouvementsEffectues: int


    def __init__(self,nom: str, estNoir: bool, position: tuple, deplacements: list[int], mouvementsEffectues: int) -> None:
        self.nom = nom
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
        for deplacement in self.deplacements:
            if self.position[0] + deplacement[0] == position[0] and self.position[1] + deplacement[1] == position[1]:
                return True
        return False


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