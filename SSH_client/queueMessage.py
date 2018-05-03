import socket
import queue
class SendMessage():
    def __init__(self, encode="UTF-8"):
        self.encode = encode
        self.send_queue = queue.Queue()

    def put(self, message):
        if isinstance(message, bytes):
            self.send_queue.put(message)
        else:
            message = message.encode('UTF-8')
            self.send_queue.put(message)

    def get(self):
        return self.send_queue.get()

class RecvMessage():
    def __init__(self, encode="UTF-8"):
        self.encode = encode
        self.recv_message = queue.Queue()

    def put(self , message):
        if isinstance(message, bytes):
            self.recv_message.put(message)
        else:
            message = message.encode('UTF-8')
            self.recv_message.put(message)

    def get(self):
        message = self.recv_message.get()
        if isinstance(message, bytes):
            return message.decode('UTF-8')
        else:
            return self.recv_message.get()


if __name__ == "__main__":
    sm = SendMessage()
    sm.put('Hello'.encode('UTF-8'))
    sm.put('World')
    print(sm.get())
    print(sm.get())

    # sm = RecvMessage()
    # sm.put('Hello'.encode('UTF-8'))
    # sm.put('World')
    # print(sm.get())
    # print(sm.get())

