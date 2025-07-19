"""
    After receiving the parsed command:DeviceCommand, it performs actions based on the command
"""
from typing import Dict
from devices.base_device import Device
from enums.device_command import DeviceCommand
class CommandHandler:
    def __init__(self, devices:Dict[str, Device]):
        """
        devices: dictionary with keys like "light", "fan" mapped to device instances.
        Example:
            {
                "light": Light(pin=17),
                "fan": Fan(pin=18)
            }
        """
        self.devices = devices
    
    def execute(self, command:DeviceCommand):
        if command == DeviceCommand.LIGHT_ON:
            self.devices["light"].turn_on()
            self._print_status("light") 
        if command == DeviceCommand.LIGHT_OFF:
            self.devices["light"].turn_off()
            self._print_status("light")
        
        if command == DeviceCommand.FAN_ON:
            self.devices["fan"].turn_on()
            self._print_status("fan")
        
        if command == DeviceCommand.FAN_OFF:
            self.devices["fan"].turn_off()
            self._print_status("fan")
        
        if command == DeviceCommand.LIGHT_STATUS:
            self._print_status("light")
        
        if command == DeviceCommand.FAN_STATUS:
            self._print_status("fan")

        if command == DeviceCommand.UNKNOWN:
            print(f"Unknown Command {command}")
    
    def _print_status(self, device:str):
        print(f"${device.capitalize()} status: {self.devices[device].get_status()}")