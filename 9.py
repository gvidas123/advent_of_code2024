from collections import deque
def main():

    file_id = 0
    numbers = []
    with open('input.txt', 'r') as file1:

        for line in file1:
            for number in line:
                numbers.append(int(number))
    file = deque([])
    empty = deque([])
    final = []
    pos = 0
    for i,number in enumerate(numbers):
        if (i%2 == 0):
            file.append((pos, file_id, int(number)))
            for a in range(int(number)):
                final.append(file_id)
                pos+=1
            file_id +=1
        else:
            empty.append((pos,int(number)))
            for i in range(number):
                final.append(None)
                pos += 1
    for (pos,file_id,size) in reversed(file):
        for space_i,(space_poz,space_sz) in enumerate(empty):
            if space_poz < pos and space_sz >= size:
                for i in range(int(size)):
                    final[pos+i] = None
                    final[space_poz+i] = file_id

                empty[space_i] = (space_poz + size, space_sz - size)
                break
    print(final)
    sum = 0
    for i,number in enumerate(final):
        if (number != None):
            sum += number*i
    print (sum)


if __name__ == '__main__':
    main()