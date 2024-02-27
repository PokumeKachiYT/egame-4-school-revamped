from PyQt6.QtWidgets import (
    QApplication,
    QTreeWidget,
    QTreeWidgetItem,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QFileDialog,
)
from PyQt6.QtGui import (
    QGuiApplication,
    QFontDatabase,
    QFont,
)
from PyQt6.QtCore import (
    QRect,
)
import sys
import server
import loader

width = height = 0

class Menu(QVBoxLayout):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
      
        new_button = QPushButton('NEW')

        load_button = QPushButton('LOAD')
        load_button.setStyleSheet('background-color: #778877;color: #FFFFFF;font-size: 25px')
        load_button.setFont(QFont('JetBrainsMono NFM Thin',25))
        load_button.clicked.connect(self.button_clicked)

        self.addWidget(new_button)
        self.addWidget(load_button)

    def button_clicked(self):
        file_name = QFileDialog.getOpenFileName(
            window,
            'Load Game',
            '${HOME}',
            'CSV Files (*.csv)',
        )
        file_path = file_name[0]
        if file_path and file_path != '':
            loader.load(file_path)

class MainWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle('Hello World')
        self.setStyleSheet('background-color: #AAAABB')
        self.showFullScreen()

        menu = Menu()
        self.setLayout(menu)

def init():
    global width,height,window

    app = QApplication(sys.argv)

    QFontDatabase.addApplicationFont('../assets/fonts/jetbrains.ttf')

    screen_rect = QGuiApplication.primaryScreen().availableGeometry()

    width, height = screen_rect.width(), screen_rect.height()

    window = MainWindow()

    sys.exit(app.exec())

if __name__ == '__main__':
    init()
