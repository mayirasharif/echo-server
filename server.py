import socket
import threading
from collections import namedtuple

# Create the Socket.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a Host and Port.
HOST = '127.0.0.1'
PORT = 8888
server_socket.bind((HOST, PORT))

# Listen for multiple clients.
server_socket.listen()

# Our echo client function
def echo_to_client(client, addr):
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

# Our RPC logic
def rpc_to_client(client, addr):
    buffer = b''
    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            buffer += data

            while b'\n' in buffer:
                raw, buffer = buffer.split(b'\n', 1)
                try:
                    procedure, a, b = unmarshal(raw.decode("utf-8"))
                    result = procedures[procedure](a, b)
                    response = f"COMPLETE,{result}\n"
                except (ValueError, UnicodeDecodeError) as exc:
                    response = f"ERR,{exc}\n"
                client.sendall(response.encode("utf-8"))
    finally:
        client.close()
            




# Our four functions
def ADD(a, b):
    return a + b

def SUBTRACT(a, b):
    return a - b

def MULTIPLY(a, b):
    return a * b

def MAX(a, b):
    return max(a, b)

# Function dictionary

procedures = {
    'ADD': ADD, 
    'SUBTRACT': SUBTRACT,
    'MULTIPLY': MULTIPLY,
    'MAX': MAX
}

# Parameter Marshaling / Unmarshaling
def marshal(procedure, a, b):

    result = ",".join([procedure, str(a), str(b)])
    return result
    

# Unmarshal an incoming request from a client.
def unmarshal(msg):
    msg = msg.strip()
    msg = msg.split(",")

    if len(msg) != 3:
        raise ValueError("Message does not contain all parameters")
    try:
        a = int(msg[1])
        b = int(msg[2])
    except ValueError:
        raise ValueError("Parameters are of incorrect type")

    if msg[0] not in ["ADD", "SUBTRACT", "MULTIPLY", "MAX", "SUB"]:
        raise ValueError("Procedure is not supported")
    return msg[0], a, b

# Continuous While Loop for continuous listening.
while True:

    # Accept client connection.
    client, addr = server_socket.accept()
    t = threading.Thread(target=echo_to_client, args=(client, addr))
    t.start()
    
