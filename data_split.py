import pandas as pd

# Replace 'data.csv' with the path to your CSV file
file_path = '/home/ayemon/KafkaProjects/kafkaspark07_90/heart.csv'

# Read the CSV file into a pandas DataFrame
data_frame = pd.read_csv(file_path)

# Calculate the number of rows to keep in each file
total_rows = len(data_frame)
rows_to_keep_80_percent = int(0.8 * total_rows)

# Split the data into two DataFrames
data_frame_80_percent = data_frame[:rows_to_keep_80_percent]
data_frame_20_percent = data_frame[rows_to_keep_80_percent:]

# Save the 80% data into one file
file_80_percent = 'heart_80.csv'
data_frame_80_percent.to_csv(file_80_percent, index=False)

# Save the 20% data into another file
file_20_percent = 'heart_20.csv'
data_frame_20_percent.to_csv(file_20_percent, index=False)

print("Data split and saved successfully.")
