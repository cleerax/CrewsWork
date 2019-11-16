from PyQt5 import QtCore, QtGui, QtWidgets


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
        for x in sorted(self.pages):
            res += str(x) + ", "
        return res[:-2]

    def getValue(self):
        return self.value

    def getPages(self):
        return self.pages


class LOS:
    def __init__(self):
        self.first = None
        self.length = 0

    def add(self, x):
        self.length += 1
        if self.first == None:
            self.first = Node(x, None)
        else:
            current = self.first
            while current.next:
                current = current.next
            current.next = Node(x, None)

    def getLength(self):
        return self.length

    def getFirst(self):
        return self.first

    def find(self, item):
        current = self.first
        while current is not None:
            if current.value == item:
                return current
            current = current.next
        return None

    def delete(self, item):
        chk = False
        if not self.first.next and self.first.value == item:
            self.first = None
            return
        elif self.first.value == item:
            self.first = self.first.next
            return
        current = self.first
        while current is not None:
            if current.next and current.next.value == item:
                current.next = current.next.next
                chk = True
                break
            current = current.next
        if not chk:
            raise Exception("Данного элемента нет")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 657)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 371, 601))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 50, 104, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 120, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.btn2Clicked)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 300, 351, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 10, 371, 601))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 351, 561))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 22))
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
        self.groupBox.setTitle(_translate("MainWindow", "Формирование"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate("MainWindow", "Введите слово:"))
        self.label_2.setText(_translate("MainWindow", "Введите номер страницы:"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Вывод"))

    subj = LOS()

    def btnClicked(self):
        try:
            if self.lineEdit.text().strip() == "" or self.lineEdit_2.text().strip() == "":
                raise Exception("Поля не заполнены")

            current = self.subj.find(self.lineEdit.text().strip())
            if current is None:
                self.subj.add(self.lineEdit.text().strip())
                current = self.subj.getFirst()
                if current.getNext() is not None:
                    while current.getNext() is not None:
                        current = current.getNext()
            if int(self.lineEdit_2.text().strip()) in current.getPages():
                raise Exception("Данная страница уже введена")
            if int(self.lineEdit_2.text().strip()) <= 0:
                raise ValueError()
            current.addPage(int(self.lineEdit_2.text().strip()))

            chk = False
            for i in range(self.listWidget.count()):
                if current.getValue() == self.listWidget.item(i).text().split(" — ")[0]:
                    self.listWidget.item(i).setText("{0} — {1}".format(current.getValue(), current.printPages()))
                    chk = True
            if chk == False:
                self.listWidget.addItem("{0} — {1}".format(current.getValue(), current.printPages()))
            self.textBrowser.append("Добавлено слово {0} на странице {1}".format(current.getValue(), self.lineEdit_2.text().strip()))
        except ValueError:
            self.textBrowser.append("Неправильно введена страница")
        except Exception as e:
            self.textBrowser.append(str(e))

    def btn2Clicked(self):
        try:
            if self.lineEdit.text().strip() == "" or self.lineEdit_2.text().strip() == "":
                raise Exception("Поля не заполнены")

            current = self.subj.find(self.lineEdit.text().strip())
            if not current:
                raise Exception("Введенного слова нет в указателе")

            page = int(self.lineEdit_2.text().strip())
            if page not in current.getPages():
                raise Exception("Введенного слова нет на введенной странице")

            if len(current.getPages()) == 1:
                current = current.getValue()
                self.subj.delete(current)
                for i in range(self.listWidget.count()):
                    if current == self.listWidget.item(i).text().split(" — ")[0]:
                        self.listWidget.takeItem(i)
                        break
                self.textBrowser.append("Слово {0} удалено из указателя".format(current))
            elif len(current.getPages()) > 1:
                self.subj.find(current.getValue()).delPage(page)
                current = self.subj.find(current.getValue())
                for i in range(self.listWidget.count()):
                    if current.getValue() == self.listWidget.item(i).text().split(" — ")[0]:
                        self.listWidget.item(i).setText("{0} — {1}".format(current.getValue(), current.printPages()))
                        break
                self.textBrowser.append("Слово {0} удалено со страницы {1}".format(current.getValue(), page))
        except ValueError:
            self.textBrowser.append("Неправильно введена страница")
        except Exception as e:
            self.textBrowser.append(str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())