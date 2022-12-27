
class Record():
    def __init__(self):
        self.id = None
        return

class Member(Record):

    def __init__(self):
        self.username = None
        self.password = None
        self.user = None
    def syntax_auth(self, name):
        excluded_character_list = [' ']
        if len(name) < 8 and len(name) > 32:
            print('Length')
            return None
        for char in excluded_character_list:
            if char in name:
                print('Excluded')
                return None
        print('Accepted')
        return name

    def get_teacher_info(self, c):
        c.execute('''SELECT * FROM teacher
                    WHERE (SELECT userID FROM member_login
                    WHERE username=:username 
                    AND password=:password)''',
                    {'username': self.username,
                    'password': self.password})
        return c.fetchall()

    def entry_point(self):
        username = input('Username: ')
        print(username)
        while (self.syntax_auth(username) is None):
            username = input('Please enter a valid Username: ')

        password = input('Password: ')
        while (self.syntax_auth(password) is None):
            password = input('Please enter a validPassword: ')
        self.username = username
        self.password = password

class Teacher(Record):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.tc = None
        self.course_list = {}
    def __repr__(self) -> str:
        return str(self.id)+','+str(self.firstname)+','+str(self.lastname)+','+str(self.tc)
    def init_attributes(self, id):

        firstname = input('Enter your first name: ')
        lastname = input('Enter your last name: ')
        tc = input('Enter your tc: ')
        while len(tc) != 13 or tc.isdigit() is not True:
            tc = input('Enter your tc: ')
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.tc = tc
    def set_teacher_attributes(self, teacher_info_list):
        self.id = teacher_info_list[0]
        self.firstname = teacher_info_list[1]
        self.lastname = teacher_info_list[2]
        self.tc = teacher_info_list[3]

        
    def set_course_attributes(self, course_info_list):
        for course in course_info_list:
            new_course = Course()
            new_course.set_attributes(course)
            self.course_list[new_course.id] = new_course

class Course(Record):

    def __init__(self):
        self.name = None
        self.teacherid = None
        self.description = None
        self.start_date = None
        self.end_date = None
        self.total_lesson_count = None
    def set_attributes(self, course_info):
        self.id = course_info[0]
        self.name = course_info[1]
        self.teacherid = course_info[2]
        self.description = course_info[3]
        self.start_date = course_info[4]
        self.end_date = course_info[5]
        self.total_lesson_count = course_info[6]
    def get_attributes(self):
        if self.id is None:
            print('get_attributes: course attributes not set')
            return []
        return_list = []
        return_list.append(self.id)
        return_list.append(self.name)
        return_list.append(self.teacherid)
        return_list.append(self.description)
        return_list.append(self.start_date)
        return_list.append(self.end_date)
        return_list.append(self.total_lesson_count)
        return return_list
        

class Lesson(Record):

    def __init__(self):
        self.date = None
        self.courseid = None

class Attendance(Record):
    def __init__(self):

        self.lessonid = None
        self.studentid = None

class Student(Record):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.tc = None
        self.course_list = {}
    def set_attributes(self):
        return
    def add_course(self, course):
        self.course_list[course.id] = course

class Course_Student(Record):
    def __init__(self):
        self.courseid = None
        self.studentid = None
    