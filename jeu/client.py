#! /usr/bin/python3

import socket
import constantes

def client(host, port): # On doit faire des entrées vide pour que les messages apparaissent
    sock = socket.socket()
    sock.connect((host, port))
    f = sock.makefile(mode="rw")
    entree = None
    while entree != "quit":
        entree = input("Attente d'une entrée...\n")
        f.write(entree+"\n")
        f.flush()
        print(f.readline(), end="")
    f.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

client(constantes.IP, constantes.PORT)