def inbound(matrix, row, col):
  if row < 0 or col < 0:
      return False
  if row > len(matrix)-1 or col > len(matrix[0])-1:
      return False
  return True

def neighboring_correct_letters(main,start,letter):  #start = (x,y)
  n = [-1,0,1]
  neighbors = 0
  for number in n:
    for number2 in n:
      if inbound(main,start[0] + number,start[1] + number2) and not(number == 0 and number2 == 0):
        if main[start[0] + number][start[1] + number2] == letter:
          if inbound(main,start[0] + (number * 2),start[1] + (number2*2)):
            if main[start[0] + (number * 2)][start[1] + (number2*2)] == 'A':
              if inbound(main,start[0] + (number * 3),start[1] + (number2*3)):
                if main[start[0] + (number * 3)][start[1] + (number2*3)] == 'S':
                  print(start[0] + (number * 3),start[1] + (number2*3))
                  neighbors+=1

  return neighbors

text =""
with open("yes.txt", 'r') as f:
        text = f.read()
lines = text.split("\n")
main = []
for line in lines:
  main.append(list(line))
answers = 0
y = 0
for string in main:
  x = 0
  for letter in string:
    if letter == 'X':
      answers = answers + neighboring_correct_letters(main,[y,x],'M')
    x += 1
  y += 1
print(answers)
