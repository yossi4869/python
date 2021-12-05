import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import serial as se
import time as ti
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
ser=se.Serial("COM3" , 115200)
conf = [] 
btn = [0] * 10
img = [] 
numbers = [1,2,3,4,5,6,7,8,9,10]
class Figure:
    def __init__(self,name,image,data):
        self.name = name 
        self.image = image
        self.data = data

class bottomnum:
    def __init__(self,num):
        self.num=num 

    def printnum(self):
        while True:
            print("Say something ...")

            with mic as source:
               r.adjust_for_ambient_noise(source) #雑音対策
               audio = r.listen(source)

            print ("Now to recognize it...")

            try:
                print(r.recognize_google(audio, language='ja-JP'))
                if r.recognize_google(audio, language='ja-JP') == "1" :
                    ser.write(bytes("0",'UTF-8'))
                    break        
                if r.recognize_google(audio, language='ja-JP') == "2" :
                    ser.write(bytes("1",'UTF-8'))
                    break    
                if r.recognize_google(audio, language='ja-JP') == "3" :
                    ser.write(bytes("2",'UTF-8'))
                    break    
                if r.recognize_google(audio, language='ja-JP') == "4" :
                    ser.write(bytes("3",'UTF-8'))
                    break    
                if r.recognize_google(audio, language='ja-JP') == "5" :
                    ser.write(bytes("4",'UTF-8'))
                    break    
                if r.recognize_google(audio, language='ja-JP') == "6" :
                    ser.write(bytes("5",'UTF-8'))
                    break    
                if r.recognize_google(audio, language='ja-JP') == "7" :
                    ser.write(bytes("6",'UTF-8'))
                    break    
                if r.recognize_google(audio, language='ja-JP') == "8" :
                    ser.write(bytes("7",'UTF-8'))
                    break    
                if r.recognize_google(audio, language='ja-JP') == "9" :
                    ser.write(bytes("8",'UTF-8'))
                    break    
                if r.recognize_google(audio, language='ja-JP') == "10" :
                    ser.write(bytes("9",'UTF-8'))
                    break    
                                                                                                                              

             # 以下は認識できなかったときに止まらないように。
            except sr.UnknownValueError:
                 print("could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        
            

# def elestim(n):
#     print(1)

class NishikawaButton(QPushButton):
    def save_num(self, num):
        self.num = num
    
    def print_num(self):
        print(self.num )
        ser.write(bytes(f'{self.num }','UTF-8'))

class MainWindow(QWidget):
    def __init__(self, parent=None):
        self.bt_nums = []
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #80ff80")

        self.setGeometry(500, 500, 1000, 600) #self.move(400, 300), self.resize(400, 500)と一緒
        self.setWindowTitle('American Sign Language Learning System')
        self.setWindowIcon(QIcon('simulog.gif'))
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
        
        for num in range(10):
            bt_num=bottomnum(num)
            self.bt_nums.append(bt_num)
            if num < 5:
                # btn[num] = QPushButton("", self)
                btn[num] = NishikawaButton("", self)
                btn[num].setIcon(QIcon(img[num]))
                btn[num].setIconSize(QSize(200,200))
                btn[num].resize(140,210)
                # btn[num].clicked.connect(bt_num.printnum)
                btn[num].save_num(num)
                btn[num].clicked.connect(bt_num.printnum)
                # btn[num].clicked.connect(lambda:print(num))
                # self.textbox1 =QLineEdit(self)
                # self.textbox1.move(500,500)
                layout.addWidget(btn[num],0,num)
            else:
                btn[num] = QPushButton("", self)
                btn[num].setIcon(QIcon(img[num]))
                btn[num].setIconSize(QSize(200,200))
                btn[num].resize(140,210)
                btn[num].clicked.connect(bt_num.printnum)
                layout.addWidget(btn[num],1,num-5)
        self.setLayout(layout)
        

        
                # self.textbox1 =QLineEdit(self)
                # self.textbox1.move(500,500)
        # self.textbox1.resize(150,50)
        # sizeHintでいいかんじの大きさにしてくれる
        # チェックボックス

    def buttonClicked(self):
        elestim(1)

if __name__ == '__main__':
    # for num in range(10):
    #      conf.append(Figure('hello',2,2))
    app = QApplication(sys.argv) #PyQtで必ず呼び出す必要のあるオブジェクト
    main_window = MainWindow() #ウィンドウクラスのオブジェクト生成
    main_window.show() #ウィンドウの表示
    sys.exit(app.exec_()) #プログラム終了   