# devices/fan.py
from .base_device import Device

class Fan(Device):
    def __init__(self, pin: int):
        super().__init__(pin=pin, device_type="Fan")
