import socket
import constantes


def client(host:str, port:int):
    sock = socket.socket()
    sock.connect((host, port))
    f = sock.makefile(mode="rw", encoding="utf-8")


    mess = ""
    while True:
        try:
            line = f.readline()
            if not line:
                break
            
            if line.strip().lower() == "exit":
                print("\n[SERVEUR] Fin de partie non prévue (Erreur serveur)")
                break

            if ":" in line or "tour des" in line:
                mess = input(line.strip() + " ").strip()
                f.write(mess + "\n")
                f.flush()
                
                if mess.lower() in ["quit", "leave"]:
                    response = f.readline()  # Attendre la réponse du serveur
                    print(response, end="")
                    break
            else:
                print(line, end="")
        except Exception as e:
            print(f"Erreur de connexion: {e}")
            break

    
    f.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print("Connexion fermée.")



client(constantes.IP, constantes.PORT)
