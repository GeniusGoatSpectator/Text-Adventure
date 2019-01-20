import curses
from CreateMap import CreateMap

class Player:
    __PositionX = 1
    __PositionY = 1
    __Player = "O"
    __IsRunning = True

    __ObjectMap = CreateMap()

    __stdscr = curses.initscr()

    def __print_player(self):
        self.__stdscr.addstr(self.__PositionY , self.__PositionX , self.__Player)

    def player(self):
        self.__ObjectMap.create_map()
        self.__print_player()

        while self.__IsRunning:
            InputKey = self.__stdscr.getch()

            if InputKey == ord("w"):
                self.__PositionY -= 1

                if self.__PositionY == 0:
                    self.__PositionY += 1

                self.__stdscr.refresh()
                self.__ObjectMap.create_map()
                self.__print_player()

            if InputKey == ord("s"):
                self.__PositionY += 1

                if self.__PositionY == 9:
                    self.__PositionY -= 1

                self.__stdscr.refresh()
                self.__ObjectMap.create_map()
                self.__print_player()

            if InputKey == ord("a"):
                self.__PositionX -= 1

                if self.__PositionX == 0:
                    self.__PositionX += 1

                self.__stdscr.refresh()
                self.__ObjectMap.create_map()
                self.__print_player()

            if InputKey == ord("d"):
                self.__PositionX += 1
                
                if self.__PositionX == 19:
                    self.__PositionX -= 1

                self.__stdscr.refresh()
                self.__ObjectMap.create_map()
                self.__print_player()
                