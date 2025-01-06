def main():
    results = []
    numbers = []
    result = ""
    with open('input.txt','r') as file:
        for line in file:
            result, row = line.split(':')
            results.append(result)
            row = row.split(' ')
            row.pop(0)
            row[len(row)-1] = row[len(row)-1].strip()
            numbers.append(row)
    i = 0
    sum = 0
    for result in results:
        if calculations(numbers[i],0,0,0,results[i]) == True or calculations(numbers[i],0,0,1,results[i]) == True or calculations(numbers[i],0,0,2,results[i]):
           sum += int(results[i])
        i += 1

    print (int(str(25) + str('5')))
    print(sum)

def calculations(numbers,current,result,operator,target):
    if outofbounds(numbers,current) == True:
        if (result == int(target)):
            return True
        return False
    if operator == 0:
        result += int(numbers[current])
        current +=1
        if calculations(numbers,current,result,0,target) == True or calculations(numbers,current,result,1,target) == True or calculations(numbers,current,result,2,target) == True:
            return True
        return False
    if operator == 1:
        result *= int(numbers[current])
        current += 1
        if calculations(numbers,current,result,0,target) == True or calculations(numbers,current,result,1,target) == True or calculations(numbers,current,result,2,target) == True:
            return True
        return False
    if operator == 2:
        result = int(str(result) + str(numbers[current]))
        current += 1
        if calculations(numbers,current,result,0,target) == True or calculations(numbers,current,result,1,target) == True or calculations(numbers,current,result,2,target) == True:
            return True
        return False


def outofbounds(numbers,current):
    if current > len(numbers) - 1:
        return True
    return False
# 1 + 2 + 3


if __name__ == "__main__":
    main()