import socket 
import constantes
from session import *

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

if __name__ == "__main__":
    Serveur().mainServeur(constantes.PORT)