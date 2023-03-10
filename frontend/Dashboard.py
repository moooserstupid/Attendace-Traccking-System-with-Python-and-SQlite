# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DashboardWindow(object):
    def setupUi(self, DashboardWindow):
        DashboardWindow.setObjectName("DashboardWindow")
        DashboardWindow.resize(1097, 653)
        self.centralwidget = QtWidgets.QWidget(DashboardWindow)
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
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(101, 16777215))
        self.frame_left_menu.setStyleSheet("")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_top_menus_2 = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus_2.setObjectName("frame_top_menus_2")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_top_menus_2)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.page_name_label = QtWidgets.QLabel(self.frame_top_menus_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page_name_label.setFont(font)
        self.page_name_label.setStyleSheet("")
        self.page_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.page_name_label.setObjectName("page_name_label")
        self.verticalLayout_26.addWidget(self.page_name_label)
        self.dashboard_menu_btn = QtWidgets.QPushButton(self.frame_top_menus_2)
        self.dashboard_menu_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.dashboard_menu_btn.setCheckable(False)
        self.dashboard_menu_btn.setChecked(False)
        self.dashboard_menu_btn.setObjectName("dashboard_menu_btn")
        self.verticalLayout_26.addWidget(self.dashboard_menu_btn)
        self.courses_menu_btn = QtWidgets.QPushButton(self.frame_top_menus_2)
        self.courses_menu_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.courses_menu_btn.setStyleSheet("")
        self.courses_menu_btn.setCheckable(False)
        self.courses_menu_btn.setObjectName("courses_menu_btn")
        self.verticalLayout_26.addWidget(self.courses_menu_btn)
        self.lessons_menu_btn = QtWidgets.QPushButton(self.frame_top_menus_2)
        self.lessons_menu_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lessons_menu_btn.setCheckable(False)
        self.lessons_menu_btn.setObjectName("lessons_menu_btn")
        self.verticalLayout_26.addWidget(self.lessons_menu_btn)
        self.students_menu_btn = QtWidgets.QPushButton(self.frame_top_menus_2)
        self.students_menu_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.students_menu_btn.setCheckable(False)
        self.students_menu_btn.setObjectName("students_menu_btn")
        self.verticalLayout_26.addWidget(self.students_menu_btn)
        self.take_attendance_menu_btn = QtWidgets.QPushButton(self.frame_top_menus_2)
        self.take_attendance_menu_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.take_attendance_menu_btn.setStyleSheet("")
        self.take_attendance_menu_btn.setCheckable(False)
        self.take_attendance_menu_btn.setObjectName("take_attendance_menu_btn")
        self.verticalLayout_26.addWidget(self.take_attendance_menu_btn)
        self.teacher_info_menu_btn = QtWidgets.QPushButton(self.frame_top_menus_2)
        self.teacher_info_menu_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.teacher_info_menu_btn.setCheckable(False)
        self.teacher_info_menu_btn.setObjectName("teacher_info_menu_btn")
        self.verticalLayout_26.addWidget(self.teacher_info_menu_btn)
        self.sign_out_btn = QtWidgets.QPushButton(self.frame_top_menus_2)
        self.sign_out_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.sign_out_btn.setCheckable(False)
        self.sign_out_btn.setObjectName("sign_out_btn")
        self.verticalLayout_26.addWidget(self.sign_out_btn)
        self.verticalLayout_23.addWidget(self.frame_top_menus_2)
        self.horizontalLayout_5.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.dashboard_page = QtWidgets.QWidget()
        self.dashboard_page.setObjectName("dashboard_page")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.dashboard_page)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.welcome_label = QtWidgets.QLabel(self.dashboard_page)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.verticalLayout_28.addWidget(self.welcome_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.courses_page = QtWidgets.QWidget()
        self.courses_page.setObjectName("courses_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.courses_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.courses_treeWidget = QtWidgets.QTreeWidget(self.courses_page)
        self.courses_treeWidget.setObjectName("courses_treeWidget")
        self.verticalLayout_5.addWidget(self.courses_treeWidget)
        self.go_to_add_course_btn = QtWidgets.QPushButton(self.courses_page)
        self.go_to_add_course_btn.setMinimumSize(QtCore.QSize(250, 0))
        self.go_to_add_course_btn.setObjectName("go_to_add_course_btn")
        self.verticalLayout_5.addWidget(self.go_to_add_course_btn, 0, QtCore.Qt.AlignRight)
        self.stackedWidget.addWidget(self.courses_page)
        self.add_course_page = QtWidgets.QWidget()
        self.add_course_page.setObjectName("add_course_page")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.add_course_page)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtWidgets.QLabel(self.add_course_page)
        self.label_14.setMaximumSize(QtCore.QSize(120, 30))
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 0, 1, 1)
        self.end_date_dateEdit = QtWidgets.QDateEdit(self.add_course_page)
        self.end_date_dateEdit.setObjectName("end_date_dateEdit")
        self.gridLayout.addWidget(self.end_date_dateEdit, 5, 1, 1, 1)
        self.start_date_dateEdit = QtWidgets.QDateEdit(self.add_course_page)
        self.start_date_dateEdit.setObjectName("start_date_dateEdit")
        self.gridLayout.addWidget(self.start_date_dateEdit, 4, 1, 1, 1)
        self.course_name_lineEdit = QtWidgets.QLineEdit(self.add_course_page)
        self.course_name_lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.course_name_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.course_name_lineEdit.setObjectName("course_name_lineEdit")
        self.gridLayout.addWidget(self.course_name_lineEdit, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.add_course_page)
        self.label_7.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.add_course_btn = QtWidgets.QPushButton(self.add_course_page)
        self.add_course_btn.setObjectName("add_course_btn")
        self.gridLayout.addWidget(self.add_course_btn, 7, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.add_course_page)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.add_course_page)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.add_course_page)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1)
        self.course_description_lineEdit = QtWidgets.QLineEdit(self.add_course_page)
        self.course_description_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.course_description_lineEdit.setObjectName("course_description_lineEdit")
        self.gridLayout.addWidget(self.course_description_lineEdit, 1, 1, 1, 1)
        self.total_lesson_count_spinBox = QtWidgets.QSpinBox(self.add_course_page)
        self.total_lesson_count_spinBox.setObjectName("total_lesson_count_spinBox")
        self.gridLayout.addWidget(self.total_lesson_count_spinBox, 6, 1, 1, 1)
        self.verticalLayout_29.addLayout(self.gridLayout)
        self.stackedWidget.addWidget(self.add_course_page)
        self.lessons_page = QtWidgets.QWidget()
        self.lessons_page.setObjectName("lessons_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.lessons_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.course_id_comboBox = QtWidgets.QComboBox(self.lessons_page)
        self.course_id_comboBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.course_id_comboBox.setObjectName("course_id_comboBox")
        self.gridLayout_4.addWidget(self.course_id_comboBox, 1, 1, 1, 1)
        self.add_lesson_btn = QtWidgets.QPushButton(self.lessons_page)
        self.add_lesson_btn.setObjectName("add_lesson_btn")
        self.gridLayout_4.addWidget(self.add_lesson_btn, 5, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.lessons_page)
        self.label_19.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)
        self.lesson_date_dateEdit = QtWidgets.QDateEdit(self.lessons_page)
        self.lesson_date_dateEdit.setObjectName("lesson_date_dateEdit")
        self.gridLayout_4.addWidget(self.lesson_date_dateEdit, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.lessons_page)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.lessons_treeWidget = QtWidgets.QTreeWidget(self.lessons_page)
        self.lessons_treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lessons_treeWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lessons_treeWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lessons_treeWidget.setTabKeyNavigation(False)
        self.lessons_treeWidget.setDragEnabled(False)
        self.lessons_treeWidget.setDragDropOverwriteMode(False)
        self.lessons_treeWidget.setAlternatingRowColors(True)
        self.lessons_treeWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.lessons_treeWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.lessons_treeWidget.setAnimated(False)
        self.lessons_treeWidget.setAllColumnsShowFocus(False)
        self.lessons_treeWidget.setWordWrap(False)
        self.lessons_treeWidget.setHeaderHidden(False)
        self.lessons_treeWidget.setObjectName("lessons_treeWidget")
        self.verticalLayout_3.addWidget(self.lessons_treeWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.delete_course_btn = QtWidgets.QPushButton(self.lessons_page)
        self.delete_course_btn.setObjectName("delete_course_btn")
        self.horizontalLayout_4.addWidget(self.delete_course_btn)
        self.update_course_btn = QtWidgets.QPushButton(self.lessons_page)
        self.update_course_btn.setObjectName("update_course_btn")
        self.horizontalLayout_4.addWidget(self.update_course_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.lessons_page)
        self.students_page = QtWidgets.QWidget()
        self.students_page.setObjectName("students_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.students_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.add_new_student_btn = QtWidgets.QPushButton(self.students_page)
        self.add_new_student_btn.setMinimumSize(QtCore.QSize(250, 0))
        self.add_new_student_btn.setMaximumSize(QtCore.QSize(250, 16777215))
        self.add_new_student_btn.setObjectName("add_new_student_btn")
        self.verticalLayout_8.addWidget(self.add_new_student_btn)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.students_treeWidget = QtWidgets.QTreeWidget(self.students_page)
        self.students_treeWidget.setMinimumSize(QtCore.QSize(502, 0))
        self.students_treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.students_treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.students_treeWidget.setObjectName("students_treeWidget")
        self.verticalLayout_10.addWidget(self.students_treeWidget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.delete_student_btn = QtWidgets.QPushButton(self.students_page)
        self.delete_student_btn.setObjectName("delete_student_btn")
        self.horizontalLayout_7.addWidget(self.delete_student_btn)
        self.update_student_btn = QtWidgets.QPushButton(self.students_page)
        self.update_student_btn.setObjectName("update_student_btn")
        self.horizontalLayout_7.addWidget(self.update_student_btn)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.students_page)
        self.label.setMaximumSize(QtCore.QSize(100, 20))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)
        self.add_students_to_course_btn = QtWidgets.QPushButton(self.students_page)
        self.add_students_to_course_btn.setMinimumSize(QtCore.QSize(250, 0))
        self.add_students_to_course_btn.setMaximumSize(QtCore.QSize(250, 16777215))
        self.add_students_to_course_btn.setObjectName("add_students_to_course_btn")
        self.gridLayout_3.addWidget(self.add_students_to_course_btn, 3, 4, 1, 1)
        self.select_course_comboBox = QtWidgets.QComboBox(self.students_page)
        self.select_course_comboBox.setObjectName("select_course_comboBox")
        self.gridLayout_3.addWidget(self.select_course_comboBox, 2, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.students_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_10)
        self.stackedWidget.addWidget(self.students_page)
        self.add_student_page = QtWidgets.QWidget()
        self.add_student_page.setObjectName("add_student_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.add_student_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.student_lastname_lineEdit = QtWidgets.QLineEdit(self.add_student_page)
        self.student_lastname_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.student_lastname_lineEdit.setObjectName("student_lastname_lineEdit")
        self.gridLayout_5.addWidget(self.student_lastname_lineEdit, 2, 1, 1, 1)
        self.add_student_btn = QtWidgets.QPushButton(self.add_student_page)
        self.add_student_btn.setObjectName("add_student_btn")
        self.gridLayout_5.addWidget(self.add_student_btn, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.add_student_page)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 4, 0, 1, 1)
        self.student_name_lineEdit = QtWidgets.QLineEdit(self.add_student_page)
        self.student_name_lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.student_name_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.student_name_lineEdit.setObjectName("student_name_lineEdit")
        self.gridLayout_5.addWidget(self.student_name_lineEdit, 1, 1, 1, 1)
        self.student_no_lineEdit = QtWidgets.QLineEdit(self.add_student_page)
        self.student_no_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.student_no_lineEdit.setObjectName("student_no_lineEdit")
        self.gridLayout_5.addWidget(self.student_no_lineEdit, 4, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.add_student_page)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.add_student_page)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.add_student_page)
        self.label_20.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 1, 0, 1, 1)
        self.student_tc_no_lineEdit = QtWidgets.QLineEdit(self.add_student_page)
        self.student_tc_no_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.student_tc_no_lineEdit.setObjectName("student_tc_no_lineEdit")
        self.gridLayout_5.addWidget(self.student_tc_no_lineEdit, 0, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_5)
        self.stackedWidget.addWidget(self.add_student_page)
        self.take_attendance_page = QtWidgets.QWidget()
        self.take_attendance_page.setObjectName("take_attendance_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.take_attendance_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lesson_id_comboBox = QtWidgets.QComboBox(self.take_attendance_page)
        self.lesson_id_comboBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lesson_id_comboBox.setObjectName("lesson_id_comboBox")
        self.gridLayout_2.addWidget(self.lesson_id_comboBox, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.take_attendance_page)
        self.label_12.setMaximumSize(QtCore.QSize(175, 16777215))
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.take_attendance_page)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.scan_tc_btn = QtWidgets.QPushButton(self.take_attendance_page)
        self.scan_tc_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scan_tc_btn.setObjectName("scan_tc_btn")
        self.gridLayout_2.addWidget(self.scan_tc_btn, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.attendance_treeWidget = QtWidgets.QTreeWidget(self.take_attendance_page)
        self.attendance_treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.attendance_treeWidget.setObjectName("attendance_treeWidget")
        self.horizontalLayout.addWidget(self.attendance_treeWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.take_attendance_btn = QtWidgets.QPushButton(self.take_attendance_page)
        self.take_attendance_btn.setMinimumSize(QtCore.QSize(250, 0))
        self.take_attendance_btn.setMaximumSize(QtCore.QSize(250, 16777215))
        self.take_attendance_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.take_attendance_btn.setObjectName("take_attendance_btn")
        self.verticalLayout_2.addWidget(self.take_attendance_btn, 0, QtCore.Qt.AlignHCenter)
        self.all_attendaces_btn = QtWidgets.QPushButton(self.take_attendance_page)
        self.all_attendaces_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.all_attendaces_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.all_attendaces_btn.setObjectName("all_attendaces_btn")
        self.verticalLayout_2.addWidget(self.all_attendaces_btn, 0, QtCore.Qt.AlignRight)
        self.stackedWidget.addWidget(self.take_attendance_page)
        self.all_attendances_page = QtWidgets.QWidget()
        self.all_attendances_page.setObjectName("all_attendances_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.all_attendances_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.all_attendances_treeWidget = QtWidgets.QTreeWidget(self.all_attendances_page)
        self.all_attendances_treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.all_attendances_treeWidget.setObjectName("all_attendances_treeWidget")
        self.verticalLayout_4.addWidget(self.all_attendances_treeWidget)
        self.stackedWidget.addWidget(self.all_attendances_page)
        self.teacher_info_page = QtWidgets.QWidget()
        self.teacher_info_page.setObjectName("teacher_info_page")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.teacher_info_page)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_75 = QtWidgets.QLabel(self.teacher_info_page)
        self.label_75.setObjectName("label_75")
        self.gridLayout_19.addWidget(self.label_75, 1, 0, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.teacher_info_page)
        self.label_74.setObjectName("label_74")
        self.gridLayout_19.addWidget(self.label_74, 2, 0, 1, 1)
        self.ti_tc_no_lineEdit = QtWidgets.QLineEdit(self.teacher_info_page)
        self.ti_tc_no_lineEdit.setEnabled(False)
        self.ti_tc_no_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.ti_tc_no_lineEdit.setObjectName("ti_tc_no_lineEdit")
        self.gridLayout_19.addWidget(self.ti_tc_no_lineEdit, 0, 1, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.teacher_info_page)
        self.label_76.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_76.setObjectName("label_76")
        self.gridLayout_19.addWidget(self.label_76, 0, 0, 1, 1)
        self.ti_username_lineEdit = QtWidgets.QLineEdit(self.teacher_info_page)
        self.ti_username_lineEdit.setEnabled(True)
        self.ti_username_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.ti_username_lineEdit.setObjectName("ti_username_lineEdit")
        self.gridLayout_19.addWidget(self.ti_username_lineEdit, 3, 1, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_12.setContentsMargins(0, 0, 1, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.update_teacher_info_btn = QtWidgets.QPushButton(self.teacher_info_page)
        self.update_teacher_info_btn.setEnabled(True)
        self.update_teacher_info_btn.setObjectName("update_teacher_info_btn")
        self.horizontalLayout_12.addWidget(self.update_teacher_info_btn)
        self.gridLayout_19.addLayout(self.horizontalLayout_12, 5, 1, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.teacher_info_page)
        self.label_77.setObjectName("label_77")
        self.gridLayout_19.addWidget(self.label_77, 3, 0, 1, 1)
        self.ti_name_lineEdit = QtWidgets.QLineEdit(self.teacher_info_page)
        self.ti_name_lineEdit.setEnabled(False)
        self.ti_name_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.ti_name_lineEdit.setObjectName("ti_name_lineEdit")
        self.gridLayout_19.addWidget(self.ti_name_lineEdit, 1, 1, 1, 1)
        self.ti_lastname_lineEdit = QtWidgets.QLineEdit(self.teacher_info_page)
        self.ti_lastname_lineEdit.setEnabled(False)
        self.ti_lastname_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.ti_lastname_lineEdit.setObjectName("ti_lastname_lineEdit")
        self.gridLayout_19.addWidget(self.ti_lastname_lineEdit, 2, 1, 1, 1)
        self.label_79 = QtWidgets.QLabel(self.teacher_info_page)
        self.label_79.setObjectName("label_79")
        self.gridLayout_19.addWidget(self.label_79, 4, 0, 1, 1)
        self.ti_password_lineEdit = QtWidgets.QLineEdit(self.teacher_info_page)
        self.ti_password_lineEdit.setEnabled(True)
        self.ti_password_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.ti_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ti_password_lineEdit.setObjectName("ti_password_lineEdit")
        self.gridLayout_19.addWidget(self.ti_password_lineEdit, 4, 1, 1, 1)
        self.verticalLayout_34.addLayout(self.gridLayout_19)
        self.stackedWidget.addWidget(self.teacher_info_page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_27.addWidget(self.stackedWidget)
        self.horizontalLayout_5.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        DashboardWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DashboardWindow)
        self.statusbar.setObjectName("statusbar")
        DashboardWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DashboardWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(DashboardWindow)

    def retranslateUi(self, DashboardWindow):
        _translate = QtCore.QCoreApplication.translate
        DashboardWindow.setWindowTitle(_translate("DashboardWindow", "Attendance System Dashboard"))
        self.page_name_label.setText(_translate("DashboardWindow", "Dashboard"))
        self.dashboard_menu_btn.setText(_translate("DashboardWindow", "Dashboard"))
        self.courses_menu_btn.setText(_translate("DashboardWindow", "Courses"))
        self.lessons_menu_btn.setText(_translate("DashboardWindow", "Lessons"))
        self.students_menu_btn.setText(_translate("DashboardWindow", "Students"))
        self.take_attendance_menu_btn.setText(_translate("DashboardWindow", "Take Attendance"))
        self.teacher_info_menu_btn.setText(_translate("DashboardWindow", "Teacher Info"))
        self.sign_out_btn.setText(_translate("DashboardWindow", "Sign Out"))
        self.welcome_label.setText(_translate("DashboardWindow", "Welcome "))
        self.courses_treeWidget.headerItem().setText(0, _translate("DashboardWindow", "Course Name"))
        self.courses_treeWidget.headerItem().setText(1, _translate("DashboardWindow", "Teacher ID"))
        self.courses_treeWidget.headerItem().setText(2, _translate("DashboardWindow", "Descrition"))
        self.courses_treeWidget.headerItem().setText(3, _translate("DashboardWindow", "Start Date"))
        self.courses_treeWidget.headerItem().setText(4, _translate("DashboardWindow", "End Date"))
        self.courses_treeWidget.headerItem().setText(5, _translate("DashboardWindow", "Count Of Lessons"))
        self.go_to_add_course_btn.setText(_translate("DashboardWindow", "Add Course"))
        self.label_14.setText(_translate("DashboardWindow", "Start Date:"))
        self.label_7.setText(_translate("DashboardWindow", "Course Name:"))
        self.add_course_btn.setText(_translate("DashboardWindow", "Add Course"))
        self.label_16.setText(_translate("DashboardWindow", "Total Lesson Count"))
        self.label_9.setText(_translate("DashboardWindow", "Course Description:"))
        self.label_15.setText(_translate("DashboardWindow", "End Date:"))
        self.add_lesson_btn.setText(_translate("DashboardWindow", "Add Lesson"))
        self.label_19.setText(_translate("DashboardWindow", "Lesson Date:"))
        self.label_21.setText(_translate("DashboardWindow", "Course ID:"))
        self.lessons_treeWidget.setSortingEnabled(True)
        self.lessons_treeWidget.headerItem().setText(0, _translate("DashboardWindow", "Lesson Date"))
        self.lessons_treeWidget.headerItem().setText(1, _translate("DashboardWindow", "Course ID"))
        self.lessons_treeWidget.headerItem().setText(2, _translate("DashboardWindow", "Course Name"))
        self.lessons_treeWidget.headerItem().setText(3, _translate("DashboardWindow", "Teacher ID"))
        self.lessons_treeWidget.headerItem().setText(4, _translate("DashboardWindow", "Teacher Name"))
        self.lessons_treeWidget.headerItem().setText(5, _translate("DashboardWindow", "Teacher Last Name"))
        self.delete_course_btn.setText(_translate("DashboardWindow", "Delete"))
        self.update_course_btn.setText(_translate("DashboardWindow", "Update"))
        self.add_new_student_btn.setText(_translate("DashboardWindow", "Add New Student"))
        self.students_treeWidget.setSortingEnabled(True)
        self.students_treeWidget.headerItem().setText(0, _translate("DashboardWindow", "Student No"))
        self.students_treeWidget.headerItem().setText(1, _translate("DashboardWindow", "Name"))
        self.students_treeWidget.headerItem().setText(2, _translate("DashboardWindow", "Surname"))
        self.students_treeWidget.headerItem().setText(3, _translate("DashboardWindow", "ID"))
        self.delete_student_btn.setText(_translate("DashboardWindow", "Delete"))
        self.update_student_btn.setText(_translate("DashboardWindow", "Update"))
        self.label.setText(_translate("DashboardWindow", "Select Course:"))
        self.add_students_to_course_btn.setText(_translate("DashboardWindow", "Add"))
        self.label_2.setText(_translate("DashboardWindow", "Add selected students to course"))
        self.add_student_btn.setText(_translate("DashboardWindow", "Add Student"))
        self.label_10.setText(_translate("DashboardWindow", "Student No:"))
        self.label_18.setText(_translate("DashboardWindow", "TC No:"))
        self.label_23.setText(_translate("DashboardWindow", "Lastname:"))
        self.label_20.setText(_translate("DashboardWindow", "Name:"))
        self.label_12.setText(_translate("DashboardWindow", "Scan students ID numbers:"))
        self.label_13.setText(_translate("DashboardWindow", "Lesson ID"))
        self.scan_tc_btn.setText(_translate("DashboardWindow", "Scan"))
        self.attendance_treeWidget.setSortingEnabled(True)
        self.attendance_treeWidget.headerItem().setText(0, _translate("DashboardWindow", "Lesson ID"))
        self.attendance_treeWidget.headerItem().setText(1, _translate("DashboardWindow", "Lesson Date"))
        self.attendance_treeWidget.headerItem().setText(2, _translate("DashboardWindow", "Course Name"))
        self.attendance_treeWidget.headerItem().setText(3, _translate("DashboardWindow", "Student Name"))
        self.attendance_treeWidget.headerItem().setText(4, _translate("DashboardWindow", "Student Surname"))
        self.attendance_treeWidget.headerItem().setText(5, _translate("DashboardWindow", "Student TC"))
        self.attendance_treeWidget.headerItem().setText(6, _translate("DashboardWindow", "Student No"))
        self.take_attendance_btn.setText(_translate("DashboardWindow", "Take Attendance"))
        self.all_attendaces_btn.setText(_translate("DashboardWindow", "View All Attendances"))
        self.all_attendances_treeWidget.setSortingEnabled(True)
        self.all_attendances_treeWidget.headerItem().setText(0, _translate("DashboardWindow", "Lesson ID"))
        self.all_attendances_treeWidget.headerItem().setText(1, _translate("DashboardWindow", "Lesson Date"))
        self.all_attendances_treeWidget.headerItem().setText(2, _translate("DashboardWindow", "Course Name"))
        self.all_attendances_treeWidget.headerItem().setText(3, _translate("DashboardWindow", "Student Name"))
        self.all_attendances_treeWidget.headerItem().setText(4, _translate("DashboardWindow", "Student Surname"))
        self.all_attendances_treeWidget.headerItem().setText(5, _translate("DashboardWindow", "Student TC"))
        self.all_attendances_treeWidget.headerItem().setText(6, _translate("DashboardWindow", "Student No"))
        self.label_75.setText(_translate("DashboardWindow", "Name:"))
        self.label_74.setText(_translate("DashboardWindow", "Lastname"))
        self.label_76.setText(_translate("DashboardWindow", "TC No:"))
        self.update_teacher_info_btn.setText(_translate("DashboardWindow", "Update"))
        self.label_77.setText(_translate("DashboardWindow", "Username:"))
        self.label_79.setText(_translate("DashboardWindow", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DashboardWindow = QtWidgets.QMainWindow()
    ui = Ui_DashboardWindow()
    ui.setupUi(DashboardWindow)
    DashboardWindow.show()
    sys.exit(app.exec_())
