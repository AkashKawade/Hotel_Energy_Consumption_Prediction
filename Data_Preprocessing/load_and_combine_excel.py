import pandas as pd
# Step 1: Load the Excel data and combine all sheets
def load_and_combine_excel(file_path):
    sheets_dict = pd.read_excel(file_path, sheet_name=None, skiprows=3)

    combined_data = []

    for sheet_name, df in sheets_dict.items():
        # Transpose the DataFrame
        df_transposed = df.transpose()

        # Use the first row as the header and keep the first row in the data
        df_transposed.columns = df_transposed.iloc[0]
        df_transposed = df_transposed[1:].reset_index(drop=True)

        # Add a new column for the Date based on the sheet name
        df_transposed['Date'] = sheet_name

        # Append the transposed DataFrame to the list
        combined_data.append(df_transposed)

    # Combine all sheets into one DataFrame
    combined_df = pd.concat(combined_data, ignore_index=True)

    # Save to CSV
    output_file_path = 'Hotel_Data_combined_Aug23toAug24.csv'
    combined_df.to_csv(output_file_path, index=False)
    return output_file_path