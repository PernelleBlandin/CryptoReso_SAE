from Jeu import *
import socket
from threading import Thread


class Session(Thread):
    def __init__(self, serveur, sock):
       super().__init__()
       self.serveur = serveur
       self.socket = sock
       self.file=sock.makefile(mode="rw")
       self.counter = 0
       self.nom = None

    def envoyer_message(self, message):
        print(message)
        self.file.write(message + "\n")
        self.file.flush()
        print(message + " écrit")

    def recuperer_entree(self, message)->str:
        recu = ""
        self.file.write(message + "\n")
        self.file.flush()
        print(message + " demandé")
        while recu == "":
            recu = self.file.readline().strip()
            print("reçu : " + recu)
        return recu

    def run(self):
        line = None
        print("Mise en place d'une nouvelle session...")
        while True:
            if self.nom == None:
               print("entree ici")
               self.nom = self.recuperer_entree("Choisissez un pseudo ")
               self.envoyer_message("Début de la recherche d'un joueur...")
               self.serveur.mettre_en_attente(self)

            if line == "quit":
                break
            else:
                self.file.write("err\n")
                self.file.flush()
            #self.file.write("Hello I'm still here")
            #self.file.flush()

            line = self.file.readline().strip()
            print("hello")
            print("Ligne reçue : " + line)
            """
            elif self.joueur2 == None:
               self.file.write("Donner un nom pour le joueur Noir : " + "\n")
               self.file.flush()
               pseudoNoir = self.file.readline().strip()
               self.joueur2 = Joueur(pseudoNoir, True)


            line = self.file.readline().strip()
            self.file.write("Début de la partie..." + "\n")
            self.file.flush()


            print("Commande reçue : " + line)

            if line == "register":
                print("Pseudo du joueur Blanc : ")
                # envoie au joueur 1 sur client1
                

                
            if line == "connect":
                print("A faire")
                print("Votre pseudo : ")
                print("Votre mot de passe : ")
                

            elif line == "play":
                self.file.write()
                self.file.flush()

            elif line == "leave":
                self.file.write("leave\n")
                self.file.flush()
                break

            elif line == "quit":
                fini = True

            if line == "replay":
                print("A faire")

            if line == "new":
                print("A faire")
                # self.joueur1 = Joueur(pseudo_blanc, est_noir=False)
                # self.joueur2 = Joueur(pseudo_noir, est_noir=True)
            """


        print("Fermeture de la session actuelle...")
        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
