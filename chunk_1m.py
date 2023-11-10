import pandas as pd

# Function to chunk the CSV
def chunk_csv(file_path, chunk_size=1000000):
    # Create a CSV reader with pandas
    csv_reader = pd.read_csv(file_path, chunksize=chunk_size, iterator=True)
    chunk_count = 0
    
    # Iterate over chunks
    for chunk in csv_reader:
        # Filter rows that are within the current million range
        filtered_chunk = chunk[(chunk['axieId'] >= chunk_count*chunk_size) & (chunk['axieId'] < (chunk_count+1)*chunk_size)]
        
        # If there's no data after filtering, skip to the next chunk
        if filtered_chunk.empty:
            continue

        # Define the name of the output file
        output_file = f'chunks/all_axies_chunk_{chunk_count*chunk_size}_{(chunk_count+1)*chunk_size-1}.csv'
        print('chunked ' + output_file)

        # Save the filtered chunk to a new CSV file
        filtered_chunk.to_csv(output_file, index=False)
        
        # Update the chunk count
        chunk_count += 1

# Path to the large CSV file
file_path = 'all_axies.csv'

# Call the function to chunk the CSV file
chunk_csv(file_path)
