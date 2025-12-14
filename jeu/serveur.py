from Jeu import * 
import socket 

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

    def mainSession(self):
        fini= False
        while not fini:
            line =self.file.readline().strip()
            print("Commande reçue : " + line)
        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

if __name__ == "__main__":
    #jouer = Jeu(None, None)
    #jouer.lancer()
    Serveur().mainServeur(5555)