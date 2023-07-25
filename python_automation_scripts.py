import os
import shutil
import requests
import smtplib
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import datetime

def organize_files(downloads_folder):
    file_types = {
        "Documents": [".txt", ".docx", ".pdf"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Music": [".mp3", ".wav"],
        "Archives": [".zip", ".rar", ".7z"],
        "Others": []
    }

    for filename in os.listdir(downloads_folder):
        if os.path.isfile(os.path.join(downloads_folder, filename)):
            file_extension = os.path.splitext(filename)[1]
            destination_folder = "Others"
            
            for folder, extensions in file_types.items():
                if file_extension.lower() in extensions:
                    destination_folder = folder
                    break

            source_path = os.path.join(downloads_folder, filename)
            destination_path = os.path.join(downloads_folder, destination_folder, filename)
            shutil.move(source_path, destination_path)

def create_calendar_event(api_key, event_title, event_start, event_end):
    credentials = Credentials.from_authorized_user(api_key)
    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': event_title,
        'start': {
            'dateTime': event_start,
            'timeZone': 'Your_Time_Zone',
        },
        'end': {
            'dateTime': event_end,
            'timeZone': 'Your_Time_Zone',
        },
    }

    service.events().insert(calendarId='primary', body=event).execute()

def check_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        send_notification_email(url)

def send_notification_email(sender_email, receiver_email, password, url):
    subject = f"Website Down: {url}"
    message = f"The website {url} is currently down."

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    # File Organizer Script
    downloads_folder = "path_to_your_downloads_folder"
    organize_files(downloads_folder)

    # Google Calendar Automation Script
    api_key = "your_google_calendar_api_key"
    event_title = "Programming Time"
    current_time = datetime.datetime.now()
    event_start = current_time.isoformat()
    event_end = (current_time + datetime.timedelta(hours=1)).isoformat()  # Assuming you track 1 hour sessions
    create_calendar_event(api_key, event_title, event_start, event_end)

    # Website Monitoring Script
    website_url = "https://example.com"
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    password = "your_email_password"
    check_website(website_url, sender_email, receiver_email, password)
