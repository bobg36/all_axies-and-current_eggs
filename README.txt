1. save_all_axies.py
saves all axies starting from axieId = 0. will take a very long time, like 2 months. saves to all_axies.csv

2. chunk_1m.py
chunks all_axies.csv into 1 million rows, into folder named 'chunk'

3. extract_eggs.py
must specify filename, output will be 'output.csv'. extracts all eggs into output.csv from specified file.

TODO:

change extract_eggs.py's output to 'old_eggs.py'. these are old eggs because they have been eggs for much longer than 5 days, and most likely forgotten by owner. unimportant, but can scan this periodically to check if hatched.



scripts to maintain current_eggs.csv
    1. write to current_eggs.csv when a new egg is created (highest id)
    2. remove from current_eggs.csv when egg has been hatched. insert into all_axies
