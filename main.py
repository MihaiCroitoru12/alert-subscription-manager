from datetime import date, datetime, timedelta
import csv
import os

def add_new_subscription():
    # Input subscription details from the user
    service_name = input("Insert the service subscription name: ")
    start_date_str = input("Insert the start date (DD/MM/YYYY): ")
    trial_duration_days = int(input("Enter the trial duration in days: "))
    mail = input("Enter your email for subscription expiration alerts:")

    # Convert the start date string to a date object and calculate the end date
    try:
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY")
        return

    end_date = start_date + timedelta(days=trial_duration_days)
    days_difference = (end_date - date.today()).days

    # Check if the CSV file exists and is not empty
    file_exists = os.path.isfile("trial_subscriptions.csv") and os.path.getsize("trial_subscriptions.csv") > 0 

    # Write the new subscription data to the CSV file
    with open("trial_subscriptions.csv", "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Service Name", "Start Date", "End Date", "Days Remaining", "Mail"])
        writer.writerow([service_name, start_date, end_date, days_difference, mail])
    print("Subscription added successfully.")

def list_all_subscriptions():
    if os.path.isfile("trial_subscriptions.csv"):
        with open("trial_subscriptions.csv", "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

def check_expiring_subscriptions():
    if os.path.isfile("trial_subscriptions.csv"):
        with open("trial_subscriptions.csv", "r", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                end_date = datetime.strptime(row["End Date"], "%Y-%m-%d").date()
                days_remaining = (end_date - date.today()).days
                if days_remaining <= 1:
                    print(f"Alert: The subscription for {row['Service Name']} is expiring soon.")

# Main menu for the user interaction
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new subscription")
        print("2. List all subscriptions")
        print("3. Check for expiring subscriptions")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Process the user's choices
        if choice == '1':
            add_new_subscription()
        elif choice == '2':
            list_all_subscriptions()
        elif choice == '3':
            check_expiring_subscriptions()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
