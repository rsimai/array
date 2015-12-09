#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# rsimai@suse.com

import time
import os

# dimensions
rows = 15
cols = 45

ship = 'X'
noship = '.'
fillup = 1.3
fillrows = 5

# rotate 1 is right, -1 is left
rotate = 1

z=[]

# output in cols x rows
def printout():
    for a in range(0,rows):
        #print a,
        out = ''
        for b in range(0,cols):
            out += z[((cols)*a+b)]
        print out
        
# create a list
def create():
    for a in range(0,rows):
        for b in range(0,cols):
            #print a,b
            if (a < fillrows) and (b/fillup == int(b/fillup)):
                z.append(ship)
            else:
                z.append(noship)


def check_out():
    for a in range(0,rows):
        pos1 = a*cols+cols-1
        pos2 = a*cols
        #print pos2, pos1
        if ((z[pos1] == ship) and (rotate == 1)) or ((z[pos2] == ship) and (rotate == -1)):
            #print "add a line"
            global rotate
            rotate = rotate * -1
            add_line()
            return
    if rotate == 1:
        move_right()
    else:
        move_left()

def move_right():
    global z
    z.insert(0,noship)
    z.pop(rows*cols-1)

def move_left():
    global z
    z.pop(0)
    z.append(noship)

def add_line():
    #print "add line"
    for a in range(0,cols):
        global z
        z.insert(0,noship)

# main
create()

for i in range(0,50):
    os.system('clear')
    printout()
    check_out()
    time.sleep(0.3)
    #print rotate
