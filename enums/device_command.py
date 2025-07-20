from enum import Enum, auto

class DeviceCommand(Enum):
    TURN_ON = auto()
    TURN_OFF = auto()
    STATUS = auto()
    UNKNOWN = auto()