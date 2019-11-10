from PyQt5 import QtWidgets, uic
import sys

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

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


if __name__ == "__main__":    
    app = QtWidgets.QApplication([])
    win = uic.loadUi("untitled.ui")

    win.show()
    sys.exit(app.exec())