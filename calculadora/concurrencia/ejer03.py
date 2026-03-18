import threading

def tarea(letra):
    for _ in range(4):
        print(letra)

letras =  ['A', 'B', 'C', 'D', 'E' , 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
hilos = []

for letra in letras:
    hilo = threading.Thread(target=tarea, args=(letra,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join() 