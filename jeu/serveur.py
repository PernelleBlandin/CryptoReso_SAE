import socket 
import constantes
from session import *
from GestionnaireDeSessions import GestionnaireDeSessions

class Serveur:

    def __init__(self, host, port):
        self.counter += 0
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.listen(10)
        self.gestionnaire = GestionnaireDeSessions(host, port)

    def mainServeur(self):
        while True:
            cli, _ = self.sock.accept()
            self.counter += 1
            session = self.gestionnaire.creer_session("client n°" + self.counter)
            print(self.counter)

if __name__ == "__main__":
    Serveur(constantes.IP, constantes.PORT).mainServeur()