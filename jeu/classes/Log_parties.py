import json
from datetime import datetime
from typing import List, Dict, Any


class Log_parties:
    def __init__(self, pseudo_blanc: str, pseudo_noir: str):
        self.pseudo_blanc = pseudo_blanc
        self.pseudo_noir = pseudo_noir
        self.coups: List[Dict[str, Any]] = []
        self.date_partie = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def ajouter_coup(self, coupe_depart: str, coup_arrivee: str, est_blanc: bool):
        """Enregistre un coup dans la mémoire
        
        Args:
            coupe_depart (str): La position de départ du coup
            coup_arrivee (str): La position d'arrivée du coup
            est_blanc (bool): True si le coup est effectué par le joueur blanc, False sinon
        """
        self.coups.append(
            {
                "tour_numero": len(self.coups) + 1,
                "joueur": "Blanc" if est_blanc else "Noir",
                "depart": str(coupe_depart),
                "arrivee": str(coup_arrivee),
                "timestamp": datetime.now().isoformat(),
            }
        )

    def sauvegarder_partie(
        self, pseudo_gagnant: str = None, chemin_fichier: str = "partie.json"
    ):
        """
        Sauvegarde la partie complète dans un fichier JSON

        Args:
            id_gagnant (str, optional): Le pseudo du gagnant
            chemin_fichier (str): Le chemin où sauvegarder le fichier
        """
        donnees = {
            "meta_data": {
                "date": self.date_partie,
                "joueurs": {"blanc": self.nom_blanc, "noir": self.nom_noir},
                "pseudo_gagnant": pseudo_gagnant,
            },
            "historique_coups": self.coups,
        }

        try:
            with open(chemin_fichier, "w", encoding="utf-8") as f:
                json.dump(donnees, f, indent=4, ensure_ascii=False)
            print(f"Partie sauvegardée avec succès dans {chemin_fichier}")
        except IOError as e:
            print(f"Erreur lors de la sauvegarde de la partie : {e}")
