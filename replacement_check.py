import pandas as pd

# Read the Excel file
file_path = 'Processed Raw Addresses 4 lac with Duplicates City and Provinces.xlsx'  # Replace with the actual file path
df = pd.read_excel(file_path)

# Print the column names to verify
print("Column names in the Excel file:", df.columns.tolist())

# Ensure the required columns exist
processed_column = 'Processed_OriginalAddress_lower'
replacements_column = 'replacements'  # Adjust this based on the actual column name
if processed_column not in df.columns:
    raise ValueError(f"Column '{processed_column}' not found in the Excel file")
if replacements_column not in df.columns:
    raise ValueError(f"Column '{replacements_column}' not found in the Excel file")

# Extract the list of replacements
replacements_list = df[replacements_column].dropna().astype(str).tolist()

# Function to check for replacement words in the address
def find_replacements(address):
    if not isinstance(address, str):
        return "Not Found"
    
    found_words = [word for word in replacements_list if word in address]
    
    if found_words:
        return "Found, " + ", ".join(found_words)
    else:
        return "Not Found"

# Apply the function to each row
df['check_replacements'] = df[processed_column].apply(find_replacements)

# Save the result to a new Excel file
output_file_path = 'output_file.xlsx'  # Replace with desired output path
df.to_excel(output_file_path, index=False)

print(f"Results saved to {output_file_path}")
