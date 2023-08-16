import curses
from curses import panel



def main():

    stdscr = curses.initscr()
    parent = curses.newwin(3, 0, 0, 0)
    child = curses.newwin(0, 80, 4, 0)

    stdscr.keypad(True)
    parent_panel = panel.new_panel( parent )
    child_panel = panel.new_panel( child )

    parent.box()
    child.box()

    panel.update_panels()
    curses.doupdate()

    
    testing = True
    while( testing ):
        # checks for quit
        key = stdscr.getkey()
        if key == 'q':
            testing = False    

    curses.endwin()



if __name__ == "__main__":
    main()
