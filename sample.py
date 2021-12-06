import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import serial as se
import time as ti
from serial.win32 import ClearCommBreak
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
ser = se.Serial("COM3", 115200)
conf = []
btn = [0] * 10
img = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class Figure:
    def __init__(self, name, image, data):
        self.name = name
        self.image = image
        self.data = data


class NishikawaButton(QPushButton):
    def save_num(self, num):
        self.num = num

    def print_num(self):
        print(self.num)
        ser.write(bytes(f"{self.num}", "UTF-8"))


class MainWindow(QWidget):
    def __init__(self, parent=None):
        self.bt_nums = []
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #80ff80")

        self.setGeometry(
            500, 500, 1000, 600
        )  # self.move(400, 300), self.resize(400, 500)と一緒
        self.setWindowTitle("American Sign Language Learning System")
        self.setWindowIcon(QIcon("simulog.gif"))
        img.append(QPixmap("gesture1.jpg"))
        img.append(QPixmap("gesture2.jpg"))
        img.append(QPixmap("gesture3.jpg"))
        img.append(QPixmap("gesture4.jpg"))
        img.append(QPixmap("gesture5.jpg"))
        img.append(QPixmap("gesture6.jpg"))
        img.append(QPixmap("gesture7.jpg"))
        img.append(QPixmap("gesture8.jpg"))
        img.append(QPixmap("gesture9.jpg"))
        img.append(QPixmap("gesture10.jpg"))

        # ボタン
        layout = QGridLayout()

        self.voice_button = QPushButton("", self)
        self.voice_button.setText("Voice Recognition!!")
        self.voice_button.resize(200, 200)
        self.voice_button.setFont(QFont("ＭＳ 明朝", 14, 50))
        s = "background-color: yellow;"
        self.voice_button.setStyleSheet(s)
        self.voice_button.clicked.connect(self.printnum)

        layout.addWidget(self.voice_button, 2, 4)
        for num in range(10):
            if num < 5:
                # btn[num] = QPushButton("", self)
                btn[num] = NishikawaButton("", self)
                btn[num].setIcon(QIcon(img[num]))
                btn[num].setIconSize(QSize(200, 200))
                btn[num].resize(140, 210)
                # btn[num].clicked.connect(bt_num.printnum)
                btn[num].save_num(num)
                v = "background-color: green;"
                btn[num].setStyleSheet(v)
                btn[num].clicked.connect(btn[num].print_num)
                # btn[num].clicked.connect(lambda:print(num))
                # self.textbox1 =QLineEdit(self)
                # self.textbox1.move(500,500)
                layout.addWidget(btn[num], 0, num)

            else:
                # btn[num] = QPushButton("", self)
                btn[num] = NishikawaButton("", self)
                btn[num].setIcon(QIcon(img[num]))
                btn[num].setIconSize(QSize(200, 200))
                btn[num].resize(140, 210)
                btn[num].save_num(num)
                v = "background-color: green;"
                btn[num].setStyleSheet(v)
                btn[num].clicked.connect(btn[num].print_num)
                layout.addWidget(btn[num], 1, num - 5)
        self.setLayout(layout)

        # self.textbox1 =QLineEdit(self)
        # self.textbox1.move(500,500)
        # self.textbox1.resize(150,50)
        # sizeHintでいいかんじの大きさにしてくれる
        # チェックボックス

        # スライダー
        # slider = QSlider(Qt.Horizontal, self)
        # slider.setFocusPolicy(Qt.NoFocus)
        # slider.setGeometry(30, 40, 100, 30)
        # slider.valueChanged.connect(self.changeValue)

        # self.label = QLabel(self)
        # self.label.setText("0")
        # self.label.setGeometry(160, 40, 80, 30)

        # self.setWindowTitle("Slider")
        # self.setGeometry(50, 50, 300, 300)

    def changeValue(self, value):
        self.label.setText(str(value))

    def printnum(self):
        s = "background-color: red;"
        self.voice_button.setStyleSheet(s)
        self.voice_button.setText("Voice Recognitioning!!")
        while True:
            app.processEvents()
            print("Say something ...")

            with mic as source:
                r.adjust_for_ambient_noise(source)  # 雑音対策
                audio = r.listen(source)

            print("Now to recognize it...")

            try:
                word = r.recognize_google(audio, language="ja-JP")
                print(r.recognize_google(audio, language="ja-JP"))
                if word == "1":
                    ser.write(bytes("0", "UTF-8"))
                    v = "background-color: red;"
                    btn[0].setStyleSheet(v)
                    break
                if word == "2":
                    ser.write(bytes("1", "UTF-8"))
                    v = "background-color: red;"
                    btn[1].setStyleSheet(v)
                    break
                if word == "3":
                    ser.write(bytes("2", "UTF-8"))
                    v = "background-color: red;"
                    btn[2].setStyleSheet(v)
                    break
                if word == "4":
                    ser.write(bytes("3", "UTF-8"))
                    v = "background-color: red;"
                    btn[3].setStyleSheet(v)
                    break
                if word == "5":
                    ser.write(bytes("4", "UTF-8"))
                    v = "background-color: red;"
                    btn[4].setStyleSheet(v)
                    break
                if word == "6":
                    ser.write(bytes("5", "UTF-8"))
                    v = "background-color: red;"
                    btn[5].setStyleSheet(v)
                    break
                if word == "7":
                    ser.write(bytes("6", "UTF-8"))
                    v = "background-color: red;"
                    btn[6].setStyleSheet(v)
                    break
                if word == "8":
                    ser.write(bytes("7", "UTF-8"))
                    v = "background-color: red;"
                    btn[7].setStyleSheet(v)
                    break
                if word == "9":
                    ser.write(bytes("8", "UTF-8"))
                    v = "background-color: red;"
                    btn[8].setStyleSheet(v)
                    break
                if word == "10":
                    ser.write(bytes("9", "UTF-8"))
                    v = "background-color: red;"
                    btn[9].setStyleSheet(v)
                    break

            # 以下は認識できなかったときに止まらないように。
            except sr.UnknownValueError:
                print("could not understand audio")
            except sr.RequestError as e:
                print(
                    "Could not request results from Google Speech Recognition service; {0}".format(
                        e
                    )
                )
        s = "background-color: yellow;"
        self.voice_button.setStyleSheet(s)
        self.voice_button.setText("Voice Recognition!!")

        QTimer.singleShot(3000, self.clearcolor)

    def clearcolor(self):
        print(1)
        for num in range(10):
            v = "background-color: green;"
            btn[num].setStyleSheet(v)


if __name__ == "__main__":
    # for num in range(10):
    #      conf.append(Figure('hello',2,2))
    app = QApplication(sys.argv)  # PyQtで必ず呼び出す必要のあるオブジェクト
    main_window = MainWindow()  # ウィンドウクラスのオブジェクト生成
    main_window.show()  # ウィンドウの表示
    sys.exit(app.exec_())  # プログラム終了
