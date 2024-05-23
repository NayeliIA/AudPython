import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 40000
s.connect((host,port))
while True:
    datos_recibidos=s.recv(1024)
    print("respuesta del servidor:", datos_recibidos.decode())
    mensaje = input("ingresa tu mensaje: ")
    #mensaje = ('1')
    s.send(mensaje.encode())
    
s.close()









'''import socket

def comunicacion(mi_socket):
    while True:
        
        print("Enviame un mensaje.")
        mensaje = input("ingresa tu mensaje: ")
        if mensaje == "salir":
            return
        mi_socket.send(mensaje.encode())
        respuesta = mi_socket.recv(1024)
        print(respuesta.decode())
    
    #llamada recursiva
    #comunicacion(mi_socket)
    
mi_socket = socket.socket()
mi_socket.connect( ('localhost', 40000) )

comunicacion(mi_socket)0

#print (respuesta.decode())
mi_socket.close()'''
        