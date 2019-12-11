from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sqlite3
import os


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
            if isinstance(x, Node):
                self.first = x
            else:
                self.first = Node(x, None)
        else:
            current = self.first
            while current.next:
                current = current.next
            if isinstance(x, Node):
                current.next = x
            else:
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
        MainWindow.resize(765, 604)
        MainWindow.setTabletTracking(False)
        MainWindow.setStyleSheet("QPushButton {border: 1px solid grey; border-radius: 5px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde)}\n"
"QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #E5CCFF) }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 371, 601))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.btnClicked)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 81, 31))
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
        self.lineEdit_2.returnPressed.connect(self.btnClicked)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 90, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.btn2Clicked)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 300, 351, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 150, 231, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.btn3Clicked)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 190, 231, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.btn4Clicked)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 0, 371, 601))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 351, 561))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.currentItemChanged.connect(self.listWidgetItemChanged)
        MainWindow.setCentralWidget(self.centralwidget)

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
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить предметный указатель"))
        self.pushButton_4.setText(_translate("MainWindow", "Загрузить предметный указатель"))
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
                self.lineEdit_2.setText(str(current.getPages()[-1]))
        except ValueError:
            self.textBrowser.append("Неправильно введена страница")
        except Exception as e:
            self.textBrowser.append(str(e))

    def btn3Clicked(self):
        try:
            sname = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "Save file", "", "*.db")[0]
            if sname.strip() == "":
                raise Exception("Сохранение отменено")
            if os.path.exists(sname):
                os.remove(sname)

            sql = sqlite3.connect(sname)
            cursor = sql.cursor()
            
            cursor.executescript("""CREATE TABLE words(id ineteger, word text);
                                    CREATE TABLE pages(id integer, page integer);""")
            current = self.subj.getFirst()
            iden = 1
            while current:
                word = current.getValue()
                pages = current.getPages()
                cursor.execute("INSERT INTO words VALUES(?, ?)", (iden, word))
                for page in pages:
                    cursor.execute("INSERT INTO pages VALUES(?, ?)", (iden, page))
                iden += 1
                current = current.getNext()
            sql.commit()
            sql.close()
            self.textBrowser.append("Указатель сохранен успешно")
        except sqlite3.DatabaseError as e:
            self.textBrowser.append("Ошибка при сохранении: " + str(e))
        except Exception as e:
            self.textBrowser.append(str(e))

    def btn4Clicked(self):
        try:
            lname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Load file", "", "*.db")[0]
            if lname.strip() == "":
                raise Exception("Загрузка отменена")

            self.subj = LOS()

            sql = sqlite3.connect(lname)
            cursor = sql.cursor()
            cursor2 = sql.cursor()

            for row in cursor.execute("SELECT * FROM words"):
                word = Node(row[1])
                for row2 in cursor2.execute("SELECT * FROM pages"):
                    if row2[0] == row[0]:
                        word.addPage(row2[1])
                self.subj.add(word)

            self.listWidget.clear()
            current = self.subj.getFirst()
            while current:
                self.listWidget.addItem("{0} — {1}".format(current.getValue(), current.printPages()))
                current = current.getNext()

            sql.close()
            self.textBrowser.append("Предметный указатель загружен")
        except sqlite3.DatabaseError as e:
            self.textBrowser.append("Ошибка при загрузке: " + str(e))
        except Exception as e:
            self.textBrowser.append(str(e))

    def listWidgetItemChanged(self):
        if self.listWidget.currentItem():
            data = self.listWidget.currentItem().text().split(" ")
            self.lineEdit.setText(data[0])
            self.lineEdit_2.setText(data[-1])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())