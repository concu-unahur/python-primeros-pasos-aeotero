import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


numero = 1
lock = threading.Lock()

def sumarUno():
    global numero
    global lock
    lock.acquire()
    time.sleep(2)
    try:
        numero += 1
    finally:
        lock.release()

def multiplicarPorDos():
    global numero
    global lock
    lock.acquire()
    try:
        numero =numero *2
    finally:
        lock.release()

t1 = threading.Thread(target= sumarUno , name= "tread de suma")
logging.info
t1.start()
print (numero)
t2 = threading.Thread(target= multiplicarPorDos , name= "tread de multiplicacion")
t2.start()
print (numero)
time.sleep(2)
print(numero)

