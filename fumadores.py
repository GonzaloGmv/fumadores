import threading
import time
import random


ingredientes = ["tabaco", "papel", "cerillas"]
mutex = threading.Semaphore(1)
semaforo = threading.Semaphore(0)
ingrediente_disponible = None

def fumador(id_fumador):
    global ingrediente_disponible
    while True:
        semaforo.acquire()
        mutex.acquire()
        if ingrediente_disponible == id_fumador:
            print("El fumador", id_fumador, "ha comenzado a fumar.")
            ingrediente_disponible = None
        mutex.release()
        time.sleep(1)  # Simulación de tiempo fumando
        mutex.acquire()
        print("El fumador", id_fumador, "ha terminado de fumar.")
        mutex.release()

def agente():
    global ingrediente_disponible
    while True:
        mutex.acquire()
        ingrediente_disponible = random.randint(0, 2)
        print("El agente ha puesto el", ingredientes[ingrediente_disponible], "sobre la mesa.")
        mutex.release()
        semaforo.release()