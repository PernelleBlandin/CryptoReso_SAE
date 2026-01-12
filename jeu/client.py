import socket
import constantes

def client(host:str, port:int):
    sock = socket.socket()
    sock.connect((host, port))
    f = sock.makefile(mode="rw")

    mess = ""
    while True:
        retour = f.readline().strip()
        if not retour:
            break
        
        print(retour)
        mess = input("> ")
        f.write(mess + "\n")
        f.flush()
        if mess == "quit":
            break

    f.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

client(constantes.IP, constantes.PORT)
