class Termite:

    def __init__(self, posicion=(0, 0), color="red"):
        self.last_postion = posicion
        self.posicion = posicion
        self.color = color
        self.load = None

    def getPos(self):
        return self.posicion
    
    def getLastPos(self):
        return self.last_postion
    
    def setLastPos(self, lastPos):
        self.last_postion = lastPos
    
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setLoad(self, load):
        self.load = load

    def getLoad(self):
        return self.load

    def moveUp(self, interval=1):
        self.posicion = (self.posicion[0], self.posicion[1] + interval)

    def moveDown(self, interval=1):
        self.posicion = (self.posicion[0], self.posicion[1] - interval)

    def moveRight(self, interval=1):
        self.posicion = (self.posicion[0] + interval, self.posicion[1])

    def moveLeft(self, interval=1):
        self.posicion = (self.posicion[0] - interval, self.posicion[1])

    def move(self, r, limits, interval=1):
        self.last_postion = self.posicion
        mov = r.randint(0, 3)
        if mov == 0:
            if self.posicion[1] < limits[1]:
                self.moveUp(interval)
        elif mov == 1:
            if self.posicion[1] > limits[0]:
                self.moveDown(interval)
        elif mov == 2:
            if self.posicion[0] > limits[2]:
                self.moveLeft(interval)
        elif mov == 3:
            if self.posicion[0] < limits[3]:
                self.moveRight(interval)

    def pickChip(self, Chips, posChips):
        if self.getPos() in posChips and not Chips[posChips[self.getPos()]].getLoaded():
            Chips[posChips[self.getPos()]].setLoaded(True)
            self.setLoad(posChips[self.getPos()])
            return self.getPos()

    def dropChip(self, Chips, posChips, auxPos):
        if self.getPos() not in posChips and not Chips[posChips[auxPos]].getLoaded():
            Chips[self.getLoad()].setLoaded(False)
            Chips[self.getLoad()].posicion = self.getPos()
            self.setLoad(None)
            return self.getPos()
                
class Chip:

    def __init__(self, index, posicion=(0, 0), color="blue"):
        self.posicion = posicion
        self.color = color
        self.index = index
        self.loaded = False

    def getLoaded(self):
        return self.loaded
    
    def setLoaded(self, status):
        self.loaded = status

    def getPos(self):
        return self.posicion

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color