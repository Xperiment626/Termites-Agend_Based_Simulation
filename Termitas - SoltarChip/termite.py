class Termite:

    def __init__(self, posicion=(0, 0), color="red"):
        self.last_postion = posicion
        self.posicion = posicion
        self.color = color
        self.load = None

    def getPos(self):
        return self.posicion
    
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
        # Checking if the current position of the Termite is in the list of position of Chips and checking if the Chip that we are on wasn't have been loaded to a Termite
        if self.getPos() in posChips and not Chips[posChips[self.getPos()]].getLoaded():
            # Changing the state of the Chip to uploaded to the Termite
            Chips[posChips[self.getPos()]].setLoaded(True)
            # Setting the index of the Chip loaded to the Termite
            self.setLoad(posChips[self.getPos()])
            # Return the current position of the Termite
            return self.getPos()

    def dropChip(self, Chips, posChips, auxPos):      
        # Here self.getPos() is the next position of the Termite because the walkTermite.py file in line 69 I'm generating movement
        if self.getPos() not in posChips and not Chips[posChips[auxPos]].getLoaded():
            # Changing the state of the Chip to downloaded from the Termite
            Chips[self.getLoad()].setLoaded(False)
            # Changing the last position of the Chip to the current(next) position of the Termite
            Chips[self.getLoad()].posicion = self.getPos()
            # Setting the load of to the Termite to None
            self.setLoad(None)
            # Return the current(next) position of the Termite
            return self.getPos()
                
class Chip:

    def __init__(self, index, posicion=(0, 0), color="blue"):
        self.posicion = posicion
        self.color = color
        self.index = index
        # Created a new attribute called 'loaded'
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