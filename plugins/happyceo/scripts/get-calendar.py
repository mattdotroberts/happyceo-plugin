#!/usr/bin/env python3
"""
Fetch today's calendar events from Google Calendar.
Usage: python3 scripts/get-calendar.py [days]
  days: number of days to look ahead (default: 1)

Configuration:
  Set GOOGLE_SERVICE_ACCOUNT_PATH and GOOGLE_CALENDAR_ID in your .env file,
  or update the constants below.
"""

import os
import sys
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Load config from .env
def load_env():
    env_path = Path(__file__).parent.parent / ".env"
    config = {}
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
    return config

env = load_env()

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = env.get('GOOGLE_SERVICE_ACCOUNT_PATH', os.environ.get('GOOGLE_SERVICE_ACCOUNT_PATH', ''))
CALENDAR_ID = env.get('GOOGLE_CALENDAR_ID', os.environ.get('GOOGLE_CALENDAR_ID', ''))

def get_events(days=1):
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    if not SERVICE_ACCOUNT_FILE:
        print("Error: GOOGLE_SERVICE_ACCOUNT_PATH not set in .env")
        sys.exit(1)
    if not CALENDAR_ID:
        print("Error: GOOGLE_CALENDAR_ID not set in .env")
        sys.exit(1)

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('calendar', 'v3', credentials=credentials)

    now = datetime.now(timezone.utc)
    end = now + timedelta(days=days)

    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=now.isoformat(),
        timeMax=end.isoformat(),
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    return events_result.get('items', [])

def format_time(event):
    """Extract and format event time."""
    start = event['start'].get('dateTime', event['start'].get('date'))
    if 'T' in start:
        dt = datetime.fromisoformat(start.replace('Z', '+00:00'))
        return dt.strftime('%H:%M')
    return 'All day'

def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    events = get_events(days)

    if not events:
        print('No events found.')
        return

    print(f'Events for the next {days} day(s):\n')
    for event in events:
        time = format_time(event)
        summary = event.get('summary', 'No title')
        location = event.get('location', '')

        print(f'  {time} - {summary}')
        if location:
            print(f'         Location: {location}')

        # Show attendees if available
        attendees = event.get('attendees', [])
        external = [a['email'] for a in attendees if not a.get('self')]
        if external:
            print(f'         Attendees: {", ".join(external)}')
        print()

if __name__ == '__main__':
    main()
