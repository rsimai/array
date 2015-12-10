#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# rsimai@suse.com

import atexit
from select import select
import sys
import termios
import time


# save the terminal settings
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# new terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

# switch to normal terminal
def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

# switch to unbuffered terminal
def set_curses_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

def kbhit():
    dr, dw, de = select([sys.stdin], [], [], 0)
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    return dr != []

atexit.register(set_normal_term)
set_curses_term()
for i in range(10):
    print 'Did you pressed any key? ...', kbhit()
    time.sleep(1)

