from Menu import menu

if __name__ == '__main__':
	unmenu=menu()
	Po = int(input("Ingrese el numero del viajero\n"))
	while (Po > 4 or Po < 1):
		print("Error Numero no valido\n")
		Po = int(input("Ingrese el numero del viajero\n"))
	op = int(input ("Seleccione la opcion deseada\n 1-Consultar Cantidad de Millas\n 2-Acumular Millas\n 3-Canjear Millas\n 4-Mostrar Datos\n 5-Mostrar Todo\n 6-Salir\n"))
	while (op!= 6):
		unmenu.manejador(Po,op)
		op = int(input ("Seleccione la opcion deseada\n 1-Consultar Cantidad de Millas\n 2-Acumular Millas\n 3-Canjear Millas\n 4-Mostrar Datos\n 5-Mostrar Todo\n 6-Salir\n"))
