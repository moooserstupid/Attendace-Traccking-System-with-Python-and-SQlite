
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, Qt, QDate
from PyQt5.QtWidgets import QMainWindow

from BarcodeScannerWebcam import BarcodeScanner
from api_request_send import RequestSendAPI

# GUI FILE
from MainWindow import Ui_MainWindow
from Dashboard import Ui_DashboardWindow


from backend.api_backend import BackendAPI


class MainWindow(QMainWindow):
    global dashboard_window
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.api = RequestSendAPI()
        self.backend = BackendAPI()

        self.ui.setupUi(self)

        self.ui.signup_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signup_page))
        self.ui.login_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login_page))
        self.ui.authenticate_login_btn.clicked.connect(self.login)
        self.ui.authenticate_signup_btn.clicked.connect(self.sign_up)
        self.show()

    def login(self):
        username = self.ui.login_username_input.text()
        password = self.ui.login_password_input.text()
        self.ui.login_username_input.clear()
        self.ui.login_password_input.clear()

        if username == '' or password == '':
            print("fields cannot be empty")
        else:
            print("username: ", username)
            print("password: ", password)
            self.api.send('Q1,'+username+','+password)
            server_reply = self.api.receive()
            if server_reply[0] == "R1":
                if server_reply[1] == 'None':
                    print("Login Failed ")
                else:
                    mainWindow.close()
                    dashboard_window = DashboardWindow(server_reply)


    def sign_up(self):
        tc = self.ui.signup_tc_input.text()
        name = self.ui.signup_name_input.text()
        lastname = self.ui.signup_lastname_input.text()
        username = self.ui.signup_username_input.text()
        password = self.ui.signup_password_input.text()

        self.ui.signup_tc_input.clear()
        self.ui.signup_name_input.clear()
        self.ui.signup_lastname_input.clear()
        self.ui.signup_username_input.clear()
        self.ui.signup_password_input.clear()

        if tc == '' or name == '' or lastname == '' or username == '' or password == '':
            print("fields cannot be empty")
        else:
            print("successfully sign up")
            print("tc        : ", tc)
            print("name      : ", name)
            print("last name : ", lastname)
            print("username  : ", username)
            print("password  : ", password)

            # if self.api.authenticate_signup():

            self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)


class DashboardWindow(QMainWindow):
    global active_user

    def __init__(self, user):
        QMainWindow.__init__(self)
        self.ui = Ui_DashboardWindow()
        self.ui.setupUi(self)
        self.active_user = user

        # Switch Pages
        self.ui.dashboard_menu_btn.clicked.connect(
            lambda: self.switch_page(self.ui.dashboard_page, "Dashboard"))
        self.ui.courses_menu_btn.clicked.connect(
            lambda: self.switch_page(self.ui.courses_page, "Courses"))
        self.ui.go_to_add_course_btn.clicked.connect(
            lambda: self.switch_page(self.ui.add_course_page, "Add Course"))
        self.ui.lessons_menu_btn.clicked.connect(
            lambda: self.switch_page(self.ui.lessons_page, "Lessons"))
        self.ui.students_menu_btn.clicked.connect(
            lambda: self.switch_page(self.ui.students_page, "Students"))
        self.ui.add_new_student_btn.clicked.connect(
            lambda: self.switch_page(self.ui.add_student_page, "Add Student"))
        self.ui.take_attendance_menu_btn.clicked.connect(
            lambda: self.switch_page(self.ui.take_attendance_page, "Take Attendance"))
        self.ui.teacher_info_menu_btn.clicked.connect(
            lambda: self.switch_page(self.ui.teacher_info_page, "Teacher Info"))

        # Buttons
        self.ui.add_course_btn.clicked.connect(self.add_course)
        self.ui.add_lesson_btn.clicked.connect(self.add_lesson)
        self.ui.add_student_btn.clicked.connect(self.add_student)
        self.ui.add_students_to_course_btn.clicked.connect(self.add_students_to_course_btn)
        self.ui.scan_tc_btn.clicked.connect(self.scan_students_tc)
        self.ui.sign_out_btn.clicked.connect(self.sign_out)

        # Set Combo Boxes Data
        teachers = ["Mo", "Ali", "Eren", "Emirhan"]
        courses = ["DBMS", "Microcontroller", "Programming"]
        lessons = ['1', '2', '3', '4', '5']
        self.ui.teacher_name_comboBox.addItems(teachers)
        self.ui.course_id_comboBox.addItems(courses)
        self.ui.select_course_comboBox.addItems(courses)
        self.ui.lesson_id_comboBox.addItems(lessons)

        # Set Date Edits to today's date
        current_date = QDate().currentDate()
        self.ui.start_date_dateEdit.setDate(current_date)
        self.ui.end_date_dateEdit.setDate(current_date)
        self.ui.lesson_date_dateEdit.setDate(current_date)

        self.show()

    def switch_page(self, page, page_name):
        self.ui.page_name_label.setText(page_name)
        self.ui.stackedWidget.setCurrentWidget(page)

    def add_course(self):
        course_name = self.ui.course_name_lineEdit.text()
        course_description = self.ui.course_description_lineEdit.text()
        teacher_name = self.ui.teacher_name_comboBox.currentText()
        start_date = self.ui.start_date_dateEdit.text()
        end_date = self.ui.end_date_dateEdit.text()
        total_lesson_count = self.ui.total_lesson_count_spinBox.text()

        self.ui.course_name_lineEdit.clear()
        self.ui.course_description_lineEdit.clear()
        self.ui.total_lesson_count_spinBox.clear()

        if course_name == '' or course_description == '' or teacher_name == '' \
                or start_date == '' or end_date == '' or total_lesson_count == '':
            print("fields cannot be empty")
        else:
            print("Course added successfully")
            print("Course Name        : ", course_name)
            print("Course Description : ", course_description)
            print("Teacher Name       : ", teacher_name)
            print("Start Date         : ", start_date)
            print("End Date           : ", end_date)
            print("Total Lesson Count : ", total_lesson_count)

    def add_lesson(self):
        lesson_date = self.ui.lesson_date_dateEdit.text()
        course_id = self.ui.course_id_comboBox.currentText()

        if lesson_date == '' or course_id == '':
            print("fields cannot be empty")
        else:
            print("Lesson added successfully")
            print("Lesson Date : ", lesson_date)
            print("Course Id   : ", course_id)

    def add_student(self):
        student_tc = self.ui.student_tc_no_lineEdit.text()
        student_name = self.ui.student_name_lineEdit.text()
        student_lastname = self.ui.student_lastname_lineEdit.text()
        student_no = self.ui.student_no_lineEdit.text()

        if student_tc == '' or student_name == '' or student_lastname == '' \
                or student_no == '':
            print("fields cannot be empty")
        else:
            print("Student added successfully")
            print("Student TC No   : ", student_tc)
            print("Student Name    : ", student_name)
            print("Student Lastname: ", student_lastname)
            print("Student No      : ", student_no)

    def add_students_to_course_btn(self):
        selected_students = self.ui.students_treeWidget.selectedItems()
        selected_course = self.ui.select_course_comboBox.currentText()
        if len(selected_students) == 0 or selected_course == '':
            print("You must select at least one student")
        else:
            print("Course added to selected students successfully")
            print("Selected Students: ", selected_students)
            print("Selected Course  : ", selected_course)

    def scan_students_tc(self):
        scanner = BarcodeScanner()
        scanned_tc_nums = scanner.scan_tc()
        print("Scanned students TC numbers:")
        for tc in scanned_tc_nums:
            print(tc)

    def sign_out(self):
        self.close()


if __name__ == "__main__":
    global app
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
