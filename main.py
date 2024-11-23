import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox
from PyQt6.QtGui import QPixmap
from funcs import take_flag, flag_game, quiz, quiz_vars
count = 0
record_quiz = 0
record_flag = 0
len_quiz = len(quiz_vars)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.flag_close = True
        self.setWindowTitle('Main')

        self.pixmap1 = QPixmap(f'Images/menu/menu.png')
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
        self.score_btn.setText('STATISTIC')
        self.score_btn.clicked.connect(self.button)

    def close_window(self):
        self.flag_close = False
        self.close()

    def closeEvent(self, event):
        if self.flag_close:
            reply = QMessageBox.question(self, 'Подтверждение выхода',
                                         'Вы действительно хотите закрыть приложение?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()


    def button(self):
        if self.sender() is self.flag_btn:
            self.window = Flag_window()
            self.window.show()
            self.close_window()
        elif self.sender() is self.quiz_btn:
            self.window = Quiz_window()
            self.window.show()
            self.close_window()
        else:
            self.window = Settings_window()
            self.window.show()
            self.close_window()


class Flag_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('FlagGame')
        self.flag_close = True
        global count
        count = 0

        self.pixmap1 = QPixmap(f'Images/menu/back.png')
        self.back = QLabel(self)
        self.back.resize(self.pixmap1.width(), self.pixmap1.height())
        self.back.move(0, 0)
        self.back.setPixmap(self.pixmap1)

        self.flag = take_flag()
        self.pic_flag = QPixmap(f'Images/flags/{self.flag}.png')
        self.picc = QLabel(self)
        self.picc.resize(self.pic_flag.width(), self.pic_flag.height())
        self.picc.move(341, 50)
        self.picc.setPixmap(self.pic_flag)

        self.score = QLabel(self)
        self.score.setText(f'<h1 style="color: rgb(0, 0, 0);"> Score: {count}')
        self.score.move(0, 60)

        self.vars = flag_game(self.flag)
        self.ans1 = QPushButton(self)
        self.ans1.resize(300, 100)
        self.ans1.move(340, 480)
        self.ans1.setText(self.vars[1])
        self.ans1.clicked.connect(self.check)


        self.ans2 = QPushButton(self)
        self.ans2.resize(300, 100)
        self.ans2.move(645, 480)
        self.ans2.setText(self.vars[2])
        self.ans2.clicked.connect(self.check)

        self.ans3 = QPushButton(self)
        self.ans3.resize(300, 100)
        self.ans3.move(340, 585)
        self.ans3.setText(self.vars[3])
        self.ans3.clicked.connect(self.check)

        self.ans4 = QPushButton(self)
        self.ans4.resize(300, 100)
        self.ans4.move(645, 585)
        self.ans4.setText(self.vars[4])
        self.ans4.clicked.connect(self.check)

        self.buttonList = [self.ans1, self.ans2, self.ans3, self.ans4]
        self.backbtn = QPushButton(self)
        self.backbtn.resize(80, 50)
        self.backbtn.setText('Back to menu')
        self.backbtn.clicked.connect(self.backk)

    def closeEvent(self, event):
        if self.flag_close:
            reply = QMessageBox.question(self, 'Подтверждение выхода',
                                         'Вы действительно хотите закрыть приложение?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()

    def backk(self):
        self.window = Window()
        self.window.show()
        self.flag_close = False
        self.close()

    def result(self):
        self.window = Result_window()
        self.window.show()
        self.flag_close = False
        self.close()

    def check(self):
        global count, record_flag
        answer = self.buttonList.index(self.sender()) + 1
        if self.flag == self.vars[answer]:
            count += 1
            record_flag = max(record_flag, count)
            self.updatee()
        else:
            self.result()

    def updatee(self):
        self.flag = take_flag()
        self.pic_flag = QPixmap(f'Images/flags/{self.flag}.png')
        self.picc.setPixmap(self.pic_flag)
        self.score.setText(f'<h1 style="color: rgb(0, 0, 0);"> Score: {count}')

        self.vars = flag_game(self.flag)
        self.ans1.setText(self.vars[1])
        self.ans2.setText(self.vars[2])
        self.ans3.setText(self.vars[3])
        self.ans4.setText(self.vars[4])


class Quiz_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Quiz')
        self.flag_close = True
        global count
        count = 0
        self.vars = quiz(count)
        self.corans = self.vars[5]

        self.pixmap1 = QPixmap(f'Images/menu/back.png')
        self.back = QLabel(self)
        self.back.resize(self.pixmap1.width(), self.pixmap1.height())
        self.back.move(0, 0)
        self.back.setPixmap(self.pixmap1)
        self.score = QLabel(self)
        self.score.setText(f'<h1 style="color: rgb(0, 0, 0);"> Score: {count}')
        self.score.move(0, 60)

        self.question = QLabel(self)
        self.question.setText(f'<h1 style="color: rgb(0, 0, 0);"> {self.vars[0]}')
        self.question.move(400, 100)
        self.question.resize(800, 50)

        self.ans1 = QPushButton(self)
        self.ans1.resize(300, 100)
        self.ans1.move(340, 480)
        self.ans1.setText(self.vars[1])
        self.ans1.clicked.connect(self.check)

        self.ans2 = QPushButton(self)
        self.ans2.resize(300, 100)
        self.ans2.move(645, 480)
        self.ans2.setText(self.vars[2])
        self.ans2.clicked.connect(self.check)

        self.ans3 = QPushButton(self)
        self.ans3.resize(300, 100)
        self.ans3.move(340, 585)
        self.ans3.setText(self.vars[3])
        self.ans3.clicked.connect(self.check)

        self.ans4 = QPushButton(self)
        self.ans4.resize(300, 100)
        self.ans4.move(645, 585)
        self.ans4.setText(self.vars[4])
        self.ans4.clicked.connect(self.check)

        self.buttonList = [self.ans1, self.ans2, self.ans3, self.ans4]

        self.backbtn = QPushButton(self)
        self.backbtn.resize(80, 50)
        self.backbtn.setText('Back to menu')
        self.backbtn.clicked.connect(self.backk)

    def closeEvent(self, event):
        if self.flag_close:
            reply = QMessageBox.question(self, 'Подтверждение выхода',
                                         'Вы действительно хотите закрыть приложение?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()

    def check(self):
        if self.vars[self.corans] == self.vars[self.buttonList.index(self.sender())+1]:
            self.updatee()
        else:
            self.result()

    def backk(self):
        self.window = Window()
        self.window.show()
        self.flag_close = False
        self.close()

    def result(self):
        self.window = Result_window()
        self.window.show()
        self.flag_close = False
        self.close()

    def updatee(self):
        global count, record_quiz
        count += 1
        self.score.setText(f'<h1 style="color: rgb(0, 0, 0);"> Score: {count}')
        record_quiz = max(record_quiz, count)
        if count == len_quiz:
            self.result()
        else:
            record_quiz = max(record_quiz, count)
            self.vars = quiz(count)
            self.corans = self.vars[5]
            self.question.setText(f'<h1 style="color: rgb(0, 0, 0);"> {self.vars[0]}')
            self.ans1.setText(self.vars[1])
            self.ans2.setText(self.vars[2])
            self.ans3.setText(self.vars[3])
            self.ans4.setText(self.vars[4])


class Settings_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.flag_close = True
        self.setWindowTitle('Statistic')

        self.pixmap1 = QPixmap(f'Images/menu/back.png')
        self.back = QLabel(self)
        self.back.resize(self.pixmap1.width(), self.pixmap1.height())
        self.back.move(0, 0)
        self.back.setPixmap(self.pixmap1)

        self.backbtn = QPushButton(self)
        self.backbtn.resize(80, 50)
        self.backbtn.setText('Back to menu')
        self.backbtn.clicked.connect(self.backk)

        global record_flag, record_quiz
        self.record_flagg = QLabel(self)
        self.record_flagg.setText(f'<h1 style="color: rgb(0, 0, 0);" > Best Score in FlagGame: {record_flag}')
        self.record_flagg.move(0, 60)

        self.record_quizz = QLabel(self)
        self.record_quizz.setText(f'<h1 style="color: rgb(0, 0, 0);"> Best Score in Quiz: {record_quiz}')
        self.record_quizz.move(0, 80)

    def closeEvent(self, event):
        if self.flag_close:
            reply = QMessageBox.question(self, 'Подтверждение выхода',
                                         'Вы действительно хотите закрыть приложение?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()


    def backk(self):
        self.window = Window()
        self.window.show()
        self.flag_close = False
        self.close()


class Result_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle('Result')
        self.move(460, 140)
        self.flag_close = True
        global count

        self.pixmap = QPixmap(f'Images/menu/lose.png')
        self.lose = QLabel(self)
        self.lose.resize(self.pixmap.width(), self.pixmap.height())
        self.lose.move(0, 0)
        self.lose.setPixmap(self.pixmap)

        self.BtnBack = QPushButton(self)
        self.BtnBack.setText('Back to menu')
        self.BtnBack.resize(200, 100)
        self.BtnBack.move(200, 50)
        self.BtnBack.clicked.connect(self.checkbtn)

        self.BtnFlag = QPushButton(self)
        self.BtnFlag.setText('FLAG GAME')
        self.BtnFlag.resize(200, 100)
        self.BtnFlag.move(200, 180)
        self.BtnFlag.clicked.connect(self.checkbtn)

        self.BtnQuiz = QPushButton(self)
        self.BtnQuiz.setText('QUIZ')
        self.BtnQuiz.resize(200, 100)
        self.BtnQuiz.move(200, 310)
        self.BtnQuiz.clicked.connect(self.checkbtn)

        self.Scoreboard = QLabel(self)
        self.Scoreboard.setText(f'<h1 style="color: rgb(0, 0, 0);"> Score:{count}')
        self.Scoreboard.resize(100, 100)
        self.Scoreboard.move(0, 0)

    def closeEvent(self, event):
        if self.flag_close:
            reply = QMessageBox.question(self, 'Подтверждение выхода',
                                         'Вы действительно хотите закрыть приложение?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()
    def backk(self):
        self.window = Window()
        self.window.show()
        self.flag_close = False
        self.close()

    def checkbtn(self):
        if self.sender() is self.BtnBack:
            self.window = Window()
            self.window.show()
            self.flag_close = False
            self.close()
        elif self.sender() is self.BtnFlag:
            self.window = Flag_window()
            self.window.show()
            self.flag_close = False
            self.close()
        else:
            self.window = Quiz_window()
            self.window.show()
            self.flag_close = False
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())