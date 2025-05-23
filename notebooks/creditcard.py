import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
csdf = pd.read_csv('../data/raw/BankChurners.csv')

# Insight 1: Customer attrition statistics
attrition_stats = csdf['Attrition_Flag'].value_counts()
attrition_percentage = (attrition_stats / len(csdf) * 100).round(2)

# Insight 2: Average credit limit by card category
avg_credit_by_card = csdf.groupby('Card_Category')['Credit_Limit'].mean().round(2)

# Insight 3: Transaction patterns
transaction_patterns = csdf[['Total_Trans_Amt', 'Total_Trans_Ct']].describe()

print("\n=== Top 3 Insights ===")
print("\n1. Customer Attrition Breakdown (%):")
print(attrition_percentage)

print("\n2. Average Credit Limit by Card Category:")
print(avg_credit_by_card)

print("\n3. Transaction Patterns Summary:")
print(transaction_patterns)

# Visualize the insights
plt.figure(figsize=(15, 5))

# Plot 1: Attrition
plt.subplot(131)
sns.barplot(x=attrition_stats.index, y=attrition_stats.values)
plt.title('Customer Attrition')

# Plot 2: Credit Limit by Card
plt.subplot(132)
sns.barplot(x=avg_credit_by_card.index, y=avg_credit_by_card.values)
plt.title('Avg Credit Limit by Card Type')

# Plot 3: Transaction Amount vs Count
plt.subplot(133)
sns.scatterplot(data=csdf, x='Total_Trans_Amt', y='Total_Trans_Ct')
plt.title('Transaction Patterns')

plt.tight_layout()
plt.show()
