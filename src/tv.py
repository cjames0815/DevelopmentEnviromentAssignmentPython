class tv:
    def __init__(self,channel, volume, on):
        try:
            if(channel < 1 or channel > 120):
                raise ValueError("Channel must be between 1 and 120")
        except ValueError as e:
            exit(e)
        else:
            self._channel = channel

        try:
            if(volume < 1 or volume > 7):
                raise ValueError("volume must be between 1 and 7")
        except ValueError as e:
            exit(e)
        else:
            self._volume = volume

        try:
            if(on != True and on != False):
                raise ValueError("On must be true or false")
        except ValueError as e:
            exit(e)
        else:
            self._on = on

    def setChannel(self, channel):
        if(self._on and channel >= 1 and channel <= 120):
            self._channel = channel


    def setVolume(self, volume):
        if(self._on and volume >= 1 and volume <= 120):
            self._volume = volume

    def turnOn(self):
        self._on = True

    def turnOff(self):
        self._on = False

    def channelUp(self):
        if (self._on and self._channel < 120):
            self._channel += 1

    def volumeUp(self):
        if (self._on and self._volume < 7):
            self._volume += 1

    def channelDown(self):
        if (self._on and self._channel > 1):
            self._channel -= 1

    def volumeDown(self):
        if (self._on and self._volume < 1):
            self._volume -= 1

    def _str_(self):
        return f"TV channel ={self.channel} volume={self.volume} on={self._on}"