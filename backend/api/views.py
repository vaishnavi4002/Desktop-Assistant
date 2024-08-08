from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Query
from .serializers import QuerySerializer
import speech_recognition as sr
import pyttsx3
import wikipediaapi
import webbrowser
import datetime
import os
import pyjokes
import ctypes
from ecapture import ecapture as ec
from django.http import HttpResponse, JsonResponse
@api_view(['POST'])
def process_speech(request):
    query_text = request.data.get('query', None)
    if not query_text:
        query_text = process_speech_logic()
    
    perform_task_logic(query_text)
    
    # Save the query to the database
    Query.objects.create(query_text=query_text)
    
    return Response({"query": query_text})

@api_view(['GET'])
def get_query_history(request):
    queries = Query.objects.all().order_by('-created_at')  # Get all queries ordered by creation date
    serializer = QuerySerializer(queries, many=True)
    return Response(serializer.data)
def get_notes(request):
    file_path = 'backend/Note.txt'
    
    if not os.path.exists(file_path):
        return JsonResponse({'error': 'No notes found'}, status=404)

    with open(file_path, 'r') as file:
        notes_content = file.read()

    return HttpResponse(notes_content, content_type='text/plain')

def process_speech_logic():
    speak('yes')
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        return query
    except Exception as e:
        return "None"

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def perform_task_logic(query):
    query = query.lower()
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipediaapi.Wikipedia('en').summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open gfg' in query:
        webbrowser.open("geeksforgeeks.org")
    elif 'who are you' in query:
        speak("I'm Ela. Your desktop voice assistant")
    elif 'play music' in query:
        music_dir = 'song'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'open code' in query:
        codePath = r"C:\Users\admin\Desktop\python project\assistant.py"
        os.startfile(codePath)
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    elif "who made you" in query or "who created you" in query:
        speak("I have been created by Vaishnavi, and Arati.")
    elif 'lock window' in query:
        ctypes.windll.user32.LockWorkStation()
    elif "camera" in query or "take a photo" in query:
        ec.capture(0, "ELA Camera ", "img.jpg")
    elif "shutdown the system" in query:
        speak("Are you sure you want to shutdown?")
        # Shutdown logic can be implemented here
    elif "write a note" in query:
        speak("What should I write, sir")
        note = process_speech_logic()
        with open('Note.txt', 'w') as file:
            speak("Sir, should I include date and time?")
            snfm = process_speech_logic()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime + " :- " + note)
            else:
                file.write(note)
    elif "show notes" in query:
        speak("Showing Notes")
        with open("Note.txt", "r") as file:
            speak(file.read())
    elif "how are you" in query:
        speak("I'm fine, glad you asked.")
    elif 'bye' in query or 'stop' in query:
        hour = int(datetime.datetime.now().hour)
        if hour >= 21 and hour < 6:
            speak("Good night, take care!")
        else:
            speak('Have a good day!')
