import datetime
import pyjokes

import talk.talk as talk
import speech_recognizer.speech_recognizer as sr

def run_charlie():
    command = sr.take_command()
    print(command)
    
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk.talk('Current time is ' + time)

    if 'joke' in command:
        joke = pyjokes.get_joke(language="en", category="neutral")
        print(joke)
        talk.talk(joke)


print('hello sir. How are you? My name is Charlie, what can I do for you today?')
talk.talk('hello sir. How are you? My name is Charlie, what can I do for you today?')

while True:
    run_charlie()