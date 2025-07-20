import time
import sounddevice
from core.command_handler import CommandHandler
from core.command_parser import CommandParser
from devices.device_registry import DeviceRegistry
from services.voice_input_service import VoiceService
from config import PIN_MAP
from services.water_level_monitoring_service import WaterLevelMonitorService

def main():
    # Initialize devices registry with pin as key and device instance as value
    devices = DeviceRegistry.create_devices()

    parser = CommandParser()
    handler = CommandHandler(devices)
    print("Smart Home Voice Control Started")

    services = [
        VoiceService(parser,handler),
        WaterLevelMonitorService(),
    ]

    for service in services:
        service.start()

if __name__ == "__main__":
    main()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("! Exiting...")
