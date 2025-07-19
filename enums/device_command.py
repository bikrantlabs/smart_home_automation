from enum import Enum, auto

class DeviceCommand(Enum):
    LIGHT_ON = auto()
    LIGHT_OFF = auto()
    FAN_ON = auto()
    FAN_OFF = auto()
    UNKNOWN = auto()
    FAN_STATUS = auto()
    LIGHT_STATUS = auto()