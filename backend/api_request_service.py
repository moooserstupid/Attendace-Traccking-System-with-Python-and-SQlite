import re
import db_manager
from db_classes import Teacher

class RequestServiceAPI():
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
                    t.set_course_attributes(query_result)
                    print('course info retrieved')
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
            if self.db.is_unique('member', username):
                print('authenticate_signup: username is unique')
                #self.db.add_new_user(username, password, firstname, lastname, tc)
            else:
                return
        else:
            return
        
    def new_user_creation(self):
        return
    def add_lesson(self):
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
        return
    def add_attendance_list(self):
        return
    def add_student_list(self, course_id, students):
        for student in students:
            studentid = student[0]
            if self.studentid_rex.match(studentid) is False:
                print('add_student_list: this studentid does not pass the vibe check')
                return
            if self.db.is_unique('student', studentid):
                firstname = student[1]
                lastname = student[2]
                if self.name_rex.match(firstname) is False or self.name_rex.match(lastname) is False:
                    print('add_student_list: names are not cool enough.')
                    return 
                tc = student[3]
                if self.tc_rex.match(tc) is not True:
                    print('add_student_list: tc not cool')
                    return
                self.db.add_new_student(studentid, firstname, lastname, tc)


    def get_teacher_courses(self):
        '''
        Returns the courses a teacher is registered to give
        '''

        if self.active_user is None:
            print('get_teacher_courses: Teacher hasnt loggged in')
            return
        return self.active_user.course_list
        
    
if __name__ == '__main__':
    requestAPI = RequestServiceAPI()
    query_result = requestAPI.db.show_all_rows('member')
    print(query_result)
    for result in query_result[0]:
        if isinstance(result, str): 
            print(result)
    requestAPI.authenticate_signup(['admin123456', 'pass12345', 'James', 'Franco', '99952226666'])
    
    # requestAPI.authenticate_login(['admin12345', 'pass12345'])
    # print(requestAPI.active_user.course_list)