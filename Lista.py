from Viajero import ViajeroFrecuente
import csv
class lista():
	__indice=[]

	def __init__ (self):
		self.__indice=[]
	def agregar(self):
		archivo=open("Prueba.csv","r")
		reader=csv.reader(archivo,delimiter=';')
		bandera=False
		for fila in reader:
			if bandera==False:
				bandera=True
			else:
				unviajero=ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
				self.__indice.append(unviajero)
		archivo.close()
		return self.__indice
	def consultar(self, Po):
		i=0
		while self.__indice[i].getnumber()!=Po and i<=len (self.__indice):
			i=i+1
		if i>len (self.__indice):
			print ("Error")
		else:
			return i
	def Millas(self,o):
		return self.__indice[o].cantidadTotaldeMillas()
	def mostrarT(self):
		for unviajero in self.__indice:
			print (unviajero)
	def acumular(self, millas, o):
		return(self.__indice[o].acumularMillas(millas))
	def canjear (self,o,c):
		return(self.__indice[o].canjearMillas(c))
	def mostrar (self,o):
		print( self.__indice[o])

