import speech_recognition as sr
import pyttsx3
import webbrowser
import music_library

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")

    elif "facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")

    elif "youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")

    elif c.lower().startswith("play music"):
        song = c.lower().split(" ")[1]  # ✅ only fixed this line
        link = music_library.music[song]
        webbrowser.open(link)

# Example usage
speak("Hello, I am Jarvis!")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    # listen for the wake up word jarvis

    while True:
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening... Please speak something")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=3, phrase_time_limit=3)

            word = r.recognize_google(audio)
            print("You said:", word)

            if "jarvis" in word.lower():
                speak("ya")
                with sr.Microphone() as source:
                    print("Jarvis activated.....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    word = r.recognize_google(audio)
                    print("Command:", word)
                    processCommand(word)

        except Exception as e:
            print("Error:", e)
