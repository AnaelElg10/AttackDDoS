import socket

# Creation socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8080))
server.listen()

print("Server listening on.....")


while True:
    client, address = server.accept()
    print(f"Connection from {address} has been established")
    
    client.send("Welcome to the server".encode())
    
    response = client.recv(4096)
    print(f"Réponse reçue: {response.decode()}")

    client.close()