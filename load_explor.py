import pandas as pd

# Load the dataset
dataset = pd.read_csv(r"C:\Shiash\intern project\cleaned_dataset2.csv")

# View the first few rows
print(dataset.head())


# 2 summaarize the data

print(dataset.dtypes)
print(dataset.describe())
print(dataset.info())


categorical_columns = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'reason', 'schoolsup']
for col in categorical_columns:
    print(f"Column: {col}")
    print(dataset[col].value_counts())
    print("\n")

# Check for missing values
missing_values = dataset.isnull().sum()
print(missing_values)
