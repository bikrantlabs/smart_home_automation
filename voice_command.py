import speech_recognition as sr

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Say something...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print("You said:", text)

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        r = sr.Recognizer()
        continue

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        break
