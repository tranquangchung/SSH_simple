import socket
import sys, os
from queueMessage import *

recvMessage = RecvMessage()
sendMessage = SendMessage()


# Login
try:
    # name_address = sys.argv[1]
    name_address = 'admin@127.0.0.1'
except:
    print("Please enter address server")

user, id_address = name_address.split('@')
# Create a TCP/IP socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (id_address, 8081)
serversocket.connect(server_address)


try:
    # check user
    message = str(user)
    sendMessage.put(message)
    serversocket.sendall(sendMessage.get())

    while True:
        recvMessage.put(serversocket.recv(2048))
        message = recvMessage.get()
        if message == "Password: ":
            password = input(message)
            sendMessage.put(password)
            serversocket.sendall(sendMessage.get())
        if message == "Connect":
            # Start communication
            print("Connecting to Server")
            while True:
                message = input("Enter command:")
                sendMessage.put(message)
                serversocket.sendall(sendMessage.get())

                recvMessage.put(serversocket.recv(2048))
                message = recvMessage.get()
                if message == "disconnection":
                    exit()
                else:
                    print(message)
        if message == "Many trial":
            print("exceeded the number of attempts to login")
            exit()
finally:
    serversocket.close()