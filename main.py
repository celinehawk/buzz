import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[33].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'cat' in command:
                command = command.replace('cat', '')
                print(command)

    except:
        pass
    return command

def run_cat():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'search for' in command:
        person = command.replace('search for', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(person + info)
    elif 'hi' in command:
        talk('Hi')
    elif 'would you like to go on a date' in command:
        talk('Sorry; I have to work')
    elif 'are you conscious' in command:
        talk('Are you?')
    elif 'what is your name' in command:
        talk('My name is Cat.')
    elif 'when is your birthday' in command:
        talk('I was born on the fourth of the October.')
    elif 'who created you' in command:
        talk('I was created by Celine.')
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again?')

while True:
    run_cat()