from classes.Echequier import Echiquier

class Jeu():
    def __init__(self, joueur1, joueur2) -> None:
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.echiquier = Echiquier()

    def lancer(self):
        self.echiquier.jouer()

if __name__ == "__main__":
    joueur_blanc = Joueur('joueur1', True)
    joueur_noir = Joueur('joueur2', False)
    jeu = Jeu(joueur_blanc, joueur_noir)
    jeu.lancer()
