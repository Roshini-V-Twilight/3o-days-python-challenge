import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 5000))

while True:
    message = input("Client: ")
    client.send(message.encode())

    if message.lower() == "exit":
        break

    reply = client.recv(1024).decode()

    if reply.lower() == "exit":
        break

    print("Server:", reply)

client.close()