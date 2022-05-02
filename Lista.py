from Viajero import ViajeroFrecuente
import csv
class lista():
	__indice=[]

	def __init__ (self):
		self.__indice=[]

	def agregar(self):
		archivo =  open ("Prueba.csv")
		reader= csv.reader (archivo,delimiter=';')
		bandera=True
		for fila in reader:
			if bandera==True:
				#Saltear Cabecera
				bandera=False
			else:
				num=int(fila[0])
				DNI=int (fila[1])
				nom=str(fila[2])
				ap=str(fila[3])
				mi=float(fila[4])
				unviajero=ViajeroFrecuente(num,DNI,nom,ap,mi)
				self.__indice.append(unviajero)
		archivo.close()
	def consultar(self, Po):
		#i=1
		for unviajero in (self.__indice):
			if (unviajero.getnumber()==Po):
				unviajero.cantidadTotaldeMillas()
			else:
				print ("error")

	def mostrar(self):
		for unviajero in self.__indice:
			print (unviajero)
	def acumular(self, millas, Po):
		self.__indice(Po).acumularMillas(millas)
	def canjear (self,Po,c):
		self.__indice(Po).canjearMillas(c)
