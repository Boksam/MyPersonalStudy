class Setup:
    def __init__(self):
        self._delta = 0.01
        self._alpha = 0.01
        self._dx = 10 ** (-4)

    def getDelta(self):
        return self._delta
    
    def getAlpha(self):
        return self._alpha
    
    def getDx(self):
        return self._dx