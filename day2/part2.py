file = open('input.txt', 'r')
data = file.read().split("\n")

score = 0

for i in data:
  opp, outcome = i.split(" ")

  if outcome == "X":
    score += 0

  if outcome == "Y":
    score += 3

  if outcome == "Z":
    score += 6

  if opp == "A":
    if outcome == "X":
      score += 3
    if outcome == "Y":
      score += 1
    if outcome == "Z":
      score += 2

  if opp == "B":
    if outcome == "X":
      score += 1
    if outcome == "Y":
      score += 2
    if outcome == "Z":
      score += 3

  if opp == "C":
    if outcome == "X":
      score += 2
    if outcome == "Y":
      score += 3
    if outcome == "Z":
      score += 1

print(score)
