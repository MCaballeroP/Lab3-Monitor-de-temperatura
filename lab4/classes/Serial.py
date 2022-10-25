
import serial

puerto = serial.Serial('COM3',9600)

puerto.close()
puerto.open()

while(True):
    dato = puerto.readline().decode().strip()
    print(dato)
