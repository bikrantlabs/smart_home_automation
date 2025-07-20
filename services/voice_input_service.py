from services.base_service import BaseService
import speech_recognition as recognizer


class VoiceService(BaseService):
    def __init__(self, parser, handler):
        super().__init__()
        self.recognizer = recognizer.Recognizer()
        self.parser = parser
        self.handler = handler
        self.wake_word = "alexa"

    def run(self):
        mic = recognizer.Microphone()
        while True:
            with mic as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                self.logger.info("Listening for wake word...")
                audio = self.recognizer.listen(source)

                try:
                    text = self.recognizer.recognize_google(audio).lower()
                    if self.wake_word in text:
                        self.logger.info("Wake word detected! Listening for command...")
                        # Now listen for the actual command
                        audio_cmd = self.recognizer.listen(source)
                        command_text = self.recognizer.recognize_google(audio_cmd).lower()
                        self.logger.user(f"Command: {command_text}")

                        commands = self.parser.parse(command_text)
                        for command in commands:
                            self.handler.execute(command)

                except recognizer.UnknownValueError:
                    self.logger.warn("Didn't catch that.")
                except recognizer.RequestError as e:
                    self.logger.error(f"Speech API error: {e}")
