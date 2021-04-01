# ops-rt-calendar

Edit generate-calendar.py to set start_date

A custom event looks like:

```
newyear = Event(
	name = "Happy new year everyone!",
	begin = "2020-12-27 00:00:00",
	end = "2021-01-01 23:59:59",
	transparent = True
)
newyear.make_all_day()
```

This generates rt-rota.ics

Commit rt-rota.ics and push, people who have subscribed to the raw githubcontent.com address will receive the update.

post-to-slack.py takes two arguments, --calendar [file] and --webhook. The webhook can be generated in Slack.
