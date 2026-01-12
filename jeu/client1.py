import socket
import constantes


def client1(host:str, port:int):
   sock = socket.socket()
   sock.connect((host, port))
   f = sock.makefile(mode="rw")


   mess = ""
   while True:
       if mess == "quit":
           break
       retour = f.readline().strip()
       mess = input(retour)
       f.write(mess + "\n")
       f.flush()


   f.close()
   sock.shutdown(socket.SHUT_RDWR)
   sock.close()


client1(constantes.IP, constantes.PORT)
