import re
from numpy import *
def pirmas():
    main = []
    x = 0
    y = 0
    direction = 0
    locations = {}
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            line = list(line)
            main.append(line)
    i = 0
    for line in main:
        x1 = 0
        for cord in line:
            if cord == '^':
                y = i
                x = x1
                break
            x1 += 1
        i += 1
    start = y,x
    cordinate = str(x) + "," + str(y)
    locations[cordinate] = " "
    while(True):
        new_cordinate = ""
        #print (y,x)
        new_location = movement(direction,y,x,main)
        if new_location[0] == -2:
            direction +=90
            if direction == 360:
                direction = 0
            continue
        if (new_location[0] == -1):
            break
        new_cordinate = str(new_location[0]) + "," + str(new_location[1])
        if locations.get(new_cordinate,0) == 0:
            locations[new_cordinate] = " "
        y,x = new_location
    sum = 0


    for location in locations.keys():
        main2 = []
        for a in main:
            line = []
            for b in a:
                line.append(b)
            main2.append(line)
        y,x = location.split(',')
        x,y = int(x),int(y)
        main2[y][x] = '#'
        if antras(main2,start[0],start[1]) == True:
            sum += 1

    print(sum)
def antras(main,y,x):
    direction = 0
    i = 0
    bumps = {}
    while (True):

        new_location = movement(direction, y, x, main)
        if new_location[0] == -2:
            if (bumps.get((str(direction) + ',' + str(new_location[1]) + ',' + str(new_location[2])),0)) != 0:
                return True
            bumps[str(direction) + ',' + str(new_location[1]) + ',' + str(new_location[2])] = "1"
            direction += 90
            if direction == 360:
                direction = 0
            continue
        if (new_location[0] == -1):
            return False
        y, x = new_location

def movement(direction,y,x,main):
    match direction:
        case  0:
            if outofbounds(y-1,x,main):
                return -1,0
            if (main[y-1][x] == "#"):
                return -2,y-1,x
            return y-1,x
        case 180:
            if outofbounds(y + 1, x, main):
                return -1,0
            if (main[y+1][x] == "#"):
                return -2,y+1,x
            return y + 1, x
        case 90:
            if outofbounds(y,x+1,main):
                return -1,0
            if (main[y][x+1] == "#"):
                return -2,y,x+1
            return y,x+1
        case 270:
            if outofbounds(y,x-1,main):
                return -1,0
            if (main[y][x-1] == "#"):
                return -2,y,x-1
            return y,x-1
    return -3,0
def outofbounds(y,x,main):
    if y < 0 or x < 0: return True
    if x >= len(main[0]) or y >= len(main): return True
    return False
if __name__ == "__main__":
    pirmas()