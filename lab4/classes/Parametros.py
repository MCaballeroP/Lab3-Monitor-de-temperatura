
import serial
import time
import sys

puerto = serial.Serial('COM3', 9600)

def controlh():
    dato = int(puerto.readline().decode().strip())
    tminh = int(input("por favor ingresé el valor mínimo de temperatura para hipotermia"))
    print("valor mínimo de temperatura hipotermia:", tminh, "°")
    tmaxh = int(input("por favor ingresé el valor maximo de temperatura para hipotermia"))
    print("valor maximo de temperatura hipotermia:", tmaxh, "°")
    puerto.write(struct.pack('>B',tminh,tmaxh ))
    control()

def controln():
    tminn = int(input("por favor ingresé el valor mínimo de temperatura normal"))
    print("valor mínimo de temperatura normal :", tminn, "°")
    tmaxn = int(input("por favor ingresé el valor maximo para temperatura normal"))
    print("valor maximo de temperatura para hipotermia:", tmaxh, "°")
    puerto.write(struct.pack('>B', tminn, tmaxn))
    control()

def controlf():
    tminh = int(input("por favor ingresé el valor mínimo de temperatura para hipotermia"))
    print("valor mínimo de temperatura hipotermia:", tminh, "°")
    tmaxh = int(input("por favor ingresé el valor maximo de temperatura para hipotermia"))
    print("valor maximo de temperatura hipotermia:", tmaxh, "°")
    puerto.write(struct.pack('>B', tminf, tmaxf))
    control()


def control():
    dato = int(puerto.readline().decode().strip())
    print("Temp=", dato)
    if dato >= tminh and dato <= tmaxh:
        temp = "H"
    elif dato > tminn and dato <= tmaxn:
        temp = "N"
    elif dato > tminf and dato <= tmaxf:
        temp = "F"
    print("Categoria:", temp)
    puerto.write(temp.encode())

    control()


control()


