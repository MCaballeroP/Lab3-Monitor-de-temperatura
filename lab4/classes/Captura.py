
import serial
import csv
import statistics
from datetime import *
import time

def Datos():
import serial

temperatura = []
print("Bienvenido")
print("La fecha de hoy es: ", date.today())
ndatos =int(input("Por favor ingresa el número de valores que deseas obtener del sensor de temperatura: "))
puerto = serial.Serial('COM3', 9600)
puerto.abrir()

for i in range(ndatos):
    dato = p.leer()
    print(dato)
    temperatura.append(float(dato))

print("Los", ndatos , "valores de temperatura que solicitaste son: ")
print(temperatura)

print("Guardando info en csv: ... ")
e = datetime.now()

datos = str(date.today())+str(e.hour)+str("_")+str(e.minute)+str("_")+str(e.second)+".csv"
f = open(ndatos, "w")
i = 0
for i in range (len(temperatura)):
    linea = ";".join([str(temperatura[i])])
    f.write(linea + "\n")
    i= i+1
f.write("el valor maximo encontrado fue: ")
f.write(str(max(temperatura))+"\n")
f.write("el valor minimo encontrado fue: ")
f.write(str(min(temperatura))+"\n")
f.write("el valor promedio es: ")
f.write(str(statistics.mean(temperatura)) + "\n")
f.close()


print("Se guardaron los datos de temperatura en : ", datos )

