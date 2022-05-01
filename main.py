import Menu
import Leer
import Lista

if __name__ == '__main__':
	Leer.leer()
	Pos = int(input("Ingrese el numero del viajero\n"))
	while Pos > 4 or Pos < 1:
		print("Error Numero no valido\n")
		Pos = int(input("Ingrese el numero del viajero\n"))
	Menu.menu(Pos)
