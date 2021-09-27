from datetime import date, timedelta
from ics import Calendar, Event

sites = ["Bath", "Bristol", "Cardiff", "Exeter"]
offset = 1  # start with Bristol
start_date = date(2021, 9, 27)
weeks_to_schedule = 12

# format = "%Y-%m-%d 00:00:00"
num_sites = len(sites)
working_week = 4  # number of days between Monday and Friday
calendar_week_len = 7

calendar = Calendar()
for week in range(weeks_to_schedule):
    monday = start_date + timedelta(days=(week * 7))
    friday = monday + timedelta(days=working_week)
    site = sites[(week + offset) % num_sites]
    turn = Event()
    turn.name = f"{site} doing RT ticket dispatching"
    turn.begin = monday.strftime("%Y-%m-%d 00:00:00")
    turn.end = friday.strftime("%Y-%m-%d 23:59:59")
    turn.make_all_day()
    turn.transparent = True
    calendar.events.add(turn)

with open("rt-rota.ics", "w") as f:
    f.writelines(calendar)
