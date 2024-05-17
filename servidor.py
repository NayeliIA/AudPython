import socket

def conexion():
    print("hola ya me conecte")
    
    mi_socket = socket.socket()
    mi_socket.bind(('localhost', 40000))
    mi_socket.listen(5)

   
    conexion, addr = mi_socket.accept()
    print ("Nueva conexion establecida")
    print (addr)


    peticion = conexion.recv(1024)
    print (peticion)

    conexion.send("Hola, te saludo desde el servidor!".encode())
        
    