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
rows = 20
cols = 37

# defender starts at cols/2
dcol = cols / 2

# characters to be used
ship = 'X'
noship = '.'
defender = 'U'
shot = '|'
bang = 'O'

# keys to be used
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

# the shots underway
s=[]

# printout matrix
m=[]

char = 'q'
shipcount = 0
scount = 0
slist = []

# get/save the terminal settings
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# new terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

# switch to normal terminal on exit
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
    check_hits()
    os.system('clear')
    for a in range(0,rows):
        out = ''
        for b in range(0,cols):
            out += m[((cols)*a+b)]
        print out
    print_defender()
    print shipcount

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
    y.insert(dcol, defender)
    
# create the matrix, ships and shots
def create_matrix():
    global shipcount
    global m
    global s
    for a in range(0,rows):
        for b in range(0,cols):
            if (a < fillrows) and (b/fillup == int(b/fillup)):
                z.append(ship)
                shipcount += 1
            else:
                z.append(noship)
            s.append(' ')
            m = s

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
        global dcol
        dcol -= 1

def defender_right():
    if y[cols-1] == defender:
        return
    else:
        y.insert(0, ' ')
        y.pop(cols)
        global dcol
        dcol += 1

def trigger_shot():
    s[(rows-1)*cols+dcol] = shot
 
def shots_up():
    for i in range(0,cols):
        s.pop(0)
        s.append(' ')

# check hits and merge for printout
def check_hits():
    global shipcount
    for i in range(0,cols*rows):
        if s[i] == shot and z[i] == ship:
            s[i] = ' '
            z[i] = noship
            m[i] = bang
            shipcount -= 1
        elif s[i] == shot:
            m[i] = shot
        else:
            m[i] = z[i]


# check end
def check_end():
    if z[cols*rows-1] == ship:
        print "Game over!"
        exit(0)
    if shipcount == 0:
        print "Well done!"
        exit(0)

# main

# prepare the terminal for keyboard input
atexit.register(set_normal_term)
set_curses_term()

# create the board
create_defender()
create_matrix()

# play loop
while True:
    # printing/checking
    check_out()
    shots_up()
    printout()
    for w in range(0,10):
        kbhit()
        if char:
            if char == lkey:
                defender_left()
                printout()
            if char == rkey:
                defender_right()
                printout()
            if char == skey:
                trigger_shot()
        
        time.sleep(0.04)
    check_end()
