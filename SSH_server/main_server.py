import socket, threading
from subprocess import Popen, PIPE

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

    def run(self):
        print("Connection from : ", clientAddress)
        self.clientsocket.sendall("Connecting".encode('UTF-8'))
        while True:
            message = self.clientsocket.recv(2048).decode('UTF-8')
            cmd = message.split()
            popen = Popen(cmd, stdout=PIPE)
            out, err = popen.communicate()
            self.clientsocket.sendall(out)


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
    user = clientsocket.recv(2048).decode('UTF-8')
    for u in username:
        if user == u[0]:
            # return flag_user = TRUE
            flag_user="TRUE"
            clientsocket.sendall(flag_user.encode('UTF-8'))
            while True:
                # check password
                clientsocket.sendall("Password: ".encode('UTF-8'))
                password = clientsocket.recv(2048).decode('UTF-8')
                if password == u[1]:
                    # return flag_pass = TRUE
                    flag_pass = "TRUE"
                    clientsocket.sendall(flag_pass.encode('UTF-8'))
                    newthread = ClientThread(clientAddress, clientsocket)
                    newthread.start()
                    break