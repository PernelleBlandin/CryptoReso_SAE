import threading, time

def boucle():
    while True:
        time.sleep(1)
        print("hello")

def boucle2():
    time.sleep(2)
    result = input("Je demande : ")
    print(result)

t = threading.Thread(target=boucle)
t.start()
t2 = threading.Thread(target=boucle2)
t2.start()