import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

# GUI FILE
from qt_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        # self.api = RequestServiceAPI()
        # self.dashboardWindow = None

        self.ui.setupUi(self)
        print("aq")

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

            # if self.api.authenticate_login():
            #     mainWindow.close()
            #     self.dashboardWindow = DashboardWindow()
            # mainWindow.close()
            # self.dashboardWindow = DashboardWindow()

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
