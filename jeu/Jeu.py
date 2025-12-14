from classes.Echequier import Echiquier
from classes.Joueur import Joueur
from classes.Historique import enregistrer_partie

class Jeu():
    def __init__(self, joueur1, joueur2) -> None:
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.echiquier = Echiquier()

    def lancer(self):
        pseudo_blanc = input("Pseudo du joueur Blanc : ").strip()
        pseudo_noir = input("Pseudo du joueur Noir : ").strip()
        self.joueur1 = Joueur(pseudo_blanc, est_noir=False)
        self.joueur2 = Joueur(pseudo_noir, est_noir=True)

        self.echiquier.jouer()

        gagnant = self.echiquier.jouer(self.joueur1, self.joueur2) # Gagnant: None (nul), True (noir), False (blanc)
        if gagnant is None:
            pseudo_gagnant = None
        elif gagnant:
            pseudo_gagnant = pseudo_noir
        else:
            pseudo_gagnant = pseudo_blanc
        enregistrer_partie(pseudo_blanc, pseudo_noir, pseudo_gagnant)


if __name__ == "__main__":
    jeu = Jeu(None, None)
    jeu.lancer()
