from abc import ABC, abstractmethod

from services.text_to_speech import AsyncTextToSpeech
# devices/base_device.py
class Device:
    def __init__(self, pin: int, device_type: str):
        self.pin = pin
        self.device_type = device_type
        self._status = "OFF"
        self._setup_gpio()
        self.tts = AsyncTextToSpeech()

    def _setup_gpio(self):
        # GPIO.setmode(GPIO.BOARD or GPIO.BCM)
        # GPIO.setup(self.pin, GPIO.OUT)
        pass

    def turn_on(self):
        self.tts.speak(f"{self.device_type} on pin {self.pin} turned ON")
        print(f"🟡 {self.device_type} on pin {self.pin} turned ON")
        self._status = "ON"

    def turn_off(self):
        self.tts.speak(f"{self.device_type} on pin {self.pin} turned OFF")
        print(f"⚫ {self.device_type} on pin {self.pin} turned OFF")
        self._status = "OFF"

    def get_status(self) -> str:
        return self._status
