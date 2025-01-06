def main() :
    array1 = []
    array2 = []
    with open('input.txt', 'r') as file:
        for line in file:
            numbers = line.split()
            array1.append(numbers[0])
            array2.append(numbers[1])
    diction1 = {}
    for number in array1:
        if (diction1.get(number,"OOPS") == "OOPS"):
            diction1.update({number:1})
        else:
            diction1.update({number:diction1[number] + 1})
    diction2 = {}
    for number in array2:
        if (diction2.get(number, "OOPS") == "OOPS"):
            diction2.update({number: 1})
        else:
            diction2.update({number: diction2[number] + 1})
    print(diction1)
    print(diction2)
    sum = 0
    for value in diction1:
        sum = sum + diction2.get(value,0) *  diction1.get(value) * int(value)
    print(sum)
if __name__ == "__main__":
    main()