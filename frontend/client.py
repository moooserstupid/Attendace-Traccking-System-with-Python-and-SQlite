import zmq
context = zmq.Context()
print("Connecting to hello world server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://193.255.169.20:5556")

for request in range(10):
    print("Sending request %s" % request)
    socket.send(b"Hello")
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))