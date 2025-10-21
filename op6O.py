import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def verbalize(text):
    ttsx.say(text)
    ttsx.runAndWait()

if __name__ == '__main__':
    verbalize("Operator 6O here, what..is..up..cuzz")
