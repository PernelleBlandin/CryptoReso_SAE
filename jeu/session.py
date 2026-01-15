from Jeu import * 
from Historique import enregistrer_partie
import socket 

class Session:
    def __init__(self, serveur, sock):
        self.serveur = serveur
        self.socket = sock
        self.file=sock.makefile(mode="rw", encoding="utf-8")
        self.counter = 0
        self.joueur1 = None
        self.joueur2 = None
        self.partie = Jeu(self.joueur1, self.joueur2)
        self.tour_noir = False
    
    def mainSession(self):
        print("Mise en place d'une nouvelle session...")
        fini = False
        while not fini:
            if self.joueur1 == None:
                self.file.write("Donner un nom pour le joueur Blanc : " + "\n")
                self.file.flush()
                pseudoBlanc = self.file.readline().strip()
                self.joueur1 = Joueur(pseudoBlanc, False)
                self.partie.joueur1 = self.joueur1

                self.file.write("Donner un nom pour le joueur Noir : " + "\n")
                self.file.flush()
                pseudoNoir = self.file.readline().strip()
                self.joueur2 = Joueur(pseudoNoir, True)
                self.partie.joueur2 = self.joueur2
                
                self.file.write("Début de la partie..." + "\n")
                echiquier = "\n" + str(self.partie.echiquier) + "\n"
                self.file.write(echiquier)
                self.file.write("C'est au tour des Blancs : \n")
                self.file.flush()
            
            resultat = self.partie.lancer()
            pseudo_gagnant = self.partie.get_pseudo_gagnant(resultat, self.joueur1.pseudo, self.joueur2.pseudo)
            enregistrer_partie(self.joueur1.pseudo, self.joueur2.pseudo, pseudo_gagnant)
                

            # On récupère les 3 parties de la commande
            line = self.file.readline().strip()
            if line == "quit":
                break
                
            parts = line.split()
            if not parts:
                continue
                
            cmd = parts[0].lower()

            print("Commande reçue : " + ("Noirs " if self.tour_noir else "Blancs ") + line)

            if cmd == "quit":
                fini = True

            elif cmd == "play":
                if len(parts) == 3:
                    res = self.partie.valider_et_deplacer(parts[1], parts[2], self.tour_noir)
                    if res == "OK":
                        self.tour_noir = not self.tour_noir
                    echiquier = "\n" + str(self.partie.echiquier) + "\n"
                    self.file.write(echiquier)
                    self.file.write(res + " (C'est au tour des " + ("Noirs" if self.tour_noir else "Blancs") + ") : \n")
                else:
                    texte = "ERREUR (Format: play caseSrc caseDst). C'est au tour des " + ("Noirs" if self.tour_noir else "Blancs") + "\n"
                    self.file.write(texte)

            elif cmd == "leave":
                self.file.write("Au revoir !\n")
                fini = True

            elif cmd == "replay":
                print("A faire")

            elif cmd == "new":
                print("A faire")
                # self.joueur1 = Joueur(pseudo_blanc, est_noir=False)
                # self.joueur2 = Joueur(pseudo_noir, est_noir=True)

            else:
                texte = "ERREUR Commande inconnue. C'est au tour des " + ("Noirs" if self.tour_noir else "Blancs") + "\n"
                self.file.write(texte)
            
            self.file.flush()

        print("Fermeture de la session actuelle...")
        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()