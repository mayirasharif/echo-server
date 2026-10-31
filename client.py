import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))


reader = client.makefile("r", encoding="utf-8")

# Parameter Marshaling / Unmarshaling
def marshal(msg):
    return msg.strip() + "\n"

def unmarshal(msg):
    parts = msg.strip().split(",", 1)
    if len(parts) != 2 or parts[0] not in ("COMPLETE", "ERR"):
        raise ValueError("Invalid server response")
    return parts[0], parts[1].strip()

# User input loop

while True:

    procedure = input("Enter operation (Press enter to quit):").upper()
    if procedure == "":
        break
    a = input("Enter first integer (Press enter to quit):")
    if a == "":
        break
    b = input("Enter second integer (Press enter to quit):")
    if b == "":
        break
    response = f"{procedure},{a},{b}"

    
    client.sendall(marshal(response).encode("utf-8"))
    server_letter = reader.readline()

    if not server_letter:
        print("Server disconnect")
        break

    try:
        status, value = unmarshal(server_letter)
    except ValueError:
        print("Client failure")
        continue
    if status == "COMPLETE":
        print(f"Result from server: {value}")
    else:
        print(f"Server error: {value}")
    

reader.close()
client.close()
