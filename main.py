import sounddevice
from core.command_handler import CommandHandler
from core.command_parser import CommandParser
from services.device_registry import DeviceRegistry
from services.voice_input_service import VoiceInputService
from config import PIN_MAP

def main():
    # Initialize devices registry with pin as key and device instance as value
    devices = DeviceRegistry.create_devices()

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
