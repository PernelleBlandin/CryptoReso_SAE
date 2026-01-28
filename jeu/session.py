from Jeu import *
import socket
from threading import Thread



class Session(Thread):
    def __init__(self, serveur, sock):
       super().__init__()
       self.serveur = serveur
       self.socket = sock
       self.file=sock.makefile(mode="rw", encoding="utf-8")
       self.counter = 0
       self.pseudo = None

    def envoyer_message(self, message):
        #print(message)
        self.file.write(message + "\n")
        self.file.flush()
        print(message + " ecrit")

    def recuperer_entree(self, message)->str:
        recu = ""
        self.file.write(message + "\n")
        self.file.flush()
        print(message + " demande")
        while recu == "":
            line = self.file.readline()
            if not line: # Déconnexion du socket
                return "quit"
            recu = line.strip()
            print("toujours pas de line reçue..." + recu)
        return recu

    def fermer_session(self):
        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def run(self):
        line = None
        print("Mise en place d'une nouvelle session...")
        while True:
            if self.pseudo == None:
               #print("entree ici")
               self.pseudo = self.recuperer_entree("Choisissez un pseudo ")
               self.envoyer_message("Debut de la recherche d'un joueur...")
               self.serveur.mettre_en_attente(self)

            if line == "quit":
                break
