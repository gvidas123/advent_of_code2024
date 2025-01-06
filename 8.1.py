def main():
    main = []
    current_letter = ""
    current_positions = []
    previous_letters = {}
    answer_positions = []
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            main.append(line)
    for row in main:
        for current_letter in row:
            if current_letter != '.' and previous_letters.get(current_letter,0) != 1:
                previous_letters[current_letter] = 1
                for a in calculations(main,current_letter):
                    answer_positions.append(a)
    answer_positions2 =[]
    [answer_positions2.append(val) for val in answer_positions if val not in answer_positions2]
    print(answer_positions2)
    print(len(answer_positions2))

def calculations(main,letter):
    locations = []
    y = 0
    for row in main:
        x = 0
        for current_letter in row:
            if (current_letter == letter):
                locations.append([y,x])
            x+=1
        y+=1
    print(locations)
    ans_locations = []
    for a in locations:
        ans_locations.append(a)
    vectorx = 0
    vectory = 0
    for i in range(len(locations)):
        for x in range(i+1,len(locations)):

            vectory = locations[i][0] - locations[x][0]
            vectorx = locations[i][1] - locations[x][1]
            vectorx = vectorx
            vectory = vectory

            #print(i,x)
            #print(vectory,vectorx)

            if (vectorx < 0 or vectory < 0):
                first_location = [locations[i][0] + vectory, locations[i][1] + vectorx]
                print([locations[i][0] - vectory, locations[i][1] - vectorx])
                while (True):
                    #print(first_location)
                    if outofbounds(first_location,main) == True:
                        break
                    ans_locations.append(first_location)
                    first_location = [first_location[0] + vectory, first_location[1] + vectorx]

                second_location = [locations[i][0] - vectory, locations[i][1] - vectorx]
                print(second_location)
                while (True):
                    if outofbounds(second_location, main) == True:
                        break
                    ans_locations.append(second_location)
                    second_location = [second_location[0] - vectory, second_location[1] - vectorx]



            else:
                first_location = [locations[i][0] - vectory, locations[i][1] - vectorx]
                while (True):
                    if outofbounds(first_location, main) == True:
                        break
                    ans_locations.append(first_location)
                    first_location = [first_location[0] - vectory, first_location[1] - vectorx]

                second_location = [locations[i][0] + vectory, locations[i][1] + vectorx]
                while (True):
                    if outofbounds(second_location, main) == True:
                        break
                    ans_locations.append(second_location)
                    second_location = [second_location[0] + vectory, second_location[1] + vectorx]
            if outofbounds(first_location,main) != True:
                ans_locations.append(first_location)
            if outofbounds(second_location,main) != True:
                ans_locations.append(second_location)
    return ans_locations




def outofbounds(cordinate,main):
    if cordinate[0] < 0 or cordinate[1]  < 0: return True
    if cordinate[1]  >= len(main[0]) or cordinate[0]  >= len(main): return True
    return False


if __name__ == '__main__':
    main()