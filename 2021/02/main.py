def get_input_as_list(filepath):
    input_file = open(filepath, "r")
    input_list = input_file.readlines()
    input_list = [input.strip('\n') for input in input_list]
    return input_list


def tokenize_input(input):
    return input.split(' ')


def solve_part_one():
    command_list = get_input_as_list('./input.txt')
    horiz_pos = 0
    depth_pos = 0

    # calculate horiz and depth
    for command in command_list:
        direction, distance = tokenize_input(command)
        if direction == "up":
            depth_pos -= int(distance)
        elif direction == "down":
            depth_pos += int(distance)
        elif direction == "forward":
            horiz_pos += int(distance)

    # calclate area
    final_area = horiz_pos * depth_pos
    return final_area


def solve_part_two():
    command_list = get_input_as_list('./input.txt')

    aim = 0
    horiz_pos = 0
    depth_pos = 0

    for command in command_list:
        direction, distance = tokenize_input(command)
        if direction == "up":
            aim -= int(distance)
        elif direction == "down":
            aim += int(distance)
        elif direction == "forward":
            horiz_pos += int(distance)
            depth_pos += (aim * int(distance))

    final_area = horiz_pos * depth_pos
    return final_area


print(solve_part_one())
print(solve_part_two())
