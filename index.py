#-*- coding: utf-8 -*-
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk, ImageTk, ImageDraw
import cv2
import time
import os
import servidor
import threading


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
#-*- coding: utf-8 -*-
#info_input1=0
thread_servidor = threading.Thread(target=servidor.conexion)
thread_servidor.start()

def MAIN(a):
    
    def tiempo():
        a=0
        MAIN(a)
    def procesar_datos(event):
        global info_input1
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


    #funcion para cambiar el enfoque
    def open_cam():
        cap = cv2.VideoCapture(0) # Abre la camara con el indice 0 (camara predeterminada)
        return cap
    
     
    def capture_image(cap,delay,canvas,root,point):
   
        ret, frame = cap.read()
        if ret:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img)
            
            #mostrar la imagen en el canvas
            
            photo = ImageTk.PhotoImage(img_pil.resize((632,300)))
            
            image_canvas = canvas.create_image(947,470, anchor=tk.CENTER, image=photo, tags=("img"))
            print(f"Imagen mostrada")
            root.update()
            time.sleep(delay)
            canvas.delete("img")
            root.update()
            #guardar la imagen
            if not os.path.exists(info_input1):
                os.makedirs(info_input1)
                
            img_name=f"{info_input1}/capture_image_{point}.png"
            cv2.imwrite(img_name, frame)
            print(f"Imagen capturada y guardada")
               
            
        else:
            print("error al capturar la imagen")          

        
    def sequence():
        print("estoy en secuencia")
        
        '''for i in range(4):
            print("Haz llegado hasta aqui")
            cap = open_cam()
            capture_image(cap, delay=2,canvas=canvas, root=root, point=i+1)
            cap.release()'''
            
                
        

           
    # Cargar las imagenes
    image1 = Image.open("img/fondocompleto.png")
    image2 = Image.open("img/tesla2.png")
    image3 = Image.open("img/process.png")
    
    # Convertir las imagenes en objetos ImageTk
    photo1 = ImageTk.PhotoImage(image1.resize((2200,1000)))
    photo2 = ImageTk.PhotoImage(image2.resize((100,100)))
    photo3 = ImageTk.PhotoImage(image3.resize((1500,900)))
    
    
    # Dibujar las imagenes en el lienzo
    canvas.create_image(1000,500,anchor=tk.CENTER, image=photo1)
    
    canvas.create_image(950,600,anchor=tk.CENTER, image=photo3)
  
        
        
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