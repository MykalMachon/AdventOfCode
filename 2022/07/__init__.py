"""
https://adventofcode.com/2022/day/7

Steps for advent of code day 7:
1. Load in input as file
2. Build the file struct step by step based on the input
3. Traverse over the file struct based and calculate folder size
4. if a folder has a file size less that is less than 100000, add it to a list
5. add up all folder sizes and return them
"""
from typing import List, TypedDict


class FileTree(TypedDict):
    """a file tree dictionary. Is returned recursively"""
    struct: List
    total_size: int


def load_file() -> List[str]:
    """Loads the input from the input.txt file"""
    with open('input.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip('\n') for line in file.readlines()]
        return lines


def build_file_tree(lines: List[str]) -> FileTree:
    """build a file tree based on the 
    list of commands and output in input.txt.
    """
    total_size = 0
    folder_struct = []
    # 1. on cd command, find folder with filename of cd,
    #    and set it's children[] to build_file_tree(input[idx:])
    # 2. on ls command, loop inputs until another cd is found,
    #    append files and folders to file_tree
    # 3. on cd .. command, or len(lines) == 0 return the current
    #    folder's files and folders, and total size
    return {"struct": folder_struct, "total_size": total_size}


def process_object(line: str) -> dict:
    """determine if a file is a folder or a file 
    and return the appropriate object and metadata as
    a dictionary
    """
    return {"line": line}


def find_folders_under_size(file_tree: FileTree, size=100001) -> List:
    """find all folders where the file_size is less than
    size. Returns a list of folders.
    """
    return []


if __name__ == "__main__":
    print("advent of code day 7")
    data = load_file()
    file_tree = build_file_tree(data)
