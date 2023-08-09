import pandas as pd

# Replace 'data.csv' with the correct path to your CSV file
file_path = '/home/ayemon/KafkaProjects/kafkaspark07_90/ptbdb_abnormal_80.csv'

# Read the CSV file into a pandas DataFrame
data_frame = pd.read_csv(file_path)


# Create the new "label" column with desired values
# For example, let's set all values in the "label" column to 0 initially
data_frame["label"] = 1

# Save the modified DataFrame back to a new CSV file
new_file_path = 'ptbdb_abnormal_80_label.csv'
data_frame.to_csv(new_file_path, index=False)

print("New column 'label' added and the modified CSV file saved successfully.")
