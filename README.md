# fumadores

El link a este repositorio es [github](https://github.com/GonzaloGmv/fumadores)

En este proyecto se ha resuelto el problema de los fumadores. Lo he resuelto representando cada ingrediente como un semaforo, aunque esto alguna vez puede hace que se bloquee el programa.

El código es el siguiente:

### Fumadores

```
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
```

### Lanzador
```
from fumadores import *

def main():
    hilos_fumadores = []
    for i in range(5):
        hilo = threading.Thread(target=fumador, args=(i,))
        hilos_fumadores.append(hilo)

    hilo_agente = threading.Thread(target=agente)

    for hilo in hilos_fumadores:
        hilo.start()

    hilo_agente.start()

    for hilo in hilos_fumadores:
        hilo.join()

    hilo_agente.join()
```

### Main
```
from lanzador import main

if __name__ == '__main__':
    main()
```    
