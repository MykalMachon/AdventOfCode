import numpy as np

def load_input_into_columns(filepath):
  # read lines in as list
  input_file = open(filepath, "r")
  input_list = input_file.readlines()
  input_list = [input.strip('\n') for input in input_list]
  # read rows in as stuff
  num_cols = len(input_list[0])
  col_list = [[] for x in range(num_cols)]
  for idx in range(num_cols):
    for input in input_list:
      col_list[idx].append(int(input[idx]))
  return col_list

def part_one(input_list):
  # setup some basic variables
  num_cols = len(input_list)
  gamma_binary = ""
  epsilon_binary = ""

  # calculate epsilon and gamma values
  for column_idx in range(num_cols): 
    # get a bincount for the columns
    column_arr = np.array(input_list[column_idx])
    column_arr_bin = np.bincount(column_arr)
    # append values to creat binary number as str
    gamma_binary += str(column_arr_bin.argmax())
    epsilon_binary += str(column_arr_bin.argmin())
    
  # calculate power consumption
  gamma_decimal = int(gamma_binary, 2)
  epsilon_decimal = int(epsilon_binary, 2)
  power_consumption = gamma_decimal * epsilon_decimal
  return power_consumption


def test_part_one():
  input_list = load_input_into_columns('test.txt')
  result = part_one(input_list)
  assert result == 198, "Test Input Doesn't provide expected output"

def run_part_one():
  input_list = load_input_into_columns('input.txt')
  result = part_one(input_list)
  print(f"Result is: {result}")

test_part_one()
run_part_one()