# services/water_level_monitor.py
import time

from services.base_service import BaseService

class WaterLevelMonitorService(BaseService):
    def __init__(self):
        super().__init__()
        self.daemon = True  # Optional: stops with main thread

    def run(self):
        # while True:
            # logic to check water level and activate motor
            self.logger.system("Checking water level...")
            time.sleep(5)  # Delay or wait for sensor input
            self.logger.system("Water level detected...")
