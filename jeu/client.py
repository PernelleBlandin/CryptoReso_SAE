import socket

def client(host, port):
    sock= socket.socket()
    sock.connect((host, port))
    f= sock.makefile(mode="rw")

    mess = ""
    while True:
        mess = input('Entrez votre message ("quit" pour quitter) -> ') + "\n"
        f.write(mess)
        f.flush()
        if mess == "quit\n": 
            break

    f.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

client("localhost", 5555)
