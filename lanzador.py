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