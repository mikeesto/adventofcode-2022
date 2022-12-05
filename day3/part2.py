file = open('input.txt', 'r')
data = file.read().split("\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"

priorities = 0

for i in range(0, len(data), 3):
  first = data[i]
  second = data[i + 1]
  third = data[i + 2]

  common = set(first).intersection(second).intersection(third).pop()

  if common.isupper():
    lower = common.lower()
    priorities += alphabet.index(lower) + 27
  else:
    priorities += (alphabet.index(common) + 1)

print(priorities)
