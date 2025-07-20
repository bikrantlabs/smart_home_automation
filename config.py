from typing import Dict
from enums.device_type import DeviceType


PIN_MAP: Dict[DeviceType, Dict[str, int]] = {
    DeviceType.LIGHT: {
        "first": 36,
        "second": 20,
        "third": 12
    },
    DeviceType.FAN: {
        "first": 30,
        "second": 22,
        "third": 16
    }
}