import speech_recognition as sr
import pyttsx3

def text_to_speech(sentence):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(sentence)
    engine.runAndWait()
    del engine

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        text = None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        text = None

    return text

