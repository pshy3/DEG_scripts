import os
import pandas as pd

# Set the directory containing the HTSeq count files
directory = "."

# Initialize an empty list to store the DataFrames
dfs = []

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Read the CSV file
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path, sep='\t', header=None, names=['gene_id', filename[:-4]])
        
        # Append the DataFrame to the list
        dfs.append(df)

# Merge the DataFrames based on the 'gene_id' column
merged_df = pd.concat(dfs, axis=1).fillna(0)

# Remove duplicate columns (if any)
merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()]

# Set 'gene_id' as the index
merged_df.set_index('gene_id', inplace=True)

# Save the merged DataFrame to a new CSV file
output_file = "combined_counts.csv"
merged_df.to_csv(output_file)

print(f"Combined counts saved to {output_file}")
