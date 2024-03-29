# How to use:
# Tested with Python 3.11.5
# Run python3 -s dataset_generator.py review.csv <output_directory>

import csv
import sys
import os
import time

if __name__ == "__main__":
    
    tic = time.perf_counter()
    
    if len(sys.argv) < 2:
        raise Exception('Please provide an input file!')

    input_csv_file = sys.argv[1]
    output_directory = sys.argv[2]

    counters_dict = {}
    
    # Create directory if not exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    with open(input_csv_file, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)  # Skip header row
        for row in csv_reader:
            key = tuple(row[0:3])
            counter = counters_dict.get(key, 0) + 1
            counters_dict[key] = counter

            output_txt_file = os.path.join(
                output_directory,
                f'{row[0]}_{row[1]}_{row[2]}_{counter}.txt'
            )

            with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
                for element in row:
                    txt_file.write(element.strip() + '\n')
    
    toc = time.perf_counter()
    elapsed_time = toc - tic
    print(elapsed_time)
