#!/usr/bin/env python

######################################################
# python code template
# pyside6 basic application with css decoration
######################################################

import sys
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Click Me!")
        self.text = QtWidgets.QLabel(
            "Hello World!", alignment=QtCore.Qt.AlignCenter
        )
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.click)

    @QtCore.Slot()
    def click(self):
        print("Clicked!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
