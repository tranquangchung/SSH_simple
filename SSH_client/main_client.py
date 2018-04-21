import socket
import sys, os
from queueMessage import *
import json

recvMessage = RecvMessage()
sendMessage = SendMessage()
import json

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
        message = json.loads(message)
        if message['state'] == "Password":
            tmp = message['state'] + ': '
            password = input(tmp)
            sendMessage.put(password)
            serversocket.sendall(sendMessage.get())
        if message['state'] == "Connect":
            # Start communication
            print("Connecting to Server")
            while True:
                cwd = message["cwd"] + ": "
                cmd = input(cwd)
                sendMessage.put(cmd)
                serversocket.sendall(sendMessage.get())

                recvMessage.put(serversocket.recv(2048))
                cmd = recvMessage.get()
                cmd = json.loads(cmd)
                if cmd == "disconnection":
                    exit()
                else:
                    print(cmd)
        if message['state'] == "Many trial":
            print("exceeded the number of attempts to login")
            exit()
finally:
    serversocket.close()