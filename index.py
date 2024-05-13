from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk, ImageTk, ImageDraw
import cv2
import time
#-*- coding:utf-8 -*-
#boton.bind("<Return>", saludar_enter) accionar cuando presionas enter
# Crear una ventana

root = tk.Tk()
root.title("Auditoria Tesla")

# Tamano de la ventana
width = 1920
height = 1080
def stopBoton():
    print("paro")

def pass_alert():
    ventana_exito = tk.Tk()
    ventana_exito.title("PASS")
    ventana_exito.geometry("500x200+800+500")
    ventana_exito.config(bg="#00FF00")
    etiqueta_exito = tk.Label(ventana_exito,text="\nPASS ✔️", font=("Arial",50),bg="#00FF00",fg="green",anchor="center")
    etiqueta_exito.pack(anchor="center")
    ventana_exito.after(5500,ventana_exito.destroy)
    
def fail_alert():
    ventana_exito = tk.Tk()
    ventana_exito.title("FAIL")
    ventana_exito.geometry("500x200+800+500")
    ventana_exito.config(bg="#FF0000")
    etiqueta_exito = tk.Label(ventana_exito,text="\nFAIL ✘️", font=("Arial",50),bg="#FF0000",fg="#FF6666",anchor="center")
    etiqueta_exito.pack(anchor="center")
    ventana_exito.after(5500,ventana_exito.destroy)
    
# Crear un lienzo (canvas)
canvas = tk.Canvas(root, width=width, height=height)
canvas.grid()

#funcion para procesar los datos cuando se presiona enter

#funcion para mostrar el video de la camara

a=0
#info_input1=0
def MAIN(a): 
    def tiempo():
        a=0
        MAIN(a)
    def procesar_datos(event):
        info_input1=input1.get()
        print("informacion input1: ", info_input1)
        
        if info_input1=='123':
            pass_alert()
            print("pase")
            
        else:
           fail_alert()
           print("falle")
           
        input1.delete(0,'end')
        input1.focus_set()
        sequence()
        
 
        

    # print("informacionn input2: ", info_input2)

    #funcion para cambiar el enfoque
    def open_cam():
        cap = cv2.VideoCapture(0) # Abre la camara con el indice 0 (camara predeterminada)
        return cap
    
    def capture_image(cap):
        for i in range(10):
            ret, frame = cap.read()
            if ret:
                cv2.imwrite("capture_image/capture_image{i}.png", frame)
                print("Imagen capturada y guardada")
                time.sleep(0.5)
        else:
            print("error al capturar la imagen")
            cap.release()
            MAIN(a)
 
    #etiqueta.grid(row=2, column=0, padx=100)

    def sequence():
    
        print("Haz llegado hasta aqui")
        cap = open_cam()
        capture_image(cap)
        #cap.release()
        a=1
        MAIN(a)
    

       
    # Cargar las imagenes
    image1 = Image.open("fondocompleto.png")
    image2 = Image.open("tesla2.png")
    image3 = Image.open("process.png")
    
    # Convertir las imagenes en objetos ImageTk
    photo1 = ImageTk.PhotoImage(image1.resize((2200,1000)))
    photo2 = ImageTk.PhotoImage(image2.resize((100,100)))
    photo3 = ImageTk.PhotoImage(image3.resize((1500,900)))
    
    
    # Dibujar las imagenes en el lienzo
    canvas.create_image(1000,500,anchor=tk.CENTER, image=photo1)
    
    canvas.create_image(950,600,anchor=tk.CENTER, image=photo3)
    #canvas.create_image(1650,850,anchor=tk.CENTER, image=photo4)
    if a==1:
        img = Image.open("/home/pi/auditorias/audpython/AudPython/capture_image/capture_image.png")
        photo5 = ImageTk.PhotoImage(img.resize((631,300))) #610.100
        canvas.create_image(947,470,anchor=tk.CENTER, image=photo5) #947-- un valor mas alto mueve la imagen hacia la derecha y uno bajo a la izq, 470 valor alto hacia abajo, valor bajo hacia arriba
        canvas.move(photo5,0,-10)
        print(a)
        root.after(5000, tiempo)
        
        
#-------------------Declaracion de los componentes--------------------
       

    #crear los inputs
    input1 = tk.Entry(root,width=0, bg="white")
    #input2 = tk.Entry(root,width=0, bg="white")
    input1.place_forget()
    #input2.place_forget()
    #colocar los inputs en el lienzo
    canvas.create_window(950, 150, window=input1, anchor = tk.CENTER)
    #canvas.create_window(950 + 50, 395, window=input2, anchor= tk.CENTER)
    #se coloca el enfoque en el primer input
    input1.focus_set()

    #asginar un ancho y alto a los inputs
   
    boton = tk.Button(root, text ="click aqui",borderwidth=-10,bg="#fff", width=100,height=100,image= photo2, command = sequence, relief=tk.RIDGE)
    button1_canvas = canvas.create_window( 960, 150, window = boton)

    #crear la etiqueta

    input1.bind("<Return>", procesar_datos)
    # Iniciar el bucle princ
    print(a)
    root.mainloop()
    
    
MAIN(a)