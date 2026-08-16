import pandas as pd

raw_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(raw_data)

# Reshaping the DataFrame
#pivoted_df = df.pivot(index='Name', columns='City', values='Age')

pivoted_df = df.pivot(
    index='Name',
    columns='City',
    values='Age'
)

print(pivoted_df.fillna(0).astype(int))