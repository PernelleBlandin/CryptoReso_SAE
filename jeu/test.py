#import threading, time
#
#def boucle():
#    while True:
#        time.sleep(1)
#        print("hello")
#
#def boucle2():
#    time.sleep(2)
#    result = input("Je demande : ")
#    print(result)
#
#t = threading.Thread(target=boucle)
#t.start()
#t2 = threading.Thread(target=boucle2)
#t2.start()

# import asyncio
# async def coroutine1():
#     print("Début de la coroutine 1")
#     await asyncio.sleep(2)
#     print("Fin de la coroutine 1")
# 
# async def coroutine2():
#     print("Début de la coroutine 2")
#     await coroutine1()
#     print("Fin de la coroutine 2")
# 
# async def main():
#     print("Début du programme principal")
#     await coroutine2()
#     print("Fin du programme principal")
# 
# asyncio.run(main())

from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.fernet import Fernet
import base64

alice_private_key = x25519.X25519PrivateKey.generate()
alice_public_key = alice_private_key.public_key()

bob_private_key = x25519.X25519PrivateKey.generate()
bob_public_key = bob_private_key.public_key()

bob_shared_key = bob_private_key.exchange(alice_public_key)
alice_shared_key = alice_private_key.exchange(bob_public_key)

print(alice_shared_key == bob_shared_key)

# bob
codeur = Fernet(base64.urlsafe_b64encode(alice_shared_key))
encrypted = codeur.encrypt("message à décoder".encode())

print(encrypted)

# alice
decodeur = Fernet(base64.urlsafe_b64encode(bob_shared_key))
decrypted = decodeur.decrypt(encrypted).decode()

print(decrypted)

# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# f = Fernet(key)
# token = f.encrypt(b"A really secret message. Not for prying eyes.")
# f.decrypt(token)