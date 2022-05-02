
from Lista import lista
class menu:
    __li=[]
    def __init__(self):
        self.__li=lista()
    def getopcion(self):
        return (self.__init__())
    def manejador(self,Po,op):
        if str.lower(op)=='a':
            self.opcion1(Po)
        elif (str.lower(op)=="b"):
            self.opcion2(Po)
        elif str.lower(op)=="c":
            self.opcion3(Po)
        elif str.lower (op)=='d':
            self.opcion4(Po)
        else:
            self.opcion5()
    def opcion1(self,Po):
        self.__li.consultar(Po)
    def opcion2(self,Po):
        M=int(input("Ingrese las millas a acumular\n"))
        self.__li.acumular(M,Po)
    def opcion3(self,Po):
        c=input("Cantidad a canjear\n")
        self.__li.canjear(Po,c)
    def opcion4(self,Po):
        self.__li.__indice[Po].mostrar
    def opcion5(self):
        self.__li.mostrar()
