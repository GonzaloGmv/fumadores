import threading
import time
import random

ingredientes = ["tabaco", "papel", "cerillas", "filtros", "green"]
mutex = threading.Semaphore(1)
semaforos_ingredientes = [threading.Semaphore(0) for _ in range(5)]

def fumador(id_fumador):
    while True:
        semaforos_ingredientes[id_fumador].acquire()
        mutex.acquire()
        print("El fumador", id_fumador, "ha comenzado a fumar.")
        mutex.release()
        time.sleep(1) 
        mutex.acquire()
        print("El fumador", id_fumador, "ha terminado de fumar.")
        mutex.release()

def agente():
    while True:
        mutex.acquire()
        ingredientes_disponibles = random.sample(range(5), 2)
        for i in ingredientes_disponibles:
            semaforos_ingredientes[i].release()
        mutex.release()
        time.sleep(1)