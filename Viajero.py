class ViajeroFrecuente():
    __numero = 0
    __DNI = 0
    __nombre = ""
    __apellido = ""
    __millasacum = 0.0
    def __init__(self,numero,DNI,nombre,apellido,millasacum):
        self.__numero = int(numero)
        self.__DNI = int(DNI)
        self.__nombre = str (nombre)
        self.__apellido = str (apellido)
        self.__millasacum = float (millasacum)
    def cantidadTotaldeMillas (self) :
        return( self.__millasacum)
    def acumularMillas (self , millas) :
        self.__millasacum = (millas+self.__millasacum)
        return (self.__millasacum)
    def canjearMillas (self , cant_a_canj):
        if cant_a_canj <= self.__millasacum:
            return self.__millasacum - cant_a_canj
        else:
            print ("Error")
    def getnumber (self):
        return self.__numero

    def __str__(self):
        return ("Numero:{}--DNI:{}--Nombre:{}--Apellido:{}--Millas:{}".format(self.__numero,self.__DNI,self.__nombre,self.__apellido,self.__millasacum))
