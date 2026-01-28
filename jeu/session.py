from Jeu import *
from Historique import enregistrer_partie
import socket
from threading import Thread
import json
import os
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
        try:
            #print(message)
            self.file.write(message + "\n")
            self.file.flush()
            print(message + " ecrit")
            return True
        except:
            print("Erreur envoi message")
            return False

    def recuperer_entree(self, message)->str:
        try:
            recu = ""
            self.file.write(message + "\n")
            self.file.flush()
            recu = self.file.readline().strip()
            print(message + " demande")
            if recu:
                return recu
            else:
                return "quit"
        except:
            return "quit"


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


    def _get_users_path(self):
        base = os.path.dirname(__file__)
        return os.path.abspath(os.path.join(base, 'users.json'))

    def charger_users(self):
        path = self._get_users_path()
        if not os.path.exists(path):
            return {}
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}



    def sauvegarder_users(self, users):
        path = self._get_users_path()
        with open(path, 'w') as f:
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
        self.envoyer_message("Bienvenue ! Connectez-vous avec 'connect <pseudo> <mdp>' ou créez un compte avec 'register <pseudo> <mdp>'")
        authentifie = False
        while not authentifie:
            try:
                commande = self.file.readline()
                if commande == "":
                    print("Client déconnecté")
                    break
                commande = commande.strip()
            except ConnectionAbortedError:
                print("Connexion interrompue")
                break
            print(f"Commande reçue : {commande}")
            
            if not commande:
                self.envoyer_message("ERR Commande requise")
                continue
            
            parts = commande.split()
            
            if len(parts) < 3 or len(parts) > 3:
                self.envoyer_message("ERR Format invalide. Utilisez: commande pseudo motdepasse")
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
 