# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashboardgZBeut.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DashboardWindow(object):
    def setupUi(self, DashboardWindow):
        if not DashboardWindow.objectName():
            DashboardWindow.setObjectName(u"DashboardWindow")
        DashboardWindow.resize(1097, 653)
        self.centralwidget = QWidget(DashboardWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Content)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(150, 0))
        self.frame_left_menu.setMaximumSize(QSize(101, 16777215))
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus_2 = QFrame(self.frame_left_menu)
        self.frame_top_menus_2.setObjectName(u"frame_top_menus_2")
        self.frame_top_menus_2.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_top_menus_2)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.login_label = QLabel(self.frame_top_menus_2)
        self.login_label.setObjectName(u"login_label")
        font = QFont()
        font.setPointSize(12)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet(u"")
        self.login_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.login_label)

        self.dashboard_menu_btn = QPushButton(self.frame_top_menus_2)
        self.dashboard_menu_btn.setObjectName(u"dashboard_menu_btn")
        self.dashboard_menu_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_26.addWidget(self.dashboard_menu_btn)

        self.courses_menu_btn = QPushButton(self.frame_top_menus_2)
        self.courses_menu_btn.setObjectName(u"courses_menu_btn")
        self.courses_menu_btn.setMinimumSize(QSize(0, 40))
        self.courses_menu_btn.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.courses_menu_btn)

        self.lessons_menu_btn = QPushButton(self.frame_top_menus_2)
        self.lessons_menu_btn.setObjectName(u"lessons_menu_btn")
        self.lessons_menu_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.lessons_menu_btn)

        self.students_menu_btn = QPushButton(self.frame_top_menus_2)
        self.students_menu_btn.setObjectName(u"students_menu_btn")
        self.students_menu_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.students_menu_btn)

        self.take_attendance_menu_btn = QPushButton(self.frame_top_menus_2)
        self.take_attendance_menu_btn.setObjectName(u"take_attendance_menu_btn")
        self.take_attendance_menu_btn.setMinimumSize(QSize(0, 40))
        self.take_attendance_menu_btn.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.take_attendance_menu_btn)

        self.teacher_info_menu_btn = QPushButton(self.frame_top_menus_2)
        self.teacher_info_menu_btn.setObjectName(u"teacher_info_menu_btn")
        self.teacher_info_menu_btn.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_26.addWidget(self.teacher_info_menu_btn)


        self.verticalLayout_23.addWidget(self.frame_top_menus_2)


        self.horizontalLayout_5.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.verticalLayout_28 = QVBoxLayout(self.dashboard_page)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.stackedWidget.addWidget(self.dashboard_page)
        self.courses_page = QWidget()
        self.courses_page.setObjectName(u"courses_page")
        self.verticalLayout_5 = QVBoxLayout(self.courses_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.courses_treeWidget = QTreeWidget(self.courses_page)
        self.courses_treeWidget.setObjectName(u"courses_treeWidget")

        self.verticalLayout_5.addWidget(self.courses_treeWidget)

        self.go_to_add_course_btn = QPushButton(self.courses_page)
        self.go_to_add_course_btn.setObjectName(u"go_to_add_course_btn")
        self.go_to_add_course_btn.setMinimumSize(QSize(250, 0))

        self.verticalLayout_5.addWidget(self.go_to_add_course_btn, 0, Qt.AlignRight)

        self.stackedWidget.addWidget(self.courses_page)
        self.add_course_page = QWidget()
        self.add_course_page.setObjectName(u"add_course_page")
        self.verticalLayout_29 = QVBoxLayout(self.add_course_page)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_14 = QLabel(self.add_course_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(120, 30))

        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)

        self.course_description_lineEdit = QLineEdit(self.add_course_page)
        self.course_description_lineEdit.setObjectName(u"course_description_lineEdit")
        self.course_description_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.course_description_lineEdit, 1, 1, 1, 1)

        self.label_15 = QLabel(self.add_course_page)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 6, 0, 1, 1)

        self.add_course_btn = QPushButton(self.add_course_page)
        self.add_course_btn.setObjectName(u"add_course_btn")

        self.gridLayout.addWidget(self.add_course_btn, 8, 1, 1, 1)

        self.course_name_lineEdit = QLineEdit(self.add_course_page)
        self.course_name_lineEdit.setObjectName(u"course_name_lineEdit")
        self.course_name_lineEdit.setMinimumSize(QSize(0, 0))
        self.course_name_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.course_name_lineEdit, 0, 1, 1, 1)

        self.end_date_dateEdit = QDateEdit(self.add_course_page)
        self.end_date_dateEdit.setObjectName(u"end_date_dateEdit")

        self.gridLayout.addWidget(self.end_date_dateEdit, 6, 1, 1, 1)

        self.label_8 = QLabel(self.add_course_page)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_7 = QLabel(self.add_course_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.total_lesson_count_spinBox = QSpinBox(self.add_course_page)
        self.total_lesson_count_spinBox.setObjectName(u"total_lesson_count_spinBox")

        self.gridLayout.addWidget(self.total_lesson_count_spinBox, 7, 1, 1, 1)

        self.label_16 = QLabel(self.add_course_page)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 7, 0, 1, 1)

        self.start_date_dateEdit = QDateEdit(self.add_course_page)
        self.start_date_dateEdit.setObjectName(u"start_date_dateEdit")

        self.gridLayout.addWidget(self.start_date_dateEdit, 5, 1, 1, 1)

        self.label_9 = QLabel(self.add_course_page)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.teacher_name_comboBox = QComboBox(self.add_course_page)
        self.teacher_name_comboBox.setObjectName(u"teacher_name_comboBox")

        self.gridLayout.addWidget(self.teacher_name_comboBox, 3, 1, 1, 1)


        self.verticalLayout_29.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.add_course_page)
        self.lessons_page = QWidget()
        self.lessons_page.setObjectName(u"add_lesson_page")
        self.verticalLayout_3 = QVBoxLayout(self.lessons_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.course_id_comboBox = QComboBox(self.lessons_page)
        self.course_id_comboBox.setObjectName(u"course_id_comboBox")
        self.course_id_comboBox.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_4.addWidget(self.course_id_comboBox, 1, 1, 1, 1)

        self.add_lesson_btn = QPushButton(self.lessons_page)
        self.add_lesson_btn.setObjectName(u"add_lesson_btn")

        self.gridLayout_4.addWidget(self.add_lesson_btn, 5, 1, 1, 1)

        self.label_19 = QLabel(self.lessons_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)

        self.lesson_date_dateEdit = QDateEdit(self.lessons_page)
        self.lesson_date_dateEdit.setObjectName(u"lesson_date_dateEdit")

        self.gridLayout_4.addWidget(self.lesson_date_dateEdit, 0, 1, 1, 1)

        self.label_21 = QLabel(self.lessons_page)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)

        self.lessons_treeWidget = QTreeWidget(self.lessons_page)
        QTreeWidgetItem(self.lessons_treeWidget)
        QTreeWidgetItem(self.lessons_treeWidget)
        QTreeWidgetItem(self.lessons_treeWidget)
        self.lessons_treeWidget.setObjectName(u"lessons_treeWidget")
        self.lessons_treeWidget.setMaximumSize(QSize(16777215, 16777215))
        self.lessons_treeWidget.setFrameShape(QFrame.StyledPanel)
        self.lessons_treeWidget.setFrameShadow(QFrame.Raised)
        self.lessons_treeWidget.setTabKeyNavigation(False)
        self.lessons_treeWidget.setDragEnabled(False)
        self.lessons_treeWidget.setDragDropOverwriteMode(False)
        self.lessons_treeWidget.setAlternatingRowColors(True)
        self.lessons_treeWidget.setTextElideMode(Qt.ElideRight)
        self.lessons_treeWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.lessons_treeWidget.setSortingEnabled(True)
        self.lessons_treeWidget.setAnimated(False)
        self.lessons_treeWidget.setAllColumnsShowFocus(False)
        self.lessons_treeWidget.setWordWrap(False)
        self.lessons_treeWidget.setHeaderHidden(False)

        self.verticalLayout_3.addWidget(self.lessons_treeWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.delete_course_btn = QPushButton(self.lessons_page)
        self.delete_course_btn.setObjectName(u"delete_course_btn")

        self.horizontalLayout_4.addWidget(self.delete_course_btn)

        self.update_course_btn = QPushButton(self.lessons_page)
        self.update_course_btn.setObjectName(u"update_course_btn")

        self.horizontalLayout_4.addWidget(self.update_course_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.lessons_page)
        self.students_page = QWidget()
        self.students_page.setObjectName(u"students_page")
        self.verticalLayout_8 = QVBoxLayout(self.students_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.add_new_student_btn = QPushButton(self.students_page)
        self.add_new_student_btn.setObjectName(u"add_new_student_btn")
        self.add_new_student_btn.setMinimumSize(QSize(250, 0))
        self.add_new_student_btn.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout_8.addWidget(self.add_new_student_btn)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.students_treeWidget = QTreeWidget(self.students_page)
        self.students_treeWidget.setObjectName(u"students_treeWidget")
        self.students_treeWidget.setMinimumSize(QSize(502, 0))
        self.students_treeWidget.setMaximumSize(QSize(16777215, 16777215))
        self.students_treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.students_treeWidget.setSortingEnabled(True)

        self.verticalLayout_10.addWidget(self.students_treeWidget)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.delete_student_btn = QPushButton(self.students_page)
        self.delete_student_btn.setObjectName(u"delete_student_btn")

        self.horizontalLayout_7.addWidget(self.delete_student_btn)

        self.update_student_btn = QPushButton(self.students_page)
        self.update_student_btn.setObjectName(u"update_student_btn")

        self.horizontalLayout_7.addWidget(self.update_student_btn)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.students_page)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 20))

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.add_students_to_course_btn = QPushButton(self.students_page)
        self.add_students_to_course_btn.setObjectName(u"add_students_to_course_btn")
        self.add_students_to_course_btn.setMinimumSize(QSize(250, 0))
        self.add_students_to_course_btn.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_3.addWidget(self.add_students_to_course_btn, 3, 4, 1, 1)

        self.select_course_comboBox = QComboBox(self.students_page)
        self.select_course_comboBox.setObjectName(u"select_course_comboBox")

        self.gridLayout_3.addWidget(self.select_course_comboBox, 2, 4, 1, 1)

        self.label_2 = QLabel(self.students_page)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setKerning(True)
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_3)


        self.verticalLayout_8.addLayout(self.verticalLayout_10)

        self.stackedWidget.addWidget(self.students_page)
        self.add_student_page = QWidget()
        self.add_student_page.setObjectName(u"add_student_page")
        self.verticalLayout_7 = QVBoxLayout(self.add_student_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.student_lastname_lineEdit = QLineEdit(self.add_student_page)
        self.student_lastname_lineEdit.setObjectName(u"student_lastname_lineEdit")
        self.student_lastname_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_5.addWidget(self.student_lastname_lineEdit, 2, 1, 1, 1)

        self.add_student_btn = QPushButton(self.add_student_page)
        self.add_student_btn.setObjectName(u"add_student_btn")

        self.gridLayout_5.addWidget(self.add_student_btn, 5, 1, 1, 1)

        self.label_10 = QLabel(self.add_student_page)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 4, 0, 1, 1)

        self.student_name_lineEdit = QLineEdit(self.add_student_page)
        self.student_name_lineEdit.setObjectName(u"student_name_lineEdit")
        self.student_name_lineEdit.setMinimumSize(QSize(0, 0))
        self.student_name_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_5.addWidget(self.student_name_lineEdit, 1, 1, 1, 1)

        self.student_no_lineEdit = QLineEdit(self.add_student_page)
        self.student_no_lineEdit.setObjectName(u"student_no_lineEdit")
        self.student_no_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_5.addWidget(self.student_no_lineEdit, 4, 1, 1, 1)

        self.label_18 = QLabel(self.add_student_page)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_23 = QLabel(self.add_student_page)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_5.addWidget(self.label_23, 2, 0, 1, 1)

        self.label_20 = QLabel(self.add_student_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_5.addWidget(self.label_20, 1, 0, 1, 1)

        self.student_tc_no_lineEdit = QLineEdit(self.add_student_page)
        self.student_tc_no_lineEdit.setObjectName(u"student_tc_no_lineEdit")
        self.student_tc_no_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_5.addWidget(self.student_tc_no_lineEdit, 0, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_5)

        self.stackedWidget.addWidget(self.add_student_page)
        self.take_attendance_page = QWidget()
        self.take_attendance_page.setObjectName(u"take_attendance_page")
        self.verticalLayout_2 = QVBoxLayout(self.take_attendance_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lesson_name_comboBox = QComboBox(self.take_attendance_page)
        self.lesson_name_comboBox.setObjectName(u"lesson_name_comboBox")
        self.lesson_name_comboBox.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_2.addWidget(self.lesson_name_comboBox, 0, 1, 1, 1)

        self.label_12 = QLabel(self.take_attendance_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(175, 16777215))

        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_13 = QLabel(self.take_attendance_page)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.scan_tc_btn = QPushButton(self.take_attendance_page)
        self.scan_tc_btn.setObjectName(u"scan_tc_btn")
        self.scan_tc_btn.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.scan_tc_btn, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.attendance_treeWidget = QTreeWidget(self.take_attendance_page)
        self.attendance_treeWidget.setObjectName(u"attendance_treeWidget")
        self.attendance_treeWidget.setMaximumSize(QSize(16777215, 16777215))
        self.attendance_treeWidget.setSortingEnabled(True)

        self.horizontalLayout.addWidget(self.attendance_treeWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.take_attendance_btn = QPushButton(self.take_attendance_page)
        self.take_attendance_btn.setObjectName(u"take_attendance_btn")
        self.take_attendance_btn.setMinimumSize(QSize(250, 0))
        self.take_attendance_btn.setMaximumSize(QSize(250, 16777215))
        self.take_attendance_btn.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_2.addWidget(self.take_attendance_btn, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.take_attendance_page)
        self.teacher_info_page = QWidget()
        self.teacher_info_page.setObjectName(u"teacher_info_page")
        self.verticalLayout_34 = QVBoxLayout(self.teacher_info_page)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_75 = QLabel(self.teacher_info_page)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_19.addWidget(self.label_75, 1, 0, 1, 1)

        self.label_74 = QLabel(self.teacher_info_page)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_19.addWidget(self.label_74, 2, 0, 1, 1)

        self.ti_tc_no_lineEdit = QLineEdit(self.teacher_info_page)
        self.ti_tc_no_lineEdit.setObjectName(u"ti_tc_no_lineEdit")
        self.ti_tc_no_lineEdit.setEnabled(True)
        self.ti_tc_no_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_19.addWidget(self.ti_tc_no_lineEdit, 0, 1, 1, 1)

        self.label_76 = QLabel(self.teacher_info_page)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_19.addWidget(self.label_76, 0, 0, 1, 1)

        self.ta_username_lineEdit = QLineEdit(self.teacher_info_page)
        self.ta_username_lineEdit.setObjectName(u"ta_username_lineEdit")
        self.ta_username_lineEdit.setEnabled(True)
        self.ta_username_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_19.addWidget(self.ta_username_lineEdit, 3, 1, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_12.setContentsMargins(0, 0, 1, 0)
        self.pushButton_30 = QPushButton(self.teacher_info_page)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setEnabled(True)

        self.horizontalLayout_12.addWidget(self.pushButton_30)


        self.gridLayout_19.addLayout(self.horizontalLayout_12, 5, 1, 1, 1)

        self.label_77 = QLabel(self.teacher_info_page)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_19.addWidget(self.label_77, 3, 0, 1, 1)

        self.ti_name_lineEdit = QLineEdit(self.teacher_info_page)
        self.ti_name_lineEdit.setObjectName(u"ti_name_lineEdit")
        self.ti_name_lineEdit.setEnabled(True)
        self.ti_name_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_19.addWidget(self.ti_name_lineEdit, 1, 1, 1, 1)

        self.ti_lastname_lineEdit = QLineEdit(self.teacher_info_page)
        self.ti_lastname_lineEdit.setObjectName(u"ti_lastname_lineEdit")
        self.ti_lastname_lineEdit.setEnabled(True)
        self.ti_lastname_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_19.addWidget(self.ti_lastname_lineEdit, 2, 1, 1, 1)

        self.label_79 = QLabel(self.teacher_info_page)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_19.addWidget(self.label_79, 4, 0, 1, 1)

        self.ti_password_lineEdit = QLineEdit(self.teacher_info_page)
        self.ti_password_lineEdit.setObjectName(u"ti_password_lineEdit")
        self.ti_password_lineEdit.setEnabled(True)
        self.ti_password_lineEdit.setMaximumSize(QSize(250, 16777215))
        self.ti_password_lineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout_19.addWidget(self.ti_password_lineEdit, 4, 1, 1, 1)


        self.verticalLayout_34.addLayout(self.gridLayout_19)

        self.stackedWidget.addWidget(self.teacher_info_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_16 = QVBoxLayout(self.page_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_27.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        DashboardWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(DashboardWindow)
        self.statusbar.setObjectName(u"statusbar")
        DashboardWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DashboardWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DashboardWindow)
    # setupUi

    def retranslateUi(self, DashboardWindow):
        DashboardWindow.setWindowTitle(QCoreApplication.translate("DashboardWindow", u"MainWindow", None))
        self.login_label.setText(QCoreApplication.translate("DashboardWindow", u"Dashboard", None))
        self.dashboard_menu_btn.setText(QCoreApplication.translate("DashboardWindow", u"Dashboard", None))
        self.courses_menu_btn.setText(QCoreApplication.translate("DashboardWindow", u"Courses", None))
        self.lessons_menu_btn.setText(QCoreApplication.translate("DashboardWindow", u"Lessons", None))
        self.students_menu_btn.setText(QCoreApplication.translate("DashboardWindow", u"Students", None))
        self.take_attendance_menu_btn.setText(QCoreApplication.translate("DashboardWindow", u"Take Attendance", None))
        self.teacher_info_menu_btn.setText(QCoreApplication.translate("DashboardWindow", u"Teacher Info", None))
        ___qtreewidgetitem = self.courses_treeWidget.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("DashboardWindow", u"Count Of Lessons", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("DashboardWindow", u"End Date", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("DashboardWindow", u"Start Date", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("DashboardWindow", u"Descrition", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("DashboardWindow", u"Teacher ID", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DashboardWindow", u"Course Name", None));
        self.go_to_add_course_btn.setText(QCoreApplication.translate("DashboardWindow", u"Add Course", None))
        self.label_14.setText(QCoreApplication.translate("DashboardWindow", u"Start Date:", None))
        self.label_15.setText(QCoreApplication.translate("DashboardWindow", u"End Date:", None))
        self.add_course_btn.setText(QCoreApplication.translate("DashboardWindow", u"Add Course", None))
        self.label_8.setText(QCoreApplication.translate("DashboardWindow", u"Teacher Name:", None))
        self.label_7.setText(QCoreApplication.translate("DashboardWindow", u"Course Name:", None))
        self.label_16.setText(QCoreApplication.translate("DashboardWindow", u"Total Lesson Count", None))
        self.label_9.setText(QCoreApplication.translate("DashboardWindow", u"Course Description:", None))
        self.add_lesson_btn.setText(QCoreApplication.translate("DashboardWindow", u"Add Lesson", None))
        self.label_19.setText(QCoreApplication.translate("DashboardWindow", u"Lesson Date:", None))
        self.label_21.setText(QCoreApplication.translate("DashboardWindow", u"Course ID:", None))
        ___qtreewidgetitem1 = self.lessons_treeWidget.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("DashboardWindow", u"Teacher Name", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("DashboardWindow", u"Teacher ID", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("DashboardWindow", u"Course Name", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("DashboardWindow", u"Course ID", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DashboardWindow", u"Lesson Date", None));

        __sortingEnabled = self.lessons_treeWidget.isSortingEnabled()
        self.lessons_treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem2 = self.lessons_treeWidget.topLevelItem(0)
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("DashboardWindow", u"VTYS", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("DashboardWindow", u"26/12/2022", None));
        ___qtreewidgetitem3 = self.lessons_treeWidget.topLevelItem(1)
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("DashboardWindow", u"VTYS", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("DashboardWindow", u"19/12/2022", None));
        ___qtreewidgetitem4 = self.lessons_treeWidget.topLevelItem(2)
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("DashboardWindow", u"VTYS", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("DashboardWindow", u"12/12/2022", None));
        self.lessons_treeWidget.setSortingEnabled(__sortingEnabled)

        self.delete_course_btn.setText(QCoreApplication.translate("DashboardWindow", u"Delete", None))
        self.update_course_btn.setText(QCoreApplication.translate("DashboardWindow", u"Update", None))
        self.add_new_student_btn.setText(QCoreApplication.translate("DashboardWindow", u"Add New Student", None))
        ___qtreewidgetitem5 = self.students_treeWidget.headerItem()
        ___qtreewidgetitem5.setText(3, QCoreApplication.translate("DashboardWindow", u"Student No", None));
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("DashboardWindow", u"ID", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("DashboardWindow", u"Surname", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("DashboardWindow", u"Name", None));
        self.delete_student_btn.setText(QCoreApplication.translate("DashboardWindow", u"Delete", None))
        self.update_student_btn.setText(QCoreApplication.translate("DashboardWindow", u"Update", None))
        self.label.setText(QCoreApplication.translate("DashboardWindow", u"Select Course:", None))
        self.add_students_to_course_btn.setText(QCoreApplication.translate("DashboardWindow", u"Add", None))
        self.label_2.setText(QCoreApplication.translate("DashboardWindow", u"Add selected students to course", None))
        self.add_student_btn.setText(QCoreApplication.translate("DashboardWindow", u"Add Student", None))
        self.label_10.setText(QCoreApplication.translate("DashboardWindow", u"Student No:", None))
        self.label_18.setText(QCoreApplication.translate("DashboardWindow", u"TC No:", None))
        self.label_23.setText(QCoreApplication.translate("DashboardWindow", u"Lastname:", None))
        self.label_20.setText(QCoreApplication.translate("DashboardWindow", u"Name:", None))
        self.label_12.setText(QCoreApplication.translate("DashboardWindow", u"Scan students ID numbers:", None))
        self.label_13.setText(QCoreApplication.translate("DashboardWindow", u"Lesson Name", None))
        self.scan_tc_btn.setText(QCoreApplication.translate("DashboardWindow", u"Scan", None))
        ___qtreewidgetitem6 = self.attendance_treeWidget.headerItem()
        ___qtreewidgetitem6.setText(6, QCoreApplication.translate("DashboardWindow", u"Student No", None));
        ___qtreewidgetitem6.setText(5, QCoreApplication.translate("DashboardWindow", u"Student TC", None));
        ___qtreewidgetitem6.setText(4, QCoreApplication.translate("DashboardWindow", u"Student Surname", None));
        ___qtreewidgetitem6.setText(3, QCoreApplication.translate("DashboardWindow", u"Student Name", None));
        ___qtreewidgetitem6.setText(2, QCoreApplication.translate("DashboardWindow", u"Lesson Name", None));
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("DashboardWindow", u"Lesson Date", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("DashboardWindow", u"Lesson ID", None));
        self.take_attendance_btn.setText(QCoreApplication.translate("DashboardWindow", u"Take Attendance", None))
        self.label_75.setText(QCoreApplication.translate("DashboardWindow", u"Name:", None))
        self.label_74.setText(QCoreApplication.translate("DashboardWindow", u"Lastname", None))
        self.label_76.setText(QCoreApplication.translate("DashboardWindow", u"TC No:", None))
        self.pushButton_30.setText(QCoreApplication.translate("DashboardWindow", u"Update", None))
        self.label_77.setText(QCoreApplication.translate("DashboardWindow", u"Username:", None))
        self.label_79.setText(QCoreApplication.translate("DashboardWindow", u"Password:", None))
    # retranslateUi

