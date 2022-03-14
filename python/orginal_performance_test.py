import time
import string
from utils import convert_str_ascii_to_string
from str_strip import function


DATASET_PATH = 'dataset.txt'
REPETITIONS = 1_500_000

################################
#       READING DATASET        #
################################
characters_array = []
excluded_array = []

with open(DATASET_PATH) as file:
    line_number = 0
    for line in file:
        line_number += 1
        converted_line = convert_str_ascii_to_string(line);
        if (line_number % 2):
            characters_array.append(converted_line)
        else:
            excluded_array.append(converted_line)


################################
#   PERFORMANCE MEASUREMENT    #
################################

# Empty loop
t0 = time.time_ns()
for _ in range(REPETITIONS):
    for index in range(len(characters_array)):
        if excluded_array[index]:
            pass
        else: 
            pass

t1 = time.time_ns()

# Empty loop + calculations
for _ in range(REPETITIONS):
    for index in range(len(characters_array)):
        if excluded_array[index]:
            characters_array[index].strip(excluded_array[index])
        else: 
            characters_array[index].strip()
t2 = time.time_ns()

loop = (t2 - t1) / (10 ** 9)
empty_loop = (t1 - t0) / (10 ** 9)
print(f'{empty_loop} [s] -> empty loop')
print(f'{loop} [s] -> empty loop + calculations')
print(f'{loop - empty_loop} [s] -> pure calculations')