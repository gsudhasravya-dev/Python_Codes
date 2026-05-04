day=input("enter a day: ")
weekdays=["monday","tuesday","wednesday","thursday","friday"]
weekends=["saturday","sunday"]
if day.lower() in weekdays:
    print("weekday")
elif day.lower() in weekends:
    print("weekend")
else:
    print("invalid")