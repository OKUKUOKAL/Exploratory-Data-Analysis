import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the 2019 dataset into a DataFrame
df = pd.read_csv("IT Salary Survey EU 2019.csv")

# Print the first 5 rows of the DataFrame
print(df.head())

# Get basic statistics about the numerical columns
print(df.describe())

# Plot histograms of the numerical columns
df.hist(bins=50, figsize=(20,15))
plt.show()

# Plot box plots of the numerical columns
df.plot(kind='box', subplots=True, layout=(5,7), figsize=(20,20))
plt.show()

# Create a scatter plot of Age vs. Years of experience
sns.scatterplot(x='Age', y='Years of experience', data=df)
plt.show()

# Create a heatmap of the correlation matrix
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()