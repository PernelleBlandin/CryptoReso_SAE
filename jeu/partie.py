class Partie:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueur1.envoyer_message("Initialisation d'une partie avec " + self.joueur2.nom)
        self.joueur2.envoyer_message("Initialisation d'une partie avec " + self.joueur1.nom)

    def envoyer_aux_deux(self, message):
        self.joueur1.envoyer_message(message)
        self.joueur2.envoyer_message(message)

    def lancer(self):
        self.envoyer_aux_deux("Début de la partie !")
