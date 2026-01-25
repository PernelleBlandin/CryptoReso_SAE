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

import asyncio
async def coroutine1():
    print("Début de la coroutine 1")
    await asyncio.sleep(2)
    print("Fin de la coroutine 1")

async def coroutine2():
    print("Début de la coroutine 2")
    await coroutine1()
    print("Fin de la coroutine 2")

async def main():
    print("Début du programme principal")
    await coroutine2()
    print("Fin du programme principal")

asyncio.run(main())