# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import entities
import exception


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(378, 386)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("User_Avatar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signupBT = QtWidgets.QPushButton(self.centralwidget)
        self.signupBT.setGeometry(QtCore.QRect(140, 250, 91, 25))
        self.signupBT.setObjectName("signupBT")
        self.phText = QtWidgets.QLineEdit(self.centralwidget)
        self.phText.setGeometry(QtCore.QRect(90, 100, 181, 25))
        self.phText.setMaxLength(11)
        self.phText.setObjectName("phText")
        self.pwText = QtWidgets.QLineEdit(self.centralwidget)
        self.pwText.setGeometry(QtCore.QRect(90, 160, 181, 25))
        self.pwText.setMaxLength(64)
        self.pwText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwText.setObjectName("pwText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 70, 101, 20))
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 130, 101, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(50, 299, 271, 31))
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")
        self.loginBT = QtWidgets.QPushButton(self.centralwidget)
        self.loginBT.setGeometry(QtCore.QRect(140, 210, 91, 25))
        self.loginBT.setObjectName("loginBT")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 22))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        self.loginBT.clicked.connect(login)
        self.signupBT.clicked.connect(signup)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "ورود / عضویت"))
        self.signupBT.setText(_translate("LoginWindow", "ثبت نام"))
        self.phText.setText(_translate("LoginWindow", "09"))
        self.label.setText(_translate("LoginWindow", "شماره همراه"))
        self.label_2.setText(_translate("LoginWindow", "رمز عبور"))
        self.message.setText(_translate("LoginWindow", "پیام"))
        self.loginBT.setText(_translate("LoginWindow", "ورود"))


def login():
    try:
        entities.User.login(ui.phText.text(), ui.pwText.text())
        ui.message.setText('با موفقیت وارد شدید')
    except exception.LoginError:
        ui.message.setText('شماره همراه یا رمز عبور اشتباه است')
    except exception.PhoneNumberFormatError:
        ui.message.setText('فرمت شماره همراه اشتباه است')


def signup():
    try:
        entities.User.add(ui.phText.text(), ui.pwText.text())
        ui.message.setText('با موفقیت ثبت نام شدید')
    except exception.SignupError:
        ui.message.setText('شماره همراه قبلا استفاده شده')
    except exception.PhoneNumberFormatError:
        ui.message.setText('فرمت شماره همراه اشتباه است')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
