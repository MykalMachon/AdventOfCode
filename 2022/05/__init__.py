"""
https://adventofcode.com/2022/day/5

steps for part 1 of today's challenge:
1. load in the cargo stacks as input
2. load in the steps that you need to take on input
3. follow the steps in step 2 on the stacks
4. grab the top items from each stack
"""

from typing import List
from functools import reduce


def load_cargo():
    """loads the cargo stacks from the input.txt file"""
    with open('input.txt', mode='r', encoding='utf-8') as file:
        lines = [line.strip('\n') for line in file.readlines()]

        # get number of stacks in the cargo
        last_line = lines[len(lines)-1].replace(' ', '')
        num_stacks = range(int(last_line[len(last_line)-1]))

        # create cargo stacks
        stacks = [[] for stack in num_stacks]
        for line in lines[:-1]:
            curr_pos = 0
            for idx, stack in enumerate(num_stacks):
                curr_char = line[curr_pos:curr_pos+3]
                curr_pos += 4
                if curr_char.replace(' ', '') != "":
                    stacks[idx].append(curr_char)
        return stacks


def load_steps():
    """load the steps and format them from steps.txt"""
    with open('steps.txt', mode='r', encoding='utf-8') as file:
        lines = [line.strip('\n') for line in file.readlines()]
        steps = []
        for line in lines:
            tokens = line.split(' ')
            steps.append({
                "num": int(tokens[1]),
                "from": int(tokens[3]),
                "to": int(tokens[5])
            })
        return steps


def move_cargo(cargo: List[List], steps: List[dict]):
    """move cargo from one position to another one by one.
    """
    for step in steps:
        to_move = step.get('num')
        idx_from = step.get('from') - 1
        idx_to = step.get('to') - 1

        # grab items from cargo[idx_from]
        items_moving = [cargo[idx_from].pop(0) for x in range(to_move)]

        # move items into cargo[idx_to]
        for item in items_moving:
            cargo[idx_to].insert(0, item)
    return cargo


def move_cargo_groups(cargo: List[List], steps: List[dict]):
    """move cargo from one position to another while holding the original shape.
    """
    for step in steps:
        to_move = step.get('num')
        idx_from = step.get('from') - 1
        idx_to = step.get('to') - 1

        # grab items from cargo[idx_from]
        items_moving = cargo[idx_from][0:to_move]
        cargo[idx_from] = cargo[idx_from][to_move:]

        # move items into cargo[idx_to]
        cargo[idx_to] = items_moving + cargo[idx_to]
    return cargo


if __name__ == "__main__":
    cargo = load_cargo()
    steps = load_steps()

    # part 1: move cargo conventionally
    new_cargo = move_cargo(cargo, steps)
    top_cargo = reduce(lambda a, c: a + c[0], new_cargo, '')

    print(top_cargo.replace('[', '').replace(']', ''))

    # part 2: margo cargo in groups
    cargo = load_cargo()

    group_cargo = move_cargo_groups(cargo, steps)
    top_group_cargo = reduce(
        lambda a, c: a + c[0] if len(c) > 0 else a, group_cargo, '')

    print(top_group_cargo.replace('[', '').replace(']', ''))
