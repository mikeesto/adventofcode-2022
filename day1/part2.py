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

calories.sort(reverse=True)
print(sum(calories[:3]))
