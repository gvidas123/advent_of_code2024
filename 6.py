import re



def pirmas():
    main = []
    x = 0
    y = 0
    direction = 0
    locations = {}
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
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
        print(new_cordinate)
        if locations.get(new_cordinate,0) == 0:
            locations[new_cordinate] = " "
        y,x = new_location
    print(locations)
    print(len(locations.keys()))
    return locations




def movement(direction,y,x,main):

    match direction:
        case  0:
            if outofbounds(y-1,x,main):
                return -1,0
            if (main[y-1][x] == "#"):
                return -2,0
            return y-1,x
        case 180:
            if outofbounds(y + 1, x, main):
                return -1,0
            if (main[y+1][x] == "#"):
                return -2,0
            return y + 1, x
        case 90:
            if outofbounds(y,x+1,main):
                return -1,0
            if (main[y][x+1] == "#"):
                return -2,0
            return y,x+1
        case 270:
            if outofbounds(y,x-1,main):
                return -1,0
            if (main[y][x-1] == "#"):
                return -2,0
            return y,x-1
    return -3,0
def outofbounds(y,x,main):
    if y < 0 or x < 0: return True
    if x >= len(main[0]) or y >= len(main): return True
    return False
if __name__ == "__main__":
    pirmas()