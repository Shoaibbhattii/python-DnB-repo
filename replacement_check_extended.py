import pandas as pd

# Read the Excel file
file_path = 'Processed Raw Addresses 4 lac with Duplicates City and Provinces.xlsx'  # Replace with the actual file path
df = pd.read_excel(file_path)

# Print the column names to verify
print("Column names in the Excel file:", df.columns.tolist())

# Ensure the required columns exist
processed_column = 'Processed_OriginalAddress_lower'
replacements_column = 'replacements'
to_do_replacement_column = 'to_do_replacement'
if processed_column not in df.columns:
    raise ValueError(f"Column '{processed_column}' not found in the Excel file")
if replacements_column not in df.columns:
    raise ValueError(f"Column '{replacements_column}' not found in the Excel file")
if to_do_replacement_column not in df.columns:
    raise ValueError(f"Column '{to_do_replacement_column}' not found in the Excel file")

# Extract the list of replacements and their corresponding replacements
replacements_df = df[[replacements_column, to_do_replacement_column]].dropna().astype(str)

# Function to check for replacement words in the address and add the new replacements
def find_replacements(address):
    if not isinstance(address, str):
        return "Not Found", ""
    
    found_words = [word for word in replacements_df[replacements_column] if word in address]
    to_do_replacements = [replacements_df[replacements_df[replacements_column] == word][to_do_replacement_column].values[0] for word in found_words]
    
    if found_words:
        return "Found, " + ", ".join(found_words), "$".join(to_do_replacements)
    else:
        return "Not Found", ""

# Apply the function to each row
df[['check_replacements', 'to_do_replacement_output']] = df[processed_column].apply(lambda x: pd.Series(find_replacements(x)))

# Save the result to a new Excel file
output_file_path = 'output_file_with_replacements.xlsx'  # Replace with desired output path
df.to_excel(output_file_path, index=False)

print(f"Results saved to {output_file_path}")
