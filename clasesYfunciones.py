import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def dormir():
    logging.info("empezando desde funcion")
    time.sleep(1)
    logging.info("finalizando desde funcion")

t1 = threading.Thread(target=dormir , name= "tread desde funcion")
t1.start()

class Unthread(threading.Thread): 
    #Entre los parentesis va la superclase de la que hereda.
    def __init__(self):
        super().__init__() # inicializa el init de la super clase
        self.name= "threadClase"

    def run(self):
        logging.info("empezando desde clase")
        time.sleep(1)
        logging.info("finalizando desde clase")

t2 = Unthread() # Para hacer un objeto nuevo es RECOMENDADO copiar y pegar nombre de la clase, XQ ? no se , pero anda. 
t2.start() 
#Esto se ejecuta llamando al run de la clase .Si no hay run , no hace nada.

"""
ESTE ES EL CODIGO DEL PROFE, HACE LO MISMO QUE EL MIO
def dormir():
    logging.info('Empenzado')
    time.sleep(1)
    logging.info('Finalizado')

class UnThread(threading.Thread):
    def __init__(self):
        super().__init__() 
        self.name = 'threadClase'

    def run(self):
        logging.info('Empezando')
        time.sleep(1)
        logging.info('Finalizado')

logging.info('Creando thread desde una función')
threadFunc = threading.Thread(target=dormir, name='thread desde una función')

logging.info('Creando thread desde una clase')
threadObj = UnThread()

logging.info('Lanzando los threads')
threadFunc.start()
threadObj.start()

"""