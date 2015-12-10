#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# rsimai@suse.com

import time
import os
import sys
import atexit
import termios
from select import select


# dimensions
rows = 10
cols = 45

# characters to be used
ship = 'X'
noship = '.'
defender = 'U'
shot = '|'
lkey = 'a'
rkey = 's'
skey = ' '

# automatic fill up
fillup = 1.3
fillrows = 5

# rotate 1 is right, -1 is left
rotate = 1

# the matrix
z=[]

# the defender
y=[]

char = ' '

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

# poll the keyboard without blocking
def kbhit():
    dr, dw, de = select([sys.stdin], [], [], 0)
    if dr:
        global char
        char = sys.stdin.read(1)
    else:
        global char
        char = ''
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    return

# output in cols x rows
def printout():
    os.system('clear')
    for a in range(0,rows):
        #print a,
        out = ''
        for b in range(0,cols):
            out += z[((cols)*a+b)]
        print out
    print_defender()

# print defender base line
def print_defender():
    out = ''
    for b in range(0,cols):
        out += y[b]
    print out

# create the defender base line
def create_defender():
    for a in range(0,cols-1):
        y.append(' ')
    y.insert(cols/2,defender)
    
# create a list
def create_matrix():
    for a in range(0,rows):
        for b in range(0,cols):
            if (a < fillrows) and (b/fillup == int(b/fillup)):
                z.append(ship)
            else:
                z.append(noship)

# check if left or right has been reached, add a line and change direction
def check_out():
    for a in range(0,rows):
        pos1 = a*cols+cols-1
        pos2 = a*cols
        if ((z[pos1] == ship) and (rotate == 1)) or ((z[pos2] == ship) and (rotate == -1)):
            global rotate
            rotate = rotate * -1
            move_down()
            return
    if rotate == 1:
        move_right()
    else:
        move_left()

# step to the right
def move_right():
    global z
    z.insert(0,noship)
    z.pop(rows*cols-1)

# step to the left
def move_left():
    global z
    z.pop(0)
    z.append(noship)

# move down by one line
def move_down():
    for a in range(0,cols):
        global z
        z.insert(0,noship)
        z.pop(cols*rows)

def defender_left():
    if y[0] == defender:
        return
    else:
        y.pop(0)
        y.append(' ')

def defender_right():
    if y[cols-1] == defender:
        return
    else:
        y.insert(0, ' ')
        y.pop(cols)

def trigger_shot():
    print "not yet :-)"


# check end
def check_end():
    if z[cols*rows-1] == ship:
        print "Game over!"
        exit(0)

# main

# prepare the terminal for keyboard input
atexit.register(set_normal_term)
set_curses_term()

# create the board
create_defender()
create_matrix()

# play loop
for i in range(0,90):
    # printing/checking
    check_out()
    printout()
    for w in range(0,10):
        key = kbhit()
        if char:
            if char == lkey:
                defender_left()
                printout()
            if char == rkey:
                defender_right()
                printout()
            if char == skey:
                trigger_shot()
        time.sleep(0.05)
    check_end()
    # waiting
