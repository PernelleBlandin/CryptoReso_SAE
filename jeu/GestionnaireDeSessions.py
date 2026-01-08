import socket
import constantes
from session import Session

class GestionnaireDeSessions:
    def __init__(self, host:str, port:int):
        self.sock = socket.socket()
        self.sock.connect((host, port))
        self.lstSessions = dict()
        #f = self.sock.makefile()

    def creer_session(self, nom_client:str)->Session:
        f = self.sock.makefile()
        sessionClient = Session(f)
        self.lstSessions[nom_client] = sessionClient

        sessionClient.communiquer()
        f.write("Bienvenue dans la session !")
        f.flush()
        return sessionClient
