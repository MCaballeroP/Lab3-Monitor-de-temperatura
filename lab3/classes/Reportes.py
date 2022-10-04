

import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation


pause = false

try:
    puerto = serial.Serial('COM3',9600)
    puerto.close()
    puerto.open()
    print("se abrio el puerto")
except
    print("Problemas abriendo el puerto")

def onclick(event):
    global pausa
    print ("Pausa")
    pausa = True

fig, ax = plt.subplots()
fig.canvas.mpl_connect('button_press_event',onclick)

ydata =[]

def update_data(i):
    if not pausa:
        punto = puerto.readline().decode().strip()
        print(punto)
        ydata.append(punto)
        ax.claer()
        ax.plot(ydata)

ani = animation.FuncAnimation(fig,update_data)
plt.show()