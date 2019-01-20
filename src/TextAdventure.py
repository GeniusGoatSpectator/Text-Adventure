import curses
from CreateMap import CreateMap

def main():
    ObjectMap = CreateMap()
    ObjectMap.CreateMap()

if __name__ == "__main__":
    stdsrc = curses.initscr()
    main()
    stdsrc.getch()
    curses.endwin()