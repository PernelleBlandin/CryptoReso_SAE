from Jeu import *
from Historique import enregistrer_partie
import socket
from threading import Thread
import time

class Session(Thread):
    def __init__(self, serveur, sock):
       super().__init__()
       self.serveur = serveur
       self.socket = sock
       self.file=sock.makefile(mode="rw", encoding="utf-8")
       self.counter = 0
       self.pseudo = None
       self.en_partie = True

    def envoyer_message(self, message):
        #print(message)
        self.file.write(message + "\n")
        self.file.flush()
        print(message + " ecrit")

    def recuperer_entree(self, message)->str:
        recu = ""
        self.file.write(message + "\n")
        self.file.flush()
        print(message + " demande")
        while recu == "":
            recu = self.file.readline().strip()
            print("toujours pas de line reçue..." + recu)
            #print("reçu : " + recu)
        return recu

    def fermer_session(self):
        self.file.close()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def run(self):
        line = None
        print("Mise en place d'une nouvelle session...")
        while True:
            try: 
                if self.pseudo == None:
                    self.pseudo = self.recuperer_entree("Choisissez un pseudo ")
                    

                while True:

                    self.en_partie = True
                    self.envoyer_message("Debut de la recherche d'un autre joueur...")
                    self.serveur.mettre_en_attente(self)
            try: 
                if self.pseudo == None:
                    self.pseudo = self.recuperer_entree("Choisissez un pseudo ")
                    

                while True:

                    self.en_partie = True
                    self.envoyer_message("Debut de la recherche d'un autre joueur...")
                    self.serveur.mettre_en_attente(self)

                    while self.en_partie:
                        time.sleep(1)
                        if self.socket._closed:
                            return
                    print(f"Le joueur {self.pseudo} repart pour une nouvelle recherche.")
                    
            except Exception as e:
                print(f"Erreur session : {e}")
            finally:
                self.fermer_session()

                    while self.en_partie:
                        time.sleep(1)
                        if self.socket._closed:
                            return
                    print(f"Le joueur {self.pseudo} repart pour une nouvelle recherche.")
                    
            except Exception as e:
                print(f"Erreur session : {e}")
            finally:
                self.fermer_session()

            if line == "quit":
                break