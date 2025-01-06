import re
def main():
    with open('input.txt', 'r') as file:
        rules = {}
        sum = 0
        instructions = []
        instruction = []
        empty_string_array = []
        for line in file:
            line = line.strip()
            if len(line) < 7 and len(line) > 3:
                number1, number2 = line.split('|')
                if rules.get(number1,0) != 0:
                    list = rules[number1]
                    list.append(number2)
                    rules[number1] = list
                else:
                    rules[number1] = [number2]
            if len(line) > 7:
                numbers = line.split(',')
                for number in numbers:
                    instruction.append(number)
                instructions.append(instruction)
                instruction = []
    for instruction in instructions:
       sum = sum + function(instruction,rules)
    print(sum)



def function(instruction,rules):
    answer = 0
    list = instruction
    middle = 0
    middle = int(instruction[len(list)//2])
    for number in reversed(instruction):
        list = list[:-1]
        for number2 in list:
            if rules.get(number,0) != 0:
                for a in rules[number]:
                    if a == number2:
                        return 0


    return middle



if __name__ == "__main__":
    main()