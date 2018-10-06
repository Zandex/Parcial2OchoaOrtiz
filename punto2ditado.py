#!/usr/bin/python3 
from threading import Thread,Semaphore
import os
import time
import threading
 
semaforo_productor_consumidor = Semaphore(0); #Crear variable semáforo
#semaforo_consumidor_productor = Semaphore(3);
semáforo_buffer=Semaphore(1)
pid = -1
time1=2
time2=1


def fproductor(id):
	global pid 		
	time.sleep(time1)	#produce
	semáforo_buffer.acquire()	#Espera buffer
	pid=id				#pasar proceso
	semaforo_productor_consumidor.release()	#Permite consumir

def fconsumidor():
	semaforo_productor_consumidor.acquire()	#esperando a que produscan
	pidcopy = pid				#Toma buffe
	#print("hay: "+str(pid))
	semáforo_buffer.release()	#suelta buffer
	time.sleep(time2)
	print ("Se consumio: "+str(pidcopy))


class Productor(Thread):
	def __init__(self,id): #Constructor de la clase
		Thread.__init__(self)
		#self.id=threading.get_ident()
		self.id=id

	def run(self):
		fproductor(self.id)

class Consumidor(Thread):
	def __init__(self): #Constructor de la clase
         Thread.__init__(self)
         
	def run(self):
		fconsumidor()

def main():
	l_productores=[Productor(1),Productor(2),Productor(3)]
	l_consumidores=[Consumidor(),Consumidor(),Consumidor()]

	semáforo_buffer.release()

	for h in l_productores:
		h.start()	
	for x in l_consumidores:
		x.start()

main()
