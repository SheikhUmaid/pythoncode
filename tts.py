import pyttsx3 as ptts
import time 
def Speak(input):
    a = ptts.init()
    a.say(input)
    a.runAndWait()
    time.sleep()

Speak("Hello world")
Speak("Hello world")