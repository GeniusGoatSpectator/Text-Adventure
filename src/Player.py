import curses
from CreateMap import CreateMap

class Player:
    __PositionX = 1
    __PositionY = 1
    __Player = "O"
    __IsRunning = True

    __ObjectMap = CreateMap()

    def Player(self):
        self.__ObjectMap