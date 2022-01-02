inputs = []
inputs_two = []
counter = 1


with open('./day_one.txt') as input_file:
    lines = input_file.readlines()
    lines = [line.rstrip() for line in lines]
    [inputs.append(line) for line in lines]

for idx, input in enumerate(inputs):
  window = inputs[idx:idx+2]
  sum = 0
  for pane in window:
    sum += pane
  inputs_two.append(sum)


for idx, input in enumerate(inputs_two):
    if idx == 0:
        continue
    if input > inputs_two[idx-1]:
        counter += 1

print(counter)
