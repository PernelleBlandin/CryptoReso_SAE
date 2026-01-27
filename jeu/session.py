from Jeu import *
import socket
from threading import Thread
import json
import os



class Session(Thread):
    def __init__(self, serveur, sock):
       super().__init__()
       self.serveur = serveur
       self.socket = sock
       self.file=sock.makefile(mode="rw", encoding="utf-8")
       self.counter = 0
       self.pseudo = None

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

    def verifier_nom(self, nom):
        if len(nom) < 3 or len(nom) > 10:
            return False
        if ' ' in nom:
            return False
        return True
    

    def verifier_motdepasse(self, motdepasse):
        if len(motdepasse) < 6:
            return False
        return True


    def charger_users(self):
        if not os.path.exists('users.json'):
            return {}
        try:
            with open('users.json', 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}



    def sauvegarder_users(self, users):
        with open('users.json', 'w') as f:
            json.dump(users, f)

    def traiter_register(self, username, password):
        if not self.verifier_nom(username):
            return "ERR Le nom doit avoir entre 3 et 10 caractères sans espaces"
        if not self.verifier_motdepasse(password):
            return "ERR Le mot de passe doit avoir au moins 6 caractères"
        users = self.charger_users()
        if username in users:
            return "ERR Cet utilisateur existe déjà"
        users[username] = password
        self.sauvegarder_users(users)
        return "OK"


    def traiter_connect(self, username, password):
        users = self.charger_users()
        if username not in users:
            return "ERR Utilisateur non trouvé"
        
        if users[username] != password:
            return "ERR Mot de passe incorrect"
        
        return "OK"

    def run(self):
        print("Mise en place d'une nouvelle session...")
        authentifie = False
        while not authentifie:
            commande = self.file.readline().strip()
            print(f"Commande reçue : {commande}")
            
            if not commande:
                self.envoyer_message("ERR Commande requise")
                continue
            
            parts = commande.split()
            
            if len(parts) < 3:
                self.envoyer_message("ERR Format invalide")
                continue
            
            cmd = parts[0].lower()
            username = parts[1]
            password = parts[2]
            
            if cmd == "register":
                response = self.traiter_register(username, password)
                self.envoyer_message(response)
                if response == "OK":
                    self.pseudo = username
                    authentifie = True
                    
            elif cmd == "connect":
                response = self.traiter_connect(username, password)
                self.envoyer_message(response)
                if response == "OK":
                    self.pseudo = username
                    authentifie = True
                    
            else:
                self.envoyer_message("ERR Commande inconnue (register ou connect)")

        print(f"Pseudo authentifié : {self.pseudo}")
        self.envoyer_message("Debut de la recherche d'un joueur...")
        self.serveur.mettre_en_attente(self)
 