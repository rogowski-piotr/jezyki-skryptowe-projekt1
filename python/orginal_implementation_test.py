import time
import string
from utils import convert_str_ascii_to_string
from str_strip import function



DATASET_PATH = 'dataset.txt'
OUTPUT_PATH = 'result_python_orginal.txt'

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
#         CALCULATIONS         #
################################
results = []
for index in range(len(characters_array)):
    results.append(characters_array[index].strip(excluded_array[index]) if excluded_array[index] else characters_array[index].strip())


################################
#         SAVE RESULT          #
################################
with open(OUTPUT_PATH, 'w', encoding='utf8') as output:
    for line in results:
        output.write(line + '\n')
