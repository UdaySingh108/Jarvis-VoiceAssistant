# Jarvis-VoiceAssistant
A Voice Assistant application named Jarvis with integrated Gemini-AI

Jarvis is a Python-based voice assistant designed to help automate tasks using voice commands. It uses Speech Recognition for understanding commands and Text-to-Speech (TTS) for providing voice responses. Additionally, it integrates APIs to fetch real-time information such as the latest news and can perform common web-based tasks like opening websites.
Features
Voice Recognition: Understands user commands using the SpeechRecognition library.
Text-to-Speech: Provides verbal responses using the pyttsx3 library.
Web Automation: Opens popular websites like Google, Facebook, YouTube, and LinkedIn with voice commands.
Music Playback: Plays specific songs from a predefined music library.
Fetches Latest News: Retrieves the latest news headlines using the NewsAPI.
AI-Generated Responses: Uses Generative AI to answer questions in less than 100 words.

To run Jarvis, you'll need to install the following Python packages:

speechrecognition
pyttsx3
requests
webbrowser
musiclibrary
google-generativeai

****
Known Issues
Wake Word Recognition: Jarvis sometimes has trouble accurately detecting the wake word. You may need to repeat the wake word "Jarvis" a few times.
Response Time: In some cases, responses may be slow due to API response time or internet speed.

****

Future Improvements
Enhancing the wake word detection system for better accuracy.
Optimizing the AI response time and improving response efficiency.
Adding more functionality like weather updates, calendar integration, etc.
License
