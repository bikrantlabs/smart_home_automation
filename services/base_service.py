from utils.logger import Logger
import threading
from abc import ABC, abstractmethod

class BaseService(ABC):
    def __init__(self):
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.logger = Logger(self.__class__.__name__)

    def start(self):
        self.thread.start()

    @abstractmethod
    def run(self):
        """Override this to implement service logic"""
        pass
