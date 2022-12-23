# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AttendanceSystemGUIqckFXN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(905, 572)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.btn_home_page = QPushButton(self.frame_top_menus)
        self.btn_home_page.setObjectName(u"btn_home_page")
        self.btn_home_page.setMinimumSize(QSize(0, 40))
        self.btn_home_page.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.btn_home_page)

        self.btn_login_page = QPushButton(self.frame_top_menus)
        self.btn_login_page.setObjectName(u"btn_login_page")
        self.btn_login_page.setMinimumSize(QSize(0, 40))
        self.btn_login_page.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.btn_login_page)

        self.btn_signup_page = QPushButton(self.frame_top_menus)
        self.btn_signup_page.setObjectName(u"btn_signup_page")
        self.btn_signup_page.setMinimumSize(QSize(0, 40))
        self.btn_signup_page.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.btn_signup_page)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_20.addLayout(self.horizontalLayout_2)


        self.verticalLayout_19.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_22 = QVBoxLayout(self.home_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.Home_label = QLabel(self.home_page)
        self.Home_label.setObjectName(u"Home_label")
        font = QFont()
        font.setPointSize(40)
        self.Home_label.setFont(font)
        self.Home_label.setStyleSheet(u"")
        self.Home_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.Home_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.go2signup_btn = QPushButton(self.home_page)
        self.go2signup_btn.setObjectName(u"go2signup_btn")
        self.go2signup_btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.go2signup_btn)

        self.go2login_btn = QPushButton(self.home_page)
        self.go2login_btn.setObjectName(u"go2login_btn")
        self.go2login_btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.go2login_btn)


        self.verticalLayout_22.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.home_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.verticalLayout_24 = QVBoxLayout(self.login_page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.login_label = QLabel(self.login_page)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setFont(font)
        self.login_label.setStyleSheet(u"")
        self.login_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.login_label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.password_label = QLabel(self.login_page)
        self.password_label.setObjectName(u"password_label")

        self.gridLayout.addWidget(self.password_label, 1, 0, 1, 1)

        self.tc_lineEdit = QLineEdit(self.login_page)
        self.tc_lineEdit.setObjectName(u"tc_lineEdit")
        self.tc_lineEdit.setMinimumSize(QSize(250, 24))

        self.gridLayout.addWidget(self.tc_lineEdit, 0, 1, 1, 1, Qt.AlignHCenter)

        self.tc_label = QLabel(self.login_page)
        self.tc_label.setObjectName(u"tc_label")
        self.tc_label.setMaximumSize(QSize(65, 16777215))

        self.gridLayout.addWidget(self.tc_label, 0, 0, 1, 1)

        self.password_lineEdit = QLineEdit(self.login_page)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password_lineEdit, 1, 1, 1, 1)

        self.login_btn = QPushButton(self.login_page)
        self.login_btn.setObjectName(u"login_btn")

        self.gridLayout.addWidget(self.login_btn, 2, 1, 1, 1, Qt.AlignRight)


        self.verticalLayout_24.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.login_page)
        self.signup_page = QWidget()
        self.signup_page.setObjectName(u"signup_page")
        self.verticalLayout_25 = QVBoxLayout(self.signup_page)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.signup_label = QLabel(self.signup_page)
        self.signup_label.setObjectName(u"signup_label")
        self.signup_label.setFont(font)
        self.signup_label.setStyleSheet(u"")
        self.signup_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.signup_label)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.surname__lineEdit = QLineEdit(self.signup_page)
        self.surname__lineEdit.setObjectName(u"surname__lineEdit")
        self.surname__lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_3.addWidget(self.surname__lineEdit, 2, 2, 1, 1)

        self.signup_btn = QPushButton(self.signup_page)
        self.signup_btn.setObjectName(u"signup_btn")

        self.gridLayout_3.addWidget(self.signup_btn, 5, 2, 1, 1, Qt.AlignRight)

        self.lineEdit = QLineEdit(self.signup_page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_3.addWidget(self.lineEdit, 3, 2, 1, 1)

        self.name_label = QLabel(self.signup_page)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout_3.addWidget(self.name_label, 1, 0, 1, 1)

        self.label = QLabel(self.signup_page)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.label, 3, 0, 1, 1)

        self.tc_label_2 = QLabel(self.signup_page)
        self.tc_label_2.setObjectName(u"tc_label_2")
        self.tc_label_2.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_3.addWidget(self.tc_label_2, 0, 0, 1, 1)

        self.name_lineEdit = QLineEdit(self.signup_page)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_3.addWidget(self.name_lineEdit, 1, 2, 1, 1)

        self.password_label_2 = QLabel(self.signup_page)
        self.password_label_2.setObjectName(u"password_label_2")

        self.gridLayout_3.addWidget(self.password_label_2, 4, 0, 1, 1)

        self.surname_label = QLabel(self.signup_page)
        self.surname_label.setObjectName(u"surname_label")

        self.gridLayout_3.addWidget(self.surname_label, 2, 0, 1, 1)

        self.tc_lineEdit_2 = QLineEdit(self.signup_page)
        self.tc_lineEdit_2.setObjectName(u"tc_lineEdit_2")
        self.tc_lineEdit_2.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_3.addWidget(self.tc_lineEdit_2, 0, 2, 1, 1)

        self.password_lineEdit_2 = QLineEdit(self.signup_page)
        self.password_lineEdit_2.setObjectName(u"password_lineEdit_2")
        self.password_lineEdit_2.setMaximumSize(QSize(250, 16777215))
        self.password_lineEdit_2.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.password_lineEdit_2, 4, 2, 1, 1)


        self.verticalLayout_25.addLayout(self.gridLayout_3)

        self.stackedWidget.addWidget(self.signup_page)

        self.verticalLayout_21.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home_page.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_login_page.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.btn_signup_page.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.Home_label.setText(QCoreApplication.translate("MainWindow", u"Attendance System", None))
#if QT_CONFIG(whatsthis)
        self.go2signup_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.go2signup_btn.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.go2login_btn.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.tc_label.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.signup_label.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.signup_btn.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.tc_label_2.setText(QCoreApplication.translate("MainWindow", u"TC No:", None))
        self.password_label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.surname_label.setText(QCoreApplication.translate("MainWindow", u"Surname:", None))
    # retranslateUi

