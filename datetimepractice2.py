from datetime import datetime
from pytz import timezone

now_pdx = datetime.now(timezone('US/Pacific'))
print(now_pdx.strftime('%I:%M:%S'))

now_ny = datetime.now(timezone('US/Eastern'))
print(now_ny.strftime('%I:%M:%S'))

now_london = datetime.now(timezone('Europe/London'))
print(now_london.strftime('%I:%M:%S'))


