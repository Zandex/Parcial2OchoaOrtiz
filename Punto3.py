#!/usr/bin/python3 
from threading import Thread,Semaphore
import os
import time
import threading

Semaforo_descargue=Semaphore(2)

semaforo_p=Semaphore(3)
cont_pesado = 0
cont_descar = 1
l_caminones=[]

class Camion(Thread):
	def __init__(self,id,peso): #Constructor de la clase
		Thread.__init__(self)
		self.peso=peso
		self.id=id
		self.estado=0
#	def givepeso(self):
#		return self.peso
#	def giveid(self):
#		return self.id
#	def give_estado(self):
#		return self.estado
	
	def run(self):
		pesar(self.id,self.peso)
		print("-- Salio zona de pesado")
		descargue(self.id,self.peso)

def pesar(car,val):
	global cont_pesado	#donde se va a pesar
	print("++ El carro: "+ str(car) +" Esta en espera de Peso")
	semaforo_p.acquire()
	posini=cont_pesado
	posini=posini+1
	if posini>3 :
		posini=1
	cont_pesado=posini
	time.sleep(1)
	print("** El carro: "+ str(car) +" Fue atendido en:"+str(posini)+ " y Pesa: " + str(val))
	semaforo_p.release()

def descargue(car,val):
	global cont_descar	#donde se va a pesar
	Semaforo_descargue.acquire()
	print("** El carro: "+ str(car) +" Esta en espera de Descargue")
	posini=cont_descar
	posini=cont_descar+3
	if posini>4 :
		posini=1
	cont_descar=posini

	time.sleep(3)
	print("++ El carro: "+ str(car) +" Fue Descargado en:"+str(posini)+ " y Pesa: " + str(val))
	Semaforo_descargue.release()

def main():
	global l_caminones
	l_caminones=[Camion(1,54),Camion(2,22),Camion(3,45),Camion(4,67),Camion(5,43)]
	for h in l_caminones:
		h.start()
main()