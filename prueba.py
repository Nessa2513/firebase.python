from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time
data = []
d = 0
valor = 0
prom = 0
placa = Arduino ('COM11')
it = util.Iterator(placa)
it.start()
a_0 = placa.get_pin('a:0:i')
led1 = placa.get_pin('d:3:p')
led2 = placa.get_pin('d:5:p')
led3 = placa.get_pin('d:6:p')
led4 = placa.get_pin('d:9:p')
led5 = placa.get_pin('d:10:p')
led6 = placa.get_pin('d:11:p')
time.sleep(0.1)
ventana = Tk()
ventana.geometry('1280x800')
ventana.title("UI para sistemas de control")

marco1 = Frame(ventana, bg="gray", highlightthickness=1, width=1280, height=800, bd= 5)
marco1.place(x = 0,y = 0)
b=Label(marco1,text="")
img = Image.open("C:/Users/Camilo/Downloads/logousa.png")
img = img.resize((150,150), Image.ANTIALIAS)
photoImg=  ImageTk.PhotoImage(img)
b.configure(image=photoImg)
b.place(x = 760,y = 20)

valor= Label(marco1, text="0.0,", bg='cadet blue1', font=("Arial Bold", 15), fg="white", width=5)
variable=StringVar()

def update_label():
    global prom
    i=0
    while i<15:
        i=i+1
        x=a_0.read()
        variable.set(x)
        data[i-1]=x
        prom=x+prom
        ventana.update()
        time.sleep(0.5)
    print(prom)
    print(len(data))

def show():
    print("estoy aca")
    


valor.configure(textvariable=variable)
valor.place(x=20, y=90)
start_button=Button(ventana,text="start",command=update_label)
start_button.place(x=20, y=160)




ventana.mainloop()
