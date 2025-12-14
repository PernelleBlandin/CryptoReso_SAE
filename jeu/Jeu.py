from classes.Echequier import Echiquier
from classes.Joueur import Joueur
from Historique import enregistrer_partie

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

        resultat = self.echiquier.jouer(self.joueur1, self.joueur2)
        if resultat == "abandon blanc":
            pseudo_gagnant = "Abandon " + pseudo_blanc + ". Victoire " + pseudo_noir
        elif resultat == "abandon noir":
            pseudo_gagnant = "Abandon " + pseudo_noir + ". Victoire " + pseudo_blanc
        elif resultat is None:
            pseudo_gagnant = None
        elif resultat:
            pseudo_gagnant = pseudo_noir
        else:
            pseudo_gagnant = pseudo_blanc
        enregistrer_partie(pseudo_blanc, pseudo_noir, pseudo_gagnant)


if __name__ == "__main__":
    jeu = Jeu(None, None)
    jeu.lancer()
