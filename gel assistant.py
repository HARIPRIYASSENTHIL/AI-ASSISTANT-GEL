import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate=150
engine.setProperty('rate', newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
def wishme():
    speak("welcome back priya!")

    hour = datetime.datetime.now().hour
    if hour >=6 and hour <= 12:
        speak("good morning dear")
    elif hour >=12 and hour < 18:
        speak("good afternoon dear")
    elif hour >=18 and hour <24:
        speak("good evening dear")
    else:
        speak("good night dear")
    speak("gel at your service. how can i help you?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("RECOGNIZING....")
        query = r.recognize_google(audio, 'en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please...")
        return "None"
    return query
def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com","123test")
    server.sendmail("haripriyasenthilkumar836@gmail.com",to,content)
    server.close
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\image\ss.png")
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " +usage)

    battery = psutil.sensors_battery
    speak("battery is at")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_jokes())
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, Sentence = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should say?")
                content = takeCommand()
                to = "haripriyasenthilkumar836@gmail.com"
                sendmail(to, content)
                speak("email sent successfully")
            except Exception as e:
                speak(e)
                speak("unable to send the message")
        elif "search in chrome" in query:
            speak("what should i search?")
            chrompath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chrompath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system("shutdown - 1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
       
        elif "remember that" in query:
            speak("what should i remember?")
            data = takeCommand()
            remember = open('data.txt', "w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open('data.txt', "r")
            speak("you said me to remember that" +remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("done")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()




