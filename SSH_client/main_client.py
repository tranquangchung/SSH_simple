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

    recvMessage.put(serversocket.recv(2048))
    flag_user = recvMessage.get()

    if flag_user == "TRUE":
        # check password
        while True:
            recvMessage.put(serversocket.recv(2048))
            message = recvMessage.get()
            password = input(message)

            sendMessage.put(password)
            serversocket.sendall(sendMessage.get())

            recvMessage.put(serversocket.recv(2048))
            flag_pass = recvMessage.get()
            if flag_pass == "TRUE":
                # Start Connection
                recvMessage.put(serversocket.recv(2048))
                message = recvMessage.get()
                print(message)

                # Start communication
                while True:
                    message = input("Enter command:")
                    sendMessage.put(message)
                    serversocket.sendall(sendMessage.get())

                    recvMessage.put(serversocket.recv(2048))
                    message = recvMessage.get()
                    print(message)
    else:
        print("Wrong username")
finally:
    print('closing socket')
    serversocket.close()