from typing import Dict
from devices.base_device import Device
from enums.device_command import DeviceCommand
from enums.device_type import DeviceType
from config import PIN_MAP
from .command_parser import ParsedCommand

class CommandHandler:
    def __init__(self, device_registry: Dict[int, Device]):
        self.device_registry = device_registry

    def execute(self, command: ParsedCommand):
        pin = PIN_MAP.get(command.device_type, {}).get(command.floor)

        if pin is None:
            print(f"No {command.device_type.name} found on {command.floor} floor.")
            return

        device = self.device_registry.get(pin)

        if not device:
            print(f"No device registered on pin {pin}")
            return

        match command.action:
            case DeviceCommand.TURN_ON:
                device.turn_on()
            case DeviceCommand.TURN_OFF:
                device.turn_off()
            case DeviceCommand.STATUS:
                print(f"{command.device_type.name.capitalize()} status at {command.floor}: {device.get_status()}")
            case _:
                print(f"Unknown command: {command}")

