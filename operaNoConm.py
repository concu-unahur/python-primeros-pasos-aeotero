import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


numero = 0

def sumarUno():
    global numero
    numero += 1

def multiplicarPorDos():
    global numero
    numero = numero * 2

t1 = threading.Thread(target= sumarUno , name= "tread de suma")
logging.info
t1.start()
print (numero)
t2 = threading.Thread(target= multiplicarPorDos , name= "tread de multiplicacion")
t2.start()
t3 = threading.Thread(target= multiplicarPorDos , name= "tread de multiplicacion")
t4 = threading.Thread(target= multiplicarPorDos , name= "tread de multiplicacion")
t5 = threading.Thread(target= multiplicarPorDos , name= "tread de multiplicacion")
t3.start()
t4.start()
t5.start()
print (numero)