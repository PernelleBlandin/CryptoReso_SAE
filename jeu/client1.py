import socket, time
import constantes
from threading import Thread
import threading

class Client:
    def __init__(self, host:str, port:int):
        self.sock = socket.socket()
        self.sock.connect((host, port))
        self.f_ecriture = self.sock.makefile(mode="rw")
        self.f_lecture = self.sock.makefile(mode="r")
        self.running = True
        self.entree = None

    def lancer(self):
        thread_envois = Thread(target=self.recuperer_envois)
        thread_envois.start()
        print("on continue !")
        thread_entrees = Thread(target=self.recuperer_entree)
        thread_entrees.start()
        print("on continue !")

    def recuperer_envois(self):
        print(threading.active_count())
        while self.running:
            recu = "rien" #self.f_lecture.readline().strip() # interrompt
            print(recu, end="") 
            time.sleep(1)
        self.f_lecture.close()
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        self.running = False
        

    def recuperer_entree(self):
        print(threading.active_count())
        while self.running:
            self.entree = input() # interrompt
            #if self.entree is not None:
            #    self.f_ecriture.write(self.entree+"\n")
            #    self.f_ecriture.flush()
            #elif self.entree == "quit":
            #    self.running = False
            time.sleep(1)
        self.f_ecriture.close()
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        self.running = False
            


client = Client(constantes.IP, constantes.PORT)
client.lancer()
