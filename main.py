import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)

def speak():
    speaker.say("I am your alexa")
    speaker.say("How can i help you")
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

speak()