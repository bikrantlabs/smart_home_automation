import speech_recognition as recognizer
class VoiceInputService:
    def __init__(self):
        self.recognizer = recognizer.Recognizer()

    def listen(self)->str:
        with recognizer.Microphone() as source:

            self.recognizer.adjust_for_ambient_noise(source,duration=0.2)
            print("Listening...")
            audio = self.recognizer.listen(source)

            try:

                text = self.recognizer.recognize_google(audio)
                print(f"You said: ${text}")
                return text.lower()

            except recognizer.UnknownValueError:
                print("Couldn't understand audio. Please speak again...")
            except recognizer.RequestError as e:
                print(f"Speech recognition error: {e}")
        
        return ""