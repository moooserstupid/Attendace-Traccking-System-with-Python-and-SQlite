import sqlite3
import os
from datetime import date, timezone
import logging
class DBManager():
    def __init__(self):
        self.conn = None
        self.c = None
        self.active_user = None
        self.active_course = None
        self.active_lesson = None
        self.table_names = ('member', 'teacher', 'student', 'course', 'lesson', 'attendance')
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
        path = os.path.dirname(os.path.realpath(__file__))
        self.conn = sqlite3.connect(os.path.join(path, 'attendance_system.db'), 
                                    detect_types=sqlite3.PARSE_DECLTYPES|
                                    sqlite3.PARSE_COLNAMES)
        self.c = self.conn.cursor()
    def disconnect_db(self):
        self.conn.commit()
        self.conn.close()

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
                                WHERE id =:userID''',{'userID':userID})
            return_value = self.c.fetchall()
        else:
            return_value = None
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
        self.c.execute('''SELECT id FROM member
                            WHERE username=:username''', {'username': username})
        query_result = self.c.fetchone()
        if query_result is not None:
            
            print('Username is not unique')
            self.disconnect_db()
            return False
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
        except sqlite3.Error as err:
            #print(err.message)
            #logging.error(err.__cause__)
            print('Could not add course')
        finally:
            self.disconnect_db()
        return True
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
    def add_new_student(self, firstname, lastname, studentid, tc):
        if self.active_user is None:
            print('No active user')
            return False
        if self.active_course is None:
            print('No course has been selected')
            return False
        self.connect_db()
        self.c.execute('''SELECT EXISTS
                            (SELECT 1 FROM student
                            WHERE tc = :tc) ''', {'tc': tc})
        query_result = self.c.fetchone()
        if query_result is True:
            print('This student already exists')
            return False
        self.increment_last_row_dict('student')

        self.c.execute('''INSERT INTO student VALUES
                            (:id, 
                            :firstname, 
                            :lastname,
                            :studentid,
                            :tc)''', 
                            {'id': self.last_insert_rowid_dict['student'], 
                            'firstname': firstname,
                            'lastname': lastname, 
                            'studentid': studentid,
                            'tc': tc})
        self.disconnect_db()
    def add_student_to_course(self, studentid, courseid):
        return
    # def add_new_entity(self, table_name: str, entity_values: dict):
    #     if self.active_user is None:
    #         print('No active user')
    #         return False
    #     if table_name not in self.table_names:
    #         print('Table does not exist')
    #         return False
    #     self.connect_db()
        

    #     self.increment_last_row_dict[table_name]

    #     value_placeholder = '('
    #     for count, key in enumerate(entity_values):
    #         if count < len(entity_values) - 1:
    #             value_placeholder = value_placeholder + ':' + key + ','
    #         else:
    #             value_placeholder = value_placeholder + ':' + key + ')'
    #     query_string = 'INSERT INTO ' + table_name + ' VALUES' + value_placeholder
        
    #     self.c.execute(query_string, entity_values)
        
    #     self.disconnect_db()
    #     print('Course added')
    #     return True
    def check_if_unique(self, table_name, id):
        return
    def increment_last_row_dict(self, table_name):
        if self.last_insert_rowid_dict[table_name] is not None:
            self.last_insert_rowid_dict[table_name] += 1
        else:
            self.last_insert_rowid_dict[table_name] = 1

if __name__ == '__main__':
    db = DBManager()
    
        