from dotenv import load_dotenv
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import google.generativeai as genai
import os


# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
load_dotenv()
newsapi_key = os.getenv('NEWSAPI_KEY')
gemini_key=os.getenv('GEMENI_KEY')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    genai.configure(api_key=gemini_key)

    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = "Please  give answer in less than 100 words"

    response = model.generate_content(command+prompt)
    return response.text.strip().replace("*", "").replace("#", "").replace("\n", " ")

def processCommand(c):
    print(c)  # Debugging print statement
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "play" in c.lower():
        song = c.lower().split(" ")[1]
        link = musiclibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't have the song {song} in the library.")
    elif "news" in c.lower():  # Now checks if "news" is anywhere in the sentence
        try:
            url = (f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}")
            response = requests.get(url)
            print(response.json)

            if response.status_code == 200:
                
                news_data = response.json()
                articles = news_data.get("articles", [])
                print(f"Articles fetched: {len(articles)}")

                if articles:
                    for article in articles[:5]:  # Limiting to 5 articles
                        print(f"Article Title: {article['title']}")
                        speak(article['title'])
                else:
                    speak("No news articles found.")
                    print("No news articles found in the response.")
            else:
                print(f"Failed to fetch news, status code: {response.status_code}")
                speak("Sorry, I couldn't fetch the news at this moment.")

        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, something went wrong while fetching the news.")
    else:
        output = aiProcess(c)
        print(f"AI Output: {output}")  # Debugging print statement
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    # Calibrate the recognizer to handle ambient noise
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Calibrated for ambient noise.")

    print("Listening continuously for wake word 'Jarvis'...")

    # Keep the microphone active and listen continuously
    with sr.Microphone() as source:
        while True:
            try:
                # Listen for the wake word continuously
                print("Listening for wake word...")  # Debugging print statement
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=8)
                word = recognizer.recognize_google(audio)
                print(f"Wake word detected: {word}")  # Debugging print statement

                if word.lower() == "jarvis":
                    speak("Yes?")
                    print("Wake word recognized, listening for command...")  # Debugging print statement
                    # Now listen for the command
                    audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)
                    c = recognizer.recognize_google(audio)
                    print(f"Command heard: {c}")  # Debugging print statement
                    processCommand(c)

            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")