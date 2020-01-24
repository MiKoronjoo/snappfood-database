# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

import entities
import exception

class Ui_infoWindow(object):
    def show_MainWindow(self):
        self.ui = Ui_MainWindow()
        self.ui.user = self.user
        self.ui.setupUi(LoginWindow)
        LoginWindow.show()

    def edit_info(self):
        try:
            self.user.first_name = self.lineEdit.text()
            self.user.last_name = self.lineEdit_2.text()
            self.user.email = self.lineEdit_4.text()
            self.message.setText('اطلاعات با موفقیت ویرایش شد')
        except exception.EmailFormatError:
            self.message.setText('فرمت ایمیل اشتباه است')
        except exception.EmailIsAlreadyUsed:
            self.message.setText('این ایمیل قبلا استفاده شده')

    def change_pw(self):
        self.user.change_password(self.lineEdit_5.text())
        self.message.setText('رمز عبور با موفقیت تغییر کرد')

    def setupUi(self, infoWindow):
        infoWindow.setObjectName("infoWindow")
        infoWindow.resize(580, 410)
        self.centralwidget = QtWidgets.QWidget(infoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 80, 151, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 80, 151, 25))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 140, 151, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 140, 241, 25))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 60, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(236, 60, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 120, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 120, 91, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 290, 151, 25))
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 290, 91, 20))
        self.label_5.setObjectName("label_5")
        self.chpwBT = QtWidgets.QPushButton(self.centralwidget)
        self.chpwBT.setGeometry(QtCore.QRect(140, 290, 89, 25))
        self.chpwBT.setObjectName("chpwBT")
        self.editBT = QtWidgets.QPushButton(self.centralwidget)
        self.editBT.setGeometry(QtCore.QRect(250, 200, 89, 25))
        self.editBT.setObjectName("editBT")
        self.backLB = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.backLB.setGeometry(QtCore.QRect(20, 330, 91, 31))
        self.backLB.setObjectName("backLB")
        infoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(infoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 22))
        self.menubar.setObjectName("menubar")
        infoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(infoWindow)
        self.statusbar.setObjectName("statusbar")
        infoWindow.setStatusBar(self.statusbar)
        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(180, 340, 211, 20))
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")

        self.retranslateUi(infoWindow)
        self.chpwBT.clicked.connect(self.change_pw)
        self.editBT.clicked.connect(self.edit_info)
        self.backLB.clicked.connect(self.show_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(infoWindow)

    def retranslateUi(self, infoWindow):
        _translate = QtCore.QCoreApplication.translate
        infoWindow.setWindowTitle(_translate("infoWindow", "اطلاعات من"))
        self.lineEdit.setText(_translate("infoWindow", self.user.first_name))
        self.lineEdit_2.setText(_translate("infoWindow", self.user.last_name))
        self.lineEdit_4.setText(_translate("infoWindow", self.user.email))
        self.lineEdit_3.setText(_translate("infoWindow", self.user.phone_number))
        self.label.setText(_translate("infoWindow", "نام"))
        self.label_2.setText(_translate("infoWindow", "نام خانوادگی"))
        self.label_3.setText(_translate("infoWindow", "ایمیل"))
        self.label_4.setText(_translate("infoWindow", "شماره همراه"))
        self.label_5.setText(_translate("infoWindow", "تغییر رمز عبور:"))
        self.chpwBT.setText(_translate("infoWindow", "تایید"))
        self.editBT.setText(_translate("infoWindow", "ویرایش"))
        self.backLB.setText(_translate("infoWindow", "بازگشت"))


class Ui_MainWindow(object):
    def show_infoWindow(self):
        self.ui = Ui_infoWindow()
        self.ui.user = self.user
        self.ui.setupUi(LoginWindow)
        LoginWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("SnappFood.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchBT = QtWidgets.QPushButton(self.centralwidget)
        self.searchBT.setGeometry(QtCore.QRect(180, 220, 71, 31))
        self.searchBT.setObjectName("searchBT")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 10, 211, 141))
        self.label.setObjectName("label")
        self.searchText = QtWidgets.QLineEdit(self.centralwidget)
        self.searchText.setGeometry(QtCore.QRect(260, 220, 331, 31))
        self.searchText.setObjectName("searchText")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 180, 411, 25))
        self.comboBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox.setObjectName("comboBox")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(180, 270, 411, 261))
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.food = QtWidgets.QWidget()
        self.food.setObjectName("food")
        self.scrollArea1 = QtWidgets.QScrollArea(self.food)
        self.scrollArea1.setGeometry(QtCore.QRect(10, 10, 391, 211))
        self.scrollArea1.setWidgetResizable(True)
        self.scrollArea1.setObjectName("scrollArea1")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 389, 209))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea1.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.food, "")
        self.resturant = QtWidgets.QWidget()
        self.resturant.setObjectName("resturant")
        self.scrollArea2 = QtWidgets.QScrollArea(self.resturant)
        self.scrollArea2.setGeometry(QtCore.QRect(10, 10, 391, 211))
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setObjectName("scrollArea2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 389, 209))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.resturant, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.userPanelMenu = QtWidgets.QMenu(self.menubar)
        self.userPanelMenu.setTearOffEnabled(False)
        self.userPanelMenu.setObjectName("userPanelMenu")
        self.userInfoMenu = QtWidgets.QMenu(self.menubar)
        self.userInfoMenu.setObjectName("userInfoMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.infoAct = QtWidgets.QAction(MainWindow)
        self.infoAct.setObjectName("infoAct")
        self.addressAct = QtWidgets.QAction(MainWindow)
        self.addressAct.setObjectName("addressAct")
        self.ordersAct = QtWidgets.QAction(MainWindow)
        self.ordersAct.setObjectName("ordersAct")
        self.resturantAct = QtWidgets.QAction(MainWindow)
        self.resturantAct.setObjectName("resturantAct")
        self.commentAct = QtWidgets.QAction(MainWindow)
        self.commentAct.setObjectName("commentAct")
        self.userPanelMenu.addAction(self.ordersAct)
        self.userPanelMenu.addAction(self.resturantAct)
        self.userPanelMenu.addAction(self.commentAct)
        self.userInfoMenu.addAction(self.infoAct)
        self.userInfoMenu.addAction(self.addressAct)
        self.menubar.addAction(self.userInfoMenu.menuAction())
        self.menubar.addAction(self.userPanelMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.infoAct.triggered.connect(self.show_infoWindow)
        self.addressAct.triggered.connect(MainWindow.close)
        self.commentAct.triggered.connect(MainWindow.close)
        self.ordersAct.triggered.connect(MainWindow.close)
        self.resturantAct.triggered.connect(MainWindow.close)
        self.searchBT.clicked.connect(MainWindow.show)
        self.comboBox.activated['QString'].connect(MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "سفارش آنلاین غذا | اسنپ‌فود"))
        self.searchBT.setText(_translate("MainWindow", "جستجو"))
        i = 0
        for address in self.user.get_addresses():
            self.comboBox.addItem("")
            self.comboBox.setItemText(i, _translate("MainWindow", str(address)))
            i += 1
        if i == 0:
            self.comboBox.addItem("")
            self.comboBox.setItemText(i, _translate("MainWindow", 'تمام رستوران‌ها'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.food), _translate("MainWindow", "غذاها"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resturant), _translate("MainWindow", "رستوران‌ها"))
        self.userPanelMenu.setTitle(_translate("MainWindow", "پنل کاربری"))
        self.userInfoMenu.setTitle(_translate("MainWindow", "اطلاعات کاربری"))
        self.infoAct.setText(_translate("MainWindow", "اطلاعات من"))
        self.addressAct.setText(_translate("MainWindow", "آدرس‌ها"))
        self.ordersAct.setText(_translate("MainWindow", "سفارش‌های من"))
        self.resturantAct.setText(_translate("MainWindow", "رستوران‌های محبوب من"))
        self.commentAct.setText(_translate("MainWindow", "نظرات من"))


class Ui_LoginWindow(object):
    def show_MainWindow(self, userId):
        self.ui = Ui_MainWindow()
        self.ui.user = entities.User(userId)
        self.ui.setupUi(LoginWindow)
        LoginWindow.show()

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(378, 386)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("SnappFood.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.loginBT.setText(_translate("LoginWindow", "ورود"))


def login():
    try:
        userId = entities.User.login(ui.phText.text(), ui.pwText.text())
        ui.message.setText('با موفقیت وارد شدید')
        ui.show_MainWindow(userId)
    except exception.LoginError:
        ui.message.setText('شماره همراه یا رمز عبور اشتباه است')
    except exception.PhoneNumberFormatError:
        ui.message.setText('فرمت شماره همراه اشتباه است')


def signup():
    try:
        userId = entities.User.add(ui.phText.text(), ui.pwText.text())
        ui.message.setText('با موفقیت ثبت نام شدید')
        ui.show_MainWindow(userId)
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
