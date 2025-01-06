import numbers
import numpy as np

def main() :
    array1 = np.array([],dtype=int)
    array2 = np.array([], dtype=int)
    with open('input.txt', 'r') as file:
        for line in file:
            numbers = line.split()
            array1 = np.append(array1, numbers[0])
            array2 = np.append(array2, numbers[1])

    array1 = np.sort(array1)
    array2 = np.sort(array2)
    print(array1)
    print(array2)
    i = 0
    sum = 0
    for number in array1:
        value = int(number) - int(array2[i])
        distance = abs(value)
        i = i + 1
        sum = sum + distance
    print(sum)
if __name__ == "__main__":
    main()
