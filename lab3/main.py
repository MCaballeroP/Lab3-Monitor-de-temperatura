
from classes.Menu import *
from classes.Parametros import *
from classes.Serial import *
from classes.Reportes import *
from classes.Captura import *

def main():
    menu = Menu("Monitor de Temperatura")
    op = menu.ver()
    if op == "1":
        menu1 = Captura
        op1== menu1.ver()
        if op1 == "1":
            d = Datos()
            p.save()
        elif op1 == "2":
            g = Reportes
            p.save()
        else:
            print("Opcion invalida")
            main()
    elif op == "2":
        menu2 = Parametros()
        op1 == menu2.ver()
        if op1 == "1":
            h = controlh
            p.save()
        elif op1 == "2":
            n = controln()
            p.save()
        elif op1 == "3":
            f = controlf()
            p.save()
        else:
            print("Opcion invalida")
            main()
    elif op == "3"
        menu3 = Reportes()
        op1 == menu2.ver()
        if op1 == "1":
            g = Reportes
            p.save()
        elif op1 == "2":
            max = Datos()
            p.save()
        elif op1 == "3":
            min = Datos()
            p.save()
        elif op1 == "4":
            prom = Datos()
            p.save()
        else:
            print("Opcion invalida")
            main()
