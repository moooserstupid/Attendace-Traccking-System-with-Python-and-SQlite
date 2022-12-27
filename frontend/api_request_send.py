import zmq
class RequestSendAPI:
    def __init__(self):
        self.context = zmq.Context()
        print("Connecting to server")
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:5555")

    def send(self, msg):
        msg = msg.encode('ascii')
        try:
            self.socket.send(msg)
            print(msg)
        except Exception as e:
            print(e)


    def receive(self):
        message_tokens = None
        try:
            message = self.socket.recv_string()
            print("Received reply [ %s ]" % (message))
            message_tokens = message.split(',')
        except Exception as e:
            print(e)
        print("recv")
        return message_tokens


if __name__ == '__main__':
    client = RequestSendAPI()

    print("Sending request %s" % client.request)
    client.send("Q1,mosalah,123")
    client.receive()

