#!/bin/bash

# dataset with two arguments (characters and excluded characters)
SIZE=100
CHARACTERS_SIZE=10
EXCLUDED_SIZE=2
OUTPUT_PATH=dataset.txt

echo python3 dataset_generator.py \
    --size ${SIZE} \
    --characters_size ${CHARACTERS_SIZE} \
    --excluded_size ${EXCLUDED_SIZE} \
    --output_path ${OUTPUT_PATH}

# dataset with one argument (characters and default excluded characters)
SIZE=100
CHARACTERS_SIZE=10
OUTPUT_PATH=dataset.txt

echo python3 dataset_generator.py \
    --size ${SIZE} \
    --characters_size ${CHARACTERS_SIZE} \
    --output_path ${OUTPUT_PATH}