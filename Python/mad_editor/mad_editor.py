import random
import curses

def mad_init():
    stdscr = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)
    return stdscr

def mad_stampa_intestazione(stdscr):
    stdscr.addstr(4, 4, "Questo e' un editor di testi matto\n    (Premi F2 per terminare)")

def mad_stampa_carattere(stdscr, c):
    (rows, cols) = stdscr.getmaxyx()
    attr = random.randrange(0, 3)
  
    if attr == 0:
        stdscr.attron(A_UNDERLINE)
        stdscr.addstr(random.randrange(0, rows), random.randrange(0, cols), chr(c))
        stdscr.attroff(A_UNDERLINE)
    elif attr ==  1:
        stdscr.attron(A_BOLD)
        stdscr.addstr(random.randrange(0, rows), random.randrange(0, cols), chr(c))
        stdscr.attroff(A_BOLD)
    elif attr == 2:
        stdscr.attron(A_STANDOUT)
        stdscr.addstr(random.randrange(0, rows), random.randrange(0, cols), chr(c))
        stdscr.attroff(A_STANDOUT)

def mad_stampa_carattere_ciclo(stdscr):
    c = stdscr.getch()
    while c != stdscr.KEY_F(2):
        c = stdsrc.getch()
        mad_stampa_carattere(stdscr, c)
    
def mad_end(stdscr):
    stdscr.refresh()
    stdscr.getch()
    stdscr.endwin()
