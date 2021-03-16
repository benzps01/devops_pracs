import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)
end = False

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('hey alexa','')
    except:
        pass

    return command

def run_alexa():
    command = take_command()
    if 'stop' in command:
        end = True
    elif 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is','')
        #person = command.replace('tell me something about','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(joke)
        talk(pyjokes.get_joke())
    else:
        talk('Please repeat again')

while end is False:
    run_alexa()
break
    