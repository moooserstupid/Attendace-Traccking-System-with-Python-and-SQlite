
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, Qt, QDate
from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem

from BarcodeScannerWebcam import BarcodeScanner
from api_request_send import RequestSendAPI

# GUI FILE
from MainWindow import Ui_MainWindow
from Dashboard import Ui_DashboardWindow


class MainWindow(QMainWindow):
    global dashboard_window
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.api = RequestSendAPI()

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
            print(server_reply)
            if server_reply[0] == "R1":
                if server_reply[1] == 'None':
                    print("Login Failed ")
                else:
                    print("success")
                    mainWindow.close()
                    server_reply.append(username)
                    server_reply.append(password)
                    dashboard_window = DashboardWindow(server_reply[2:])


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
        self.api = RequestSendAPI()
        self.ui = Ui_DashboardWindow()
        self.ui.setupUi(self)

        self.active_user = user
        print(self.active_user)

        # Teacher Info
        self.ui.ti_tc_no_lineEdit.setText(self.active_user[2])
        self.ui.ti_name_lineEdit.setText(self.active_user[0])
        self.ui.ti_lastname_lineEdit.setText(self.active_user[1])
        self.ui.ti_username_lineEdit.setText(self.active_user[3])
        self.ui.ti_password_lineEdit.setText(self.active_user[4])

        self.ui.welcome_label.setText("Welcome " + self.active_user[0] + " " + self.active_user[1])

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
        self.ui.all_attendaces_btn.clicked.connect(
            lambda: self.switch_page(self.ui.all_attendances_page, "All Attendances"))
        self.ui.teacher_info_menu_btn.clicked.connect(
            lambda: self.switch_page(self.ui.teacher_info_page, "Teacher Info"))

        # Buttons
        self.ui.add_course_btn.clicked.connect(self.add_course)
        self.ui.add_lesson_btn.clicked.connect(self.add_lesson)
        self.ui.add_student_btn.clicked.connect(self.add_student)
        self.ui.add_students_to_course_btn.clicked.connect(self.add_students_to_course_btn)
        self.ui.scan_tc_btn.clicked.connect(self.scan_students_tc)
        self.ui.sign_out_btn.clicked.connect(self.sign_out)
        self.ui.update_teacher_info_btn.clicked.connect(self.update_teacher_info)
        self.ui.take_attendance_btn.clicked.connect(self.take_attendance)

        course_names = self.get_tabel_column_values("course", 1)
        lesson_ids = self.get_tabel_column_values("lesson", 0)

        self.ui.course_id_comboBox.addItems(course_names)
        self.ui.select_course_comboBox.addItems(course_names)
        self.ui.lesson_id_comboBox.addItems(lesson_ids)

        # Set Date Edits to today's date
        current_date = QDate().currentDate()
        self.ui.start_date_dateEdit.setDate(current_date)
        self.ui.end_date_dateEdit.setDate(current_date)
        self.ui.lesson_date_dateEdit.setDate(current_date)

        self.show_tabel_on_tree_widget("course", self.ui.courses_treeWidget)
        self.show_tabel_on_tree_widget("student", self.ui.students_treeWidget)
        self.show_tabel_on_tree_widget("attendance", self.ui.all_attendances_treeWidget)
        self.show_lessons_tabel()
        # self.show_attendance_tabel()

        self.show()

    def show_lessons_tabel(self):
        self.api.send('Q4,lesson')
        server_reply = self.api.receive()
        rows = []
        for i in range(1, len(server_reply)):
            r = server_reply[i].split(';')
            rows.append(r)
        for row in rows:
            self.api.send('Q5,course,' + row[2])
            server_reply = self.api.receive()
            data = server_reply[2:4]
            row = row[1:]
            row.extend(data)

            self.api.send('Q5,teacher,' + row[3])
            server_reply = self.api.receive()
            data = server_reply[2:4]
            row.extend(data)

            QTreeWidgetItem(self.ui.lessons_treeWidget, row)
    def show_attendance_tabel(self):
        self.api.send('Q4,attendance')
        server_reply = self.api.receive()
        rows = []
        for i in range(1, len(server_reply)):
            r = server_reply[i].split(';')
            rows.append(r)
        print(rows)
        for row in rows:
            self.api.send('Q5,lesson,' + row[1])
            server_reply = self.api.receive()
            print(server_reply)
            data = server_reply[2:4]
            row = row[1:]
            row.extend(data)
            self.api.send('Q5,student,' + row[2])
            server_reply = self.api.receive()
            print(server_reply)
            data = server_reply[2:4]
            row.extend(data)

            QTreeWidgetItem(self.ui.lessons_treeWidget, row)
    def show_tabel_on_tree_widget(self, tabel_name, treeWidget):
        rows = self.get_tabel_values(tabel_name)
        for row in rows:
            QTreeWidgetItem(treeWidget, row[1:])
    def get_tabel_values(self, tabel_name):
        self.api.send('Q4,'+tabel_name)
        server_reply = self.api.receive()
        rows = []
        for i in range(1, len(server_reply)):
            r = server_reply[i].split(';')
            rows.append(r)
        return rows
    def get_tabel_column_values(self, tabel_name, column_index):
        rows = self.get_tabel_values(tabel_name)
        print(rows)
        column_values = []
        for row in rows:
            column_values.append(row[column_index])
        return column_values
    def switch_page(self, page, page_name):
        self.ui.page_name_label.setText(page_name)
        self.ui.stackedWidget.setCurrentWidget(page)

    def add_course(self):
        course_name = self.ui.course_name_lineEdit.text()
        course_description = self.ui.course_description_lineEdit.text()
        # teacher_name = self.ui.teacher_name_comboBox.currentText()
        start_date = self.ui.start_date_dateEdit.text()
        end_date = self.ui.end_date_dateEdit.text()
        total_lesson_count = self.ui.total_lesson_count_spinBox.text()

        self.ui.course_name_lineEdit.clear()
        self.ui.course_description_lineEdit.clear()
        self.ui.total_lesson_count_spinBox.clear()

        if course_name == '' or course_description == '' or start_date == ''\
                or end_date == '' or total_lesson_count == '':
            print("fields cannot be empty")
        else:
            self.api.send(f"Q6,{course_name},{course_description},"
                          f"{start_date},{end_date},{total_lesson_count}")
            server_reply = self.api.receive()
            if server_reply[0] == "R6":
                if server_reply[1] == "success":
                    print("Course added successfully")
                elif server_reply[1] == "failed":
                    print("Failed to add course")

    def add_lesson(self):
        lesson_date = self.ui.lesson_date_dateEdit.text()
        course_id = self.ui.course_id_comboBox.currentText()

        if lesson_date == '' or course_id == '':
            print("fields cannot be empty")
        else:
            self.api.send(f"Q7,{lesson_date},{course_id}")
            server_reply = self.api.receive()
            if server_reply[0] == "R7":
                if server_reply[1] == "success":
                    print("Lesson added successfully")
                elif server_reply[1] == "failed":
                    print("Failed to add lesson")

    def add_student(self):
        student_tc = self.ui.student_tc_no_lineEdit.text()
        student_name = self.ui.student_name_lineEdit.text()
        student_lastname = self.ui.student_lastname_lineEdit.text()
        student_no = self.ui.student_no_lineEdit.text()

        if student_tc == '' or student_name == '' or student_lastname == '' \
                or student_no == '':
            print("fields cannot be empty")
        else:
            self.api.send(f"Q8,{student_no},{student_name},{student_lastname},"
                          f"{student_tc}")
            server_reply = self.api.receive()
            if server_reply[0] == "R8":
                if server_reply[1] == "success":
                    print("Student added successfully")
                elif server_reply[1] == "failed":
                    print("Failed to add student")

    def add_students_to_course_btn(self):
        selected_students = self.ui.students_treeWidget.selectedItems()
        selected_course = self.ui.select_course_comboBox.currentText()
        if len(selected_students) == 0 or selected_course == '':
            print("You must select at least one student")
        else:
            for student in selected_students:
                print("Selected Students: ", student.text(0))
                self.api.send(f"Q9,{selected_course},{student.text(0)}")
                server_reply = self.api.receive()
                if server_reply[0] == "R9":
                    if server_reply[1] == "success":
                        print("Course added to selected students successfully")
                    elif server_reply[1] == "failed":
                        print("Failed to add selected students to course")

    def scan_students_tc(self):
        scanner = BarcodeScanner()
        scanned_tc_nums = scanner.scan_tc()
        selected_lesson_id = self.ui.lesson_id_comboBox.currentText()
        for tc in scanned_tc_nums:
            QTreeWidgetItem(self.ui.attendance_treeWidget, [selected_lesson_id, tc])

    def take_attendance(self):
        attendance_root = self.ui.attendance_treeWidget.invisibleRootItem()
        child_count = attendance_root.childCount()
        for i in range(child_count):
            item = attendance_root.child(i)
            self.api.send(f"Q10,{item.text(0)},{item.text(1)}")
            server_reply = self.api.receive()
            if server_reply[0] == "Q10":
                if server_reply[1] == "success":
                    print("Course added to selected students successfully")
                elif server_reply[1] == "failed":
                    print("Failed to add selected students to course")
            # print(item.text(0), item.text(1))

    def update_teacher_info(self):
        old_username = self.active_user[3]
        self.active_user[3] = self.ui.ti_username_lineEdit.text()
        self.active_user[4] = self.ui.ti_password_lineEdit.text()
        self.api.send("Q3,"+old_username+','+self.active_user[3]+','+self.active_user[4])

        print("updated successfully")

    def sign_out(self):
        self.close()


if __name__ == "__main__":
    global app
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
