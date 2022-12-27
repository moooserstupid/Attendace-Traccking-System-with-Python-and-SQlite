import sqlite3
import os
from datetime import date, timezone
import sys
import db_classes as record
class DBManager():
    def __init__(self):
        self.conn = None
        self.c = None
        self.is_db_conn_open = False
        self.active_user = None
        self.active_course = None
        self.active_lesson = None
        self.table_names = ('member', 'teacher', 'student', 'course', 'lesson', 'attendance', 'course_student')
        self.table_dict = {'member': record.Member, 'teacher': record.Teacher, 
                            'student': record.Student, 'course': record.Course,
                            'lesson': record.Lesson, 'attendance': record.Attendance,
                            'course_student': record.Course_Student}
        
        self.last_insert_rowid_dict = {}
        self.connect_db()
        for table in self.table_names:
            self.c.execute('''SELECT id FROM ''' + table +  
                            ''' WHERE rowid = (SELECT MAX(rowid) FROM '''+ table + ''')''')
            query_result = self.c.fetchall()
            if not query_result:
                self.last_insert_rowid_dict[table] = None
            else: 
                self.last_insert_rowid_dict[table] = int(query_result[0][0])
        self.disconnect_db()

    def connect_db(self):
        try:
            path = os.path.dirname(os.path.realpath(__file__))
            self.conn = sqlite3.connect(os.path.join(path, 'attendance_system.db'), 
                                        detect_types=sqlite3.PARSE_DECLTYPES|
                                        sqlite3.PARSE_COLNAMES)
            self.c = self.conn.cursor()
            self.is_db_conn_open = True
        except Exception as e:
            print('db_manager: Could not open a db connection')
        
    def disconnect_db(self):
        try:
            self.conn.commit()
            self.conn.close()
            self.is_db_conn_open = False
        except Exception as e:
            print('db_manager: Could not commit changes and close the db connection')

    def user_login(self, username, password):
        return_value = None
        self.connect_db()
        self.c.execute('''SELECT userID FROM member
                WHERE username=:username 
                AND password=:password''',
                {'username': username,
                'password': password})
        query_result = self.c.fetchall()
        if query_result:
            userID = query_result[0][0]
            print(userID)
            self.active_user = userID
            self.c.execute('''SELECT * FROM teacher 
                                WHERE id =:userID''',
                                {'userID':userID})
            return_value = self.c.fetchone()
        else:
            return_value = None
        self.disconnect_db()
        return return_value
    def get_user_courses(self):
        return_value = None
        if self.active_user is None:
            print('db_manager: No active_user')
            return return_value
        self.connect_db()
        self.c.execute('''SELECT * FROM course 
                            WHERE teacherid = :id''', 
                            {'id': self.active_user})
        return_value = self.c.fetchall()
        self.disconnect_db()
        return return_value
    def delete_row(self, table_name, row_id):
        if table_name not in self.table_names:
            print('Table ' + table_name + ' does not exist')
            return False   
        if self.last_insert_rowid_dict[table_name] is None:
            print('Table ' + table_name + ' does not have any rows')
            return False
        if self.last_insert_rowid_dict[table_name] < row_id:
            print('Invalid row number for table ' + table_name)
            return False
        
        self.connect_db()
        self.c.execute('''SELECT * FROM {}
                            WHERE id = :row_id'''.format(table_name), 
                            {'row_id': row_id})
        query_result = self.c.fetchall()
        print(query_result)
        if query_result:
            self.c.execute('''DELETE FROM {}
                                WHERE id = :row_id'''.format(table_name),
                                {'row_id': row_id})
            print('row deleted')
            if row_id == self.last_insert_rowid_dict[table_name]:
                if row_id == 1:
                    self.last_insert_rowid_dict[table_name] = None
                else:
                    self.last_insert_rowid_dict[table_name] -= 1
            self.disconnect_db()
            return True
        else:
            self.disconnect_db()
            return False
    def delete_all_rows(self, table_name):
        if table_name not in self.table_names:
            print('Table ' + table_name + ' does not exist')
            return False
        if self.last_insert_rowid_dict[table_name] is None:
            print('Table ' + table_name + ' does not have any rows')
            return False

        
        self.connect_db()
        self.c.execute('''DELETE FROM {}'''.format(table_name))
        print('Table' + table_name + ' has been reset')
        self.last_insert_rowid_dict[table_name] = None
        self.disconnect_db()
        return True
    def show_all_rows(self, table_name):
        if table_name not in self.table_names:
            print('Table ' + table_name + ' does not exist')
            return False
        if self.last_insert_rowid_dict[table_name] is None:
            print('Table ' + table_name + ' does not contain any data')
            return False
        self.connect_db()
        self.c.execute('''SELECT * FROM {}'''.format(table_name))
        query_result = self.c.fetchall()
        self.disconnect_db()
        return query_result
    def add_new_user(self, username, password, firstname, lastname, tc):
        self.connect_db()
        self.increment_last_row_dict('teacher')
        self.increment_last_row_dict('member')

        self.c.execute('''INSERT INTO teacher VALUES
                             (:id,
                             :firstname, 
                             :lastname,
                             :tc)''', 
                             {'id': self.last_insert_rowid_dict['teacher'],
                             'firstname': firstname, 
                             'lastname': lastname,
                             'tc': tc})
        
        self.c.execute('''INSERT INTO member VALUES
                             (:id,
                             :username, 
                             :password,
                             :userID)''', 
                             {'id': self.last_insert_rowid_dict['member'],
                             'username': username, 
                             'password': password,
                             'userID': self.last_insert_rowid_dict['teacher']})
        self.disconnect_db()
    def add_new_course(self, name, description, start_date: date, end_date: date, total_lesson_count):
        if self.active_user is None:
            print('No active user')
            return False
        self.connect_db()
        return_value = False
        try:
            self.increment_last_row_dict('course')
            self.c.execute('''INSERT INTO course VALUES
                                (:id, 
                                :name, 
                                :teacherid,
                                :description,
                                :start_date,
                                :end_date,
                                :total_lesson_count)''', 
                                {'id': self.last_insert_rowid_dict['course'], 
                                'name': name,
                                'teacherid': self.active_user, 
                                'description': description,
                                'start_date': start_date,
                                'end_date': end_date,
                                'total_lesson_count': total_lesson_count})
            
            print('Course added')
            return_value = True
        except sqlite3.Error as err:
            print('Could not add course')
            self.decrement_last_row_dict('course')
            return_value = False
        finally:
            self.disconnect_db()
            return return_value
        
    def find_student(self, tc):
        if self.active_user is None:
            print('No active user')
            return False
        if self.active_course is None:
            print('No course has been selected')
            return False
        
        self.connect_db()
        self.c.execute('''SELECT * FROM student
                            WHERE tc = :tc''', {'tc': tc})
        query_result = self.c.fetchone()
        print('Found')
        self.disconnect_db()
        return query_result
    def select_course(self, course_id):
        self.active_course = course_id
    def add_attendance(self, lessonid, studentid):
        try:
            self.connect_db()
            self.increment_last_row_dict('attendance')

            self.c.execute('''INSERT INTO attendance VALUES
                                (:id,
                                :lessonid, 
                                :studentid)''', 
                                {'id': self.last_insert_rowid_dict['attendance'],
                                'lessonid': lessonid, 
                                'studentid': studentid})
            print(sys._getframe().f_code.co_name + ': Attendance for student {} lesson {} inserted successfully'.format(studentid, lessonid))
        except Exception as e:
            print(e)
            self.decrement_last_row_dict('attendance')
            print(sys._getframe().f_code.co_name + ': Attendance insert failure student {} lesson {}'.format(studentid, lessonid))
        finally:
            self.disconnect_db()
    def add_new_student(self, studentid, firstname, lastname, tc):
        if self.active_user is None:
            print('No active user')
            return False
        self.connect_db()
        try:

            self.increment_last_row_dict('student')

            self.c.execute('''INSERT INTO student VALUES
                                (:id,
                                :studentid, 
                                :firstname, 
                                :lastname,
                                :tc)''', 
                                {'id': self.last_insert_rowid_dict['student'],
                                'studentid': studentid, 
                                'firstname': firstname,
                                'lastname': lastname, 
                                'tc': tc})
        except Exception as e:
            print(sys._getframe().f_code.co_name + ': Could not insert student with id ' + studentid)
            self.decrement_last_row_dict('student')
        finally:
            self.disconnect_db()
    def add_student_to_course(self, courseid, studentid):

        self.connect_db()
        self.increment_last_row_dict('course_student')
        self.c.execute('''INSERT INTO course_student VALUES
                            (:id,
                            :courseid,
                            :studentid)''', 
                            {'id' : self.last_insert_rowid_dict['course_student'],
                            'courseid' : courseid,
                            'studentid' : studentid})
        self.disconnect_db()
        
        return
    def add_lesson(self, date, courseid):

        return_value = None
        self.connect_db()
        self.c.execute('''INSERT INTO lesson VALUES
                            (:id,
                            :date,
                            :courseid)''',
                            {'id': self.last_insert_rowid_dict['lesson'],
                            'date': date,
                            'courseid': courseid})
        query_result = self.c.fetchone()
        if query_result:
            return_value = query_result
        else:
            return_value = None 
        self.disconnect_db()
        return return_value
    def get_row_from_value(self, table_name, column_name, value):
        return_value = None
        self.connect_db()
        self.c.execute('''SELECT * FROM {}
                            WHERE {} = :value'''.format(table_name, column_name),
                            {'value': value})
        return_value = self.c.fetchall()
        
        self.disconnect_db()
        if return_value:
            return return_value
        else:
            return None
    def get_row_from_id(self, table_name, row_id):
        
        self.connect_db()
        
        self.c.execute('''SELECT * FROM {}
                            WHERE id = :row_id'''.format(table_name), 
                            {'row_id': row_id})
        query_result = self.c.fetchone()
        self.disconnect_db()
        if query_result:
            return query_result
        else:
            return None
    def is_unique(self, table_name, column_name, id):
        if table_name not in self.table_names:
            print('is_unique: table {} does not exist'.format(table_name))
            return False
        return_value = False
        self.connect_db()
        self.c.execute('''SELECT EXISTS
                            (SELECT 1 FROM {}
                            WHERE {} = :row_id)'''.format(table_name, column_name), 
                                {'row_id': id})
        query_result = self.c.fetchone()[0]
        print(query_result)
        self.disconnect_db()
        if query_result:
            print('is_unique: value {} for row {} already exists'.format(id, column_name))
            return_value = False
        else:
            print('is_unique: this row does not exist')
            return_value = True
        return return_value
    def is_composite_key_unique(self, table_name, column1_name, column1_value, column2_name, column2_value):
        self.connect_db()
        self.c.execute('''SELECT EXISTS
                            (SELECT 1 FROM {}
                            WHERE {} = :value1
                            AND {} = :value2)'''.format(table_name, 
                            column1_name, column2_name),
                            {'value1': column1_value,
                            'value2': column2_value})
        query_result = self.c.fetchone()
        print(query_result)
        self.disconnect_db()
        if query_result is not None: query_result = query_result[0]    
        if query_result:
            print('is_composite_key_unique: composite key with the values {} {} exist'.format(
                column1_value, column2_value))
            return False
        else:
            print('is_composite_key_unique: composite key with the values {} {} does not exist'.format(
                column1_value, column2_value))
            return True

    def increment_last_row_dict(self, table_name):
        if self.last_insert_rowid_dict[table_name] is None:
            self.last_insert_rowid_dict[table_name] = 1
        else:
            self.last_insert_rowid_dict[table_name] += 1
    def decrement_last_row_dict(self, table_name):
        if self.last_insert_rowid_dict[table_name] is None:
            return
        if self.last_insert_rowid_dict[table_name] - 1 == 0:
            self.last_insert_rowid_dict[table_name] = None
        else:
            self.last_insert_rowid_dict[table_name] -= 0

if __name__ == '__main__':
    db = DBManager()
    
        