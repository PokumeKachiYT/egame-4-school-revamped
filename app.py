from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QLabel,
)
from PyQt6 import QtGui
from PyQt6.QtGui import QFontDatabase,QFont
import sys
import server

width = height = 0

class Menu(QVBoxLayout):
    label = None
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        label = QLabel()

        line_edit = QLineEdit()
        line_edit.textChanged.connect(label.setText)

        button = QPushButton('Click me')
        button.setStyleSheet('background-color: #222233;color: #FFFFFF;font-size: 25px')
        button.setFont(QFont('Courier',25))
        button.clicked.connect(self.button_clicked)

        self.addWidget(button)
        self.addWidget(line_edit)
        self.addWidget(label)

    def button_clicked(self):
        print('lcikced')

class MainWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle('Hello World')
        self.showFullScreen()

        menu = Menu()
        self.setLayout(menu)

def init():
    global width,height

    app = QApplication(sys.argv)

    QFontDatabase.addApplicationFont('jetbrains.ttf')

    screen_rect = QtGui.QGuiApplication.primaryScreen().availableGeometry()

    width, height = screen_rect.width(), screen_rect.height()

    window = MainWindow()
    window.setStyleSheet('background-color: #111122')

    sys.exit(app.exec())

if __name__ == '__main__':
    init()
