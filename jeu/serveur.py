import socket
import constantes
from session import *
from threading import Thread


class Serveur:
   def __init__(self):
       self.counter = 0
       self.sessions_connectees = set()


   def mainServeur(self, port):
       sock= socket.socket()
       sock.bind(("0.0.0.0", port))
       sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       sock.listen(10)
       while True:
           cli, _ = sock.accept()
           sess = Session(self, cli)
           self.sessions_connectees.add(sess)
           t = Thread(target=sess.mainSession)
           t.start()
           print("au prochain")


if __name__ == "__main__":
   Serveur().mainServeur(constantes.PORT)
