import curses

class CreateMap:
    
    def CreateMap(self):
        stdsrc = curses.initscr()

        stdsrc.addstr(0 , 0 , "####################")
        for i in range(8):
            stdsrc.addstr(i , 0 , "#                   #")
        stdsrc.addstr(10 , 0 , "####################")

        curses.endwin()