# Simple Chat Client
# Oasis Infobyte Internship Project

import socket

HOST = "127.0.0.1"   # server IP (localhost)
PORT = 5060          # same port as server

# create socket object (TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
except ConnectionRefusedError:
    print("Could not connect to server. Make sure server.py is running.")
    exit()

print("Connected to server.")
print("You will reply after server sends a message.")
print("Type 'exit' to end the chat.\n")

while True:
    # receive message from server
    data = client_socket.recv(1024)
    if not data:
        print("Server disconnected.")
        break

    server_msg = data.decode()
    print("Server:", server_msg)

    if server_msg.lower() == "exit":
        print("Server ended the chat.")
        break

    # send reply to server
    msg = input("You (client): ")
    client_socket.sendall(msg.encode())

    if msg.lower() == "exit":
        print("You ended the chat.")
        break

# close connection
client_socket.close()
print("Client closed.")
