import re
from enums.device_type import DeviceType
from enums.device_command import DeviceCommand

FLOORS = ["first", "second", "third"]
DEVICES = ["light", "fan"]

class ParsedCommand:
    def __init__(self, device_type: DeviceType, floor: str, action: DeviceCommand):
        self.device_type = device_type
        self.floor = floor
        self.action = action

    def __repr__(self):
        return f"<ParsedCommand {self.device_type.name} at {self.floor} -> {self.action.name}>"

class CommandParser:
    def parse(self, input_text: str) -> list[ParsedCommand]:
        commands = []
        split_pattern = r"\band\b|\bthen\b|,|;|\balso\b|\bplus\b|\bas well as\b"

        parts = re.split(split_pattern, input_text, flags=re.IGNORECASE)

        for part in parts:
            part = part.strip()
            if not part:
                continue
            command = self._parse_single_command(part)
            if command:
                commands.append(command)

        return commands

    def _parse_single_command(self, text: str) -> ParsedCommand | None:
        text = text.lower()
        floor = next((f for f in FLOORS if f in text), None)
        device = next((d for d in DEVICES if d in text), None)

        if not device or not floor:
            return None

        if "on" in text or "activate" in text:
            action = DeviceCommand.TURN_ON
        elif "off" in text or "deactivate" in text:
            action = DeviceCommand.TURN_OFF
        elif "status" in text:
            action = DeviceCommand.STATUS
        else:
            return None

        return ParsedCommand(DeviceType[device.upper()], floor, action)
