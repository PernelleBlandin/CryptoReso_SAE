import socket
import constantes
from session import *


class Serveur:
   def __init__(self):
       self.counter = 0
       self.clients = []


   def mainServeur(self, port):
       sock= socket.socket()
       sock.bind(("0.0.0.0", port))
       sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       sock.listen(10)
       sock.settimeout(1.0)
       
       print(f"Serveur en écoute sur le port {port}. Appuyez sur Ctrl+C pour l'arrêter.\n")
       
       try:
           while True:
               try:
                   cli, addr = sock.accept()
                   sess = Session(self, cli)
                   sess.mainSession()
               except socket.timeout:
                   continue

       except KeyboardInterrupt:
           print("\nArrêt du serveur en cours...")

       finally:
           sock.close()
           print("Serveur fermé.")


if __name__ == "__main__":
   Serveur().mainServeur(constantes.PORT)