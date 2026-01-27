import socket
import constantes


def client(host:str, port:int, commande:str):
    sock = socket.socket()
    sock.connect((host, port))
    f = sock.makefile(mode="rw", encoding="utf-8")

    f.write(commande + "\n")
    f.flush()

    mess = ""
    while True:
        line = f.readline()
        if not line:
            break
       
        ligne = line.strip()
        if ligne and (any(mot in ligne for mot in ["tour des", "Choisissez", "Attente"]) or ligne.endswith(":")):
            mess = input(ligne + " ")
            f.write(mess + "\n")
            f.flush()
            if mess.lower() == "quit":
               break
        else:
            print(ligne)
            parts = commande.split()
            cmd, pseudo, mdp = parts[0], parts[1], parts[2]

            if ligne == "ERR Le nom doit avoir entre 3 et 10 caractères sans espaces":
                nouveau_pseudo = input("Entrez un nouveau pseudo: ")
                commande = f"{cmd} {nouveau_pseudo} {mdp}"
                f.write(commande + "\n")
                f.flush()
                continue

            if ligne == "ERR Cet utilisateur existe déjà":
                nouveau_pseudo = input("Pseudo déjà pris. Entrez un autre pseudo: ")
                commande = f"{cmd} {nouveau_pseudo} {mdp}"
                f.write(commande + "\n")
                f.flush()
                continue

            if ligne == "ERR Le mot de passe doit avoir au moins 6 caractères":
                nouveau_mdp = input("Entrez un nouveau mot de passe: ")
                commande = f"{cmd} {pseudo} {nouveau_mdp}"
                f.write(commande + "\n")
                f.flush()
                continue

            if ligne in (
                "ERR Utilisateur non trouvé",
                "ERR Mot de passe incorrect",
            ):
                f.close()
                sock.shutdown(socket.SHUT_RDWR)
                sock.close()
                print("Connexion fermée.")
                return False
    return True
    



if __name__ == '__main__':
    while True:
        cmd = input('Tapez "register" pour vous inscrire ou "connect" pour vous connecter: ')
        if cmd not in ("register", "connect"):
            print("Commande non reconnue.")
            continue

        pseudo = input('Entrez votre pseudo: ')
        motdepasse = input('Entrez votre mot de passe: ')
        commande = f"{cmd} {pseudo} {motdepasse}"

        succes = client(constantes.IP, constantes.PORT, commande)

        if succes:
            break
        else:
            print("Réessayez.\n")
