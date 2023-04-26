class Tv():
    def __init__(self):
        self.setCanal(0)
        self.volume = 0

    def setCanal(self, canal):
        if (canal > 0) and (canal <= 100):
            self.canal = canal 

    def aumentarVolume(self):
        if (self.volume < 100):
            self.volume += 1

    def diminuirVolume(self):
        if (self.volume > 0):
            self.volume -= 1

tv = Tv() 
print(vars(tv))
tv.setCanal(56)
print(vars(tv))
tv.aumentarVolume()
print(vars(tv))
tv.diminuirVolume()
print(vars(tv))