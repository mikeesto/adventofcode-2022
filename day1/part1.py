file = open('input.txt', 'r')
data = file.read().split("\n")

calories = []
count = 0

for i in data:
  if i == "":
    calories.append(count)
    count = 0
  else:
    count += int(i)

print(max(calories))
