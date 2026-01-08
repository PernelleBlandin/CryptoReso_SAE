import socket
import constantes
from serveur import serveur
from session import session

def client2(host:str, port:int):
    sock = socket.socket()
    sock.connect((host, port))
    f = sock.makefile(mode="rw")

    mess = ""
    while True:
        mess = input()
        if mess == "play":
            session.play()
            print(f"Deplacement de {case_src} à {case_dest}")


        elif mess == "quit": 
            break
        retour = f.readline().strip()
        mess = input(retour)
        f.write(mess + "\n")
        f.flush()

    f.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

client2(constantes.IP, constantes.PORT)
