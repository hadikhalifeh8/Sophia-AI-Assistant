import os
import eel

from engine.features import *
from engine.command import *

eel.init('www')
playAssistantSound()

# os.system('start chrome.exe --app="http://localhost:8000/index.html"')
# pip install eel
# pip install playsound==1.2.2
# pip install pyttsx3
# pip install SpeechRecognition
# pip install PyAudio
# pip install pywhatkit  (YouTube Automation, Google Search, WhatsApp Messaging, Text to Handwriting, Send Emails)

eel.start('index.html', mode='chrome', host='localhost', block=True)