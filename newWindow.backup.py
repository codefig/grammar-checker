# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\projects\newWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1536, 1109)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textInput = QtGui.QTextEdit(self.centralwidget)
        self.textInput.setObjectName(_fromUtf8("textInput"))
        self.verticalLayout.addWidget(self.textInput)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.textOutput = QtGui.QTextEdit(self.widget)
        self.textOutput.setObjectName(_fromUtf8("textOutput"))
        self.horizontalLayout_3.addWidget(self.textOutput)
        self.splitter = QtGui.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.clearOutputBtn = QtGui.QPushButton(self.splitter)
        self.clearOutputBtn.setObjectName(_fromUtf8("clearOutputBtn"))
        self.clearInputBtn = QtGui.QPushButton(self.splitter)
        self.clearInputBtn.setObjectName(_fromUtf8("clearInputBtn"))
        self.horizontalLayout_3.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.widget)
        self.widget.raise_()
        self.textInput.raise_()
        self.widget.raise_()
        self.textInput.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        #connect buttons to actions 
        self.clearOutputBtn.clicked.connect(self.clear_output)
        self.clearInputBtn.clicked.connect(self.clear_input)
        self.textInput.textChanged.connect(self.checkInputOnChanged)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Grammar Checker Xbar", None))
        self.clearOutputBtn.setText(_translate("MainWindow", "CLEAR OUTPUT", None))
        self.clearInputBtn.setText(_translate("MainWindow", "CLEAR INPUTS", None))

    def clear_output(self):
        print("This is the clear output function")

    def clear_input(self):
        print("This is the clear input function")

    def checkInputOnChanged(self):
        self.inputText = self.textInput.toPlainText()
        print("This function checks if input changed by letters")
        print(self.inputText)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

