from datetime import datetime

def calculate_hours_by_day(day):
    resume_day = {
        "hours": [],
        "bank_time": 0
    }
    time1 = datetime.strptime('{}:{}'.format(day[0][:2],day[0][2:4]), "%H:%M")
    time2 = datetime.strptime('{}:{}'.format(day[1][:2],day[1][2:4]), "%H:%M")
    if len(day) > 2:
        time3 = datetime.strptime('{}:{}'.format(day[2][:2],day[2][2:4]), "%H:%M")
        time4 = datetime.strptime('{}:{}'.format(day[3][:2],day[3][2:4]), "%H:%M")
        bank_time = ((time4 - time3) + (time2 - time1))
    else:
        bank_time = time2 - time1
    bank_minutes = bank_time.total_seconds() / 60 - 528
    resume_day["bank_time"] = bank_minutes
    for hourtime in day:
        resume_day["hours"].append('{}:{}:{}'.format(hourtime[:2],hourtime[2:4],hourtime[4:6]))
    return resume_day

def generate_banktime(points):
    result = {}
    for year, months in points.items():
        result[year] = {}
        for month, days in months.items():
            result[year][month] = {}
            for day, hours in days.items():
                result[year][month][day] = calculate_hours_by_day(hours)
    return result