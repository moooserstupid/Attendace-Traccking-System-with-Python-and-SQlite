import re
import db_manager
from db_classes import Teacher
from datetime import datetime

class BackendAPI():
    def __init__(self):
        self.db = db_manager.DBManager()
        
        self.active_user = None
        self.username_rex = re.compile(r'[a-zA-Z0-9_]{8,36}$')
        self.password_rex = re.compile(r'[a-zA-Z0-9$@_/.]{4,}$')
        self.name_rex = re.compile(r'[a-zA-Z]{2,20}$')
        self.tc_rex = re.compile(r'[0-9]{11}$')
        self.studentid_rex = re.compile(r'[0-9]{9}$')
    def handle(self, request):
        '''101
        '''
    def authenticate_login(self, login_credentials):
        username = login_credentials[0]
        password = login_credentials[1]
        username_check = self.username_rex.match(username)
        password_check = self.password_rex.match(password)
        if username_check and password_check:
            query_result = self.db.user_login(username, password)
            print('Valid username and password')
            
            if query_result is not None:
                t = Teacher()
                print(query_result)
                t.set_teacher_attributes(query_result)
                self.active_user = t
                query_result = self.db.get_user_courses()
                if query_result is not None: 
                    self.active_user.set_course_attributes(query_result)
                    print('course info retrieved')
                return self.active_user
            else:
                print('Username or password not found') 
                
        else:
            print('Invalid username')
    def authenticate_signup(self, signup_credentials):
        '''
        
        
        '''
        
        username = signup_credentials[0]
        password = signup_credentials[1]
        firstname = signup_credentials[2]
        lastname = signup_credentials[3]
        tc = signup_credentials[4]
        username_check = True
        #username_check = self.username_rex.match(username)
        password_check = self.password_rex.match(password)
        firstname_check = self.name_rex.match(firstname)
        lastname_check = self.name_rex.match(lastname)
        tc_check = self.tc_rex.match(tc)
        if firstname_check and lastname_check:
            print('authenticate_signup: names pass the vibe check')
        else:
            return
        if tc_check:
            print('authenticate_signup: tc cool too')
        else: 
            return

        if username_check and password_check:
            if self.db.is_unique('member', 'username', username):
                print('authenticate_signup: username is unique')
                self.db.add_new_user(username, password, firstname, lastname, tc)
            else:
                print('authenticate_signup: username is taken')
                return
        else:
            return
        
    def add_course_list(self, course_list):
        if self.active_user is None:
            print('add_course_list: No logged in user')
            return
        for course in course_list:
            name = course[0]
            description = course[1]
            start_date = course[2]
            end_date = course[3]
            total_lesson_count = course[4]
            if self.db.add_new_course(name, description, start_date, end_date, total_lesson_count):
                print('add_course_list: ' + name + ' added successfully!')
            else:
                print('add_course_list: ' + name + ' could not be added.')

        return
    def edit_course_list(self, new_course_list):
        if self.active_user is None:
            print('')
        return
    def add_lesson_list(self, lesson_list):
        '''
        
        '''

        if self.active_user is None:
            print('add_lesson_list: No active user')
            return
        for lesson in lesson_list:
            date = lesson[0]
            courseid = lesson[1]
            course_info = self.db.get_row_from_id('course', courseid)
            print(course_info)
            if course_info is None:
                print('add_lesson_list: course {} has not been registered'.format(courseid))
                return
            start_date = course_info[4]
            end_date = course_info[5]

            if date >= start_date and date <= end_date:
                print('add_lesson_list: date {} is valid for course {}'.format(date, course_info[1]))
                if self.db.is_composite_key_unique('lesson', 'date', date, 'courseid', courseid):
                    print('composite key does not exist')
                    self.db.add_lesson(date, courseid)
                else:
                    print('composite key exists')
            else:
                print('add_lesson_list: date {} is invalid for course {}'.format(date, course_info[1]))
    def log_out(self):
        print('add_attendance_list: No active user')
        self.active_user = None
        return



        
    def add_attendance_list(self, lessonid, tc_list):
        if self.active_user is None:
            print('add_attendance_list: No active user')
            return
        query_result = self.db.get_row_from_id('lesson', lessonid)
        if query_result is None:
            print('That lesson session has not been created')
            return

        courseid = query_result[2]
        print(self.active_user.course_list)
        if int(courseid) not in self.active_user.course_list:
            print('That lesson session has not been created for this user')
            return
        
        for tc in tc_list:
            if self.tc_rex.match(tc):
                query_result = self.db.get_row_from_value('student', 'tc', tc)
                print(query_result)
                if query_result is None:
                    print('add_attendace_list: student with tc {} does not exist'.format(tc))
                    continue
                else:
                    studentid = query_result[0][1]
                    
                    if self.db.is_composite_key_unique('course_student', 'courseid', courseid, 'studentid', studentid):
                        print('student {} doesnt take course {}'.format(studentid, courseid))
                        continue
                    if self.db.is_composite_key_unique('attendance', 'lessonid', lessonid, 'studentid', studentid):
                        self.db.add_attendance(lessonid, studentid)
                    else:
                        print('attendance for student {} with lesson {} already exists'.format(studentid, lessonid))
            else:
                print('add_attendace_list: tc {} is invalid'.format(tc))

    
    def add_student_list(self, students):
        for student in students:
            studentid = student[0]
            if self.studentid_rex.match(studentid) is False:
                print('add_student_list: this studentid does not pass the vibe check')
                continue
            if self.db.is_unique('student', 'studentid', studentid):
                
                firstname = student[1]
                lastname = student[2]
                if self.name_rex.match(firstname) is False or self.name_rex.match(lastname) is False:
                    print('add_student_list: names are not cool enough.')
                    continue
                tc = student[3]
                if self.db.is_unique('student', 'tc', tc) and self.db.is_unique('teacher', 'tc', tc):

                    if self.tc_rex.match(tc) is False:
                        print('add_student_list: tc {} not cool'.format(tc))
                        continue
                    self.db.add_new_student(studentid, firstname, lastname, tc)
                else:
                    print('add_student_list: tc {} already exists in our system'.format(tc))
                    continue
            else:
                print('add_student_list: studentid {} already exists'.format(studentid))
                continue
    def add_student_to_course(self, courseid, studentid):
        if self.active_user is None:
            print('No active user')
            return
        if courseid not in self.active_user.course_list:
            print('add_student_to_course: this course has not been registered for the current user.')
            return
        if self.db.is_unique('student', 'studentid', studentid):
            print('add_student_to_course: this student has not been registered')
            return
        if self.db.is_composite_key_unique('course_student', 'courseid', courseid, 'studentid', studentid):
            self.db.add_student_to_course(courseid, studentid)

        else: 
            print('add_student_to_course: this student has already been added to this course')
            return
        print('course {} added to student {}'.format(courseid, studentid))
    def reset_table(self, table_name):
        self.db.delete_all_rows(table_name=table_name)

    def get_teacher_courses(self):
        '''
        Returns the courses a teacher is registered to give
        '''

        if self.active_user is None:
            print('get_teacher_courses: Teacher hasnt loggged in')
            return
        course_string = ''
        for course_id, course in self.active_user.course_list.items():
            course_attribute_list = course.get_attributes()
            for attribute in course_attribute_list:
                course_string += str(attribute) + ','
            course_string = course_string + '\n'
        return course_string
    
if __name__ == '__main__':
    backend_session = BackendAPI()
    query_result = backend_session.db.show_all_rows('attendance')
    print(query_result)
    print(backend_session.authenticate_login(['admin12345', 'pass12345']))
    print(backend_session.authenticate_login(['mosalah1', 'pass123']))
    #backend_session.add_attendance_list(1, ['99951326666'])
 
    