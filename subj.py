from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sqlite3
import os
import re


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
        self.lineEdit.setGeometry(QtCore.QRect(10, 90, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.btnClicked)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnClicked)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(200, 70, 171, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 90, 104, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.returnPressed.connect(self.btnClicked)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 130, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.btn2Clicked)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 310, 351, 281))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 190, 231, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.btn3Clicked)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 230, 231, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.btn4Clicked)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 30, 351, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.btn10Clicked)
        self.pushButton_10.setStyleSheet("QPushButton {border: 1px solid grey; border-radius: 5px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #21c400)}\n"
"QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #21c400, stop: 1 #E5CCFF) }")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 280, 371, 321))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 351, 281))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.currentItemChanged.connect(self.listWidgetItemChanged)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 0, 371, 281))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 351, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 70, 171, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.btn5Clicked)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 351, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 351, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 120, 351, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 160, 351, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.btn6Clicked)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 190, 351, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.btn7Clicked)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 250, 351, 21))
        self.pushButton_8.setStyleSheet("QPushButton {border: 1px solid grey; border-radius: 5px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #ff0000)}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ff0000, stop: 1 #E5CCFF) }")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.btn8Clicked)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 220, 351, 21))
        self.pushButton_9.setStyleSheet("QPushButton {border: 1px solid grey; border-radius: 5px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #0080ff)}\n"
"QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0080ff, stop: 1 #E5CCFF) }")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.btn9Clicked)
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
        self.pushButton_10.setText(_translate("MainWindow", "Составить указатель по текстовому файлу"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Вывод"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Операции с указателем"))
        self.label_3.setText(_translate("MainWindow", "-----Сортировка-----"))
        self.pushButton_5.setText(_translate("MainWindow", "Отсортировать"))
        self.comboBox.setItemText(0, _translate("MainWindow", "По алфавиту"))
        self.comboBox.setItemText(1, _translate("MainWindow", "По алфавиту в обратном порядке"))
        self.label_4.setText(_translate("MainWindow", "-----Поиск-----"))
        self.pushButton_6.setText(_translate("MainWindow", "Найти слова, содержащие введенную строку"))
        self.pushButton_7.setText(_translate("MainWindow", "Найти слова, которые есть на введенной странице"))
        self.pushButton_8.setText(_translate("MainWindow", "Отменить поиск и сортировку"))
        self.pushButton_9.setText(_translate("MainWindow", "Сохранить изменения"))

    subj = LOS()

    def btnClicked(self):
        try:
            if self.lineEdit.text().strip() == "" or self.lineEdit_2.text().strip() == "":
                raise Exception("Поля не заполнены")

            current = self.subj.find(self.lineEdit.text().strip().lower().capitalize())
            if current is None:
                self.subj.add(self.lineEdit.text().strip().lower().capitalize())
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

            current = self.subj.find(self.lineEdit.text().strip().lower().capitalize())
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
            sname = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "Save file", "", "Database (*.db)")[0]
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

            self.printSubj()

            sql.close()
            self.textBrowser.append("Предметный указатель загружен")
        except sqlite3.DatabaseError as e:
            self.textBrowser.append("Ошибка при загрузке: " + str(e))
        except Exception as e:
            self.textBrowser.append(str(e))

    def btn5Clicked(self):
        if self.comboBox.currentIndex() == 0:
            self.listWidget.sortItems()
            self.textBrowser.append("Указатель отсортирован по алфавиту")
        if self.comboBox.currentIndex() == 1:
            self.listWidget.sortItems(Qt.Qt.DescendingOrder)
            self.textBrowser.append("Указатель отсортирован по алфавиту в обратном порядке")

    def btn6Clicked(self):
        try:
            if self.lineEdit_3.text().strip() == "":
                raise Exception("Фильтр поиска не введен")
            self.listWidget.clear()
            current = self.subj.getFirst()
            n = 0
            while current:
                if self.lineEdit_3.text().strip().lower() in current.getValue().lower():
                    self.listWidget.addItem("{0} — {1}".format(current.getValue(), current.printPages()))
                    n += 1
                current = current.getNext()
            if self.listWidget.count() == 0:
                self.printSubj()
                raise Exception("Совпадений не найдено")
            self.textBrowser.append("Совпадений найдено: " + str(n))
        except Exception as e:
            self.textBrowser.append(str(e))

    def btn7Clicked(self):
        try:
            if self.lineEdit_3.text().strip() == "":
                raise Exception("Фильтр поиска не введен")
            page = int(self.lineEdit_3.text().strip())
            self.listWidget.clear()
            current = self.subj.getFirst()
            n = 0
            while current:
                if page in current.getPages():
                    self.listWidget.addItem("{0} — {1}".format(current.getValue(), current.printPages()))
                    n += 1
                current = current.getNext()
            if self.listWidget.count() == 0:
                self.printSubj()
                raise Exception("Совпадений не найдено")
            self.textBrowser.append("Совпадений найдено: " + str(n))
        except ValueError:
            self.textBrowser.append("Неправильна введена страница")
        except Exception as e:
            self.textBrowser.append(str(e))

    def btn8Clicked(self):
        self.printSubj()
        self.textBrowser.append("Изменения отменены")

    def btn9Clicked(self):
        self.subj = LOS()
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i).text()
            word, pages = item.split(" — ")
            pages = list(map(int, pages.split(", ")))
            word = Node(word)
            for page in pages:
                word.addPage(page)
            self.subj.add(word)
        self.textBrowser.append("Изменения сохранены")

    def btn10Clicked(self):
        try:
            lname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Open File", "", "Text Files (*.txt);;All Files (*.*)")[0]
            if lname.strip() == "":
                raise Exception("Формирование отменено")

            file1 = open(lname, 'r')
            for line in file1:
                for word in re.split("['.',:;\"\' '?''!'-+=/—-]", line):
                    print(word)
                    

        except UnicodeDecodeError:
            self.textBrowser.append("Ошибка при чтении: выбран неверный файл")
        except Exception as e:
            self.textBrowser.append(str(e))

    def listWidgetItemChanged(self):
        if self.listWidget.currentItem():
            data = self.listWidget.currentItem().text().split(" ")
            self.lineEdit.setText(data[0])
            self.lineEdit_2.setText(data[-1])

    def printSubj(self):
        self.listWidget.clear()
        current = self.subj.getFirst()
        while current:
            self.listWidget.addItem("{0} — {1}".format(current.getValue(), current.printPages()))
            current = current.getNext()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())