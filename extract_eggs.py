import pandas as pd

# Replace 'your_file_path.csv' with the path to your CSV file
file_path = 'chunks/all_axies_chunk_1000000_1999999.csv'
output_file_path = 'output.csv'

# Read the CSV file
df = pd.read_csv(file_path)

is_egg = df['genes'] == '0x0'
egg_count = (df['genes'] == '0x0').sum()

egg_df = df[is_egg]
egg_df.to_csv(output_file_path, index=False)
