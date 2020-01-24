# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


# from ui.add_family_member import *
# from ui.user_edit_window import *
# from ui.user_show_window import *
# from ui.search_doctors_window import *

def get_follow_apt_id(text):
    global id
    id = text


class Ui_MainWindow(object):
    def open_show_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_user_show_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_edit_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_user_edit_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_add_family_member_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_add_family_member_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_search_doctors_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_search_doctors_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 781, 451))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # self.set_appointment = QtWidgets.QPushButton(self.centralwidget)
        # self.set_appointment.setGeometry(QtCore.QRect(644, 490, 111, 21))
        # self.set_appointment.setObjectName("set_appointment")
        self.search_doctors = QtWidgets.QPushButton(self.centralwidget)
        self.search_doctors.setGeometry(QtCore.QRect(644, 463, 111, 20))
        self.search_doctors.setObjectName("search_doctors")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 520, 251, 16))
        self.label_2.setObjectName("label_2")
        self.appointment_id_input = QtWidgets.QLineEdit(self.centralwidget)
        self.appointment_id_input.setGeometry(QtCore.QRect(410, 520, 201, 20))
        self.appointment_id_input.setObjectName("appointment_id_input")
        self.follow_btn = QtWidgets.QPushButton(self.centralwidget)
        self.follow_btn.setGeometry(QtCore.QRect(650, 520, 111, 21))
        self.follow_btn.setObjectName("follow_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menumy_orofile = QtWidgets.QMenu(self.menubar)
        self.menumy_orofile.setObjectName("menumy_orofile")
        self.menusee_my_appointments = QtWidgets.QMenu(self.menumy_orofile)
        self.menusee_my_appointments.setObjectName("menusee_my_appointments")
        self.menusaved_doctors = QtWidgets.QMenu(self.menumy_orofile)
        self.menusaved_doctors.setObjectName("menusaved_doctors")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionby_name = QtWidgets.QAction(MainWindow)
        self.actionby_name.setObjectName("actionby_name")
        self.actionby_family = QtWidgets.QAction(MainWindow)
        self.actionby_family.setObjectName("actionby_family")
        self.actionby_specialty = QtWidgets.QAction(MainWindow)
        self.actionby_specialty.setObjectName("actionby_specialty")
        self.actionby_place = QtWidgets.QAction(MainWindow)
        self.actionby_place.setObjectName("actionby_place")
        self.actionshow = QtWidgets.QAction(MainWindow)
        self.actionshow.setObjectName("actionshow")
        self.actionedit = QtWidgets.QAction(MainWindow)
        self.actionedit.setObjectName("actionedit")
        self.actionadd_family_member = QtWidgets.QAction(MainWindow)
        self.actionadd_family_member.setObjectName("actionadd_family_member")
        self.actionsee_my_family_appointments = QtWidgets.QAction(MainWindow)
        self.actionsee_my_family_appointments.setObjectName("actionsee_my_family_appointments")
        self.actionmy_reservations = QtWidgets.QAction(MainWindow)
        self.actionmy_reservations.setObjectName("actionmy_reservations")
        self.actionmy_family_reservations = QtWidgets.QAction(MainWindow)
        self.actionmy_family_reservations.setObjectName("actionmy_family_reservations")
        self.actionview_saved_doctors = QtWidgets.QAction(MainWindow)
        self.actionview_saved_doctors.setObjectName("actionview_saved_doctors")
        self.actionadd_saved_doctors = QtWidgets.QAction(MainWindow)
        self.actionadd_saved_doctors.setObjectName("actionadd_saved_doctors")
        self.menusee_my_appointments.addAction(self.actionmy_reservations)
        self.menusee_my_appointments.addAction(self.actionmy_family_reservations)
        self.menusaved_doctors.addAction(self.actionview_saved_doctors)
        self.menusaved_doctors.addAction(self.actionadd_saved_doctors)
        self.menumy_orofile.addAction(self.actionshow)
        self.menumy_orofile.addAction(self.actionedit)
        self.menumy_orofile.addAction(self.actionadd_family_member)
        self.menumy_orofile.addSeparator()
        self.menumy_orofile.addAction(self.menusee_my_appointments.menuAction())
        self.menumy_orofile.addAction(self.actionsee_my_family_appointments)
        self.menumy_orofile.addAction(self.menusaved_doctors.menuAction())
        self.menubar.addAction(self.menumy_orofile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ###############################################

        self.actionshow.triggered.connect(lambda: self.open_show_window())
        self.actionedit.triggered.connect(lambda: self.open_edit_window())
        self.actionadd_family_member.triggered.connect(lambda: self.open_add_family_member_window())
        self.search_doctors.clicked.connect(lambda: self.open_search_doctors_window())
        self.actionmy_family_reservations.triggered.connect(
            lambda: self.Clicked(dbms.view_other_appointments(create_connection("db.sqlite"), dbms.current_logged_in)))
        self.actionmy_reservations.triggered.connect(
            lambda: self.Clicked(dbms.view_your_appointments(create_connection("db.sqlite"), dbms.current_logged_in)))
        self.actionsee_my_family_appointments.triggered.connect(
            lambda: self.Clicked(dbms.view_family_appointments(create_connection("db.sqlite"), dbms.current_logged_in)))
        self.actionview_saved_doctors.triggered.connect(
            lambda: self.Clicked(dbms.get_saved_doctors(create_connection("db.sqlite"), dbms.current_logged_in)))
        self.actionadd_saved_doctors.triggered.connect(lambda: self.open_search_doctors_window())
        self.follow_btn.clicked.connect(lambda: self.Clicked(
            dbms.follow_appointment_info(create_connection("db.sqlite"), id, dbms.current_logged_in)))
        self.appointment_id_input.textChanged.connect(get_follow_apt_id)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ""))
        # self.set_appointment.setText(_translate("MainWindow", "get appointment"))
        self.search_doctors.setText(_translate("MainWindow", "search doctors"))
        self.label_2.setText(_translate("MainWindow", "follow your appointment by follow_code"))
        self.follow_btn.setText(_translate("MainWindow", "follow"))
        self.menumy_orofile.setTitle(_translate("MainWindow", "my profile"))
        self.menusee_my_appointments.setTitle(_translate("MainWindow", "see my appointments"))
        self.menusaved_doctors.setTitle(_translate("MainWindow", "saved doctors"))
        self.actionby_name.setText(_translate("MainWindow", "by name"))
        self.actionby_name.setStatusTip(_translate("MainWindow", "choose your doctor by name"))
        self.actionby_name.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionby_family.setText(_translate("MainWindow", "by family"))
        self.actionby_family.setStatusTip(_translate("MainWindow", "choose your doctor by family"))
        self.actionby_family.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionby_specialty.setText(_translate("MainWindow", "by specialty"))
        self.actionby_specialty.setStatusTip(_translate("MainWindow", "choose your doctor by specialty"))
        self.actionby_specialty.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionby_place.setText(_translate("MainWindow", "by place"))
        self.actionby_place.setStatusTip(_translate("MainWindow", "choose your doctor by place"))
        self.actionby_place.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionshow.setText(_translate("MainWindow", "show"))
        self.actionshow.setStatusTip(_translate("MainWindow", "show profile"))
        self.actionedit.setText(_translate("MainWindow", "edit"))
        self.actionedit.setStatusTip(_translate("MainWindow", "edit profile"))
        self.actionadd_family_member.setText(_translate("MainWindow", "add family member"))
        self.actionsee_my_family_appointments.setText(_translate("MainWindow", "see my family appointments"))
        self.actionmy_reservations.setText(_translate("MainWindow", "my reservations"))
        self.actionmy_family_reservations.setText(_translate("MainWindow", "my family reservations"))
        self.actionview_saved_doctors.setText(_translate("MainWindow", "view saved doctors"))
        self.actionadd_saved_doctors.setText(_translate("MainWindow", "add saved doctors"))

    def Clicked(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
