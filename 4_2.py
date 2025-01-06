def inbound(matrix, row, col):
  if row < 0 or col < 0:
      return False
  if row > len(matrix)-1 or col > len(matrix[0])-1:
      return False
  return True

def neighboring_correct_letters(main,start):  #start = (y,x)
  n = [-1,1]
  neighbors = 0
  array = []
  M = 0
  S = 0
  y = start[0]
  x = start[1]
  if inbound(main,y - 1,x + 1) and inbound(main,y - 1,x - 1 ) and inbound(main,y +1,x + 1) and inbound(main,y + 1,x - 1):
    for number in [+1,-1]:
      for number2 in [+1,-1]:
        if main[y+number][x+number2] == 'M':
          M +=1
        if main[y+number][x+number2] == 'S':
          S += 1
    for number in [+1,-1]:
      for number2 in [+1,-1]:
        if main[y+number][x+number2] == 'M' and main[y+(number*-1)][x+number2*-1] == 'S' and M == 2 and S == 2:
          return 1
  return 0

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
    if letter == 'A':
      answers = answers + neighboring_correct_letters(main,[y,x])
    x += 1
  y += 1
print(answers)
