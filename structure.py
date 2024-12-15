import pandas as pd

# Load the dataset (replace 'file_path' with your actual file)
file_path = r"C:\Users\hp\Downloads\student+performance\student\student-mat.csv"
raw_data = pd.read_csv(file_path, delimiter=';')  # Read the CSV using the correct delimiter

# Preview the first few rows to see if it loaded properly
print(raw_data.head())

# Remove extra quotes around values if present
raw_data = raw_data.replace('"', '', regex=True)

# Verify the structure is consistent (optional, you can skip this check if not needed)
consistent = all(raw_data.apply(len) == len(raw_data.columns))
if consistent:
    print("Structure is consistent across all rows.")
else:
    print("Inconsistent structure detected. Please review.")

# Save the cleaned dataset (optional)
cleaned_file_path = r"C:\Users\hp\Desktop\practice.py\cleaned_dataset.csv"  # Replace with desired save location
raw_data.to_csv(cleaned_file_path, index=False)

# Preview the cleaned data
print(raw_data.head())

# Print the column names
print("Columns in the cleaned dataset:")
print(raw_data.columns)
