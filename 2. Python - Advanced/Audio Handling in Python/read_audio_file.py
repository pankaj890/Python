import speech_recognition as sr

r = sr.Recognizer()

audio = 'C:/Users/Pankaj Goyal/git/Python/Python Advanced/audio.wav'

with sr.AudioFile(audio) as source:
    print("Speak Anything : ")
    audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))

    except Exception as e:
        print("Sorry, could not recognize your voice")
        print(e)
