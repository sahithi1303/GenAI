import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Sample accounts data as a list of lists
accounts_list = [
    ["ACC301", "Savings", "John Smith", 5250.75, "2022-07-10", True],
    ["ACC302", "Checking", "Lisa Johnson", 2800.50, "2021-12-05", True],
    ["ACC303", "Credit Card", "Robert Davis", -1500.25, "2022-03-18", False],
    ["ACC304", "Investment", "Sarah Wilson", 12500.00, "2020-09-22", True],
    ["ACC305", "Loan", "Michael Brown", -7800.00, "2022-02-14", False]
]

# Define column names
column_names = ["Account ID", "Account Type", "Account Holder", "Balance", "Opening Date", "Active Status"]

# Create DataFrame from list
accounts_df_list = pd.DataFrame(accounts_list, columns=column_names)

# Convert data types
accounts_df_list["Balance"] = pd.to_numeric(accounts_df_list["Balance"])
accounts_df_list["Opening Date"] = pd.to_datetime(accounts_df_list["Opening Date"])

print("Accounts DataFrame created from List:")
print(accounts_df_list)

# Sample accounts data as a tuple of tuples
accounts_tuple = (
    ("ACC401", "Savings", "Jennifer Lee", 6350.25, "2021-10-12", True),
    ("ACC402", "Checking", "Daniel Martinez", 3200.75, "2022-04-18", True),
    ("ACC403", "Credit Card", "Amanda Taylor", -2800.50, "2021-11-30", False),
    ("ACC404", "Investment", "Christopher Clark", 22000.00, "2020-05-15", True),
    ("ACC405", "Loan", "Elizabeth Wright", -5200.75, "2022-01-20", False)
)

# Create DataFrame from tuple
accounts_df_tuple = pd.DataFrame(accounts_tuple, columns=column_names)

# Convert data types
accounts_df_tuple["Balance"] = pd.to_numeric(accounts_df_tuple["Balance"])
accounts_df_tuple["Opening Date"] = pd.to_datetime(accounts_df_tuple["Opening Date"])

print("\nAccounts DataFrame created from Tuple:")
print(accounts_df_tuple)

# Combine both DataFrames
combined_accounts_df = pd.concat([accounts_df_list, accounts_df_tuple], ignore_index=True)

print("\nCombined Accounts DataFrame:")
print(combined_accounts_df)

# Add account age calculation
current_date = datetime.now()
combined_accounts_df["Account Age (Days)"] = (current_date - combined_accounts_df["Opening Date"]).dt.days

# Basic analysis
print("\nAccount Type Distribution:")
print(combined_accounts_df["Account Type"].value_counts())

print("\nAccounts with Negative Balance (Debt):")
print(combined_accounts_df[combined_accounts_df["Balance"] < 0])

print("\nAccounts with Positive Balance:")
print(combined_accounts_df[combined_accounts_df["Balance"] > 0])

# Calculate total balance by account type
account_type_balance = combined_accounts_df.groupby("Account Type")["Balance"].sum()
print("\nTotal Balance by Account Type:")
print(account_type_balance)

# Calculate average balance by account type
account_type_avg_balance = combined_accounts_df.groupby("Account Type")["Balance"].mean()
print("\nAverage Balance by Account Type:")
print(account_type_avg_balance)

# Count active vs inactive accounts
active_status_count = combined_accounts_df["Active Status"].value_counts()
print("\nActive vs Inactive Accounts:")
print(active_status_count)
