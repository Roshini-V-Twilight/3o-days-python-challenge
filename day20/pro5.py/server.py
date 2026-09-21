import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))
server.listen(1)

print("Waiting for client...")

client, address = server.accept()

print("Client connected:", address)

while True:
    message = client.recv(1024).decode()

    if message.lower() == "exit":
        break

    print("Client:", message)

    reply = input("Server: ")
    client.send(reply.encode())

    if reply.lower() == "exit":
        break

client.close()
server.close()