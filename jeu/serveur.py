import socket
import constantes
from session import *
from threading import Thread
from queue import Queue
from partie import *


class Serveur:
   def __init__(self):
       self.counter = 0
       self.sessions_connectees = set()
       self.sessions_en_attente = Queue(-1)

   def mettre_en_attente(self, session:Session):
       self.sessions_en_attente.put(session)
       while self.sessions_en_attente._qsize() > 1:
           #print("condition")
           joueurBlanc = self.sessions_en_attente.get_nowait()
           joueurNoir = self.sessions_en_attente.get_nowait()
           partie = Partie(joueurBlanc, joueurNoir)
           partie.lancer()

   def retirer_en_attente(self, session):
       self.sessions_en_attente.pop(session)

   def mainServeur(self, port):
       sock= socket.socket()
       sock.bind(("0.0.0.0", port))
       sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       sock.listen(10)
       while True:
           cli, _ = sock.accept()
           sess = Session(self, cli)
           self.sessions_connectees.add(sess)
           sess.start()
           print("Au prochain !")

if __name__ == "__main__":
   Serveur().mainServeur(constantes.PORT)
