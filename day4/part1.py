file = open('input.txt', 'r')
data = file.read().split("\n")

overlapped = 0

for i in data:
  first, second = i.split(',')

  first_start, first_end = map(int, first.split('-'))
  second_start, second_end = map(int, second.split('-'))

  first = [i for i in range(first_start, first_end + 1)]
  second = [i for i in range(second_start, second_end + 1)]

  if (len(set(first).difference(second))) == 0 or len(set(second).difference(first)) == 0:
    overlapped += 1

print(overlapped)
