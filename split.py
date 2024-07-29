import pandas as pd

# Function to split the dataframe into chunks and save each chunk to an Excel file
def split_excel_into_chunks(input_file, chunk_size=100000):
    # Read the Excel file
    df = pd.read_excel(input_file)

    # Calculate the number of chunks
    num_chunks = len(df) // chunk_size + (1 if len(df) % chunk_size != 0 else 0)

    # Split the dataframe into chunks and save each chunk to a separate Excel file
    for i in range(num_chunks):
        start_row = i * chunk_size
        end_row = (i + 1) * chunk_size
        chunk = df.iloc[start_row:end_row]
        
        output_file = f'lac_chunk_{i+1}.xlsx'
        chunk.to_excel(output_file, index=False)
        print(f'Chunk {i+1} saved as {output_file}')

# Example usage
input_file = 'Processed Raw Addresses 4 lac with Duplicates City and Provinces.xlsx'
split_excel_into_chunks(input_file)
