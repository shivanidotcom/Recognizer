import pyttsx3
import speech_recognition as sr

def getVoice():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something..!")
        audio = r.listen(source)
        print("done !\n")
    try:
        text = r.recognize_google(audio)
        print("you said"+ text)
    except Exception as e:
        print(e)

getVoice();