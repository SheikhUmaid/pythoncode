import pyttsx3 as ptt

a = ptt.init()

voices = a.getProperty('voices')
print(voices)