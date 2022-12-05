file = open('input.txt', 'r')
data = file.read().split("\n")

score = 0

for i in data:
  opp, mine = i.split(" ")

  if mine == "X":
    score += 1

  if mine == "Y":
    score += 2

  if mine == "Z":
    score += 3

  if opp == "A":
    if mine == "X":
      score += 3
    if mine == "Y":
      score += 6
    if mine == "Z":
      score += 0

  if opp == "B":
    if mine == "X":
      score += 0
    if mine == "Y":
      score += 3
    if mine == "Z":
      score += 6

  if opp == "C":
    if mine == "X":
      score += 6
    if mine == "Y":
      score += 0
    if mine == "Z":
      score += 3

print(score)
