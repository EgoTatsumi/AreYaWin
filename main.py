import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap, QImage, QTransform, QColor
from funcs import take_flag


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
            self.close()
        elif self.sender() is self.quiz_btn:
            self.window = Quiz_window()
            self.window.show()
            self.close()
        else:
            self.window = Settings_window()
            self.window.show()
            self.close()


class Flag_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('FlagGame')

        self.pic_flag = QPixmap(f'Images/flags/{take_flag()}.png')
        self.picc = QLabel(self)
        self.picc.resize(self.pic_flag.width(), self.pic_flag.height())
        self.picc.move(341, 50)
        self.picc.setPixmap(self.pic_flag)

        self.ans1 = QPushButton(self)
        self.ans1.resize(300, 100)
        self.ans1.move(340, 480)

        self.ans2 = QPushButton(self)
        self.ans2.resize(300, 100)
        self.ans2.move(645, 480)

        self.ans3 = QPushButton(self)
        self.ans3.resize(300, 100)
        self.ans3.move(340, 585)

        self.ans4 = QPushButton(self)
        self.ans4.resize(300, 100)
        self.ans4.move(645, 585)

        self.back = QPushButton(self)
        self.back.resize(80, 50)
        self.back.setText('Back to menu')
        self.back.clicked.connect(self.backk)


    def backk(self):
        self.window = Window()
        self.window.show()
        self.close()




class Quiz_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('ffffff')

        self.ans1 = QPushButton(self)
        self.ans1.resize(300, 100)
        self.ans1.move(340, 480)

        self.ans2 = QPushButton(self)
        self.ans2.resize(300, 100)
        self.ans2.move(645, 480)

        self.ans3 = QPushButton(self)
        self.ans3.resize(300, 100)
        self.ans3.move(340, 585)

        self.ans4 = QPushButton(self)
        self.ans4.resize(300, 100)
        self.ans4.move(645, 585)

        self.back = QPushButton(self)
        self.back.resize(80, 50)
        self.back.setText('Back to menu')
        self.back.clicked.connect(self.backk)

    def backk(self):
        self.window = Window()
        self.window.show()
        self.close()



class Settings_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1280, 720)

        self.back = QPushButton(self)
        self.back.resize(80, 50)
        self.back.setText('Back to menu')
        self.back.clicked.connect(self.backk)


    def backk(self):
        self.window = Window()
        self.window.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())