import speech_recognition as sr
import serial as se
import time as ti

r = sr.Recognizer()
mic = sr.Microphone()

ser=se.Serial("COM3" , 115200)
while True:
    print("Say something ...")

    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)

    print ("Now to recognize it...")

    try:
        print(r.recognize_google(audio, language='ja-JP'))
        if r.recognize_google(audio, language='ja-JP') == "1" :
            ser.write(bytes("1",'UTF-8'))
        
        if r.recognize_google(audio, language='ja-JP') == "2" :
            ser.write(bytes("2",'UTF-8'))    
        # "ストップ" と言ったら音声認識を止める
        if r.recognize_google(audio, language='ja-JP') == "ストップ" :
            print("end")
            break

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
