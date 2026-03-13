import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
# import json
import os
import time
from dotenv import load_dotenv

load_dotenv()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(text):
    print("Assistant:" , text)
    engine.say(text)
    engine.runAndWait()
    
def take_commands():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5)

            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in')
            print(f"You said : {command}")
            return command.lower()
        
    except sr.WaitTimeoutError:
        print("no command found.")
        return "timeout"
    except sr.UnknownValueError:
        return "timeout"
    except sr.RequestError:
        speak("Network error. Please check your internet connection.")
        return "timeout"
    except Exception:
        speak("Something went Wrong.")
        return "timeout"

def analyze_command(command):
    your_word = command.lower().split()
    if any(word in your_word for word in["hi","hello","hey"]):
        return "greeting"
    elif any(word in your_word for word in["time","clock"]):
        return "time"
    elif any(word in your_word for word in ["find","search","google"]):
        return "search"
    elif any(word in your_word for word in ["date","today"]):
        return "date"
    elif any(word in your_word for word in["weather","temperature"]):
        return "weather"
    elif any(word in your_word for word in["bye","exit","stop","thank","quit"]):
        return "exit"
    else:
        return "unknown"
    
def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"This is {time} now")
def tell_date():
    date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today is {date}")
def web_search(query):
    speak("Wait a Minute, Searching on google")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def get_weather_data(city):
    my_api_key = os.getenv("Weather_API_Key")
    if not my_api_key:
        speak("Sorry can't check weather right now.")
        return 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api_key}&units=metric"
    try:
        responses = requests.get(url).json()
        if responses.get("cod") != 200:
            speak("City not found.")
            return 
        temp = responses["main"]["temp"]
        description = responses["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp} degree with {description}")
    except Exception:
        speak("Failed to access weather data.")

# def check_custom_commands():
    
time.sleep(1)
Assistant_name = "Maeve"
speak(f"Helloo, my name is {Assistant_name}, your personal Voice Assistant, How can I help you?")
while True:

    command = take_commands()
    if command == "":
        continue
    if command == "timeout":
        speak("no command found, shutting down...")
        break

    purpose = analyze_command(command)
    
    if purpose == "greeting":
        speak("Hii there, Nice to meet you.")

    elif purpose == "time":
        tell_time()
    
    elif purpose =="date":
        tell_date()
    
    elif purpose == "search":
        speak("What do you want to search?")
        query = take_commands()
        if query:
            web_search(query)
    elif purpose == "weather":
        speak("Which city's weather you want to know?")
        city = take_commands()
        if city:
            get_weather_data(city)
    elif purpose == "exit":
        speak("Thank You, Have a nice day.")
        break

    else:
        speak("Sorry, I can't deal with that. ")