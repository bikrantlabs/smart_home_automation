from services.base_service import BaseService
import speech_recognition as recognizer
from core.command_parser import CommandParser
from core.command_handler import CommandHandler

class VoiceService(BaseService):
    def __init__(self, parser: CommandParser, handler: CommandHandler):
        super().__init__()
        self.recognizer = recognizer.Recognizer()
        self.parser = parser
        self.handler = handler

    def run(self):
        mic = recognizer.Microphone()
        while True:
            with mic as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                self.logger.info("Listening...")
                audio = self.recognizer.listen(source)

                try:
                    text = self.recognizer.recognize_google(audio)
                    self.logger.user(f"You said: {text.capitalize()}")

                    commands = self.parser.parse(text.lower())
                    for command in commands:
                        self.handler.execute(command)

                except recognizer.UnknownValueError:
                    self.logger.warning("Couldn't understand. Try again.")
                except recognizer.RequestError as e:
                    self.logger.error(f"Recognition error: {e}")
