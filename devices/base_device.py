from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self):
        self._status = "OFF"  # Default initial status


    @abstractmethod
    def turn_on(self):
        pass


    @abstractmethod
    def turn_on(self):
        pass


    @abstractmethod
    def get_status(self):
        pass
