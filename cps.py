# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cps.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 98)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_decor2 = QtWidgets.QLabel(self.centralwidget)
        self.label_decor2.setGeometry(QtCore.QRect(0, 0, 1360, 100))
        self.label_decor2.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.label_decor2.setText("")
        self.label_decor2.setObjectName("label_decor2")
        self.label_text1 = QtWidgets.QLabel(self.centralwidget)
        self.label_text1.setGeometry(QtCore.QRect(30, 0, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_text1.setFont(font)
        self.label_text1.setStyleSheet("color: rgb(70, 255, 255);")
        self.label_text1.setObjectName("label_text1")
        self.label_decor3 = QtWidgets.QLabel(self.centralwidget)
        self.label_decor3.setGeometry(QtCore.QRect(0, 90, 1360, 10))
        self.label_decor3.setStyleSheet("background-color: rgb(45, 45, 90);")
        self.label_decor3.setText("")
        self.label_decor3.setObjectName("label_decor3")
        self.btn_test1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_test1.setGeometry(QtCore.QRect(360, 25, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_test1.setFont(font)
        self.btn_test1.setStyleSheet("QPushButton {\n"
"color: rgb(70, 255, 255);\n"
"background-color: rgb(60, 63, 65);\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(190, 190, 190) ;\n"
"}\n"
"QPushButton:pressed {\n"
"    color:rgb(180, 180, 180) ;\n"
"}")
        self.btn_test1.setObjectName("btn_test1")
        self.btn_test2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_test2.setGeometry(QtCore.QRect(545, 30, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_test2.setFont(font)
        self.btn_test2.setStyleSheet("QPushButton {\n"
"color: rgb(70, 255, 255);\n"
"background-color: rgb(60, 63, 65);\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(190, 190, 190) ;\n"
"}\n"
"QPushButton:pressed {\n"
"    color:rgb(180, 180, 180) ;\n"
"}")
        self.btn_test2.setObjectName("btn_test2")
        self.btn_count3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_count3.setGeometry(QtCore.QRect(810, 25, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_count3.setFont(font)
        self.btn_count3.setStyleSheet("QPushButton {\n"
"color: rgb(70, 255, 255);\n"
"background-color: rgb(60, 63, 65);\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(190, 190, 190) ;\n"
"}\n"
"QPushButton:pressed {\n"
"    color:rgb(180, 180, 180) ;\n"
"}")
        self.btn_count3.setObjectName("btn_count3")
        self.btn_programm4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_programm4.setGeometry(QtCore.QRect(1105, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_programm4.setFont(font)
        self.btn_programm4.setStyleSheet("QPushButton {\n"
"color: rgb(70, 255, 255);\n"
"background-color: rgb(60, 63, 65);\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(190, 190, 190) ;\n"
"}\n"
"QPushButton:pressed {\n"
"    color:rgb(180, 180, 180) ;\n"
"}")
        self.btn_programm4.setObjectName("btn_programm4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 100, 1360, 605))
        self.stackedWidget.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_cps = QtWidgets.QWidget()
        self.page_cps.setMaximumSize(QtCore.QSize(1360, 768))
        self.page_cps.setObjectName("page_cps")
        self.label_text_1page = QtWidgets.QLabel(self.page_cps)
        self.label_text_1page.setGeometry(QtCore.QRect(30, 70, 1191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_text_1page.setFont(font)
        self.label_text_1page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_text_1page.setObjectName("label_text_1page")
        self.label_2text_1page = QtWidgets.QLabel(self.page_cps)
        self.label_2text_1page.setGeometry(QtCore.QRect(28, -10, 621, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_2text_1page.setFont(font)
        self.label_2text_1page.setStyleSheet("color: rgb(70, 255, 255);")
        self.label_2text_1page.setObjectName("label_2text_1page")
        self.btn_start_1page = QtWidgets.QPushButton(self.page_cps)
        self.btn_start_1page.setGeometry(QtCore.QRect(100, 140, 530, 200))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start_1page.setFont(font)
        self.btn_start_1page.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 63, 65);\n"
"    color: rgb(70, 255, 255);\n"
"border-radius: 15px;              \n"
"border: 3px solid rgb(45, 45, 90)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(45, 45, 90);\n"
"border: 3px solid rgb(60, 63, 65);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(47, 47, 94);\n"
"}")
        self.btn_start_1page.setObjectName("btn_start_1page")
        self.btn_stop_1page = QtWidgets.QPushButton(self.page_cps)
        self.btn_stop_1page.setGeometry(QtCore.QRect(730, 230, 530, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stop_1page.setFont(font)
        self.btn_stop_1page.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 63, 65);\n"
"    color: rgb(70, 255, 255);\n"
"border-radius: 15px;              \n"
"border: 3px solid rgb(216, 35, 38);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(216, 35, 38);\n"
"border: 3px solid rgb(60, 63, 65);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(226, 36, 39);\n"
"}")
        self.btn_stop_1page.setObjectName("btn_stop_1page")
        self.label_5text_1page = QtWidgets.QLabel(self.page_cps)
        self.label_5text_1page.setGeometry(QtCore.QRect(960, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5text_1page.setFont(font)
        self.label_5text_1page.setStyleSheet("color: rgb(190, 190, 190);")
        self.label_5text_1page.setObjectName("label_5text_1page")
        self.lcdNumber_1page = QtWidgets.QLCDNumber(self.page_cps)
        self.lcdNumber_1page.setGeometry(QtCore.QRect(963, 130, 81, 31))
        self.lcdNumber_1page.setStyleSheet("background-color: rgb(60, 63, 65);\n"
"color: rgb(70, 255, 255);")
        self.lcdNumber_1page.setObjectName("lcdNumber_1page")
        self.label_6text_1page = QtWidgets.QLabel(self.page_cps)
        self.label_6text_1page.setGeometry(QtCore.QRect(30, 354, 1091, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_6text_1page.setFont(font)
        self.label_6text_1page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_6text_1page.setObjectName("label_6text_1page")
        self.label_7text_1page = QtWidgets.QLabel(self.page_cps)
        self.label_7text_1page.setGeometry(QtCore.QRect(30, 400, 1121, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_7text_1page.setFont(font)
        self.label_7text_1page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_7text_1page.setObjectName("label_7text_1page")
        self.label_decor3_1page = QtWidgets.QLabel(self.page_cps)
        self.label_decor3_1page.setGeometry(QtCore.QRect(0, 505, 1360, 10))
        self.label_decor3_1page.setStyleSheet("background-color: rgb(45, 45, 90);")
        self.label_decor3_1page.setText("")
        self.label_decor3_1page.setObjectName("label_decor3_1page")
        self.label_decor2_1page = QtWidgets.QLabel(self.page_cps)
        self.label_decor2_1page.setGeometry(QtCore.QRect(0, 515, 1360, 100))
        self.label_decor2_1page.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.label_decor2_1page.setText("")
        self.label_decor2_1page.setObjectName("label_decor2_1page")
        self.label_text8_1page = QtWidgets.QLabel(self.page_cps)
        self.label_text8_1page.setGeometry(QtCore.QRect(607, 540, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_text8_1page.setFont(font)
        self.label_text8_1page.setStyleSheet("color:rgb(70, 255, 255);\n"
"background-color: rgb(60, 63, 65);")
        self.label_text8_1page.setObjectName("label_text8_1page")
        self.btn_play_1page = QtWidgets.QPushButton(self.page_cps)
        self.btn_play_1page.setGeometry(QtCore.QRect(1227, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_play_1page.setFont(font)
        self.btn_play_1page.setStyleSheet("QPushButton {\n"
"color: rgb(70, 255, 255);\n"
"background-color: rgb(60, 63, 65); \n"
"border-radius: 10px;              \n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(190, 190, 190) ;\n"
"}\n"
"QPushButton:pressed {\n"
"    color:rgb(180, 180, 180) ;\n"
"}")
        self.btn_play_1page.setObjectName("btn_play_1page")
        self.btn_stop_music_1page = QtWidgets.QPushButton(self.page_cps)
        self.btn_stop_music_1page.setGeometry(QtCore.QRect(1227, 78, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stop_music_1page.setFont(font)
        self.btn_stop_music_1page.setStyleSheet("QPushButton {\n"
"color: rgb(70, 255, 255);\n"
"background-color: rgb(60, 63, 65); \n"
"border-radius: 10px;              \n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(190, 190, 190) ;\n"
"}\n"
"QPushButton:pressed {\n"
"    color:rgb(180, 180, 180) ;\n"
"}")
        self.btn_stop_music_1page.setObjectName("btn_stop_music_1page")
        self.label_music_1page = QtWidgets.QLabel(self.page_cps)
        self.label_music_1page.setGeometry(QtCore.QRect(1217, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_music_1page.setFont(font)
        self.label_music_1page.setStyleSheet("color: rgb(70, 255, 255);")
        self.label_music_1page.setObjectName("label_music_1page")
        self.lcdNumber_time_1page = QtWidgets.QLCDNumber(self.page_cps)
        self.lcdNumber_time_1page.setGeometry(QtCore.QRect(1105, 185, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lcdNumber_time_1page.setFont(font)
        self.lcdNumber_time_1page.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_time_1page.setStyleSheet("    border: none;\n"
"    outline: none;\n"
"color: rgb(70, 255, 255);")
        self.lcdNumber_time_1page.setObjectName("lcdNumber_time_1page")
        self.label_3text_1page = QtWidgets.QLabel(self.page_cps)
        self.label_3text_1page.setGeometry(QtCore.QRect(865, 190, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3text_1page.setFont(font)
        self.label_3text_1page.setStyleSheet("color: rgb(190, 190, 190);")
        self.label_3text_1page.setObjectName("label_3text_1page")
        self.lcdNumber = QtWidgets.QLCDNumber(self.page_cps)
        self.lcdNumber.setGeometry(QtCore.QRect(1160, 370, 101, 61))
        self.lcdNumber.setStyleSheet("\n"
"color: rgb(70, 255, 255);\n"
"background-color: rgb(43, 43, 43);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.stackedWidget.addWidget(self.page_cps)
        self.page_2space = QtWidgets.QWidget()
        self.page_2space.setObjectName("page_2space")
        self.btn_start_2page = QtWidgets.QPushButton(self.page_2space)
        self.btn_start_2page.setGeometry(QtCore.QRect(280, 220, 361, 171))
        self.btn_start_2page.setMaximumSize(QtCore.QSize(1360, 768))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start_2page.setFont(font)
        self.btn_start_2page.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 63, 65);\n"
"    color: rgb(70, 255, 255);\n"
"border-radius: 15px;              \n"
"border: 3px solid rgb(45, 45, 90)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(45, 45, 90);\n"
"border: 3px solid rgb(60, 63, 65);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(47, 47, 94);\n"
"}")
        self.btn_start_2page.setObjectName("btn_start_2page")
        self.label_3text_2page = QtWidgets.QLabel(self.page_2space)
        self.label_3text_2page.setGeometry(QtCore.QRect(33, 65, 1011, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3text_2page.setFont(font)
        self.label_3text_2page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_3text_2page.setObjectName("label_3text_2page")
        self.label_decor2_2page = QtWidgets.QLabel(self.page_2space)
        self.label_decor2_2page.setGeometry(QtCore.QRect(0, 505, 1360, 100))
        self.label_decor2_2page.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.label_decor2_2page.setText("")
        self.label_decor2_2page.setObjectName("label_decor2_2page")
        self.label_decor3_2page = QtWidgets.QLabel(self.page_2space)
        self.label_decor3_2page.setGeometry(QtCore.QRect(0, 505, 1360, 10))
        self.label_decor3_2page.setStyleSheet("background-color: rgb(45, 45, 90);")
        self.label_decor3_2page.setText("")
        self.label_decor3_2page.setObjectName("label_decor3_2page")
        self.label_text8_2page = QtWidgets.QLabel(self.page_2space)
        self.label_text8_2page.setGeometry(QtCore.QRect(607, 540, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_text8_2page.setFont(font)
        self.label_text8_2page.setStyleSheet("color: rgb(70, 255, 255);\n"
"background-color: rgb(60, 63, 65);")
        self.label_text8_2page.setObjectName("label_text8_2page")
        self.label_6text_2page = QtWidgets.QLabel(self.page_2space)
        self.label_6text_2page.setGeometry(QtCore.QRect(30, 410, 941, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_6text_2page.setFont(font)
        self.label_6text_2page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_6text_2page.setObjectName("label_6text_2page")
        self.btn_stop_2page = QtWidgets.QPushButton(self.page_2space)
        self.btn_stop_2page.setGeometry(QtCore.QRect(700, 220, 361, 171))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stop_2page.setFont(font)
        self.btn_stop_2page.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 63, 65);\n"
"    color: rgb(70, 255, 255);\n"
"border-radius: 15px;              \n"
"border: 3px solid rgb(216, 35, 38);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(216, 35, 38);\n"
"border: 3px solid rgb(60, 63, 65);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(226, 36, 39);\n"
"}")
        self.btn_stop_2page.setObjectName("btn_stop_2page")
        self.lcdNumber_2page = QtWidgets.QLCDNumber(self.page_2space)
        self.lcdNumber_2page.setGeometry(QtCore.QRect(780, 160, 81, 41))
        self.lcdNumber_2page.setStyleSheet("    border: none;\n"
"    outline: none;\n"
"color: rgb(70, 255, 255);")
        self.lcdNumber_2page.setObjectName("lcdNumber_2page")
        self.lcdNumber_time1_page_2 = QtWidgets.QLCDNumber(self.page_2space)
        self.lcdNumber_time1_page_2.setGeometry(QtCore.QRect(550, 160, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lcdNumber_time1_page_2.setFont(font)
        self.lcdNumber_time1_page_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_time1_page_2.setStyleSheet("    border: none;\n"
"    outline: none;\n"
"color: rgb(70, 255, 255);")
        self.lcdNumber_time1_page_2.setObjectName("lcdNumber_time1_page_2")
        self.label_4text_2page = QtWidgets.QLabel(self.page_2space)
        self.label_4text_2page.setGeometry(QtCore.QRect(490, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4text_2page.setFont(font)
        self.label_4text_2page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_4text_2page.setObjectName("label_4text_2page")
        self.label_7text_2page = QtWidgets.QLabel(self.page_2space)
        self.label_7text_2page.setGeometry(QtCore.QRect(705, 165, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_7text_2page.setFont(font)
        self.label_7text_2page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_7text_2page.setObjectName("label_7text_2page")
        self.label_text_2page = QtWidgets.QLabel(self.page_2space)
        self.label_text_2page.setGeometry(QtCore.QRect(30, 113, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_text_2page.setFont(font)
        self.label_text_2page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_text_2page.setObjectName("label_text_2page")
        self.label_5text_2page = QtWidgets.QLabel(self.page_2space)
        self.label_5text_2page.setGeometry(QtCore.QRect(30, 6, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_5text_2page.setFont(font)
        self.label_5text_2page.setStyleSheet("color: rgb(70, 255, 255);")
        self.label_5text_2page.setObjectName("label_5text_2page")
        self.lcdNumber2_2page = QtWidgets.QLCDNumber(self.page_2space)
        self.lcdNumber2_2page.setGeometry(QtCore.QRect(980, 410, 101, 51))
        self.lcdNumber2_2page.setStyleSheet("\n"
"color: rgb(70, 255, 255);\n"
"background-color: rgb(43, 43, 43);")
        self.lcdNumber2_2page.setObjectName("lcdNumber2_2page")
        self.btn_hide = QtWidgets.QPushButton(self.page_2space)
        self.btn_hide.setGeometry(QtCore.QRect(990, 120, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_hide.setFont(font)
        self.btn_hide.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    outline: none;\n"
"   color: rgb(43, 43, 43);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(43, 43, 43);\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.btn_hide.setObjectName("btn_hide")
        self.stackedWidget.addWidget(self.page_2space)
        self.page_3count = QtWidgets.QWidget()
        self.page_3count.setObjectName("page_3count")
        self.label_2text_3page = QtWidgets.QLabel(self.page_3count)
        self.label_2text_3page.setGeometry(QtCore.QRect(30, 10, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_2text_3page.setFont(font)
        self.label_2text_3page.setStyleSheet("color: rgb(70, 255, 255);")
        self.label_2text_3page.setObjectName("label_2text_3page")
        self.label_1text_3page = QtWidgets.QLabel(self.page_3count)
        self.label_1text_3page.setGeometry(QtCore.QRect(30, 75, 1141, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_1text_3page.setFont(font)
        self.label_1text_3page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_1text_3page.setObjectName("label_1text_3page")
        self.btn_plus_3page = QtWidgets.QPushButton(self.page_3count)
        self.btn_plus_3page.setGeometry(QtCore.QRect(245, 210, 401, 151))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus_3page.setFont(font)
        self.btn_plus_3page.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 63, 65);\n"
"    color: rgb(70, 255, 255);\n"
"border-radius: 15px;              \n"
"border: 3px solid rgb(45, 45, 90)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(45, 45, 90);\n"
"border: 3px solid rgb(60, 63, 65);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(47, 47, 94);\n"
"}")
        self.btn_plus_3page.setObjectName("btn_plus_3page")
        self.btn_minus_3page = QtWidgets.QPushButton(self.page_3count)
        self.btn_minus_3page.setGeometry(QtCore.QRect(695, 210, 401, 151))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.btn_minus_3page.setFont(font)
        self.btn_minus_3page.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 63, 65);\n"
"    color: rgb(70, 255, 255);\n"
"border-radius: 15px;              \n"
"border: 3px solid rgb(45, 45, 90)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(45, 45, 90);\n"
"border: 3px solid rgb(60, 63, 65);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(47, 47, 94);\n"
"}")
        self.btn_minus_3page.setObjectName("btn_minus_3page")
        self.btn_stop_3page = QtWidgets.QPushButton(self.page_3count)
        self.btn_stop_3page.setGeometry(QtCore.QRect(565, 380, 220, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stop_3page.setFont(font)
        self.btn_stop_3page.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 63, 65);\n"
"    color: rgb(70, 255, 255);\n"
"border-radius: 15px;              \n"
"border: 3px solid rgb(216, 35, 38);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(216, 35, 38);\n"
"border: 3px solid rgb(60, 63, 65);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(226, 36, 39);\n"
"}")
        self.btn_stop_3page.setObjectName("btn_stop_3page")
        self.lcdNumber_3page = QtWidgets.QLCDNumber(self.page_3count)
        self.lcdNumber_3page.setGeometry(QtCore.QRect(245, 130, 851, 61))
        self.lcdNumber_3page.setStyleSheet("background-color: rgb(60, 63, 65);\n"
"color: rgb(70, 255, 255);")
        self.lcdNumber_3page.setObjectName("lcdNumber_3page")
        self.label_decor2_3page = QtWidgets.QLabel(self.page_3count)
        self.label_decor2_3page.setGeometry(QtCore.QRect(0, 505, 1360, 100))
        self.label_decor2_3page.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.label_decor2_3page.setText("")
        self.label_decor2_3page.setObjectName("label_decor2_3page")
        self.label_decor3_3page = QtWidgets.QLabel(self.page_3count)
        self.label_decor3_3page.setGeometry(QtCore.QRect(0, 505, 1360, 10))
        self.label_decor3_3page.setStyleSheet("background-color: rgb(45, 45, 90);")
        self.label_decor3_3page.setText("")
        self.label_decor3_3page.setObjectName("label_decor3_3page")
        self.label_text8_3page = QtWidgets.QLabel(self.page_3count)
        self.label_text8_3page.setGeometry(QtCore.QRect(607, 540, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_text8_3page.setFont(font)
        self.label_text8_3page.setStyleSheet("color: rgb(70, 255, 255);\n"
"background-color: rgb(60, 63, 65);")
        self.label_text8_3page.setObjectName("label_text8_3page")
        self.stackedWidget.addWidget(self.page_3count)
        self.page_4programm = QtWidgets.QWidget()
        self.page_4programm.setObjectName("page_4programm")
        self.label_1text_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_1text_4page.setGeometry(QtCore.QRect(30, 80, 1311, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_1text_4page.setFont(font)
        self.label_1text_4page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_1text_4page.setObjectName("label_1text_4page")
        self.label_4text_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_4text_4page.setGeometry(QtCore.QRect(30, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_4text_4page.setFont(font)
        self.label_4text_4page.setStyleSheet("color: rgb(70, 255, 255);")
        self.label_4text_4page.setObjectName("label_4text_4page")
        self.label_5text_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_5text_4page.setGeometry(QtCore.QRect(30, 130, 1311, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5text_4page.setFont(font)
        self.label_5text_4page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_5text_4page.setObjectName("label_5text_4page")
        self.label_6text_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_6text_4page.setGeometry(QtCore.QRect(30, 170, 1271, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_6text_4page.setFont(font)
        self.label_6text_4page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_6text_4page.setObjectName("label_6text_4page")
        self.label_7text_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_7text_4page.setGeometry(QtCore.QRect(30, 215, 951, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_7text_4page.setFont(font)
        self.label_7text_4page.setStyleSheet("color: rgb(70, 255, 255);")
        self.label_7text_4page.setObjectName("label_7text_4page")
        self.label_8text_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_8text_4page.setGeometry(QtCore.QRect(30, 280, 1281, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_8text_4page.setFont(font)
        self.label_8text_4page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_8text_4page.setObjectName("label_8text_4page")
        self.label_9text_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_9text_4page.setGeometry(QtCore.QRect(30, 320, 751, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_9text_4page.setFont(font)
        self.label_9text_4page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_9text_4page.setObjectName("label_9text_4page")
        self.label_10text_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_10text_4page.setGeometry(QtCore.QRect(30, 360, 1171, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_10text_4page.setFont(font)
        self.label_10text_4page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_10text_4page.setObjectName("label_10text_4page")
        self.label_11text_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_11text_4page.setGeometry(QtCore.QRect(30, 405, 1321, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_11text_4page.setFont(font)
        self.label_11text_4page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_11text_4page.setObjectName("label_11text_4page")
        self.label_12text_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_12text_4page.setGeometry(QtCore.QRect(30, 445, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_12text_4page.setFont(font)
        self.label_12text_4page.setStyleSheet("color: rgb(150, 150, 150);")
        self.label_12text_4page.setObjectName("label_12text_4page")
        self.label_decor2_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_decor2_4page.setGeometry(QtCore.QRect(0, 505, 1360, 100))
        self.label_decor2_4page.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.label_decor2_4page.setText("")
        self.label_decor2_4page.setObjectName("label_decor2_4page")
        self.label_decor3_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_decor3_4page.setGeometry(QtCore.QRect(0, 505, 1360, 10))
        self.label_decor3_4page.setStyleSheet("background-color: rgb(45, 45, 90);")
        self.label_decor3_4page.setText("")
        self.label_decor3_4page.setObjectName("label_decor3_4page")
        self.label_text8_4page = QtWidgets.QLabel(self.page_4programm)
        self.label_text8_4page.setGeometry(QtCore.QRect(607, 540, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_text8_4page.setFont(font)
        self.label_text8_4page.setStyleSheet("color: rgb(70, 255, 255);\n"
"background-color: rgb(60, 63, 65);")
        self.label_text8_4page.setObjectName("label_text8_4page")
        self.stackedWidget.addWidget(self.page_4programm)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPS Test"))
        self.label_text1.setText(_translate("MainWindow", "CPS Test"))
        self.btn_test1.setText(_translate("MainWindow", "Клик тест"))
        self.btn_test2.setText(_translate("MainWindow", "Кпс пробела"))
        self.btn_count3.setText(_translate("MainWindow", "Счётчик кликов"))
        self.btn_programm4.setText(_translate("MainWindow", "О программе"))
        self.label_text_1page.setText(_translate("MainWindow", "Каков ваш максимальный CPS? Проверьте вашу скорость клика в данном тесте."))
        self.label_2text_1page.setText(_translate("MainWindow", "Клик тест 10 секунд"))
        self.btn_start_1page.setText(_translate("MainWindow", "Старт"))
        self.btn_stop_1page.setText(_translate("MainWindow", "Сброс"))
        self.label_5text_1page.setText(_translate("MainWindow", "клики"))
        self.label_6text_1page.setText(_translate("MainWindow", "Таймер запустится сразу как нажмете кнопку Старт, поэтому не медлите "))
        self.label_7text_1page.setText(_translate("MainWindow", "и жмите быстрее! Ваш cps будет известен сразу после окончания таймера."))
        self.label_text8_1page.setText(_translate("MainWindow", "2022 © CPS Test"))
        self.btn_play_1page.setText(_translate("MainWindow", "play"))
        self.btn_stop_music_1page.setText(_translate("MainWindow", "stop"))
        self.label_music_1page.setText(_translate("MainWindow", "Music"))
        self.label_3text_1page.setText(_translate("MainWindow", "Времени осталось:"))
        self.btn_start_2page.setText(_translate("MainWindow", "Старт"))
        self.label_3text_2page.setText(_translate("MainWindow", "Узнай максимальный CPS твоего пробела. Ломать пробел здесь 👇"))
        self.label_text8_2page.setText(_translate("MainWindow", "2022 © CPS Test"))
        self.label_6text_2page.setText(_translate("MainWindow", "Ваш cps будет будет известен сразу после окончания таймера."))
        self.btn_stop_2page.setText(_translate("MainWindow", "Сброс"))
        self.label_4text_2page.setText(_translate("MainWindow", "Время:"))
        self.label_7text_2page.setText(_translate("MainWindow", "Клики:"))
        self.label_text_2page.setText(_translate("MainWindow", "Кнопка \"Старт\" : Первый клик - лкм, остальные клики - пробел."))
        self.label_5text_2page.setText(_translate("MainWindow", "Кпс пробела"))
        self.btn_hide.setText(_translate("MainWindow", "🤪"))
        self.label_2text_3page.setText(_translate("MainWindow", "Счётчик кликов"))
        self.label_1text_3page.setText(_translate("MainWindow", "Хотите что-нибудь посчитать? Воспользуйтесь простым счетчиком кликов 👇"))
        self.btn_plus_3page.setText(_translate("MainWindow", "+"))
        self.btn_minus_3page.setText(_translate("MainWindow", "-"))
        self.btn_stop_3page.setText(_translate("MainWindow", "Сброс"))
        self.label_text8_3page.setText(_translate("MainWindow", "2022 © CPS Test"))
        self.label_1text_4page.setText(_translate("MainWindow", "Этa программа была создана для точного измерения скорости клика. Обычно скорость"))
        self.label_4text_4page.setText(_translate("MainWindow", "О программе"))
        self.label_5text_4page.setText(_translate("MainWindow", "измеряется в КПС (от англ. CPS - clicks per second). Число КПС получают путем деления"))
        self.label_6text_4page.setText(_translate("MainWindow", "количества кликов на время. Чаще всего такие программы используются геймерами."))
        self.label_7text_4page.setText(_translate("MainWindow", "Какой КПС считается хорошим?"))
        self.label_8text_4page.setText(_translate("MainWindow", "Большинство игроков могут кликать со скорость 5-7 КПС на протяжении 10-60 секунд "))
        self.label_9text_4page.setText(_translate("MainWindow", "без применения каких-либо особых техник клика."))
        self.label_10text_4page.setText(_translate("MainWindow", "=> 7-8 можно считать хорошим результатом, он достигается довольно просто."))
        self.label_11text_4page.setText(_translate("MainWindow", "=> 9 и больше - это очень хороший результат, его трудно достичь обычным кликаньем,"))
        self.label_12text_4page.setText(_translate("MainWindow", "для этого требуются специальные навыки."))
        self.label_text8_4page.setText(_translate("MainWindow", "2022 © CPS Test"))
