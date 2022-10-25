
class Menu:
    def __init__(self,lab3):
        self.lab3=lab3

    def ver(self):
        print("Bienvenido Al Sistema".center(20,"*")) 
        print("Monitor de temperatura:" + self.lab3)
        print("1. Captura de datos ")
        print("2. Configuracion de parametros ")
        print("3. Reportes")
        op=input(">>>")
        
        return op

class Captura:
    def ver(self):
        print("Por favor escoja alguna de las opciones".center(20,"*"))
        print("1. Escoger cantidad de datos")
        print("2. grafica en tiempo real")
        op = input(">>>")

        return op

class Parametros:
    def ver(self):
        print("Por favor escoja alguna de las opciones".center(20, "*"))
        print("1. Definir rango de temperatura para hipotermia")
        print("2. Definir rango de temperatura normal")
        print("3. Definir rango de temperatura para fiebre")
        op = input(">>>")

        return op

class Reportes:
    def ver(self):
        print("Por favor escoja alguna de las opciones".center(20, "*"))
        print("1. Gráfica de los datos capturados")
        print("2. Valor maximo de temperatura")
        print("3. Valor minimo de temperatura")
        print("4. Promedio de temperatura")
        op = input(">>>")

        return op