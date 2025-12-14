import socket
import constantes

def client(host, port):
    sock = socket.socket()
    sock.connect((host, port))
    f = sock.makefile(mode="rw")

    mess = ""
    while True:
        print(mess)
        if mess == "quit": 
            break
        retour = f.readline().strip()
        print(retour)
        mess = input()
        f.write(mess + "\n")
        f.flush()

    f.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

client("localhost", constantes.PORT)
