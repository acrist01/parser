import calendar
import datetime

class Calendar(object):

    def get_days_in_month(self):
        now = datetime.datetime.now()
        return calendar.monthrange(now.year, now.month)[1]