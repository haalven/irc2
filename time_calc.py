
# time calculations

from datetime import datetime, timezone, timedelta
from xterm_control import light, normal


'''
CONVERT OBJECT -> STRING
'''

# datetime object -> date and time string

def dt2ymd(dt): return dt.strftime('%y-%m-%d %H:%M:%S')



# datetime object -> time only string

def dt2hms(dt): return dt.strftime('%H:%M:%S')



# timedelta object -> time interval string

def td2str(td):
    secs = td.total_seconds()
    mins, secs = divmod(secs, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
    if days >= 365:
        years = days / 365.242
        return f'{years:.1f} years'
    elif days >= 30:
        months = days / 30.437
        return f'{months:.1f} months'
    elif days >=  7: return f'{days:.0f} days'
    elif days >=  1: return f'{days:.0f} days, {hour:.0f} hours'
    elif hour >=  1: return f'{hour:.0f} hours, {mins:.0f} mins'
    elif mins >= 10: return f'{mins:.0f} mins'
    elif mins >=  1: return f'{mins:.0f} mins, {secs:.0f} secs'
    else: return f'{secs:.0f} secs'



'''
DATETIME AND TIMEDELTA OBJECTS
'''


# now -> datetime object

def dt_now():

    dt = datetime.now(tz=timezone.utc)

    return dt.astimezone()



# unixtime string -> datetime object

def ts2dt(timestamp):

    try: ts = float(timestamp.strip())
    except Exception: return None

    dt = datetime.fromtimestamp(ts)

    return dt.astimezone()



# tag/servertime -> datetime object

def st2dt(servertime):

    dt = datetime.fromisoformat(servertime)

    return dt.astimezone()



# seconds string -> timedelta object

def sec2td(sec):

    try: s = float(sec.strip())
    except Exception: return None

    return timedelta(seconds=s)



'''
LINE PREFIX
'''


# now prefix

def now():
    
    return light() + dt2hms(dt_now()) + normal()



# datetime prefix

def pre(dt):

    pre = light() + dt2hms(dt) + normal()

    return pre

