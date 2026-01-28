from classes.Echequier import Echiquier
from classes.Joueur import Joueur
from Historique import enregistrer_partie


class Jeu():
    def __init__(self, joueur1, joueur2) -> None:
       self.joueur1 = joueur1
       self.joueur2 = joueur2
       self.echiquier = Echiquier()

    def lancer_solo(self):
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


    def valider_et_deplacer(self, src_str, dst_str, est_noir):
        """Valide et effectue un coup pour le serveur
        
        Returns:
            str: le résultat du coup
        """
        try:
            if len(src_str) != 2 or len(dst_str) != 2:
                return "ERREUR Format invalide (ex: a3)"
            
            col_dep = ord(src_str[0].lower()) - ord('a')
            lig_dep = int(src_str[1]) - 1
            col_arr = ord(dst_str[0].lower()) - ord('a')
            lig_arr = int(dst_str[1]) - 1
            
            depart = (col_dep, lig_dep)
            arrivee = (col_arr, lig_arr)
            
            if not self.echiquier.pos_valide(depart) or not self.echiquier.pos_valide(arrivee):
                return "ERREUR Position hors plateau"
            
            piece = self.echiquier.get_piece(depart)
            if not piece:
                return "ERREUR Pas de pièce à cette position"
            
            if piece.est_noir != est_noir:
                return "ERREUR Ce n'est pas votre pièce"
            
            if arrivee not in self.echiquier.recuperer_coups_possibles(piece):
                return "ERREUR Coup impossible"
            
            if not self.echiquier.simuler_coup(piece, arrivee):
                return "ERREUR Ce coup vous met en échec"
            
            self.echiquier.deplacer(piece, arrivee)
            return "OK"
        except Exception as e:
            return f"ERREUR {str(e)}"


if __name__ == "__main__":
    jeu = Jeu(None, None)
    res = jeu.lancer_solo()
    print(f"Fin de partie, résultat : {res}")

