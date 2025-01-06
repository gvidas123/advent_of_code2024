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
       sum += (function(instruction,rules))

    print(sum)



def function(instruction,rules):
    answer = 0
    list = instruction
    middle = 0
    middle = 0
    for number in reversed(instruction):
        list = list[:-1]
        for number2 in list:
            if rules.get(number,0) != 0:
                for a in rules[number]:
                    if a == number2:
                        return int(incorrect(instruction, rules)[len(instruction) // 2])
    return 0

def incorrect(instruction,rules):
    list = instruction
    i = len(instruction)-1
    for number in reversed(instruction):
        x = 0
        list = list[:-1]
        for number2 in list:

            if rules.get(number, 0) != 0:
                for a in rules[number]:
                    if a == number2:
                        instruction[i], instruction[x] = instruction[x],instruction[i]

                        return incorrect(instruction, rules)
            x += 1
        i -= 1
    return instruction
if __name__ == "__main__":
    main()