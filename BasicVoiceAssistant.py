
import speech_recognition as sr 
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens for user's voice input and converts it to text"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=3
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-US')
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None

def tell_time():
    """Tells the current time"""
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def tell_date():
    """Tells the current date"""
    today = datetime.date.today()
    current_date = today.strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")

def search_web(query):
    """Searches the web based on user query"""
    speak("Searching the web for you")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def main():
    """Main function to run the voice assistant"""
    speak("Hello, how can I help you today?")
    while True:
        query = listen()
        if query:
            if "hello" in query:
                speak("Hello! How can I assist you?")
            elif "time" in query:
                tell_time()
            elif "date" in query:
                tell_date()
            elif "search for" in query:
                search_query = query.replace("search for", "")
                search_web(search_query)
            elif "exit" in query or "quit" in query:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I didn't catch that. Please try again.")

if __name__ == "__main__":
    main()
