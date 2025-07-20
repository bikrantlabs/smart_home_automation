# services/device_registry.py
from typing import Dict
from config import PIN_MAP
from devices.base_device import Device
from devices.light import Light
from devices.fan import Fan
from enums.device_type import DeviceType


class DeviceRegistry:
    @staticmethod
    def create_devices() -> Dict[int, Device]:
        device_registry: Dict[int, Device] = {}

        for device_type, floor_pins in PIN_MAP.items():
            for floor, pin in floor_pins.items():
                if device_type == DeviceType.LIGHT:
                    device_registry[pin] = Light(pin=pin)
                elif device_type == DeviceType.FAN:
                    device_registry[pin] = Fan(pin=pin)

        return device_registry