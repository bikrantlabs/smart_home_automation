from devices.base_device import Device

class Fan(Device):

    def __init__(self, pin:int):
        super().__init__()
        self.pin = pin
        self._setup_gpio()
    
    def _setup_gpio(self):
        # TODO: Setup GPIO Pin
        pass

    def turn_on(self):
        
        # TODO: Set: GPIO.outpu(self.pin,HIGH)
        print("Fan turned ON")
        self.status = "ON"


    def turn_off(self):
        # TODO: Set: GPIO.outpu(self.pin,LOW)
        print("Fan turned OFF")
        self.status = "OFF"

    def get_status(self):
        return self.status