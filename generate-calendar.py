from datetime import date, timedelta

sites = ['Bath',
         'Bristol',
         'Cardiff',
         'Exeter']
offset = 1 # start with Bristol
start_date = date(2019,10,7)
weeks_to_schedule = 12
format = '%a %d %b'
for week in range(weeks_to_schedule):
  monday = start_date + timedelta(days=(week * 7))
  friday = monday + timedelta(days=4)
  print(monday.strftime(format), "--", friday.strftime(format), "  ",
        sites[(week + offset ) % 4])
