#!/bin/bash

SIZE=3
CHARACTERS_SIZE=10
EXCLUDED_SIZE=2
OUTPUT_PATH=dataset.txt

bash dataset_generator.py \
    --size ${SIZE} \
    --characters_size ${CHARACTERS_SIZE} \
    --excluded_size ${EXCLUDED_SIZE} \
    --output_path ${OUTPUT_PATH}