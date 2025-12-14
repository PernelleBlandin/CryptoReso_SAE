from Jeu import * 
import socket 
import constantes

class Serveur:
    def __init__(self):
        self.counter = 0

    def mainServeur(self, port):
        sock= socket.socket()
        sock.bind(("0.0.0.0", port))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.listen(10)
        while True:
            cli, _ = sock.accept()
            sess= Session(self, cli)
            sess.mainSession()

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
                print("là")
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
        self.socket.close()

if __name__ == "__main__":
    #jouer = Jeu(None, None)
    #jouer.lancer()
    Serveur().mainServeur(constantes.PORT)