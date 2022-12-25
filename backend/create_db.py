from datetime import datetime
import sqlite3
import os
import db_classes
path = os.path.dirname(os.path.realpath(__file__))
conn = sqlite3.connect(os.path.join(path, 'attendance_system.db'), 
                                    detect_types=sqlite3.PARSE_DECLTYPES|
                                    sqlite3.PARSE_COLNAMES)
c = conn.cursor()
def create_login_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS member 
                        (id INTEGER NOT NULL,
                        username TEXT NOT NULL, 
                        password TEXT NOT NULL, 
                        userID INTEGER NOT NULL,
                        CONSTRAINT login_pk PRIMARY KEY (username),
                        CONSTRAINT member_teacher_fk FOREIGN KEY (userID)
                        REFERENCES teacher(id))''')
def create_teacher_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS teacher 
                        (id INTEGER NOT NULL,
                        firstname TEXT NOT NULL, 
                        lastname TEXT NOT NULL, 
                        tc TEXT NOT NULL,
                        CONSTRAINT teacher_pk PRIMARY KEY (id))''')
def create_course_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS course 
                        (id INTEGER NOT NULL, 
                        name TEXT NOT NULL, 
                        teacherid INTEGER NOT NULL, 
                        description TEXT,
                        start_date timestamp NOT NULL,
                        end_date timestamp NOT NULL,
                        total_lesson_count INTEGER NOT NULL,
                        CONSTRAINT course_pk PRIMARY KEY (id),
                        CONSTRAINT course_teacher_fk FOREIGN KEY(teacherid)
                        REFERENCES teacher(id))''')
def create_student_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS student 
                        (id INTEGER NOT NULL, 
                        studentid TEXT NOT NULL,
                        firstname TEXT NOT NULL, 
                        lastname TEXT NOT NULL,
                        tc TEXT NOT NULL UNIQUE,
                        CONSTRAINT student_pk PRIMARY KEY (studentid))''')
def create_student_course_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS course_student 
                        (id INTEGER NOT NULL,
                        courseid INTEGER NOT NULL, 
                        studentid TEXT NOT NULL,
                        CONSTRAINT course_student_pk PRIMARY KEY (id),
                        CONSTRAINT sc_course_fk FOREIGN KEY(courseid)
                            REFERENCES course(id),
                        CONSTRAINT sc_student_fk FOREIGN KEY(studentid)
                            REFERENCES student(studentid))''')
def create_lesson_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS lesson
                        (id INTEGER NOT NULL, 
                        date timestamp NOT NULL, 
                        courseid TEXT NOT NULL,
                        CONSTRAINT lesson_pk PRIMARY KEY (id), 
                        CONSTRAINT lesson_course_fk FOREIGN KEY(courseid)
                            REFERENCES course(id))''')
def create_attendance_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS attendance
                        (id INTEGER NOT NULL, 
                        lessonid TEXT NOT NULL, 
                        studentid TEXT NOT NULL,
                        CONSTRAINT attendance_pk PRIMARY KEY (id),
                        CONSTRAINT attendance_lesson_fk FOREIGN KEY(lessonid)
                            REFERENCES lesson(id),
                        CONSTRAINT attendance_student_fk FOREIGN KEY(studentid)
                            REFERENCES student(studentid))''')

def insert_teacher_table(teacher):
    with conn:
        c.execute('''INSERT INTO teacher VALUES
                            (:id,
                            :firstname, 
                            :lastname,
                            :tc)''', 
                            {'id': teacher.id,
                            'firstname': teacher.firstname, 
                            'lastname': teacher.lastname,
                            'tc': teacher.tc})

def insert_login_table(id, username, password, userID):
    with conn:
        c.execute('''INSERT INTO member VALUES
                            (:id,
                            :username, 
                            :password,
                            :userID)''', 
                            {'id': id,
                            'username': username, 
                            'password': password,
                            'userID': userID})

def insert_course_table(course):
    with conn:
        c.execute('''INSERT INTO course VALUES
                            (:id, 
                            :name, 
                            :teacherid,
                            :description,
                            :start_date,
                            :end_date,
                            :total_lesson_count)''', 
                            {'id': course.id, 
                            'name': course.name,
                            'teacherid': course.teacherid, 
                            'description': course.description,
                            'start_date': course.start_date,
                            'end_date': course.end_date,
                            'total_lesson_count': course.total_lesson_count})

def insert_course_student_table(id, courseid, studentid):
    with conn:
        c.execute('''INSERT INTO course_student VALUES
                            (:id,
                            :courseid, 
                            :studentid)''', 
                            {'id': id,
                            'courseid': courseid, 
                            'studentid': studentid})

def db_master():
    t = db_classes.Teacher()
    c = db_classes.Course()
    t.set_teacher_attributes([1, 'Ali', 'Asghar', '9995132222'])
    c.set_attributes([1, 'Introduction to Audio Sampling', 1, None, datetime(2022 , 12, 20), datetime(2023, 1, 1), 11])
    #insert_teacher_table(t)
    insert_login_table(1, 'admin12345', 'pass12345', 1)
    insert_course_table(c)

    return
create_login_table()
create_teacher_table()
create_course_table()
create_lesson_table()
create_student_table()
create_attendance_table()
create_student_course_table()

db_master()