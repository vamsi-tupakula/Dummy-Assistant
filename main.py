import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def get_command():
    try:
        with sr.Microphone() as source:
            print("Say something!....")
            voice = listener.listen(source)
            command = ''
            command = listener.recognize_google(voice)
            if command != '':
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa','')
    except:
        print("sorry....")
    return command

def run_alexa():
    command = get_command()
    if 'play' in command:
        command = command.replace('play','')
        speak('playing' + command)
        pywhatkit.playonyt(command)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('current time is ' + time)

run_alexa()