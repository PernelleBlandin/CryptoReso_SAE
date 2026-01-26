import socket
import constantes
from session import *
from queue import Queue
from partie import *

class Serveur:
   def __init__(self):
       self.counter = 0
       self.sessions_connectees = set()
       self.sessions_en_attente = Queue(-1)

   def mettre_en_attente(self, session:Session):
    self.sessions_en_attente.put(session)
    if self.sessions_en_attente.qsize() > 1:
        joueurBlanc = self.sessions_en_attente.get()
        joueurNoir = self.sessions_en_attente.get()
        partie = Partie(joueurBlanc, joueurNoir)
        Thread(target=partie.lancer).start()

   def retirer_en_attente(self, session):
       self.sessions_en_attente.pop(session)

   def mainServeur(self, port):
       sock= socket.socket()
       sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       sock.bind(("0.0.0.0", port))
       sock.listen(10)
       try:
           while True:
               cli, _ = sock.accept()
               sess = Session(self, cli)
               self.sessions_connectees.add(sess)
               sess.start()
               print("Au prochain !")
       except KeyboardInterrupt:
           print("\nArrêt du serveur...")
           sock.close()

if __name__ == "__main__":
   Serveur().mainServeur(constantes.PORT)