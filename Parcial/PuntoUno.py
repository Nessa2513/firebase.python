import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time

placa = Arduino ('COM3')
it = util.Iterator(placa)
it.start()
a_0 = placa.get_pin('a:0:i')
a_1 = placa.get_pin('a:1:i')
a_2 = placa.get_pin('a:2:i')
led1 = placa.get_pin('d:8:o')
led2 = placa.get_pin('d:9:p')
led3 = placa.get_pin('d:10:p')
led1 = placa.get_pin('d:11:p')
led2 = placa.get_pin('d:12:o')
led3 = placa.get_pin('d:13:o')
time.sleep(0.5)
ventana = Tk()
ventana.geometry('1280x800')
ventana.title("Punto Uno")

# Fetch the service account key JSON file contents
#cred = credentials.Certificate('key/key.json')
# Initialize the app with a service account, granting admin privileges
#firebase_admin.initialize_app(cred, {
 #   'databaseURL': 'https://tarea3-d2963.firebaseio.com/'
#})


Frame1 = Frame(ventana, bg="gray", highlightthickness=1, width=1280, height=800, bd= 5)
Frame1.place(x = 0,y = 0)

valor= Label(Frame1, bg='cadet blue1', font=("Arial Bold", 15), fg="black", width=5)
adc_data=StringVar()
valor2= Label(Frame1, bg='cadet blue1', font=("Arial Bold", 15), fg="black", width=5)
adc_data2=StringVar()
valor3= Label(Frame1, bg='cadet blue1', font=("Arial Bold", 15), fg="black", width=5)
adc_data3=StringVar()
variable=StringVar()
      
def adc_read1():
    x=a_0.read()
    print(x)
    adc_data.set(x)
    time.sleep(0.1)
    #ref = db.reference('sensor')
    #ref.update({
     #   'sensor1/adc': lector_1
     #   })

def adc_read2():
    x=a_1.read()
    print(x)
    adc_data2.set(x)
    time.sleep(0.1)
    #ref = db.reference('sensor')
   # ref.update({
   #     'sensor2/adc': lector_2
  #      })

def adc_read3():
    x=a_2.read()
    print(x)
    adc_data3.set(x)
    time.sleep(0.1)
 #   ref = db.reference('sensor')
  #  ref.update({
   #     'sensor3/adc': lector_3
    #    })
    
valor.configure(textvariable=adc_data)
valor.place(x=20, y=30)
start_button=Button(Frame1,text="lector 1",command=adc_read1)
start_button.place(x=95, y=32)

valor2.configure(textvariable=adc_data2)
valor2.place(x=20, y=80)
start_button2=Button(Frame1,text="lector 2",command=adc_read2)
start_button2.place(x=95, y=82)

valor3.configure(textvariable=adc_data3)
valor3.place(x=20, y=130)
start_button3=Button(Frame1,text="lector 3",command=adc_read3)
start_button3.place(x=95, y=132)

ventana.mainloop()

