from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 566)
        MainWindow.setStyleSheet("QPushButton{background-color: #D72E0B; \n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  cursor: pointer;}\n"
"\n"
"QPushButton:hover{background-color: #C81C01;}\n"
"\n"
"QLabel#label_3{background-color: #FF5623;}\n"
"\n"
"QMainWindow{background-color: #010001;}\n"
"\n"
"\n"
"QLabel#label_4{background-color: #E2E0E2;}\n"
"\n"
"QLabel#label_5{background-color: #E2E0E2;}\n"
"\n"
"QFrame#frame{background-color: #E2E0E2;}\n"
"\n"
"QFrame#frame_2{background-color: #E2E0E2;}\n"
"\n"
"QFrame#frame_3{background-color: #E2E0E2;}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 1061, 84))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setText("")

        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Showhide)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Showhide)
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Showhide)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.Showhide)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Showhide)
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.ShowBack)
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("nwaasd.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1091, 101))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 110, 611, 451))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 60, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(240, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(250, 0, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 0, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(440, 60, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(370, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(490, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(490, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(370, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(240, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(490, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(370, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(240, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(490, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4.setGeometry(QtCore.QRect(370, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(240, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame)
        self.comboBox_5.setGeometry(QtCore.QRect(490, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_5.setGeometry(QtCore.QRect(370, 240, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(240, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame)
        self.comboBox_6.setGeometry(QtCore.QRect(490, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_6.setGeometry(QtCore.QRect(370, 270, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(240, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.comboBox_7 = QtWidgets.QComboBox(self.frame)
        self.comboBox_7.setGeometry(QtCore.QRect(490, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.checkBox_7 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_7.setGeometry(QtCore.QRect(370, 300, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(240, 300, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame)
        self.comboBox_8.setGeometry(QtCore.QRect(40, 320, 69, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 340, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(40, 360, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(350, 380, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 330, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(400, 330, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(400, 380, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 380, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(630, 110, 421, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.horizontalLayoutWidget_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(630, 180, 421, 361))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.horizontalLayoutWidget_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.label_3.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Showhide(self):
        self.frame.hide()
        self.frame_2.hide()
        self.frame_3.hide()

    def ShowBack(self):
        self.frame.show()
        self.frame_2.show()
        self.frame_3.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vajra "))
        self.pushButton.setText(_translate("MainWindow", "Main"))
        self.pushButton_3.setText(_translate("MainWindow", "Tunner"))
        self.pushButton_2.setText(_translate("MainWindow", "Camera"))
        self.pushButton_4.setText(_translate("MainWindow", "Auto"))
        self.pushButton_5.setText(_translate("MainWindow", "Science"))
        self.pushButton_6.setText(_translate("MainWindow", "Rocks"))
        self.label_4.setText(_translate("MainWindow", "Ip Address"))
        self.label_5.setText(_translate("MainWindow", "GaCC Command"))
        self.label_6.setText(_translate("MainWindow", "Telescopic 1"))
        self.pushButton_7.setText(_translate("MainWindow", "Apply"))
        self.pushButton_8.setText(_translate("MainWindow", "Reload"))
        self.pushButton_9.setText(_translate("MainWindow", "Send"))
        self.checkBox.setText(_translate("MainWindow", ":5021"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Medium"))
        self.comboBox.setItemText(1, _translate("MainWindow", "add more item here"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Medium"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "add more item here"))
        self.checkBox_2.setText(_translate("MainWindow", ":5021"))
        self.label_7.setText(_translate("MainWindow", "Telescopic 1"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Medium"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "add more item here"))
        self.checkBox_3.setText(_translate("MainWindow", ":5021"))
        self.label_8.setText(_translate("MainWindow", "Telescopic 1"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Medium"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "add more item here"))
        self.checkBox_4.setText(_translate("MainWindow", ":5021"))
        self.label_9.setText(_translate("MainWindow", "Telescopic 1"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Medium"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "add more item here"))
        self.checkBox_5.setText(_translate("MainWindow", ":5021"))
        self.label_10.setText(_translate("MainWindow", "Telescopic 1"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Medium"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "add more item here"))
        self.checkBox_6.setText(_translate("MainWindow", ":5021"))
        self.label_11.setText(_translate("MainWindow", "Telescopic 1"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Medium"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "add more item here"))
        self.checkBox_7.setText(_translate("MainWindow", ":5021"))
        self.label_12.setText(_translate("MainWindow", "Telescopic 1"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "Cameras"))
        self.label_13.setText(_translate("MainWindow", "Cut, Del Min, Max"))
        self.label_14.setText(_translate("MainWindow", "0,0,0,0"))
        self.pushButton_10.setText(_translate("MainWindow", "Get Cameras"))
        self.pushButton_11.setText(_translate("MainWindow", "Get Controls"))
        self.pushButton_12.setText(_translate("MainWindow", "Set Value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
