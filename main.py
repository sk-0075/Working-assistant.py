import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
      with sr.Microphone() as source:
             print('listening...')
             voice = listener.listen(source)
             command = listener.recognize_google(voice)
             command = command.lower()
             if 'alexa' in command:
                 command = command.replace('alexa', '')
                 print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', "")
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who the hell is' in command:
        person = command.replace('who the hell is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('mai saurav ki hun aur rahungi bhi')
    elif 'do you love me' in command:
        talk('chup kar kute saurav ki hun')
    elif 'tell me your number' in command:
        talk('8544754745')
    elif'tera malik kon hai' in command:
        talk('mera malik saurav hai')
    else:
        talk('zor se bol brother.')
while True:
    run_alexa()

