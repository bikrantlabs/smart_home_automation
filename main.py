import sounddevice
from core.command_handler import CommandHandler
from core.command_parser import CommandParser
from devices import Light, Fan

from services.voice_input_service import VoiceInputService
def main():
    devices = {
        "light":Light(pin=10),
        "fan": Fan(pin=28)
    }

    voice_service = VoiceInputService()
    parser = CommandParser()
    handler = CommandHandler(devices)
    print("Smart Home Voice Control Started")

    while True:
        text = voice_service.listen()
        if not text:
            continue

        commands = parser.parse(text)

        for command in commands:
            handler.execute(command)

if __name__ == "__main__":
    main()