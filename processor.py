import pyttsx3
import speech_recognition as sr
import datetime

class Processor:
    def __init__(self):
        self.text = None

    def listening(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            micro = r.listen(source)
        self.text = r.recognize_google(micro)
        return self.text

    def speaking(self):
        speaker = pyttsx3.init()
        speaker.say(self.text)
        speaker.runAndWait()

    def mytime(self):
        time = datetime.datetime.now()
        self.text = time.strftime('%H:%M')

    def myday(self):
        day = datetime.date.today()
        self.text = day
