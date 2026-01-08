from classes.Echequier import Echiquier
from classes.Joueur import Joueur

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
        pseudo_gagnant = self.get_pseudo_gagnant(resultat, pseudo_blanc, pseudo_noir)

        return resultat

    def get_pseudo_gagnant(self, resultat, pseudo_blanc, pseudo_noir):
        if resultat == "abandon blanc":
            return "Abandon " + pseudo_blanc + ". Victoire " + pseudo_noir
        elif resultat == "abandon noir":
            return "Abandon " + pseudo_noir + ". Victoire " + pseudo_blanc
        elif resultat is None:
            return None
        elif resultat:
            return pseudo_noir
        return pseudo_blanc

    def lancer_pour_serveur(self, file):
        # Cette méthode devra appeler une version de echiquier.jouer adaptée au réseau
        return self.echiquier.jouer_serveur(file)

if __name__ == "__main__":
    jeu = Jeu(None, None)
    res = jeu.lancer()
    print(f"Fin de partie, résultat : {res}")
