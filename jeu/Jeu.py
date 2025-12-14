from classes.Echequier import Echiquier

class Jeu():
    def __init__(self) -> None:
        self.echiquier = Echiquier()

    def lancer(self):
        self.echiquier.jouer()

if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancer()
