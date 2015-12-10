#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# rsimai@suse.com

import time
import os

# dimensions
rows = 10
cols = 45

# characters to be used
ship = 'X'
noship = '.'
defender = 'U'
shot = '|'

# automatic fill up
fillup = 1.3
fillrows = 5

# rotate 1 is right, -1 is left
rotate = 1

# the matrix
z=[]

# the defender
y=[]


# output in cols x rows
def printout():
    for a in range(0,rows):
        #print a,
        out = ''
        for b in range(0,cols):
            out += z[((cols)*a+b)]
        print out
    
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

# check end
def check_end():
    if z[cols*rows-1] == ship:
        print "Game over!"
        exit(0)

# main

# prepare
create_defender()
create_matrix()

# play loop
for i in range(0,90):
    # printing/checking
    os.system('clear')
    check_out()
    printout()
    print_defender()
    check_end()

    # waiting
    time.sleep(0.1)
