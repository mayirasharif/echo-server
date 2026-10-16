import socket

# Create the Socket.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a Host and Port.
HOST = '127.0.0.1'
PORT = 8888
server_socket.bind((HOST, PORT))

# Listen for a max 2 connections / clients.
server_socket.listen(2)

# Continuous While Loop for continuous listening.
while True:

    # Accept client connection.
    client, addr = server_socket.accept()
    # Print client message.
    print(client.recv(1024).decode())
    # Send message to client.
    client.send("Hello there! This is the server.".encode())
