The **main.py** serves as a subscription management tool, allowing users to track and monitor their service subscriptions. It includes adding new subscriptions, listing all subscriptions, and checking for subscriptions nearing their expiration. When adding a new subscription, user is prompted for service name, start date, trial duration, and an email address for alerts. The script calculates the end date and days remaining until expiration, storing all data in a CSV file named 'trial_subscriptions.csv'. 

This **overwrite_days.py** is designed to update the remaining days before subscription expiration in a CSV file named 'trial_subscriptions.csv'. The script works by reading the existing subscription data from the CSV file, recalculating the 'days_difference' (the number of days until the subscription expires) for each entry, and then overwriting the CSV file with the updated information. It calculates the 'days_difference' by comparing the current date with the subscription's end date, ensuring that the information is always up-to-date. 

The **send_mail_alerts.py** automates the process of sending email alerts for subscriptions that are near to expire. It works by reading subscription data from a CSV file, identifying subscriptions that are due to expire within a day, and then using SendGrid's SMTP service to send email alerts. The script handles the entire process from parsing the CSV data to constructing and sending HTML-formatted emails, ensuring users are notified about their expiring subscriptions. 

<img src="https://github.com/MihaiCroitoru12/alert-subscription-manager/assets/147843903/8e7df12b-f08c-400d-bdb2-b3ec463a6317" alt="sub_alert" width="400" height="500"/>



