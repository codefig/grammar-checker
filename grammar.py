# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grammar.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textInput = QtGui.QTextEdit(self.centralwidget)
        self.textInput.setGeometry(QtCore.QRect(0, 0, 811, 291))
        self.textInput.setStyleSheet(_fromUtf8("background-color:#34495e;\n"
"color:#fff"))
        self.textInput.setObjectName(_fromUtf8("textInput"))
        self.errorOutput = QtGui.QTextEdit(self.centralwidget)
        self.errorOutput.setGeometry(QtCore.QRect(3, 320, 621, 251))
        self.errorOutput.setStyleSheet(_fromUtf8("background-color:#ccc;\n"
"color:red;"))
        self.errorOutput.setObjectName(_fromUtf8("errorOutput"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 330, 141, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 370, 105, 33))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuAnalysis = QtGui.QMenu(self.menubar)
        self.menuAnalysis.setObjectName(_fromUtf8("menuAnalysis"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Word_Bag = QtGui.QAction(MainWindow)
        self.actionLoad_Word_Bag.setObjectName(_fromUtf8("actionLoad_Word_Bag"))
        self.actionExit_Application = QtGui.QAction(MainWindow)
        self.actionExit_Application.setObjectName(_fromUtf8("actionExit_Application"))
        self.actionUse_PSG = QtGui.QAction(MainWindow)
        self.actionUse_PSG.setObjectName(_fromUtf8("actionUse_PSG"))
        self.actionUse_SCG = QtGui.QAction(MainWindow)
        self.actionUse_SCG.setObjectName(_fromUtf8("actionUse_SCG"))
        self.actionUse_Xbar = QtGui.QAction(MainWindow)
        self.actionUse_Xbar.setObjectName(_fromUtf8("actionUse_Xbar"))
        self.menuSettings.addAction(self.actionLoad_Word_Bag)
        self.menuSettings.addAction(self.actionExit_Application)
        self.menuAnalysis.addAction(self.actionUse_PSG)
        self.menuAnalysis.addAction(self.actionUse_SCG)
        self.menuAnalysis.addAction(self.actionUse_Xbar)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Grammar Checker", None))
        self.label.setText(_translate("MainWindow", "Errors and Warnings", None))
        self.pushButton.setText(_translate("MainWindow", "Clear", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis", None))
        self.actionLoad_Word_Bag.setText(_translate("MainWindow", "Load Word Bag", None))
        self.actionExit_Application.setText(_translate("MainWindow", "Exit Application", None))
        self.actionUse_PSG.setText(_translate("MainWindow", "Use PSG", None))
        self.actionUse_SCG.setText(_translate("MainWindow", "Use SCG", None))
        self.actionUse_Xbar.setText(_translate("MainWindow", "Use Xbar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

