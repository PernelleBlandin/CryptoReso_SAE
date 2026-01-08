from Jeu import * 
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
            line =self.file.readline().strip()

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

            else:
                self.file.write("err\n")
                self.file.flush()

        print("Fermeture de la session actuelle...")
        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()