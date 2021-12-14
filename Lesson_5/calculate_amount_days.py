from datetime import datetime
import math


def days_before_event(hours_flag: bool) -> int:
    current_time = datetime.now()
    new_year_time = datetime(2022, 1, 1)
    delta = new_year_time - current_time
    delta_days = delta.days
    if hours_flag:
        delta_hours = math.floor(delta.seconds / 3600)
        print(f"{delta_days} days, {delta_hours} hour")
    else:
        print(f"{delta_days} days")
    return 0
