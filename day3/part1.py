file = open('input.txt', 'r')
data = file.read().split("\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"

priorities = 0

for i in data:
  first = i[:int(len(i) / 2)]
  second = i[int(len(i) / 2):]
  common = set(first).intersection(second).pop()

  if common.isupper():
    lower = common.lower()
    priorities += alphabet.index(lower) + 27
  else:
    priorities += (alphabet.index(common) + 1)

print(priorities)
