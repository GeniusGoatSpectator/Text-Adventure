import curses
from Player import Player

def main():
    ObjectPayer = Player()
    ObjectPayer.player()

if __name__ == "__main__":
    stdsrc = curses.initscr()
    main()
    curses.endwin()