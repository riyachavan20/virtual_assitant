import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your Virtual Assistent. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'tell me' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'weather' in query:
            webbrowser.open("https://www.accuweather.com/en/in/aurangabad/189320/weather-forecast/189320")
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'location' in query:
            webbrowser.open("https://www.gps-coordinates.net/my-location")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\Desktop\\my music'
            songs = os.listdir(music_dir)
            print(random.choice(songs))  
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        
        elif 'english poem' in query:
            poem = 'C:\\Users\\HP\\Desktop\\poem'
            poeme = os.listdir(poem)
            print(random.choice(poeme))  
            os.startfile(os.path.join(poem, random.choice(poeme)))

        elif 'marathi poem' in query:
            kavita = 'C:\\Users\\HP\\Desktop\\kavita m'
            poemm = os.listdir(kavita)
            print(poemm)    
            os.startfile(os.path.join(kavita, poemm[0]))

        elif 'hindi poem' in query:
            kavitah = 'C:\\Users\\HP\\Desktop\\kavita h'
            poemh = os.listdir(kavitah)
            print(random.choice(poemh))  
            os.startfile(os.path.join(kavitah, random.choice(poemh)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open word' in query:
            word = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\word"
            os.startfile(word)

        elif 'open powerpoint' in query:
            powerpoint = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint"
            os.startfile(powerpoint)

        elif 'open excel' in query:
            excel = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel"
            os.startfile(excel)

        elif 'open calculator' in query:
            calci = "C:\Windows\System32\calc.exe"
            os.startfile(calci)

        elif 'open camera' in query:
            cam = "microsoft.windows.camera:"
            os.startfile(cam)

           
