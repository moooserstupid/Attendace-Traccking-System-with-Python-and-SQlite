
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.login_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.login_page)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.authenticate_login_btn = QtWidgets.QPushButton(self.login_page)
        self.authenticate_login_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.authenticate_login_btn.setStyleSheet("")
        self.authenticate_login_btn.setObjectName("authenticate_login_btn")
        self.gridLayout.addWidget(self.authenticate_login_btn, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(self.login_page)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.login_page)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.login_username_input = QtWidgets.QLineEdit(self.login_page)
        self.login_username_input.setMaximumSize(QtCore.QSize(250, 16777215))
        self.login_username_input.setObjectName("login_username_input")
        self.gridLayout.addWidget(self.login_username_input, 0, 1, 1, 1)
        self.login_password_input = QtWidgets.QLineEdit(self.login_page)
        self.login_password_input.setMaximumSize(QtCore.QSize(250, 16777215))
        self.login_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password_input.setObjectName("login_password_input")
        self.gridLayout.addWidget(self.login_password_input, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.signup_btn = QtWidgets.QPushButton(self.login_page)
        self.signup_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.signup_btn.setObjectName("signup_btn")
        self.verticalLayout_2.addWidget(self.signup_btn, 0, QtCore.Qt.AlignLeft)
        self.stackedWidget.addWidget(self.login_page)
        self.signup_page = QtWidgets.QWidget()
        self.signup_page.setObjectName("signup_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.signup_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.signup_page)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.signup_username_input = QtWidgets.QLineEdit(self.signup_page)
        self.signup_username_input.setMaximumSize(QtCore.QSize(250, 16777215))
        self.signup_username_input.setObjectName("signup_username_input")
        self.gridLayout_2.addWidget(self.signup_username_input, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.signup_page)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.signup_page)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.signup_lastname_input = QtWidgets.QLineEdit(self.signup_page)
        self.signup_lastname_input.setMaximumSize(QtCore.QSize(250, 16777215))
        self.signup_lastname_input.setObjectName("signup_lastname_input")
        self.gridLayout_2.addWidget(self.signup_lastname_input, 2, 2, 1, 1)
        self.authenticate_signup_btn = QtWidgets.QPushButton(self.signup_page)
        self.authenticate_signup_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.authenticate_signup_btn.setStyleSheet("")
        self.authenticate_signup_btn.setObjectName("authenticate_signup_btn")
        self.gridLayout_2.addWidget(self.authenticate_signup_btn, 5, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label_7 = QtWidgets.QLabel(self.signup_page)
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.signup_page)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.signup_tc_input = QtWidgets.QLineEdit(self.signup_page)
        self.signup_tc_input.setMaximumSize(QtCore.QSize(250, 16777215))
        self.signup_tc_input.setObjectName("signup_tc_input")
        self.gridLayout_2.addWidget(self.signup_tc_input, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.signup_page)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.signup_name_input = QtWidgets.QLineEdit(self.signup_page)
        self.signup_name_input.setMaximumSize(QtCore.QSize(250, 16777215))
        self.signup_name_input.setObjectName("signup_name_input")
        self.gridLayout_2.addWidget(self.signup_name_input, 1, 2, 1, 1)
        self.signup_password_input = QtWidgets.QLineEdit(self.signup_page)
        self.signup_password_input.setMaximumSize(QtCore.QSize(250, 16777215))
        self.signup_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_password_input.setObjectName("signup_password_input")
        self.gridLayout_2.addWidget(self.signup_password_input, 4, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.login_btn = QtWidgets.QPushButton(self.signup_page)
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout_3.addWidget(self.login_btn, 0, QtCore.Qt.AlignLeft)
        self.stackedWidget.addWidget(self.signup_page)
        self.verticalLayout_27.addWidget(self.stackedWidget)
        self.horizontalLayout_5.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attendance System"))
        self.label_9.setText(_translate("MainWindow", "Attendance System"))
        self.authenticate_login_btn.setText(_translate("MainWindow", "Log In"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.signup_btn.setText(_translate("MainWindow", "Sign Up"))
        self.label_3.setText(_translate("MainWindow", "Sign Up"))
        self.label_4.setText(_translate("MainWindow", "Password:"))
        self.label_5.setText(_translate("MainWindow", "Username:"))
        self.authenticate_signup_btn.setText(_translate("MainWindow", "Sign Up"))
        self.label_7.setText(_translate("MainWindow", "TC No:"))
        self.label_8.setText(_translate("MainWindow", "Lastname:"))
        self.label_6.setText(_translate("MainWindow", "Name:"))
        self.login_btn.setText(_translate("MainWindow", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
