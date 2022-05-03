from Lista import lista
class menu:
    __li=lista()
    def __init__(self):
        self.__li=lista()
    def manejador(self,Po,op):
        self.__li.agregar()
        o=self.__li.consultar(Po)
        if (op)==1:
            self.opcion1(o)
        elif (op)==2:
            self.opcion2(o)
        elif (op)==3:
            self.opcion3(o)
        elif (op)==4:
            self.opcion4(o)
        else:
            self.opcion5()
    def opcion1(self,o):
        print(self.__li.Millas(o))
    def opcion2(self,o):
        M=int(input("Ingrese las millas a acumular\n"))
        print (self.__li.acumular(M,o))
    def opcion3(self,o):
        c=float(input("Cantidad a canjear\n"))
        print(self.__li.canjear(o,c))
    def opcion4(self,o):
        print (self.__li.mostrar(o))
    def opcion5(self):
         (self.__li.mostrarT())
