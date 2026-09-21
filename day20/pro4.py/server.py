import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))
server.listen(1)

print("Waiting for client...")

client, address = server.accept()

message = client.recv(1024).decode()
print("Client:", message)

client.send("Hello from Server!".encode())

client.close()
server.close()