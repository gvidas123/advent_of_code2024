def main() :
    with open('input.txt', 'r') as file:
        main_array = []
        for line in file:
            main_array.append(line.split())
    true_false = []
    print(main_array)
    for array in main_array:
       true_false.append(calculations(array))
    print(true_false)
    print(sum(true_false))

def calculations(array):
    array = [int(number) for number in array]
    previous = array[0]

    if previous < array[1]:
        for number in array[1:]:
            if (previous == number):
                return 0
            if( previous > number):
                return 0
            else:
                if (int(previous) + 3 < int(number)) :
                    return 0
            previous = number
    else:
        if previous > array[1]:
            print(array[1:])
            for number in array[1:]:
                if (previous == number):
                    return 0
                if( previous < number):
                    return 0
                else:
                    if (previous > number + 3) :
                        return 0
                previous = number
        else:
            return 0


    return 1
if __name__ == "__main__":
        main()