import socket, threading
from subprocess import Popen, PIPE
import time
from queueMessage import *
from cml import *
import os

recvMessage = RecvMessage()
sendMessage = SendMessage()

fname="username"
username = []
threads = []
N_connection = 2

with open(fname, 'r') as f:
    for user in f:
        username.append(user.split())

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket, username):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        # print("New connection added: ", clientAddress)
        self.recvMessage = RecvMessage()
        self.sendMessage = SendMessage()
        self.username = username
        self.cwd = [os.getcwd()] #current working directory
        self.cmd = CommandLine(self.cwd)

    def checkLogin(self):
        self.recvMessage.put(self.clientsocket.recv(2048))
        user = self.recvMessage.get()
        for u in self.username:
            if user == u[0]:
                trial_password = 0
                while True:
                    # check password
                    message = '{"state": "Password", "cwd": "None"}'
                    self.sendMessage.put(message)
                    self.clientsocket.sendall(self.sendMessage.get())

                    self.recvMessage.put(self.clientsocket.recv(2048))
                    password = self.recvMessage.get()
                    if password == u[1]:
                        message = '{{"state": "Connect", "cwd": "{0}"}}'.format(self.cwd[0])
                        self.sendMessage.put(message)
                        self.clientsocket.sendall(self.sendMessage.get())
                        return True
                    if trial_password == 5:
                        message = '{"state": "Many trial", "cwd": "None"}'
                        self.sendMessage.put(message)
                        self.clientsocket.sendall(self.sendMessage.get())
                        return False
                    trial_password += 1
        return False

    def run(self):
        if self.checkLogin():
            print("Connection from :", clientAddress)
            while True:
                self.recvMessage.put(self.clientsocket.recv(2048))
                message = self.recvMessage.get()
                if message != "exit":
                    respond = self.cmd.parse_command(message)
                    self.sendMessage.put(respond)
                    self.clientsocket.sendall(self.sendMessage.get())
                else:
                    # disconnect this thread
                    respond = '{"state": "disconnection"}'
                    self.sendMessage.put(respond)
                    self.clientsocket.sendall(self.sendMessage.get())
                    break

    def close(self):
        self.clientsocket.close()
        print("Disconnection from :", clientAddress)

def isalive():
    """
    check thread is alive or die
    if die then remove this thead out of theads
    :return:
    """
    global threads
    for thread in threads:
        if not thread.isAlive():
            thread.close()
            threads.remove(thread)



LOCALHOST = "127.0.0.1"
PORT = 8081
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")

while True:
    if len(threads) < N_connection:
        server.listen(1)
        clientsocket, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsocket, username)
        newthread.start()
        threads.append(newthread)
    isalive()