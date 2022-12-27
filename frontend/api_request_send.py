from backend.api_request_service import ServiceRequestAPI
import zmq
class RequestSendAPI:
    def __init__(self):
        self.request = None
        self.context = zmq.Context()
        print("Connecting to server")
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://193.255.169.20:5556")
        self.service = ServiceRequestAPI()
    def send(self, msg):
        self.socket.send(bin(msg))

    def receive(self):
        message = client.receive()
        print("Received reply %s [ %s ]" % (client.request, message))
        message_tokens = message.split(',')
        return message_tokens


if __name__ == '__main__':
    client = RequestSendAPI()

    print("Sending request %s" % client.request)
    client.send("Q1,mosalah,123")
    client.receive()

