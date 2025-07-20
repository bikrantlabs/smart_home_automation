import pyttsx3
from services.base_service import BaseService
import threading
import queue
from gtts import gTTS
import pygame
import tempfile
import time

class AsyncTextToSpeech:
    def __init__(self):
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()

        pygame.mixer.init()

    def _run(self):
        while True:
            text = self.queue.get()
            if text is None:
                break
            self._speak(text)

    def _speak(self, text: str):
        try:
            tts = gTTS(text, lang='en', slow=False)
            with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
                tts.save(fp.name)
                pygame.mixer.music.load(fp.name)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
        except Exception as e:
            print(f"[TTS Error] {e}")

    def speak(self, text: str):
        self.queue.put(text)

    def stop(self):
        self.queue.put(None)
        self.thread.join()
