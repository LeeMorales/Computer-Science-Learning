print("数字，日期和时间5")
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
#创建一周的列表
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday']
weekends = ['Saturday', 'Sunday']

#初始化
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


def last_friday():
    print(datetime.today())
    print(get_previous_byday('Monday'))
    print(get_previous_byday('Tuesday'))
    print(get_previous_byday('Friday'))
    print(get_previous_byday('Saturday'))
    # 显式的传递开始日期
    print(get_previous_byday('Sunday', datetime(2012, 12, 21)))

    # 使用dateutil模块
    d = datetime.now()
    # 下一个周五
    print(d + relativedelta(weekday=FR))
    # 上一个周五
    print(d + relativedelta(weekday=FR(-1)))
    # 下一个周六， 为什么如果今天是周六，下一个/上一个都返回今天的日期？？
    print(d + relativedelta(weekday=SA))
    # 上一个周六
    print(d + relativedelta(weekday=SA(-1)))


if __name__ == '__main__':
    last_friday()

from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)
    def date_range(start, stop, step):
        while start < stop:
            yield start
        start += step
        def month_range():
            a_day = timedelta(days=1)
            first_day, last_day = get_month_range()
            while first_day < last_day:
                print(first_day)
                first_day += a_day
            # 使用生成器
            for d in date_range(datetime(2012, 9, 1), datetime(2012, 10, 1),
                                timedelta(hours=6)):
                print(d)
        if __name__ == '__main__':
            month_range()

from datetime import datetime, timedelta
from pytz import timezone
import pytz


def tz_local():
    d = datetime(2012, 12, 21, 9, 30, 0)
    print(d)

    # Localize the date for Chicago
    central = timezone('US/Central')
    loc_d = central.localize(d)
    print(loc_d)

    # Convert to Bangalore time
    bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
    print(bang_d)


    # 夏令时
    d = datetime(2013, 3, 10, 1, 45)
    loc_d = central.localize(d)
    print(loc_d)
    later = loc_d + timedelta(minutes=30)
    print(later)
    # 使用normalize修正这个问题
    later = central.normalize(loc_d + timedelta(minutes=30))
    print(later)

    # 一个普遍策略是先转换为UTC时间，使用UTC时间来进行计算
    print(loc_d)
    utc_d = loc_d.astimezone(pytz.utc)
    print(utc_d)

    later_utc = utc_d + timedelta(minutes=30)
    # 转回到本地时间
    print(later_utc.astimezone(central))

    # 根据ISO 3166国家代码查找时区名称
    print(pytz.country_timezones['IN'])

if __name__ == '__main__':
    tz_local()