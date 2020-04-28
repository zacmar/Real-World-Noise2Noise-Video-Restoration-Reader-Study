# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from frame_display import Ui_Form


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, ui_form):
        MainWindow.setObjectName("MainWindow")
        self.ui_form = ui_form
        MainWindow.resize(816, 385)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 270, 102, 34))
        self.pushButton.setObjectName("Next")
        self.pushButton.pressed.connect(self.advance)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 170, 291, 71))
        self.label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 291, 71))
        self.label_2.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 250, 291, 81))
        self.label_3.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 7, 451, 71))
        self.label_4.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 100, 101, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 180, 101, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 260, 102, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 0, 211, 151))
        self.label_5.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 160, 211, 101))
        self.label_6.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(320, 200, 120, 80))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def advance(self):
        MainWindow.hide()
        ui_form.setupUi()
        ui_form.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Noise2Noise Video Restoration Reader Study"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.label.setText(_translate("MainWindow", "Least presence of \"flickering-like\" artifacts. The frames are temporally coherent, i.e. there are no obvious mismatches between the frames."))
        self.label_2.setText(_translate("MainWindow", "Overall best viewing experience. If you had to watch a full length movie, of the 3 methods shown you would choose this."))
        self.label_3.setText(_translate("MainWindow", "Significant smoothing. Compared to the other methods, you feel like the frames are smoothed to the extend that important image features are lost."))
        self.label_4.setText(_translate("MainWindow", "Upon pressing Next, you will be shown 3 different sequences of image frames. They show the same footage, but that have been denoised by different methods. Please select the following properties accordingly:"))
        self.pushButton_2.setText(_translate("MainWindow", "Overall\n"
"Best"))
        self.pushButton_3.setText(_translate("MainWindow", "Least\n"
"Flickering"))
        self.pushButton_4.setText(_translate("MainWindow", "Significant\n"
"Smoothing"))
        self.label_5.setText(_translate("MainWindow", "For the first two (\"Overall Best\", \"Least Flickering\"), one method has to be chosen. For \"Significant Smoothing\", 0 or 1 method can be chosen. Please keep this in mind and only select it if the definition is met."))
        self.label_6.setText(_translate("MainWindow", "There will be 8 samples. If you have finished one, please press Next again to advance to the next one."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui_form = Ui_Form()
    ui.setupUi(MainWindow, ui_form)
    MainWindow.show()
    sys.exit(app.exec_())
