class Piece:
    nom: str
    deplacements: list[int]
    position: tuple
    est_noir: bool
    mouvements_effectues: int


    def __init__(self,nom: str, est_noir: bool, position: tuple, deplacements: list[int], mouvements_effectues: int) -> None:
        self.nom = nom
        self.est_noir = est_noir
        self.position = position
        self.deplacements = []
        self.mouvements_effectues = 0

    def getMouvementsPossibles(self) -> List[int]:  # type: ignore[empty-body]
        """Retourne la liste des mouvements possibles de la pièce

        Returns:
            List[int]: la liste de tuples de mouvements possibles
        """
        return self.deplacements

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
    
    def __str__(self) -> str:
        cote = 'Noir' if self.est_noir else 'Blanc'
        return 'Type : Piece' \
               ' - Position : ' + str(self.position) + \
               ' - Côte : ' + cote + \
               ' -- Value : ' + str(self.value) + \
               ' -- Mouvements effectués : ' + str(self.mouvements_effectues)

    def __eq__(self, other: object) -> bool:
        """Vérifie si deux pièces sont égales

        Args:
            other (object): la pièce à comparer

        Returns:
            bool: true si les pièces sont égales, false sinon
        """
        if not isinstance(other, Piece):
            return NotImplemented
        if (
                self.board == other.board and self.side == other.side
                and self.position == other.position
                and self.__class__ == other.__class__
        ):
            return True
        return False