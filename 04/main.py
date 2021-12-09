"""
Process the input as needed
@return: input_list, board_mats
"""
def process_input(filepath):
    with open(filepath, 'r') as input_file:
        raw_input_list = input_file.readlines()
        draw_list = raw_input_list[0]
        return draw_list
