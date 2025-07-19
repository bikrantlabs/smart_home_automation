import re
from enums.device_command import DeviceCommand
class CommandParser:
    def parse(self, input_text:str) -> list[DeviceCommand]:
        commands = []

        split_pattern = r"\band\b|\bthen\b|,|;|\balso\b|\bplus\b|\bas well as\b"

        parts = re.split(split_pattern, input_text, flags=re.IGNORECASE) 

        for part in parts:
            part = part.strip()
            if not part:
                continue
            
            cmd = self._parse_single_command(part)
            if cmd != DeviceCommand.UNKNOWN:
                commands.append(cmd)
        return commands

    def _parse_single_command(self, text:str)->DeviceCommand:
        text = text.lower()

        print(f"Parsing the text {text}")
        if "light" in text:
            if any(word in text for word in ["on", "activate"]):
                return DeviceCommand.LIGHT_ON
            elif any(word in text for word in ["off", "deactivate"]):
                return DeviceCommand.LIGHT_OFF
            elif any(word in text for word in ["status"]):
                return DeviceCommand.LIGHT_STATUS
        
        elif "fan" in text:
            if any(word in text for word in ["on", "activate"]):
                return DeviceCommand.FAN_ON
            elif any(word in text for word in ["off", "deactivate"]):
                return DeviceCommand.FAN_OFF
            elif any(word in text for word in ["status"]):
                return DeviceCommand.FAN_STATUS

        return DeviceCommand.UNKNOWN