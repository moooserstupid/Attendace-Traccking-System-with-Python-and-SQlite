
import sys
from PySide2.QtWidgets import *


# GUI FILE
from ui_MainWindow import Ui_MainWindow
from ui_Dashboard import Ui_DashboardWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_home_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        self.ui.btn_login_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login_page))
        self.ui.btn_signup_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signup_page))
        self.ui.go2login_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login_page))
        self.ui.go2signup_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signup_page))
        self.ui.login_btn.clicked.connect(Login)

        self.show()


class DashboardWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_DashboardWindow()
        self.ui.setupUi(self)

        self.ui.dashboard_menu_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard_page))
        self.ui.courses_menu_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.courses_page))
        self.ui.dashboard_menu_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard_page))
        self.ui.lessons_menu_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.lessons_page))
        self.ui.students_menu_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.students_page))
        self.ui.go_to_add_course_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add_student_page))
        self.ui.take_attendance_menu_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.take_attendance_page))
        self.ui.teacher_info_menu_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.teacher_info_page))
        self.show()




def Login():
    mainWindow.close()
    dashboardWindow = DashboardWindow()


def SignUp():
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
