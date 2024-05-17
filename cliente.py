import socket

def comunicacion(mi_socket):
    mensaje = input("ingresa tu mensaje: ")
    if mensaje == "salir":
        return
    mi_socket.send(mensaje.encode())
    respuesta = mi_socket.recv(1024)
    print(respuesta.decode())
    
    #llamada recursiva
    comunicacion(mi_socket)
    
mi_socket = socket.socket()
mi_socket.connect( ('localhost', 40000) )

comunicacion(mi_socket)

#print (respuesta.decode())
mi_socket.close()

        