class Joueur:
    def __init__(self, pseudo: str, est_noir: bool) -> None:
        self.pseudo = pseudo
        self.est_noir = est_noir

    def __str__(self) -> str:
        return "Joueur " + self.pseudo + " (Noir)" if self.est_noir else "Joueur " + self.pseudo + " (Blanc)"
