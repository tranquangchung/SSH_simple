import socket, threading
from subprocess import Popen, PIPE
import time
from queueMessage import *

recvMessage = RecvMessage()
sendMessage = SendMessage()

fname="username"
username = []
with open(fname, 'r') as f:
    for user in f:
        username.append(user.split())

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        print("New connection added: ", clientAddress)
        self.recvMessage = RecvMessage()
        self.sendMessage = SendMessage()


    def run(self):
        print("Connection from : ", clientAddress)
        message = "connecting"
        self.sendMessage.put(message)
        self.clientsocket.sendall(self.sendMessage.get())

        while True:
            self.recvMessage.put(self.clientsocket.recv(2048))
            message = self.recvMessage.get()
            cmd = message.split()
            popen = Popen(cmd, stdout=PIPE)
            out, err = popen.communicate()
            self.sendMessage.put(out)
            self.clientsocket.sendall(self.sendMessage.get())


LOCALHOST = "127.0.0.1"
PORT = 8081
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsocket, clientAddress = server.accept()

    # check login
    recvMessage.put(clientsocket.recv(2048))
    user = recvMessage.get()
    for u in username:
        if user == u[0]:
            # return flag_user = TRUE
            flag_user="TRUE"
            sendMessage.put(flag_user)
            clientsocket.sendall(sendMessage.get())
            while True:
                # check password
                pw = "Password: "
                sendMessage.put(pw)
                clientsocket.sendall(sendMessage.get())

                recvMessage.put(clientsocket.recv(2048))
                password = recvMessage.get()

                if password == u[1]:
                    # return flag_pass = TRUE
                    flag_pass = "TRUE"
                    sendMessage.put(flag_pass)
                    clientsocket.sendall(sendMessage.get())
                    newthread = ClientThread(clientAddress, clientsocket)
                    newthread.start()
                    break