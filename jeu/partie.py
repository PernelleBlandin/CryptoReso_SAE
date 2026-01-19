from jeu import Jeu
from session import *

class Partie:
    def __init__(self, joueurBlanc:Session, joueurNoir:Session):
        self.joueurBlanc = joueurBlanc
        self.joueurNoir = joueurNoir
        self.joueurBlanc.envoyer_message("Initialisation d'une partie avec " + self.joueurNoir.pseudo)
        self.joueurNoir.envoyer_message("Initialisation d'une partie avec " + self.joueurBlanc.pseudo)
        self.partie = Jeu(self.joueurBlanc, self.joueurNoir) # que prend Jeu en paramètre ?
        self.tour_noir = False

    def envoyer_aux_deux(self, message):
        self.joueurBlanc.envoyer_message(message)
        self.joueurNoir.envoyer_message(message)

    def envoyer_au_joueur_courant(self, message):
        if not self.tour_noir:
            self.joueurBlanc.envoyer_message(message)
        else:
            self.joueurNoir.envoyer_message(message)

    def demander_au_joueur_courant(self, message):
        if not self.tour_noir:
            return self.joueurBlanc.recuperer_entree(message)
        else:
            return self.joueurNoir.recuperer_entree(message)

    def lancer(self):
        self.envoyer_aux_deux("Debut de la partie !")
        fini = False
        line = None
        while not fini: 
            if line is not None:
                #line = self.demander_au_joueur_courant("Attente")
                if not line:
                    print("On est passé là")
                    break
                
                print("Commande reçue : " + (self.joueurNoir.pseudo if self.tour_noir else self.joueurBlanc.pseudo) + " " + str(line))

                # On récupère les parties de la commande
                parts = line.split()
                print(parts)

                #if not parts:
                #    continue

                cmd = parts[0].lower()

                if cmd == "quit":
                    if self.joueurBlanc is not None:
                        if self.tour_noir:
                            pseudo_gagnant = "Abandon " + self.joueurNoir.pseudo + ". Victoire " + self.joueurBlanc.pseud
                        else:
                            pseudo_gagnant = "Abandon " + self.joueurBlanc.pseudo + ". Victoire " + self.joueurNoir.pseudo
                        enregistrer_partie(self.joueurBlanc.pseudo, self.joueurNoir.pseudo, pseudo_gagnant)
                        self.envoyer_au_joueur_courant("OK")
                    fini = True

                elif cmd == "play":
                    if len(parts) == 3:
                        res = self.partie.valider_et_deplacer(parts[1], parts[2], self.tour_noir)
                        if res == "OK":
                            self.tour_noir = not self.tour_noir
                        echiquier = "\n" + str(self.partie.echiquier) + "\n"
                        self.envoyer_au_joueur_courant(echiquier)
                        line = self.demander_au_joueur_courant(res + ", C'est au tour des " + ("Noirs" if self.tour_noir else "Blancs") + " : \n")
                    else:
                        self.demander_au_joueur_courant("ERREUR (Format: play caseSrc caseDst). C'est au tour des " + ("Noirs" if self.tour_noir else "Blancs") + "\n")

                elif cmd == "leave":
                    if self.joueurBlanc is not None:
                        if self.tour_noir:
                            pseudo_gagnant = "Abandon " + self.joueurNoir.pseudo + ". Victoire " + self.joueurBlanc.pseudo
                        else:
                            pseudo_gagnant = "Abandon " + self.joueurBlanc.pseudo + ". Victoire " + self.joueurNoir.pseudo
                        enregistrer_partie(self.joueurBlanc.pseudo, self.joueurNoir.pseudo, pseudo_gagnant)
                        self.envoyer_au_joueur_courant("OK")
                        fini = True
                    else:
                        self.envoyer_au_joueur_courant("ERR Aucune partie active")

                elif cmd == "replay":
                    print("A faire")

                elif cmd == "new":
                    print("A faire")
                    # self.joueurBlanc = Joueur(pseudo_blanc, est_noir=False)
                    # self.joueurNoir = Joueur(pseudo_noir, est_noir=True)

                else:
                    texte = "ERREUR Commande inconnue. C'est au tour des " + ("Noirs" if self.tour_noir else "Blancs") + "\n"
                    line = self.demander_au_joueur_courant(texte)
            else:
                line = self.demander_au_joueur_courant("C'est au tour des " + ("Noirs" if self.tour_noir else "Blancs") + " : \n")


        print("Fermeture des sessions...")
        self.joueurBlanc.fermer_session()
        self.joueurNoir.fermer_session()
