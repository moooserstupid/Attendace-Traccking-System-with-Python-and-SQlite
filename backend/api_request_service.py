import db_manager

class RequestServiceAPI():
    def __init__(self):
        self.db = db_manager()
        self.active_user = None
    def handle(self, request):
        '''101
        '''
    def authenticate_login(self, login_credentials):
        if len(login_credentials) == 2:
            if len(self.db.get_user_id()) == 1:
                
        else:
    def authenticate_signup(self, signup_credentials):
        return
    def new_user_creation(self):
        return
    def exisitng_user_access(self):
        return
    def add_lesson(self):
        return
    def add_course_list(self):
        return
    def add_attendance_list(self):
        return
    def add_student_list(self, students):
        return
    
    