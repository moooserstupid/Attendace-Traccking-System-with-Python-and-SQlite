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
                server.send('R1,failed')
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
            if server.backend.authenticate_signup([username, password, firstname, lastname, tc]):
                server.send('R2,success')
            else:
                server.send('R2,failed')
        elif message_tokens[0] == 'Q3':
            # Update username and password
            old_username = message_tokens[1]
            new_username = message_tokens[2]
            new_password = message_tokens[3]
            if server.backend.db.update_teacher_info(old_username, new_username, new_password):
                server.send("R3,success")
            else:
                server.send('R3,failed')
        elif message_tokens[0] == 'Q4':
            # Show Rows From Tabel
            table_name = message_tokens[1]
            rows = server.backend.db.show_all_rows(table_name)
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
            table_name = message_tokens[1]
            column_id = message_tokens[2]
            data = ""
            #row = db.get_row_from_id(tabel_name, column_id)
            for r in row:
                data += str(r) + ","
            data = data[:-1]
            server.send("R5,"+data)
        elif message_tokens[0] == 'Q6':
            # Add course
            name = message_tokens[1]
            description = message_tokens[2]
            start_date = message_tokens[3]
            end_date = message_tokens[4]
            lesson_count = message_tokens[5]
            if server.backend.add_course([name, description, start_date, end_date, lesson_count]):
                server.send('R6,success')
            else:
                server.send('R6,failed')
        
        elif message_tokens[0] == 'Q7':
            # Add lesson
            date = message_tokens[1]
            courseid = message_tokens[2]
            if server.backend.add_lesson([date, courseid]):
                server.send('Q7,success')
            else:
                server.send('Q7,failed')
        elif message_tokens[0] == 'Q8':
            # Add student id
            studentid = message_tokens[1]
            firstname = message_tokens[2]
            lastname = message_tokens[3]
            tc = message_tokens[4]
            if server.backend.add_student([studentid, firstname, lastname, tc]):
                server.send('R8,failed')
            else:
                server.send('R8,success')
            
            
        elif message_tokens[0] == 'Q9':
            # Add selected student to course
            courseid = message_tokens[1]
            studentid = message_tokens[2]
            if server.backend.add_student_to_course(courseid, studentid):
                server.send('R9,success')
            else:
                server.send('R9,failed')
            
        elif message_tokens[0] == 'Q10':
            #take attendance
            lessonid = message_tokens[1]
            tc = message_tokens[2]
            if server.backend.add_attendance(lessonid, tc):
                server.send('R10,success')
            else:
                server.send('R10,failed')









