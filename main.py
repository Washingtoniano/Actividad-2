from Menu import menu

if __name__ == '__main__':
    unmenu=menu()
    Po = int(input("Ingrese el numero del viajero\n"))
    while Po > 4 or Po < 1:
        print("Error Numero no valido\n")
        Po = int(input("Ingrese el numero del viajero\n"))
    op = str(input ("Seleccione la opcion deseada\n a-Consultar Cantidad de Millas\n b-Acumular Millas\n c-Canjear Millas\n d-Mostrar Datos\n e-Salir\n"))
    while (op!= 'e'):
        unmenu.manejador(Po,op)
        op = str(input ("Seleccione la opcion deseada\n a-Consultar Cantidad de Millas\n b-Acumular Millas\n c-Canjear Millas\n d-Mostrar Datos\n"))

