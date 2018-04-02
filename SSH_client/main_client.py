import socket
import sys

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
    message = str(user).encode('UTF-8')
    serversocket.sendall(message)
    flag_user = serversocket.recv(2048).decode('UTF-8')
    if flag_user == "TRUE":
        # check password
        while True:
            message = serversocket.recv(2048).decode('UTF-8')
            password = input(message)
            serversocket.sendall(password.encode('UTF-8'))
            flag_pass = serversocket.recv(2048).decode('UTF-8')
            if flag_pass == "TRUE":
                # Start Connection
                message = serversocket.recv(2048).decode('UTF-8')
                print(message)
                while True:
                    message = input("Enter command:")
                    serversocket.sendall(message.encode('UTF-8'))
                    message = serversocket.recv(2048)
                    print(message.decode('UTF-8'))
    else:
        print("Wrong username")
finally:
    print('closing socket')
    serversocket.close()