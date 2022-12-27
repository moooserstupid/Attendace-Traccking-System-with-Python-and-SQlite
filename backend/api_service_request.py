import time
import zmq
import api_backend

class ServiceRequestAPI():
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:5555")
        self.backend = api_backend.BackendAPI()
    def send(self, message):
        message = message.encode('ascii')
        server.socket.send(message)
    def recieve(self):
        return server.socket.recv_string()


if __name__ == '__main__':
    server = ServiceRequestAPI()
    while True:
        print("Server Running")
        message = server.recieve()
        print("Received request: %s" % message)
        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
        #server.socket.send(b"World")
        message_tokens = message.split(',')
        if message_tokens[0] == 'Q1':
            username = message_tokens[1]
            password = message_tokens[2]
            reply = server.backend.authenticate_login([username, password])
            if reply is None:
                server.send('R1,None')
            else:
                server.send('R1,' + reply.__repr__())
        elif message_tokens[0] == 'Q2':
            '''
            sign up
            '''
            username = message_tokens[1]
            password = message_tokens[2]
            firstname = message_tokens[3]
            lastname = message_tokens[4]
            tc = message_tokens[5]
            server.backend()
            server.send('')



