import socket, time
import constantes
from threading import Thread
import threading

class Client:
    def __init__(self, host:str, port:int):
        self.sock = socket.socket()
        self.sock.connect((host, port))
        self.f_ecriture = self.sock.makefile(mode="rw", encoding="utf-8")
        self.f_lecture = self.sock.makefile(mode="r", encoding="utf-8")
        self.running = True
        self.entree = None

    def lancer(self):
        thread_envois = Thread(target=self.recuperer_envois)
        thread_envois.start()
        print("on continue !")
        thread_entrees = Thread(target=self.recuperer_entree)
        thread_entrees.start()
        print("on continue !")

    def fermer(self):
        if self.running:
            self.running = False
            try:
                self.sock.shutdown(socket.SHUT_RDWR)
            except:
                pass
            try:
                self.sock.close()
            except:
                pass

    def recuperer_envois(self):
        print(threading.active_count())
        while self.running:
            try:
                recu = self.f_lecture.readline() # interrompt
                if recu == "" :
                    print("Connexion fermée par le serveur.")
                    self.running = False
                    break

                recu = recu.strip()
                if recu:
                    print(recu)

                if recu.strip().lower() == "quit":
                    self.running = False
                    break
            except:
                break
            #print(self.f_lecture.read())
            
        self.fermer()

    def recuperer_entree(self):
        print(threading.active_count())
        print(" Connecté au serveur. Tapez 'register/connect pseudo mdp' (ou 'quit' pour quitter) :")
        while self.running:
            try:
                self.entree = input() # interrompt
                if not self.entree:
                    continue
                if self.running:
                    self.f_ecriture.write(self.entree+"\n")
                    self.f_ecriture.flush()

                if self.entree.strip().lower() == "quit":
                    self.running = False
                    break
            except:
                break
            #time.sleep(1)
        self.fermer()
            


client = Client(constantes.IP, constantes.PORT)
client.lancer()
