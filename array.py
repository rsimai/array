#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# rsimai@suse.com
# Hackweek 13, learning Python

import time
import os
import sys
import atexit
import termios
from select import select


# dimensions
rows = 25
cols = 50

# defender starts at cols/2
dcol = cols / 2

# characters to be used
ship = 'X'
noship = ' '
defender = 'U'
nodefender = '_'
shot = '|'
bang = 'O'

# keys to be used
lkey = 'a'
rkey = 's'
skey = ' '

# automatic fill up
fillup = 1.7
fillrows = 5
blocks = 2

# rotate 1 is right, -1 is left
rotate = 1

# the matrix
<<<<<<< HEAD
z = []

# the defender
y = []

# the shots underway
s = []

# printout matrix
m = []
=======
z=[]

# the defender
y=[]

# the shots underway
s=[]

# printout matrix
m=[]
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4

char = 'q'
shipcount = 0
shotcount = 0
slist = []

# get/save the terminal settings
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# new terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

<<<<<<< HEAD

=======
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
# switch to normal terminal on exit
def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

<<<<<<< HEAD

=======
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
# switch to unbuffered terminal
def set_curses_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

<<<<<<< HEAD

=======
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
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

<<<<<<< HEAD

=======
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
# output in cols x rows
def printout():
    check_hits()
    os.system('clear')
<<<<<<< HEAD
    for a in range(0, rows):
        out = ''
        for b in range(0, cols):
=======
    for a in range(0,rows):
        out = ''
        for b in range(0,cols):
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
            out += m[((cols)*a+b)]
        print out
    print_defender()
    print "Shots:", shotcount, "Ships left:", shipcount, "of", shipcountorig
    print "Left: \"" + lkey + "\"", " Right: \"" + rkey + "\"", " Fire: \"" + skey + "\""

<<<<<<< HEAD

# print defender base line
def print_defender():
    out = ''
    for b in range(0, cols):
        out += y[b]
    print out


# create the defender base line
def create_defender():
    for a in range(0, cols-1):
        y.append(nodefender)
    y.insert(dcol, defender)


=======
# print defender base line
def print_defender():
    out = ''
    for b in range(0,cols):
        out += y[b]
    print out

# create the defender base line
def create_defender():
    for a in range(0,cols-1):
        y.append(nodefender)
    y.insert(dcol, defender)
    
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
# create the matrix, ships and shots
def create_matrix():
    global shipcount
    global m
    global s
<<<<<<< HEAD
    for a in range(0, rows):
        for b in range(0, cols):
=======
    for a in range(0,rows):
        for b in range(0,cols):
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
            if (a < fillrows) and (b/fillup == int(b/fillup)):
                z.append(ship)
                shipcount += 1
            else:
                z.append(noship)
            s.append(' ')
            m = s
            global shipcountorig
            shipcountorig = shipcount

<<<<<<< HEAD

# check if left or right has been reached, add a line and change direction
def check_out():
    for a in range(0, rows):
=======
# check if left or right has been reached, add a line and change direction
def check_out():
    for a in range(0,rows):
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
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

<<<<<<< HEAD

# step to the right
def move_right():
    global z
    z.insert(0, noship)
    z.pop(rows*cols-1)


=======
# step to the right
def move_right():
    global z
    z.insert(0,noship)
    z.pop(rows*cols-1)

>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
# step to the left
def move_left():
    global z
    z.pop(0)
    z.append(noship)

<<<<<<< HEAD

# move down by one line
def move_down():
    for a in range(0, cols):
        global z
        z.insert(0, noship)
        z.pop(cols*rows)


=======
# move down by one line
def move_down():
    for a in range(0,cols):
        global z
        z.insert(0,noship)
        z.pop(cols*rows)

>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
def defender_left():
    if y[0] == defender:
        return
    else:
        y.pop(0)
        y.append(nodefender)
        global dcol
        dcol -= 1

<<<<<<< HEAD

=======
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
def defender_right():
    if y[cols-1] == defender:
        return
    else:
        y.insert(0, nodefender)
        y.pop(cols)
        global dcol
        dcol += 1

<<<<<<< HEAD

=======
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
def trigger_shot():
    s[(rows-1)*cols+dcol] = shot
    global shotcount
    shotcount += 1
<<<<<<< HEAD


def shots_up():
    for i in range(0, cols):
        s.pop(0)
        s.append(' ')


# check hits and merge for printout
def check_hits():
    global shipcount
    for i in range(0, cols*rows):
=======
 
def shots_up():
    for i in range(0,cols):
        s.pop(0)
        s.append(' ')

# check hits and merge for printout
def check_hits():
    global shipcount
    for i in range(0,cols*rows):
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
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
<<<<<<< HEAD
    for i in range(0, cols):
=======
    for i in range(0,cols):
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
        if z[(rows-1)*cols+i] == ship:
            print
            print "Game over! You missed", shipcount, "ship(s)!"
            print
            exit(0)
    if shipcount == 0:
        print
        print "Well done!"
        print
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
<<<<<<< HEAD
    for w in range(0, 12):
=======
    for w in range(0,15):
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
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
<<<<<<< HEAD

        time.sleep(0.005)
=======
        
        time.sleep(0.02)
>>>>>>> 46e79a7f5e0d7f5b5bcbf3bc59ec25d113d594f4
    check_end()
