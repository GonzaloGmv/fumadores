import threading
import time
import random


ingredientes = ["tabaco", "papel", "cerillas", "filtros", "green"]
mutex = threading.Semaphore(1)
semaforo = threading.Semaphore(0)
ingrediente_disponible = None

def fumador(id_fumador):
    while True:
        semaforo.acquire()
        print("El fumador", id_fumador, "ha comenzado a fumar.")
        time.sleep(1)  # Simulación de tiempo fumando
        print("El fumador", id_fumador, "ha terminado de fumar.")

# Función para el agente
def agente():
    while True:
        mutex.acquire()
        ingrediente_disponible = random.randint(0, 4)
        print("El agente ha puesto el", ingredientes[ingrediente_disponible], "sobre la mesa.")
        mutex.release()
        semaforo.release()