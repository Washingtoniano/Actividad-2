from Leer import leer
from Lista import lista
def menu (Pos):

    print("Seleccione la opcion deseada\n a-Consultar Cantidad de Millas\n b-Acumular Millas\n c-Canjear Millas\n d-Mostrar Datos\n")
    op = str(input ())



    if str.lower(op)=='a':
       lista(Pos)
    elif (str.lower(op)=="b"):

        M=input("Ingrese las millas a acumular\n")
        return(lista.__init__(Pos))

    elif str.lower(op)=="c":
        c=input("Cantidad a canjear\n")
        return(lista(Pos))
    elif str.lower (op)=='d':
       lista.mostrar()
    else:
        print("Error")
        menu(Pos)

