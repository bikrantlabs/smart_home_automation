# devices/light.py
from .base_device import Device

class Light(Device):
    def __init__(self, pin: int):
        super().__init__(pin=pin, device_type="Light")
