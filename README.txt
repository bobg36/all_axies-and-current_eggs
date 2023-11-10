1. save_all_axies.py
saves all axies starting from axieId = 0. will take a very long time, like 2 months. saves to all_axies.csv

2. chunk_1m.py
chunks all_axies.csv into 1 million rows, into folder named 'chunk'

3. extract_eggs.py
must specify filename, output will be 'output.csv'. extracts all eggs into output.csv from specified file.

TODO:

-create current_eggs.csv from extracted eggs. 
-iterate through current_eggs.csv and check with graphql API if hatched or not.
    - if hatched, insert into all_axies

