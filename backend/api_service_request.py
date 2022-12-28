import time
import zmq
import api_backend

from db_manager import DBManager

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
        return server.socket.recv().decode()


if __name__ == '__main__':
    server = ServiceRequestAPI()
    db = DBManager()
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
        elif message_tokens[0] == 'Q3':
            # Update username and password
            old_username = message_tokens[1]
            new_username = message_tokens[2]
            new_password = message_tokens[3]
            db.update_teacher_info(old_username, new_username, new_password)
            # server.send("R3,")
        elif message_tokens[0] == 'Q4':
            # Show Rows From Tabel
            tabel_name = message_tokens[1]
            rows = db.show_all_rows(tabel_name)
            data = ""
            for row in rows:
                for r in row:
                    data += str(r) + ";"
                data = data[:-1]
                data += ','
            data = data[:-1]
            server.send("R4,"+data)

        elif message_tokens[0] == 'Q5':
            # Get row from id
            tabel_name = message_tokens[1]
            column_id = message_tokens[2]
            data = ""
            row = db.get_row_from_id(tabel_name, column_id)
            for r in row:
                data += str(r) + ","
            data = data[:-1]
            server.send("R5,"+data)








