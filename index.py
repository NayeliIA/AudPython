#-*- coding: utf-8 -*-
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk, ImageTk, ImageDraw
import cv2
import time
import os
import socket
import threading
import tensorflow.lite as tflite
root = tk.Tk()
root.title("Auditoria Tesla")

# Tamano de la ventana
width = 1920
height = 1080
host = "localhost"
port = 40000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
result = s.connect_ex((host,port))
if result == 0:
    print("el servidor esta conectado")
    conn.close()
    s.close()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

else:
    print("esperando ...")
    
s.bind((host,port))
s.listen(5)
conn, addr = s.accept()




    
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
#thread_servidor = threading.Thread(target=conexion)
#thread_servidor.start()

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
        #sequence()


    #funcion para cambiar el enfoque 
    def open_cam():
        cap = cv2.VideoCapture(0) # Abre la camara con el indice 0 (camara predeterminada)
        return cap
    
     
    def capture_image(cap, datos, delay,canvas,root,point):
   
        ret, frame = cap.read()
        if ret:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img)
            #mostrar la imagen en el canvas
            
            photo = ImageTk.PhotoImage(img_pil.resize((632,300)))
            
            image_canvas = canvas.create_image(947,470, anchor=tk.CENTER, image=photo, tags=("img"))
            print("Imagen mostrada")
            root.update()
            time.sleep(delay)
            canvas.delete("img")
            root.update()
            
            
            #guardar la imagen
            if not os.path.exists(datos):
                os.makedirs(datos)
                
            img_name=f"/home/pi/auditoriatesla/AudPython/{datos}/img_{point}.png"
            cv2.imwrite(img_name, frame)
            print("Imagen capturada y guardada", img_name)
               
            
        else:
            print("error al capturar la imagen")          

    
     
    def sequence(datos):
        print("estoy en secuencia")
        print("Haz llegado hasta aqui")
        cap = open_cam()
        capture_image(cap, datos, delay=2,canvas=canvas, root=root, point=1)
        modelo()
        cap.release()
        respuesta = "2"
        conn.send(respuesta.encode())
        conexion()
            
                
    def modelo():
        interpreter = tf.lite.Interpreter(model_path="modelo.tflite")
        interpreter.allocate_tensors()
        
        #obtener detalles del modelo
        
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        
        #definir las clases
        
        class_names = ['buenas','buenas2','malas',...]
        
        #cargar y preparar la imagen
        
        image_path = '/content/75956306935442820000.jpeg'
        img_height = 170
        img_width = 170
        
        img = tf.keras.utils.load_img(image_path,target_size=(img_height, img_width))
        img_array = tf.keras.utils.img_to_array(img)
        imag_array = tf.expand_dims(img_array,0) #crear un lote de una sola imagen
        
        #ejecutar el modelo y obtener predicciones
        
        interpreter.set_tensor(input_details[0]['index'], img_array)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])
        
        #procesar las predicciones
        
        score = tf.nn.softmax(output_data[0])
        
        print("This image most likely belongs to {} with a {:.2f} percent confidence".format(class_names[np.argmax(score)],100*np.max(score)))
                                             
        
        
            
    def conexion():
        
        print("conexion desde: ", addr)

        while True:
            datos_recibidos = conn.recv(1024)
            datos = datos_recibidos.decode().strip()
            if not datos_recibidos:
                break
            print("Datos recibidos: ", datos_recibidos.decode())
            if datos == "1":
                sequence(datos)
           
            else:
                respuesta = "comando no reconocido"
                conn.send(respuesta.encode())
                
                
           
       
    
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
    root.update()
    respuesta = "Wait"
    conn.send(respuesta.encode())
    conexion()
    
    root.mainloop()
    
    
      
MAIN(a)