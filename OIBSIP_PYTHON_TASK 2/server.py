# Simple Chat Server
# Oasis Infobyte Internship Project

import socket

HOST = "127.0.0.1"   # localhost
PORT = 5060          # any free port number

# create socket object (TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to address
server_socket.bind((HOST, PORT))

# listen for only one client
server_socket.listen(1)
print("Server started. Waiting for client to connect...")

# accept connection
conn, addr = server_socket.accept()
print("Client connected from:", addr)
print("Type messages and press Enter to send.")
print("Type 'exit' to end the chat.\n")

while True:
    # server sends message first
    msg = input("You (server): ")
    conn.sendall(msg.encode())

    if msg.lower() == "exit":
        print("You ended the chat.")
        break

    # receive message from client
    data = conn.recv(1024)
    if not data:
        print("Client disconnected.")
        break

    client_msg = data.decode()
    print("Client:", client_msg)

    if client_msg.lower() == "exit":
        print("Client ended the chat.")
        break

# close connections
conn.close()
server_socket.close()
print("Server closed.")
