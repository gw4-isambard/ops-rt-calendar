#!/usr/bin/env python

import requests
import json
import argparse
from ics import Calendar, Event

parser = argparse.ArgumentParser(description="Post reminder to slack.")
parser.add_argument(
    "--webhook",
    required=True,
    help="Slack Incoming Webhook URL in the form https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX",
)
parser.add_argument(
    "--calendar",
    help="URL to .ical file (defaults to GitHub repo)",
    default="https://raw.githubusercontent.com/gw4-isambard/ops-rt-calendar/master/rt-rota.ics",
)
args = parser.parse_args()

# Download and parse .ics
cal = Calendar(requests.get(args.calendar).text)
# Find today's event
event = list(cal.timeline.now())[0]

# Post to Slack
payload = {"text": event.name}
headers = {"content-type": "application/json"}

slack = requests.post(args.webhook, data=json.dumps(payload), headers=headers)
