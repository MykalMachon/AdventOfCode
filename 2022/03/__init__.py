"""
steps for today's challenge:
1. break down the rucksacks into two even pieces. 
2. parse through each of these two even pieces and find a common character
2.1 this could probably be done with a map of some sort
3. rank all of these items according to the priority system
4. sum the ranks fo all of these items
"""

from typing import List
from functools import reduce


def load_input():
    """loads inputs from a local text file"""
    with open('./input.txt', 'r', encoding='utf-8') as file:
        return [line.strip('\n') for line in file.readlines()]


def split_rucksack(rucksack: str):
    """splits a rucksack into two components
    """
    split_point = int(len(rucksack)/2)
    return [rucksack[:split_point], rucksack[split_point:]]


def get_common_items(lines: List[str]):
    """finds items that are in both compartments in each rucksack
    """
    items = []
    compartments = []
    # get the compartments to process
    for rucksack in lines:
        compartments.append(split_rucksack(rucksack))

    for idx, compartment in enumerate(compartments):
        acc = set(compartment[0])
        for item in compartment[1]:
            if {item}.issubset(acc):
                items.append(item)
                break

    return items


def get_item_priorities(items: List[str]):
    """receives a list of characters and returns their
    respective priorities given the challenges index.
    """
    new_priorities = []
    for item in items:
        is_upper = item.isupper()
        ascii_idx = ord(item.lower()) - 97
        priority = ascii_idx + 1 \
            if is_upper is False \
            else ascii_idx + 27
        new_priorities.append((item, priority))
    return new_priorities


if __name__ == "__main__":
    print("starting AOC 2022 Day 03")
    data = load_input()
    common_items = get_common_items(data)
    priorities = get_item_priorities(common_items)
    sum_of_priorities = reduce(lambda a, c: a + c[1], priorities, 0)
    print(f"Sum of priorities is: {sum_of_priorities} ")
