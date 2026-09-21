import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))
server.listen(1)

print("Server is waiting for a connection...")

client, address = server.accept()

print("Connected to:", address)

client.close()
server.close()