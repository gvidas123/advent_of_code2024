def main():
    with open('input.txt', 'r') as file:
        main_array = ""
        for line in file:
            main_array += line
    enabled = True
    comma = False
    tracking = False
    number = ""
    first_number = 0
    second_number = 0
    previous = ''
    sum = 0
    for letter in main_array:
        if letter == 'd':
            previous = 'd'
            tracking = True
            continue
        if previous == 'd' and letter == 'o':
            previous = letter
            continue
        if previous == 'o' and letter == '(':
            comma = False
            previous = letter
            continue
        if previous == '(' and letter == ')' and comma!= True:
            enabled = True
            tracking = False
            continue
        if (previous == 'o' and letter == 'n'):
            previous = letter
            continue
        if (previous == 'n' and letter == '\''):
            previous = letter
            comma = True
            continue
        if (previous == '\'' and letter == 't' ):
            previous = letter
            continue
        if (previous == 't' and letter == '('):
            previous = letter
            continue
        if previous == '(' and letter == ')' and comma == True:
            enabled = False
            tracking = False
            continue
        if letter == 'm' and enabled == True:
            previous = letter
            tracking = True
            continue
        else:
            if tracking != True:
                continue
        if previous == 'm' and letter == 'u':
            previous = 'u'
            continue
        if previous == 'u' and letter == 'l':
            previous = 'l'

            continue
        if previous == 'l' and letter == '(':
            previous = '('
            continue
        if (previous == '(' and ord(letter) <= ord('9')) and ord(letter) >= ord('0'):
            previous = letter
            number = number + letter
            continue
        if ord(letter) <= ord('9') and ord(letter) >= ord('0') and ord(previous) >= ord('0') and ord(previous) <= ord('9'):
            previous = letter
            number = number + letter
            continue
        if  ord(previous) >= ord('0') and ord(previous) <= ord('9') and letter == ','and comma != True:
            first_number = int(number)
            number = ""
            previous = ','
            comma = True
            continue
        if (previous == ',' and ord(letter) <= ord('9')) and ord(letter) >= ord('0'):
            previous = letter
            number = number + letter
            continue
        if ord(previous)  >= ord('0') and ord(previous)  <= ord('9') and letter == ')' and comma == True:
            second_number = int(number)
            sum = sum + int(first_number) * int(second_number)
        number = ""
        comma = False
        tracking == False
        previous == ''
        tracking = False
    print(enabled)
    print (sum)



if __name__ == "__main__":
    main()