#!/usr/bin/python

import time
import datetime


# Function that converts timestamp to human readable date time
# @param {float} timestamp
# @returns {string} human readable datetime
#          2016-09-26 15:13:00
# BUT DOING IT THE HARDWAY, by using math

# 1. give me the rough date (not accounting for leapyear)
# bonus: 
#   1. make it accurate without using third party library
#   2. make it accurate using whatever library you want

def timeConvert(timestamp):
    years = timestamp / 60 / 60 / 24 / 365
    year = 1970 + years
    percYear = (years-int(years))
    month = percYear * 12
    percDay = (month-int(month))
    day = percDay * 30
    percHour = (day-int(day))
    hour = percHour * 24
    percMin = (hour-int(hour))
    minute = percMin * 60
    percSec = (minute-int(minute))
    second = percSec * 60

    print "{}-{}-{} {}:{}:{}".format(int(year), int(month), int(day), int(hour), int(minute), int(second))

timeConvert(time.time())

# This just returns number of leap years between
# start and end year
def howManyLeapYearsSince(start=1970, end=None):
    years = [i for i in range(int(start), int(end) + 1)] # this makes a list of years, between two dates
    numYears = 0


    for year in years:
        isLeapYear = False
        if year % 4:
            if year % 100:
                if year % 400:
                    isLeapYear = True
                else:
                    isLeapYear = False
            else:
                isLeapYear = False
        else:
            isLeapYear = False

        if isLeapYear is True:
            #print "Year {} has 365 days".format(year)
            pass
        else:
            #print "Year {} leap year!".format(year)
            numYears += 1

    return numYears

def isYearALeapYear(year=1970):
    if year % 4:
        if year % 100:
            if year % 400:
                isLeapYear = True
            else:
                isLeapYear = False
        else:
            isLeapYear = False
    else:
        isLeapYear = False

    return isLeapYear

def howManyDaysInTheYearSoFar(month=9):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    return sum(months[0:month-1])


def timeConvert2(timestamp):
    years = timestamp / 60 / 60 / 24 / 365
    year = 1970 + years
    percYear = (years-int(years))
    month = percYear * 12
    percDay = percYear * 365
    day = percDay * 30
    percHour = (day-int(day))
    hour = percHour * 24
    percMin = (hour-int(hour))
    minute = percMin * 60
    percSec = (minute-int(minute))
    second = percSec * 60

    leapYears = howManyLeapYearsSince(start=1970, end=year)
    day += leapYears

    day = percDay - howManyDaysInTheYearSoFar(month=int(month))
    print "{}-{}-{} {}:{}:{}".format(int(year), int(month), int(day), int(hour), int(minute), int(second))

timeConvert2(time.time())


class DateTime(object):

    year    = 1970
    month   = 0
    day     = 0
    hour    = 0
    minute  = 0
    second  = 0

    def __init__(self, *args, **kwargs):
        if kwargs.get('timestamp'):
            self.rawtime   = kwargs.get('timestamp')
            self.timestamp = int(kwargs.get('timestamp'))
        else:
            self.rawtime   = time.time() 
            self.timestamp = int(time.time())

        self.rawtime -= float(60 * 60 * 4)
        self.timestamp -= 60 * 60 * 4

        self.calculate()

    def calculate(self, *args, **kwargs):
        days = 0
        while days < self.timestamp / 60 / 60 / 24:
            days += 1

        totalDays = days
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        monthStrings = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        doMonths = True
        while doMonths is True:
            monthIndex = 0

            for daysInMonth in months:
                if len(months) > monthIndex + 1 and totalDays - months[monthIndex + 1] <= 0:
                    doMonths = False
                    break
                
                if totalDays <= 0:
                    doMonths = False
                    break
                
                subtractDays = 0
                if monthIndex == 1:
                    if isYearALeapYear(self.year) is False:
                        subtractDays = 29
                    else:
                        subtractDays = 28
                else:
                    subtractDays = daysInMonth

                totalDays -= subtractDays

                #print "{} {} {}".format(self.year, monthStrings[monthIndex], subtractDays)
                
                monthIndex += 1

            if totalDays <= 0:
                doMonths = False
                break

            if doMonths:
                self.year += 1

        self.month = monthIndex + 1
        self.day   = totalDays + 1

        remainingSeconds = float(self.rawtime) - (float(days) * 86400.0)
        hour = remainingSeconds / 60.0 / 60.0
        self.hour = int(hour)
        minutesRemaining = (hour - int(hour)) * 60
        self.minute = int(minutesRemaining)
        secondsRemaining = (minutesRemaining - int(minutesRemaining)) * 60.0
        self.second = int(secondsRemaining)

    def datetime(self, *args, **kwargs):
        return "{}-{}-{} {}:{}:{}".format(int(self.year), int(self.month), int(self.day), int(self.hour), int(self.minute), int(self.second))


datetime1 = DateTime()
print datetime1.datetime()


print time.strftime("%Y-%m-%d %H:%M:%S")

