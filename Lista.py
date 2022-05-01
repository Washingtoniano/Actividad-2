import Viajero
class lista():
	__indice=[Viajero.ViajeroFrecuente]
	def __init__ (self):
		self.__indice=[]
	def agregar(self, unviajero):
		self.__indice.append(self, unviajero)
	def buscar(self, Pos):
		for cant in range (self.__indice):
			if Viajero.ViajeroFrecuente.getnumber == Pos:
				return cant
	def mostrar(self):
		for Viajero in self.__indice:
			Viajero.Mostrar()
