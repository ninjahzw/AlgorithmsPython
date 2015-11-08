from datetime import date, timedelta, datetime

def is_in_days_seconds(int_time, int_days):
    try:
        seconds_per_day = 86400
        total_seconds = 86400 * int_days

        if not isinstance(int_time, int):
            int_time = int(int_time)
        if not isinstance(int_days, int):
            int_days = int(int_days)
        then = datetime.fromtimestamp(int_time)
        print then
        now = datetime.now()
        if (now-then).total_seconds() > total_seconds:
            return False
        return True
    except Exception:
        return False
        

print (is_in_days_seconds('1432228308', 7))

