from classes.Echequier import Echiquier
from classes.Joueur import Joueur
from Historique import enregistrer_partie


class Jeu():
    def __init__(self, joueur1, joueur2) -> None:
       self.joueur1 = joueur1
       self.joueur2 = joueur2
       self.echiquier = Echiquier()


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


