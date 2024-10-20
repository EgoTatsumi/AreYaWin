import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap, QImage, QTransform, QColor

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1280, 720)

        self.pixmap1 = QPixmap('Images/menu/menu.png')
        self.menu = QLabel(self)
        self.menu.resize(self.pixmap1.width(), self.pixmap1.height())
        self.menu.move(0, 0)
        self.menu.setPixmap(self.pixmap1)

        self.flag_btn = QPushButton(self)
        self.flag_btn.move(800, 250)
        self.flag_btn.resize(300, 100)
        self.flag_btn.setText('FLAG GAME')
        self.flag_btn.clicked.connect(self.button)

        self.quiz_btn = QPushButton(self)
        self.quiz_btn.move(800, 380)
        self.quiz_btn.resize(300, 100)
        self.quiz_btn.setText('QUIZ')
        self.quiz_btn.clicked.connect(self.button)

        self.score_btn = QPushButton(self)
        self.score_btn.move(800, 500)
        self.score_btn.resize(300, 100)
        self.score_btn.setText('SETTINGS')
        self.score_btn.clicked.connect(self.button)




    def button(self):
        if self.sender() is self.flag_btn:
            self.window = Flag_window()
            self.window.show()
        elif self.sender() is self.quiz_btn:
            self.window = Quiz_window()
            self.window.show()
        else:
            self.window = Settings_window()
            self.window.show()


class Flag_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1280, 720)


class Quiz_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1280, 720)

class Settings_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1280, 720)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())