import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataset = pd.read_csv(r"C:\Shiash\intern project\cleaned_dataset2.csv")

# numeric correlation 
numerical_data = dataset.select_dtypes(include=[float, int])
correlation_matrix = numerical_data.corr()
print(correlation_matrix)

# include str correlation
dataset_encoded = pd.get_dummies(dataset)
correlation_matrix = dataset_encoded.corr()


# visualize coreltion 

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.show()


# Plot distributions of grades (G1, G2, G3):

dataset[['G1', 'G2', 'G3']].hist(figsize=(10, 5), bins=15)
plt.show()


#    analyze the impact of studytime on G3:

sns.boxplot(x='studytime', y='G3', data=dataset)
plt.show()

