import socket

HOST = "127.0.0.1"
PORT = 5000

# socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexion
client.connect((HOST, PORT))

# mensaje
mensaje = "Cliente1"
client.send(mensaje.encode())

# repuesta
respuesta = client.recv(1024).decode()
print(f"Respuesta del servidor: {respuesta}")



client.close()