import socket
import threading

# Create the Socket.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a Host and Port.
HOST = '127.0.0.1'
PORT = 8888
server_socket.bind((HOST, PORT))

# Listen for multiple clients.
server_socket.listen()

# Our client function
def talk_to_client(client, addr):
    while True:
        # Echo message
        echo = client.recv(1024).decode()

        # Break if client disconnects (empty response)
        if echo == '':
            break

        # Print message
        print(f"{addr} says: {echo}")
        
        # Send message to client.
        client.send(echo.encode())
    client.close()

# Continuous While Loop for continuous listening.
while True:

    # Accept client connection.
    client, addr = server_socket.accept()
    t = threading.Thread(target=talk_to_client, args=(client, addr))
    t.start()
    
