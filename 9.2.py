def main():
    numbers = []
    current_id = 0
    current = 1
    with open('input.txt', 'r') as file:
        for line in file:
            for number in line:
                numbers.append(int(number))

    i = 0
    for number in numbers:
        if (i >= len(numbers)):
            break
        if (current == 1):
            count = numbers[i]
            numbers.pop(i)
            for a in range(count):
                numbers.insert(i,current_id)
            current_id += 1
            current = 0
            i+= count
            continue
        if (current == 0):
            count = numbers[i]
            numbers.pop(i)
            for a in range(count):
               numbers.insert(i,-1)
            current = 1
            i+= count
            continue
    i = len(numbers) - 1
    x = 0

    current_number = -1
    size = 0
    start = 0
    x = len(numbers) - 1
    print(numbers)
    for number in reversed(numbers):

        if (current_number == -1 and number != -1):
            start = x
            current_number = number
            size = 1
            x-=1
            continue
        if number == current_number and number !=-1:
            size +=1
            x -= 1
            continue
        else:

            if(size > 0):
                i = 0
                open_size = 0
                open_start = 0
                while (i <= x ):
                    if (numbers[i] == -1 and open_size != 0):
                        open_size += 1
                    if (numbers[i] == -1 and open_size == 0):
                        open_start = i
                        open_size +=1
                    if numbers[i] != -1:

                        open_start = 0
                        open_size = 0
                    placed = False
                    if (open_size == size):
                        while(True):
                            numbers[open_start] = numbers[start]
                            numbers[start] = -1
                            open_start +=1
                            start -= 1
                            size -=1
                            if (size == 0):
                                open_size = 0
                                open_start = 0
                                placed = True
                                break
                    if placed == True:
                        break

                    i+=1
                current_number = -1
            if (current_number == -1 and number != -1):
                start = x
                current_number = number
                size = 1
                x -= 1
                continue
            if number == current_number and number != -1:
                size += 1
                x -= 1
                continue
            x -= 1
    print(numbers)
    sum = 0
    i = 0
    for number in numbers:
        if number != -1:
            sum += number * i
        i+=1
    print(sum)



if __name__ == '__main__':
    main()