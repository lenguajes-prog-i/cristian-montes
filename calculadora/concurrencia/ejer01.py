import threading
import time

def programar():
    print("inicio 1")
    time.sleep(4)
    print("finalizado 1")


def beber_agua():
    print("inicio 2")
    time.sleep(6)
    print("finalizado 2")
    

def estudiar():
    print("inicio 3")
    time.sleep(4)
    print("finalizado 3")

inicio = time.perf_counter()

programar()
beber_agua()
estudiar()  

print(threading.active_count())   # activar el threading
print(threading.enumerate())      # activar el threading


fin = time.perf_counter()

tiempo = fin - inicio
print(tiempo)


# concurrencia
#programar()
#beber_agua()
#estudiar()


# Hilo 

inicio = time.perf_counter()

hilo_programar= threading.Thread(target=programar, args=())
hilo_programar.start()

hilo_beber_agua= threading.Thread(target=beber_agua, args=())
hilo_beber_agua.start()

hilo_estudiar = threading.Thread(target=estudiar, args=())
hilo_estudiar.start()


hilo_programar.join()
hilo_beber_agua.join()
hilo_estudiar.join()    



fin = time.perf_counter()

tiempo = fin - inicio
print(tiempo)
