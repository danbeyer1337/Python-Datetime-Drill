from datetime import datetime
from pytz import timezone

now_pdx = datetime.now(timezone('US/Pacific'))
print(now_pdx)

now_ny = datetime.now(timezone('US/Eastern'))
print(now_ny)

now_london = datetime.now(timezone('Europe/London'))
print(now_london)


