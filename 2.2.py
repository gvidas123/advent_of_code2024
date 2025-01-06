def main() :
    with open('input.txt', 'r') as file:
        main_array = []
        for line in file:
            main_array.append(line.split())
    true_false = []
    print(main_array)
    for array in main_array:
        if len(array) <= 2:
            true_false.append(1)
            continue
        true_false.append(calculations(array))
    print(true_false)
    print(sum(true_false))

def calculations(array):
    array = [int(number) for number in array]
    previous = array[0]

    if previous < array[1]:
        for number in array[1:]:
            if (previous == number):
                return endgame(array)
            if( previous > number):
                return endgame(array)
            else:
                if (int(previous) + 3 < int(number)) :
                    return endgame(array)
            previous = number
    else:
        if previous > array[1]:
            for number in array[1:]:
                if (previous == number):
                    return endgame(array)
                if( previous < number):
                    return endgame(array)
                else:
                    if (previous > number + 3) :
                        return endgame(array)
                previous = number
        else:
            return endgame(array)
    return 1
def endgame(array):
    i = 0
    starter = array.copy()
    for number in array:
        array = starter.copy()
        array.pop(i)
        if bs(array) == 1:
            return 1
        i = i + 1
    return 0
def bs(array):
    previous = array[0]

    if previous < array[1]:
        for number in array[1:]:
            if (previous == number):
                return 0
            if (previous > number):
                return 0
            else:
                if (int(previous) + 3 < int(number)):
                    return 0
            previous = number
    else:
        if previous > array[1]:
            for number in array[1:]:
                if (previous == number):
                    return 0
                if (previous < number):
                    return 0
                else:
                    if (previous > number + 3):
                        return 0
                previous = number
        else:
            return 0
    return 1
if __name__ == "__main__":
        main()