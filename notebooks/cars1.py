import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('../data/raw/cars.csv')

# Display data types of each column
print("Column data types:")
print(df.dtypes)

# Get initial data understanding
print("\nSample of the data:")
print(df.head())

# Select only numeric columns
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Now we can safely create correlations
crr = numeric_df.corr()

# Create heatmap with numeric data
plt.figure(figsize=(12,8))
sns.heatmap(crr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Numeric Features')
plt.tight_layout()
plt.show()


# 1. Histograms for all numeric columns
numeric_df.hist(figsize=(15,10), bins=30)
plt.suptitle('Distribution of Numeric Features', y=1.02)
plt.tight_layout()
plt.show()

# 2. Box plots for outlier detection
plt.figure(figsize=(15,6))
numeric_df.boxplot()
plt.xticks(rotation=45)
plt.title('Boxplots of Numeric Features')
plt.tight_layout()
plt.show()


# Calculate required subplot dimensions
n_cols = len(numeric_df.columns)
n_rows = (n_cols + 1) // 2  # Ceiling division to handle odd numbers

# Create KDE plots with dynamic grid
fig, axes = plt.subplots(nrows=n_rows, ncols=2, figsize=(15, 5*n_rows))
axes = axes.flatten()  # Flatten to make indexing easier

for idx, col in enumerate(numeric_df.columns):
    sns.kdeplot(data=numeric_df[col], ax=axes[idx])
    axes[idx].set_title(f'Distribution of {col}')

# Hide empty subplots if odd number of columns
if n_cols % 2 != 0:
    axes[-1].set_visible(False)

plt.tight_layout()
plt.show()

# Print summary statistics
print("\nSummary Statistics:")
print(numeric_df.describe())