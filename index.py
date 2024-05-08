from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import time
#boton.bind("<Return>", saludar_enter) accionar cuando presionas enter
# Crear una ventana

root = tk.Tk()
root.title("SUBARU SIDE")
# Tamaño de la ventana
width = 1920
height = 1080
def stopBoton():
    print("paro")

# Crear un lienzo (canvas)
canvas = tk.Canvas(root, width=width, height=height)
canvas.grid()

#funcion para procesar los datos cuando se presiona enter

#funcion para mostrar el video de la camara

a=0
def MAIN(a): 
    def tiempo():
        a=0
        MAIN(a)
    def procesar_datos(event):
        info_input1=input1.get()
        print("informacion input1: ", info_input1)
        input1.delete(0,'end')
        input1.focus_set()
        sequence()

    # print("informacion input2: ", info_input2)

    #funcion para cambiar el enfoque
    def open_cam():
        cap = cv2.VideoCapture(0) # Abre la cámara con el índice 0 (cámara predeterminada)
        return cap
    def capture_image(cap):
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("capture_image/capture_image.png", frame)
            print("imagen capturada y guardada")
            time.sleep(0.05)
        else:
                print("error al capturar la imagen")
                MAIN(a)
            
    #etiqueta.grid(row=2, column=0, padx=100)

    def sequence():
        print("Haz llegado hasta aqui")
        cap = open_cam()
        capture_image(cap)
        cap.release()
        a=1
        MAIN(a)
    
        
        
   
    # Cargar las imagenes
    image1 = Image.open("icono.1.png")
    image2 = Image.open("harman.png")
    image3 = Image.open("AI_lab_logo.png")
    image4 = Image.open("sanmina.png")
    

    # Convertir las imágenes en objetos ImageTk
    photo1 = ImageTk.PhotoImage(image1.resize((2200,1000)))
    photo2 = ImageTk.PhotoImage(image2.resize((190,100)))
    photo3 = ImageTk.PhotoImage(image3.resize((195,70)))
    photo4 = ImageTk.PhotoImage(image4.resize((195,100)))
    
    # Dibujar las imágenes en el lienzo
    canvas.create_image(1000,500,anchor=tk.CENTER, image=photo1)
    
    canvas.create_image(250,850,anchor=tk.CENTER, image=photo3)
    canvas.create_image(1650,850,anchor=tk.CENTER, image=photo4)
    if a==1:
        img = Image.open("C:/Users/nayeli_garcia/Desktop/python_website/capture_image/capture_image.png")
        photo5 = ImageTk.PhotoImage(img.resize((1100,500)))
        canvas.create_image(1007,502,anchor=tk.CENTER, image=photo5)
        #canvas.move(photo5, -50, 0)
        print(a)
        root.after(5000, tiempo)
       
    

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
   
    boton = tk.Button(root, text ="click aquí",borderwidth=-10,bg="#fff", width=190,height=100,image= photo2, command = stopBoton)

    button1_canvas = canvas.create_window( 960, 150, window = boton)

    #crear la etiqueta

    input1.bind("<Return>", procesar_datos)
    # Iniciar el bucle princ
    print(a)
    root.mainloop()
MAIN(a)