from collections import deque
def main():
    cordinates = []
    with open("input.txt",'r') as file:
        for line in file:
            cordinates.append(line.strip())
    answer = 0
    for y,row in enumerate(cordinates):
        for x,cordinate in enumerate(row):
            if int(cordinate) == int(0):
                answer += start(y,x,cordinates)
                print(answer)



def start(y,x,cordinates):
    print(y,x,"cordinates")
    been_to = {}
    answer = 0
    poses = neighbors([y,x],cordinates)
    print(poses,"after one iteration")
    while(True):
        new = []
        for pos in poses:
            neighbors2 = neighbors(pos,cordinates)
            for neighbor in neighbors2:
                new.append(neighbor)
        poses.clear()
        for a in new:
            if int(cordinates[int(a[0])][int(a[1])]) == 9:
                answer+=1

        for a in new:
            poses.append(a)


        new = []
        print(poses)
        if not poses:
            break
    return answer



def neighbors(pose, cordinates):
    valid_neighbors = []

    y = pose[0]
    x = pose[1]
    if valid(y - 1, x, cordinates, pose) == True: valid_neighbors.append([y - 1, x]) #top
    if valid(y, x + 1, cordinates, pose) == True: valid_neighbors.append([y, x + 1]) #right
    if valid(y + 1, x, cordinates, pose) == True: valid_neighbors.append([y + 1, x]) #bot
    if valid(y, x - 1, cordinates, pose) == True: valid_neighbors.append([y, x - 1]) #left
    return valid_neighbors

def valid(y,x,cordinates,pose):
    if out_of_bounds(y, x, cordinates) == False:
        if int(cordinates[y][x]) - 1 == int(cordinates[pose[0]][pose[1]]):
            return True
    return False

def out_of_bounds(y,x,cordinates):
    if y < 0 or x < 0 or y >= len(cordinates) or x >= len(cordinates[0]): return True
    return False

if __name__ == '__main__':
    main()