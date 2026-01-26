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
        self.envoyer_aux_deux("\n" + str(self.partie.echiquier) + "\n")
        fini = False
        line = None
        try:
            while not fini: 
                if line is not None:
                    if not line:
                        print("On est passé là")
                        break
                    
                    print("Commande reçue : " + (self.joueurNoir.pseudo if self.tour_noir else self.joueurBlanc.pseudo) + " " + str(line))

                    # On récupère les parties de la commande
                    parts = line.split()
                    print(parts)

                    if not parts:
                        continue

                    cmd = parts[0].lower()

                    if cmd == "quit":
                        if self.tour_noir:
                            pseudo_gagnant = "Abandon " + self.joueurNoir.pseudo + ". Victoire " + self.joueurBlanc.pseudo
                        else:
                            pseudo_gagnant = "Abandon " + self.joueurBlanc.pseudo + ". Victoire " + self.joueurNoir.pseudo
                        enregistrer_partie(self.joueurBlanc.pseudo, self.joueurNoir.pseudo, pseudo_gagnant)
                        self.envoyer_aux_deux("quit")
                        fini = True

                    elif cmd == "play":
                        if len(parts) == 3:
                            res = self.partie.valider_et_deplacer(parts[1], parts[2], self.tour_noir)
                            if res == "OK":
                                self.tour_noir = not self.tour_noir
                                
                                # Envoi du coup à l'adversaire
                                adversaire = self.joueurNoir if self.tour_noir else self.joueurBlanc
                                adversaire.envoyer_message(f"play_ad {parts[1]} {parts[2]}")

                                # Vérification Echec et Mat / Pat
                                est_echec = self.partie.echiquier.est_en_echec(self.tour_noir)
                                coups_possibles = self.partie.echiquier.coups_legaux(self.tour_noir)

                                if est_echec:
                                    if not coups_possibles:
                                        self.envoyer_aux_deux("\n" + str(self.partie.echiquier) + "\n")
                                        gagnant = self.joueurNoir.pseudo if not self.tour_noir else self.joueurBlanc.pseudo
                                        self.envoyer_aux_deux(f"ECHEC ET MAT ! Victoire de {gagnant}")
                                        enregistrer_partie(self.joueurBlanc.pseudo, self.joueurNoir.pseudo, gagnant)
                                        fini = True
                                        continue
                                    else:
                                        res = "ECHEC"
                                elif not coups_possibles:
                                    self.envoyer_aux_deux("\n" + str(self.partie.echiquier) + "\n")
                                    self.envoyer_aux_deux("PAT ! Match nul.")
                                    enregistrer_partie(self.joueurBlanc.pseudo, self.joueurNoir.pseudo, "Nul")
                                    fini = True
                                    continue

                            echiquier = "\n" + str(self.partie.echiquier) + "\n"
                            self.envoyer_aux_deux(echiquier)
                            line = self.demander_au_joueur_courant(res + ", C'est au tour des " + ("Noirs" if self.tour_noir else "Blancs") + " : \n")
                        else:
                            line = self.demander_au_joueur_courant("ERREUR (Format: play caseSrc caseDst). C'est au tour des " + ("Noirs" if self.tour_noir else "Blancs") + "\n")

                    elif cmd == "leave":
                        if self.tour_noir:
                            pseudo_gagnant = "Abandon " + self.joueurNoir.pseudo + ". Victoire " + self.joueurBlanc.pseudo
                        else:
                            pseudo_gagnant = "Abandon " + self.joueurBlanc.pseudo + ". Victoire " + self.joueurNoir.pseudo
                        enregistrer_partie(self.joueurBlanc.pseudo, self.joueurNoir.pseudo, pseudo_gagnant)
                        self.envoyer_au_joueur_courant("OK")
                        fini = True

                    elif cmd == "replay":
                        self.joueurBlanc, self.joueurNoir = self.joueurNoir, self.joueurBlanc
                        self.partie = Jeu(self.joueurBlanc, self.joueurNoir)
                        self.tour_noir = False
                        self.envoyer_aux_deux("Nouvelle partie relancée avec le meme joueur!")
                        self.envoyer_aux_deux("\n"+ str(self.partie.echiquier)+"\n")
                        line = self.demander_au_joueur_courant("C'est au tour des Blancs : \n")

                    elif cmd == "new":
                        self.envoyer_au_joueur_courant("OK")
                        fini = True

                else:
                    texte = "ERREUR Commande inconnue. C'est au tour des " + ("Noirs" if self.tour_noir else "Blancs") + "\n"
                    line = self.demander_au_joueur_courant(texte)
            else:
                line = self.demander_au_joueur_courant("C'est au tour des " + ("Noirs" if self.tour_noir else "Blancs") + " : \n")
        
        except Exception as e:
            print(f"Erreur critique dans la partie : {e}")
            self.envoyer_aux_deux("exit")

        finally:
            print("Fermeture des sessions...")

        choix_blanc = None
        choix_noir = None

        while True:
            if not choix_blanc:
                choix_blanc = self.joueurBlanc.recuperer_entree("Partie terminée. Tapez 'replay' pour rejouer ou 'quit' pour quitter : ").lower()
            if not choix_noir:
                choix_noir = self.joueurNoir.recuperer_entree("Partie terminée. Tapez 'replay' pour rejouer ou 'quit' pour quitter : ").lower()

            if choix_blanc == "replay" and choix_noir == "replay":
                self.envoyer_aux_deux ("OK")
                self.partie = Jeu(self.joueurBlanc, self.joueurNoir) 
                self.tour_noir = False
                self.lancer()
                return
            
            elif choix_blanc == "new" or choix_noir == "new":
                self.envoyer_aux_deux("OK")
                if choix_blanc == "new": self.joueurBlanc.pseudo = None
                if choix_noir == "new": self.joueurNoir.pseudo = None
                break

            if choix_blanc == "quit" or choix_noir == "quit":
                self.envoyer_aux_deux("OK - Déconnexion.")
                break

            self.joueurBlanc.fermer_session()
            self.joueurNoir.fermer_session()

        print("Fermeture des sessions...")
        self.joueurBlanc.fermer_session()
        self.joueurNoir.fermer_session()
