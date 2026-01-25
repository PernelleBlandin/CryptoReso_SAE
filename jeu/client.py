import socket
import constantes


def client(host:str, port:int):
   sock = socket.socket()
   sock.connect((host, port))
   f = sock.makefile(mode="rw", encoding="utf-8")


   mess = ""
   while True:
       line = f.readline()
       if not line:
           break
       
       ligne = line.strip()
       if ligne and any(mot in ligne for mot in [":", "tour des", "Choisissez", "Attente"]):
           mess = input(ligne + " ")
           f.write(mess + "\n")
           f.flush()
           if mess.lower() in ["quit", "leave"]:
               break
       else:
           print(line, end="")


   f.close()
   sock.shutdown(socket.SHUT_RDWR)
   sock.close()


client(constantes.IP, constantes.PORT)
