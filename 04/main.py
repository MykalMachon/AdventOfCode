"""
Process the input as needed
@return: input_list, board_mats
"""


def process_input(filepath):
    with open(filepath, 'r', encoding="utf-8") as input_file:
        raw_input_list = input_file.readlines()
        # read in the draw list
        draw_list = raw_input_list[0].strip('\n').split(',')
        # read in the boards
        curr_board = []
        boards = []
        for idx, line in enumerate(raw_input_list[0:]):
            # process each line's content
            if line.strip() == "":
                continue
            else:
                row_values = line.split()
                row_value_dicts = [{"value": value,  "drawn": False}
                                   for value in row_values]
                curr_board.append(row_value_dicts)
            # if it's the end of a board... added it to the map
            if idx % 6 == 0 and idx != 0:
                boards.append(curr_board)
                curr_board = []

        return draw_list, boards

# returns the IDX of the winning board


def calculate_winning_board(draw_list, boards):
    board_list = boards.copy()
    # yucky O^4 code to update all the boards
    for number in draw_list:
        # for each board...
        for board in board_list:
            # for each row in each board...
            for row_idx, row in enumerate(board):
                # for each item in each row in each board...
                for col_idx, item in enumerate(row):
                    if item.value == number:
                        item.checked = True
                        # check if this caused a win in column or row

    return 0

# returns the score of a given board at any point in the game


def calculate_board_score(board):
    return 0


def test_part_one():
    draw_list, boards = process_input('test.txt')
    print(draw_list)
    print(f"Num Boards: {len(boards)}")
    winning_board = calculate_winning_board(draw_list, boards)
    winning_score = calculate_board_score(winning_board)
    print(f"Board #{winning_board} won, with a score of {winning_score}")


test_part_one()
