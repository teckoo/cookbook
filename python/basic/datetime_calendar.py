"""
Snippets for datetime and calendar related usage
"""
import datetime
import calendar
import time


def print_usage():
    """
    basic date and time type usage
    format string is at
    https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
    """
    n = datetime.datetime.now()
    print("default datetime now: %s" % n)
    print(n.strftime("%Y-%m-%d-%H-%M-%S"))
    # '2019-01-29-12-28-41'

    print("Current time zone is %s" % str(time.tzname))

    print("Current month is %s" % calendar.month_name[3])


if __name__ == "__main__":
    print_usage()
