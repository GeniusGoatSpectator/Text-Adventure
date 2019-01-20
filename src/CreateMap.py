import curses

class CreateMap:
    
    def create_map(self):
        stdsrc = curses.initscr()

        stdsrc.addstr(0 , 0 , "####################")
        for i in range(1 , 9):
            stdsrc.addstr(i , 0 , "#                  #")
        stdsrc.addstr(9 , 0 , "####################")
