import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail_alert(expiring_subscriptions, recipient_email):
    # Configuration for SendGrid API
    sendgrid_api_key = ''  # SendGrid API key
    sendgrid_username = 'apikey'  # Default username for SendGrid SMTP
    sendgrid_smtp_server = 'smtp.sendgrid.net'
    sendgrid_smtp_port = 465  # SSL port for SMTP

    # Creating the email message
    message = MIMEMultipart('alternative')
    message['Subject'] = 'Subscription Alert'
    message['From'] = 'subscription.alert.notification@gmail.com'
    message['To'] = recipient_email

    # Building the HTML content for the email
    html_body = "<html><body>"
    html_body += "<p>WARNING! The following subscriptions will expire in 1 day.</p>"
    html_body += "<ul>"
    for subscription_name in expiring_subscriptions:
        html_body += f"<li><strong>{subscription_name}</strong></li>"
    html_body += "</ul>"
    html_body += "</body></html>"

    # Attaching the HTML content to the email
    message.attach(MIMEText(html_body, 'html'))

    # Sending the email using SMTP
    try:
        smtp_server = smtplib.SMTP_SSL(sendgrid_smtp_server, sendgrid_smtp_port)
        smtp_server.login(sendgrid_username, sendgrid_api_key)
        smtp_server.send_message(message)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong:", ex)

def main():
    # Reading data from a CSV file
    with open('trial_subscriptions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skipping the header row
        expiring_subscriptions = []
        for row in reader:
            service_name = row[0]
            email_address = row[4]
            days_difference = int(row[3])
            
            # Checking if subscription is expiring and adding it to the list
            if days_difference == 1:
                expiring_subscriptions.append(service_name)
        
        # Sending email alerts for expiring subscriptions
        if expiring_subscriptions:
            send_mail_alert(expiring_subscriptions, email_address)

if __name__ == "__main__":
    main()
