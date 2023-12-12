import csv
from datetime import datetime, timedelta

# Function to calculate days difference
def calculate_days_difference(end_date_str):
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()  # Adjusted to the correct format
    return (end_date - datetime.now().date()).days

def overwrite_days_difference(csv_file_path):
    # Read the current data from the CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)

    # Update 'days_difference' for each row
    for row in lines[1:]:  # Skip header row
        end_date_str = row[2]  # Assuming end_date is at index 2
        row[3] = calculate_days_difference(end_date_str)  # Update days_difference

    # Write the updated data back to the CSV file
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

# Define the path to your CSV file
csv_file_path = 'trial_subscriptions.csv'

if __name__ == "__main__":
    overwrite_days_difference(csv_file_path)

