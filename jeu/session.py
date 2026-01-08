from Jeu import * 
from Historique import enregistrer_partie
import socket 

class Session:
    def __init__(self, serveur, sock):
        self.serveur = serveur
        self.socket = sock
        self.file=sock.makefile(mode="rw")
        self.counter = 0
        self.joueur1 = None
        self.joueur2 = None
        self.partie = Jeu(self.joueur1, self.joueur2)

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
            self.file.flush()
            
            resultat = self.partie.lancer_pour_serveur(self.file)
            
            pseudo_gagnant = self.partie.get_pseudo_gagnant(resultat, self.joueur1.pseudo, self.joueur2.pseudo)
            enregistrer_partie(self.joueur1.pseudo, self.joueur2.pseudo, pseudo_gagnant)

            line = self.file.readline().strip()
            print("Commande reçue : " + line)
            if line == "quit":
                fini = True
        print("Fermeture de la session actuelle...")
        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()