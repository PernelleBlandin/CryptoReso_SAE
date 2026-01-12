from threading import Thread
from io import TextIOWrapper
from Jeu import * 
import socket 

class Session(Thread):
    def __init__(self, file:TextIOWrapper):
        self.file=file

    def communiquer(self):
        while True:
            if mess == "quit":
                break
            recu = self.file.readline.strip()
            mess = input(recu)
            self.file.write(mess + "\n")
            self.file.flush()
        self.file.close()






"""
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
                self.file.write("Donner un nom pour le joueur Noir : " + "\n")
                self.file.flush()
                pseudoNoir = self.file.readline().strip()
                self.joueur2 = Joueur(pseudoNoir, True)

            self.file.write("Début de la partie..." + "\n")
            self.file.flush()
            line = self.file.readline().strip()
            print("Commande reçue : " + line)
            if line == "quit":
                fini = True
        print("Fermeture de la session actuelle...")
        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()"""