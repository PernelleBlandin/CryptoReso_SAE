import socket
import constantes


def client(host:str, port:int):
   sock = socket.socket()
   sock.connect((host, port))
   f = sock.makefile(mode="rw")


   mess = ""
   while True:
       line = f.readline()
       if not line:
           break
       
       if ":" in line or "tour des" in line:
           mess = input(line.strip() + " ")
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
