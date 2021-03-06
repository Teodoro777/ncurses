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
        stdscr.addstr(random.randrange(0, rows), random.randrange(0, cols), chr(c), curses.A_UNDERLINE)
    elif attr ==  1:
        stdscr.addstr(random.randrange(0, rows), random.randrange(0, cols), chr(c), curses.A_BOLD)
    elif attr == 2:
        stdscr.addstr(random.randrange(0, rows), random.randrange(0, cols), chr(c), curses.A_STANDOUT)

def mad_stampa_carattere_ciclo(stdscr):
    c = stdscr.getch()
    while c != curses.KEY_F2:
        mad_stampa_carattere(stdscr, c)
        c = stdscr.getch() 

def mad_end(stdscr):
    stdscr.refresh()
    curses.endwin()
