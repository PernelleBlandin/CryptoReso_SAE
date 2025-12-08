from classes.Echequier import Echiquier

class Jeu():
    def __init__(self) -> None:
        self.echiquier = Echiquier()

    def lancer(self):
        print("Bienvenue dans le jeu d'échecs !\n")
        print(self.echiquier)


if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancer()