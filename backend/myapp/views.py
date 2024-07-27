# from django.shortcuts import render, redirect
# import speech_recognition as sr
# import pyttsx3
# import wikipedia
# import webbrowser
# import datetime
# import os
# import pyjokes
# import ctypes
# from ecapture import ecapture as ec

# recognizer = sr.Recognizer()

# def speak(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)
#     engine.setProperty('volume', 0.9)
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     engine.say(text)
#     engine.runAndWait()

# def process_speech():
#     with sr.Microphone() as source:
#         recognizer.pause_threshold = 1
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#     try:
#         query = recognizer.recognize_google(audio, language="en-in")
#         return query
#     except Exception as e:
#         speak("Sorry, I did not get that")
#         return "None"

# def index(request):
#     if request.method == 'POST' and 'task' in request.POST:
#         task = request.POST['task']
#         if task == 'perform_task':
#             return perform_task(request)
#     return render(request, 'index.html')

# def perform_task(request):
#     query = process_speech().lower()
#     if 'wikipedia' in query:
#         speak('Searching Wikipedia...')
#         query = query.replace("wikipedia", "")
#         results = wikipedia.summary(query, sentences=2)
#         speak("According to Wikipedia")
#         speak(results)
#     elif 'open youtube' in query:
#         webbrowser.open("youtube.com")
#     elif 'open google' in query:
#         webbrowser.open("google.com")
#     elif 'open gfg' in query:
#         webbrowser.open("geeksforgeeks.org")
#     elif 'who are you' in query:
#         speak("I'm Ela, your desktop voice assistant")
#     elif 'play music' in query:
#         music_dir = 'song'
#         songs = os.listdir(music_dir)
#         os.startfile(os.path.join(music_dir, songs[0]))
#     elif 'the time' in query:
#         strTime = datetime.datetime.now().strftime("%H:%M:%S")
#         speak(f"The time is {strTime}")
#     elif 'open code' in query:
#         codePath = r"C:\Users\admin\Desktop\python project\assistant.py"
#         os.startfile(codePath)
#     elif 'joke' in query:
#         speak(pyjokes.get_joke())
#     elif 'lock window' in query:
#         ctypes.windll.user32.LockWorkStation()
#     elif 'camera' in query or 'take a photo' in query:
#         ec.capture(0, "ELA Camera ", "img.jpg")
#     elif 'shutdown the system' in query:
#         speak("Are you sure you want to shutdown?")
#         shutdown = input("Do you wish to shutdown your computer? (yes/no)")
#         if shutdown == "yes":
#             os.system("shutdown /s /t 1")
#     elif 'write a note' in query:
#         speak("What should I write?")
#         note = process_speech()
#         file = open('Note.txt', 'w')
#         speak("Should I include date and time?")
#         snfm = process_speech()
#         if 'yes' in snfm or 'sure' in snfm:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             file.write(strTime + " :- " + note)
#         else:
#             file.write(note)
#     elif 'show notes' in query:
#         speak("Showing Notes")
#         file = open("Note.txt", "r")
#         speak(file.read())
#     elif 'how are you' in query:
#         speak("I'm fine, glad you asked")
#     elif 'bye' in query or 'stop' in query:
#         hour = int(datetime.datetime.now().hour)
#         if hour >= 21 or hour < 6:
#             speak("Good night, take care!")
#         else:
#             speak('Have a good day!')
#         exit()
#     return render(request, 'results.html', {'query': 'Task performed successfully'})
