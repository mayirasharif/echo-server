import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

response = input("Type in what you want to send: ")

# Parameter Marshaling / Unmarshaling
def marshal(msg):
    pass

def unmarshal(msg):
    pass

# User input loop
while response != "quit" and response != "":
    client.send(response.encode())
    server_letter = client.recv(1024).decode()
    print(f"Server Response: {server_letter} ")
    response = input("Type in what you want to send: ")

client.close()
