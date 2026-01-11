import time
import pyttsx3
import speech_recognition as sr
import eel




@eel.expose
def speak(text):
    engine = pyttsx3.init()

    # get male / female voice [0,1]
    voices = engine.getProperty('voices')
    # print(f'the voices is: {voices}')

    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)

    # engine.say("I will speak this text")
    eel.DisplayMessage(text) # from main.js
    engine.say(text)
    engine.runAndWait()
    
    


# def get_active_microphone():
#     """Pick the best available microphone (headset > bluetooth > default)"""
#     mic_list = sr.Microphone.list_microphone_names()

#     preferred_keywords = ["headset", "bluetooth", "airpods", "jbl", "earbuds", "hands-free"]

#     for index, name in enumerate(mic_list):
#         lower_name = name.lower()
#         for keyword in preferred_keywords:
#             if keyword in lower_name:
#                 print(f"Using microphone: {name}")
#                 return sr.Microphone(device_index=index)

#     print("Using default microphone")
#     return sr.Microphone()   # fallback to Windows default


# def takeCommand():
#     r = sr.Recognizer()

#     mic = get_active_microphone()

#     with mic as source:
#         print("Calibrating mic...")
#         r.adjust_for_ambient_noise(source, duration=1)

#         print("Listening...")
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language="en")
#         print("User said:", query)
#         return query.lower()

#     except sr.UnknownValueError:
#         print("Could not understand audio")
#         return ""
#     except sr.RequestError as e:
#         print("Speech service error:", e)
#         return ""    
    


@eel.expose
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...") # from main.js
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)
        
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...") # from main.js
        query = r.recognize_google(audio, language='en')
        print(f"user said: {query}")
        # speak(query) # repeat what user said
        time.sleep(2)
        eel.DisplayMessage(query) # from main.js
        # eel.ShowHood()
        
    except Exception as e:
        return "None, sorry"
    
    return query.lower()

# text = takeCommand()

# speak(text)
    
    

# speak("Hello, I am Sophia, I am an AI Assistant.")


@eel.expose
def allCommands():
    query = takeCommand()
    print(f"the query in allCommands is: {query}")
    
    if 'open' in query:
        # print("I run")
        from engine.features import openCommand
        openCommand(query)
        
    elif 'on youtube':
        from engine.features import PlayYoutube
        PlayYoutube(query)
    else:
        print("Not run")
        
    eel.ShowHood()    
        
    