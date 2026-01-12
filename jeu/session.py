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
                self.file.write("Donner un nom pour le joueur Noir : " + "\n")
                self.file.flush()
                pseudoNoir = self.file.readline().strip()
                self.joueur2 = Joueur(pseudoNoir, True)
                
                self.partie.joueur1 = self.joueur1
                self.partie.joueur2 = self.joueur2
                self.file.write("Début de la partie..." + "\n")
                self.file.flush()

            # On récupère les 3 parties de la commande
            line = self.file.readline().strip()
            parts = line.split()
            cmd = parts[0].lower()

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
            elif cmd == "play":
                if len(parts) == 3:
                    res = self.partie.valider_et_deplacer(parts[1], parts[2], self.tour_noir)
                    if res == "OK":
                        self.tour_noir = not self.tour_noir
                    self.file.write(res + "\n")
                else:
                    self.file.write("Format invalide (ex: a2 a4). Appuyez sur Entrée...\n")
                self.file.flush()
            else:
                self.file.write("ERREUR Commande inconnue\n")
                self.file.flush()

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