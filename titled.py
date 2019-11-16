# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        self.pages = []

    def addPage(self, page):
        self.pages.append(page)

    def delPage(self, page):
        self.pages.remove(page)

    def getNext(self):
        return self.next

    def printPages(self):
        res = ""
        for x in self.pages:
            res += str(x) + ", "
        return res[:-2]

    def getValue(self):
        return self.value

    def getPages(self):
        return self.pages


class LOS:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def add(self, x):
        self.length += 1
        if self.first == None:
            self.first = self.last = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

    def getLength(self):
        return self.length

    def getFirst(self):
        return self.first

    def find(self, item):
        current = self.first
        while current is not None:
            if current.getValue() == item:
                return current
            current = current.next
        return None

    def delete(self, item):
        chk = False
        current = self.first
        while current is not None:
            if current.next == item:
                current.next = current.next.next
                chk = True
            current = current.next
        if not chk:
            raise Exception("Данного элемента нет")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 680)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 371, 621))
        self.groupBox.setObjectName("groupBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 50, 181, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(120, 90, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnClicked)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 171, 16))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(200, 50, 104, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 10, 371, 621))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 351, 331))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Предметный указатель"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton.setText(_translate("MainWindow", "Добавить слово"))
        self.label.setText(_translate("MainWindow", "Введите слово:"))
        self.label_2.setText(_translate("MainWindow", "Введите номер страницы:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))

    subj = LOS()

    def btnClicked(self):
        try:
            if self.plainTextEdit.toPlainText().strip() == "" or self.plainTextEdit_2.toPlainText().strip() == "":
                raise Exception("Поля не заполнены")

            current = self.subj.find(self.plainTextEdit.toPlainText().strip())
            if current is None:
                self.subj.add(self.plainTextEdit.toPlainText().strip())
                #if self.subj.getFirst().getNext() == None:
                current = self.subj.getFirst()
                if current.getNext() is not None:
                    while current.getNext() is not None:
                        current = current.getNext()
            if int(self.plainTextEdit_2.toPlainText().strip()) in current.getPages():
                raise Exception("Данная страница уже введена")
            if int(self.plainTextEdit_2.toPlainText().strip()) <= 0:
                raise ValueError()
            current.addPage(int(self.plainTextEdit_2.toPlainText().strip()))

            chk = False
            for i in range(self.listWidget.count()):
                if current.getValue() == self.listWidget.item(i).text().split(' ')[0][:-1]:
                    self.listWidget.item(i).setText("{0}. {1}".format(current.getValue(), current.printPages()))
                    chk = True
            if chk == False:
                self.listWidget.addItem("{0} — {1}".format(current.getValue(), current.printPages()))
        except ValueError:
            print("Неправильно введена страница")
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())