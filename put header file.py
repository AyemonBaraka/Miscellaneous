import pandas as pd

# Replace 'your_dataset.csv' with the actual file name or provide the data directly
# If providing data directly, you can use 'data' as shown below
# data = [[your data goes here]]

# Read the dataset without header
df = pd.read_csv('/home/ayemon/KafkaProjects/kafkaspark07_90/ptbdb_normal_80.csv', header=None)

# Assigning column names 't1', 't2', ..., 't188'
col_names = [f't{i}' for i in range(1, 189)]
df.columns = col_names

# Write DataFrame with header to a new CSV file
df.to_csv('ptbdb_normal_80.csv', index=False)

print("Headers added and the new CSV file 'dataset_with_headers.csv' created successfully.")
