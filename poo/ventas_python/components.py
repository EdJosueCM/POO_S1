
from utilities import borrarPantalla, gotoxy
import time

class Menu:
    def __init__(self, titulo="", opciones=[], col=6, fil=1):
        self.titulo = titulo
        self.opciones = opciones
        self.col = col
        self.fil = fil

    def menu(self):
        max_longitud_opcion = max(len(opcion) for opcion in self.opciones)
        longitud_marco = max(len(self.titulo), max_longitud_opcion) + 4 
        marco_superior = "\033[0;34m*" + "-" * (longitud_marco + 2) + "*\033[0m"
        titulo_centralizado = f"\033[0;34m* {self.titulo.center(longitud_marco)} *\033[0m"
        print(marco_superior)
        print(titulo_centralizado)

        for opcion in self.opciones:
            print(f"\033[0;34m* {opcion.ljust(longitud_marco)} *\033[0m")

        print(marco_superior)

        opc = input(f"Elija opción[1...{len(self.opciones)}]: ")
        return opc
    

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor

    def solo_letras(self,mensaje,mensajeError): 
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor
    
    def cedula():
        pass
    
class otra:
    pass    

if __name__ == '__main__':
    # instanciar el menu
    opciones_menu = ["1. Entero", "2. Letra", "3. Decimal"]
    menu = Menu(titulo="-- Mi Menú --", opciones=opciones_menu, col=10, fil=5)
    # llamada al menu
    opcion_elegida = menu.menu()
    print("Opción escogida:", opcion_elegida)
    valida = Valida()
    if(opciones_menu==1):
      numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
      print("Número validado:", numero_validado)
    
    numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
    print("Número validado:", numero_validado)
    
    letra_validada = valida.solo_letras("Ingrese una letra:", "Mensaje de error")
    print("Letra validada:", letra_validada)
    
    decimal_validado = valida.solo_decimales("Ingrese un decimal:", "Mensaje de error")
    print("Decimal validado:", decimal_validado)