import socket
import threading
import  index

def conexion():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = "localhost"
    port = 40000
    s.bind((host,port))
    s.listen(5)
    conn, addr = s.accept()
    print("conexion desde: ", addr)

    while True:
        datos_recibidos = conn.recv(1024)
        if not datos_recibidos:
            break
        print("Datos recibidos: ", datos_recibidos.decode())
        if datos_recibidos.decode().strip() == "1":
            index.sequence()
       
        else:
            respuesta = "comando no reconocido"
            conn.send(respuesta.encode())
            
    conn.close()
    s.close()






'''import socket

def conexion():
    print("hola ya me conecte")
    
    mi_socket = socket.socket()
    mi_socket.bind(('localhost', 40000))
    mi_socket.listen(5)

   
    conexion, addr = mi_socket.accept()
    print ("Nueva conexion establecida")
    print (addr)
    
    while True:
        peticion = conexion.recv(1024)
        print (peticion.decode())

    conexion.send("Hola, te saludo desde el servidor!".encode())'''
        
    