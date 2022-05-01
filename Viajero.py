class ViajeroFrecuente:
    __numero = 0
    __DNI = 0
    __nombre = 0
    __apellido = 0
    __millasacum = 0
    def __init__(self,numero,DNI,nombre,apellido,millasacum):
        self.__numero = int(numero)
        self.__DNI = int (DNI)
        self.__nombre = str (nombre)
        self.__apellido = str (apellido)
        self.__millasacum = int (millasacum)
    def cantidadTotaldeMillas (self) :
        return self.__millasacum
    def acumularMillas (self , millas) :
        self.__millasacum = (millas+self.__millasacum)
        return self.__millasacum
    def canjearMillas (self , cant_a_canj):
        if cant_a_canj <= self.__millasacum:
            return self.__millasacum - cant_a_canj
        else:
            return "Error"
    def getnumber (self):
        return self.__numero
    def mostrar (self):
        print ("Nombre:" ,self.__nombre )
        print ("Apellido:",self.__apellido)

