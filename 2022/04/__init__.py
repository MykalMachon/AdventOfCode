"""
https://adventofcode.com/2022/day/4

steps for part 1 of today's challenge:
1. break input down into lines ("pairs of elves")
2. look at each pair and create ranges based on assignments
3. use sets to find if either set is a subset of the other 
4.1 if either of the sets are subsets, return True, else False.
"""

from typing import List, Tuple
from functools import reduce


def load_input():
    """loads inputs from a local text file"""
    with open('./input.txt', 'r', encoding='utf-8') as file:
        return [line.strip('\n') for line in file.readlines()]


def get_range_pairs(lines: List[str]) -> List[Tuple]:
    """gets pairs of range from the list"""
    range_pairs = []
    for line in lines:
        items = line.split(',')
        item_range_strs = [item.split('-') for item in items]
        item_range_iter = [range(int(r[0]), int(r[1])+1)
                           for r in item_range_strs]
        item_ranges = [{x for x in r} for r in item_range_iter]
        range_pairs.append(item_ranges)
    return range_pairs


def find_subsets(pairs: List[List[int]]):
    """find pairs where either subset is a pair of itself
    This indicates a complete overlap of duties.
    """
    subsets = []
    for pair in pairs:
        if pair[0].issubset(pair[1]):
            subsets.append(True)
        elif pair[1].issubset(pair[0]):
            subsets.append(True)
        else:
          subsets.append(False)
    return subsets


if __name__ == "__main__":
    print("starting AOC 2022 Day 04")
    input = load_input()
    pairs = get_range_pairs(input)
    subset_overlap = find_subsets(pairs)
    subset_overlap_sum = reduce(lambda a, c: a+1 if c is True else a, subset_overlap, 0)
    print(f"there are {subset_overlap_sum} overlapping schedules")
