#import sqlite3
import db_classes as record
import db_manager as db
from datetime import datetime
# conn = sqlite3.connect('attendance_system.db', detect_types=sqlite3.PARSE_DECLTYPES |
#                                                         sqlite3.PARSE_COLNAMES)
# c = conn.cursor()

# class DatabaseManager():

    # def __init__(self):
    #     # self.conn = sqlite3.connect(':memory:')
    #     # self.c = self.conn.cursor()
    #     return
    # def insert_into(self, table_name: str, value_dict : dict):
    #     value_placeholder = '('
    #     for count, key in enumerate(value_dict):
    #         if count < len(value_dict) - 1:
    #             value_placeholder = value_placeholder + ':' + key + ','
    #         else:
    #             value_placeholder = value_placeholder + ':' + key + ')'
    #     query_string = 'INSERT INTO ' + table_name + ' VALUES' + value_placeholder
        
    #     c.execute(query_string, value_dict)
    #     return c.fetchall()

# def create_login_table():
#     with conn:
#         c.execute('''CREATE TABLE IF NOT EXISTS member 
#                         (id INTEGER NOT NULL,
#                         username TEXT NOT NULL, 
#                         password TEXT NOT NULL, 
#                         userID INTEGER NOT NULL,
#                         CONSTRAINT login_pk PRIMARY KEY (username),
#                         CONSTRAINT member_teacher_fk FOREIGN KEY (userID)
#                         REFERENCES teacher(id))''')
# def insert_login_table(id, username, password, userID):
#     with conn:
#         c.execute('''INSERT INTO teacher VALUES
#                             (:id,
#                             :username, 
#                             :password,
#                             :userID)''', 
#                             {'id': id,
#                             'username': username, 
#                             'password': password,
#                             'userID': userID})

# def get_teacher_id(username, password):
#     c.execute('''SELECT userID FROM member
#                 WHERE username=:username 
#                 AND password=:password''',
#                 {'username': username,
#                 'password': password})
#     return c.fetchall()

# def create_teacher_table():
#     with conn:
#         c.execute('''CREATE TABLE IF NOT EXISTS teacher 
#                         (id INTEGER NOT NULL,
#                         firstname TEXT NOT NULL, 
#                         lastname TEXT NOT NULL, 
#                         tc TEXT NOT NULL,
#                         CONSTRAINT teacher_pk PRIMARY KEY (id))''')
# def insert_teacher_table(teacher: record.Teacher):
#     with conn:
#         c.execute('''INSERT INTO teacher VALUES
#                             (:id,
#                             :firstname, 
#                             :lastname,
#                             :tc)''', 
#                             {'id': teacher.id,
#                             'firstname': teacher.firstname, 
#                             'lastname': teacher.lastname,
#                             'tc': teacher.tc})
# def get_teacher_from_login(userID):
#     c.execute('''SELECT * FROM teacher
#                 WHERE id=:userID''',
#                 {'userID': userID})
#     return c.fetchall()
# def get_all_teachers():
#     c.execute('''SELECT * FROM teacher''')
#     return c.fetchall()


# def create_course_table():
#     with conn:
#         c.execute('''CREATE TABLE IF NOT EXISTS course 
#                         (id INTEGER NOT NULL, 
#                         name TEXT NOT NULL, 
#                         teacherid INTEGER NOT NULL, 
#                         description TEXT,
#                         start_date timestamp NOT NULL,
#                         end_date timestamp NOT NULL,
#                         total_lesson_count INTEGER NOT NULL,
#                         CONSTRAINT course_pk PRIMARY KEY (id),
#                         CONSTRAINT course_teacher_fk FOREIGN KEY(teacherid)
#                         REFERENCES teacher(id))''')

# def insert_course_table(course):
#     with conn:
#         c.execute('''INSERT INTO course VALUES
#                             (:id, 
#                             :name, 
#                             :teacherid,
#                             :description,
#                             :start_date,
#                             :end_date,
#                             :total_lesson_count)''', 
#                             {'id': course.id, 
#                             'name': course.name,
#                             'teacherid': course.teacherid, 
#                             'description': course.description,
#                             'start_date': course.start_date,
#                             'end_date': course.end_date,
#                             'total_lesson_count': course.total_lesson_count})
# def get_course_teacher(teacherid):
#     c.execute('''SELECT * FROM course 
#                 WHERE teacherid=:teacherid''', 
#                 {'teacherid': teacherid})
#     return c.fetchall()

# def create_student_table():
#     with conn:
#         c.execute('''CREATE TABLE IF NOT EXISTS student 
#                         (id INTEGER NOT NULL, 
#                         firstname TEXT NOT NULL, 
#                         lastname TEXT NOT NULL, 
#                         studentid TEXT NOT NULL,
#                         tc TEXT NOT NULL,
#                         CONSTRAINT student_pk PRIMARY KEY (id))''')
# def insert_student_table(student):
#     with conn:
#         c.execute('''INSERT INTO student VALUES
#                             (:id, 
#                             :firstname, 
#                             :lastname,
#                             :studentid,
#                             :tc)''', 
#                             {'id': student.id, 
#                             'firstname': student.firstname,
#                             'lastname': student.lastname, 
#                             'studentid': student.studentid,
#                             'tc': student.tc})
# def get_student_from_tc(tc):
#     c.execute('''SELECT * FROM student 
#                 WHERE tc=:tc''', 
#                 {'tc': tc})
#     return c.fetchall()

# def create_lesson_table():
#     with conn:
#         c.execute('''CREATE TABLE IF NOT EXISTS lesson
#                         (id INTEGER NOT NULL, 
#                         date DATE NOT NULL, 
#                         courseid TEXT NOT NULL,
#                         CONSTRAINT lesson_pk PRIMARY KEY (id), 
#                         CONSTRAINT lesson_course_fk FOREIGN KEY(courseid)
#                             REFERENCES course(id))''')
# def insert_lesson_table(lesson):
#     with conn:
#         c.execute('''INSERT INTO lesson VALUES
#                             (:id, 
#                             :date, 
#                             :courseid)''', 
#                             {'id': lesson.id, 
#                             'date': lesson.date,
#                             'courseid': lesson.courseid})


# def create_attendance_table():
#     with conn:
#         c.execute('''CREATE TABLE IF NOT EXISTS attendance
#                         (id INTEGER NOT NULL, 
#                         lessonid TEXT NOT NULL, 
#                         studentid TEXT NOT NULL,
#                         CONSTRAINT attendance_pk PRIMARY KEY (id),
#                         CONSTRAINT attendance_lesson_fk FOREIGN KEY(lessonid)
#                             REFERENCES lesson(id),
#                         CONSTRAINT attendance_student_fk FOREIGN KEY(studentid)
#                             REFERENCES student(id))''')
# def insert_attendance_table(attendance):
#     with conn:
#         c.execute('''INSERT INTO lesson VALUES
#                             (:id, 
#                             :lessonid, 
#                             :studentid)''', 
#                             {'id': attendance.id, 
#                             'lessonid': attendance.lessonid,
#                             'studentid': attendance.studentid})
# def get_attendances_from_lesson(lessonid):
#     c.execute('''SELECT * FROM attendance 
#                 WHERE lessonid=:lessonid''', 
#                 {'lessonid': lessonid})
#     return c.fetchall()

# create_login_table()
# create_teacher_table()
# create_course_table()
# create_lesson_table()
# create_student_table()
# create_attendance_table()


# t = record.Teacher()

# c.execute('''SELECT * FROM teacher''')
# print(c.fetchall())
# t.set_attributes([[1, 'Ali', 'Asghar', '9995132222']], [])

# #member.entry_point()
#insert_login_table(1, 'admin12345', 'pass12345', t.id)
# #c.execute('''SELECT id FROM teacher WHERE rowid = (SELECT MAX(rowid) FROM teacher)''')
# #last_row_id = c.fetchall()
# #print(last_row_id)
# conn.close()
#new_db = db.DBManager()
#new_db.add_new_user(1, 'admin', 'pass12345')
#print(new_db.delete_row('teacher',1))
#new_db.add_new_user('admin12345', 'pass12345', 'Ali', 'Asghar', '99951328888')
#print(new_db.user_login('admin12345', 'pass12345'))
#print(new_db.add_new_course('Introduction to Audio Sampling', None, datetime(2022 , 12, 20), datetime(2023, 1, 1), 11))
#print(new_db.delete_all_rows('course'))
# print(new_db.show_all_rows('course'))
# print(new_db.last_insert_rowid_dict)
date_str = '2020-12-01 00:00:00'
date_list = date_str.split(' ')
new_date_list = date_list[0].split('-')
date = datetime(int(new_date_list[0]), int(new_date_list[1]), int(new_date_list[2]))
print(date)

